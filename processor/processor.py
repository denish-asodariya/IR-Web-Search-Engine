# Import necessary libraries and modules
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import heapq
from nltk.corpus import wordnet
from nltk.metrics import edit_distance

# Initialize the Flask app
app = Flask(__name__)

# Define the list of documents
documents = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

# Initialize the TfidfVectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit the TfidfVectorizer to the documents and obtain the tf-idf matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Define the suggest_correction function
def suggest_correction(query):
    """
    Suggests a corrected version of the query using NLTK WordNet.

    Parameters:
    query (str): The query to be corrected.

    Returns:
    str or None: The corrected version of the query or None if no correction is found.
    """
    # Get the synsets for the query
    synsets = wordnet.synsets(query)

    # If synsets are found, proceed with correction
    if synsets:
        # Get all the lemma names for the synsets
        all_lemma_names = [lemma for synset in synsets for lemma in synset.lemma_names()]

        # Calculate the edit distance between query and each lemma name
        distances = [(lemma, edit_distance(query, lemma)) for lemma in all_lemma_names]

        # Sort the distances and return the closest match
        closest_match = min(distances, key=lambda x: x[1])

        return closest_match[0]

    # If no synsets are found, return None
    else:
        return None

# Define the process_query route
@app.route('/query', methods=['POST'])
def process_query():
    """
    Processes the query and returns the top k similar documents.

    Parameters:
    None

    Returns:
    JSON response containing the top k similar documents.
    """
    # Get the JSON data from the request
    data = request.json

    # Extract the query and top_k from the data
    query = data.get('query', '')
    k = data.get('top_k', 5)

    # Suggest a corrected version of the query
    query_correction = suggest_correction(query)

    # If a correction is suggested, return a JSON response with the suggested correction
    if query_correction:
        return jsonify({"message": f"Did you mean '{query_correction}'?"})

    # Transform the query to a vector
    query_vector = tfidf_vectorizer.transform([query])

    # Calculate the cosine similarity between the query vector and the tfidf_matrix
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

    # Get the top k indices with the highest similarity scores
    top_k_indices = heapq.nlargest(k, range(len(similarity_scores)), similarity_scores.take)

    # Create a list of dictionaries containing the top k results
    top_k_results = [{"document": documents[i], "similarity_score": similarity_scores[i]} for i in top_k_indices]

    # Return the top k results as a JSON response
    return jsonify({"results": top_k_results})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)