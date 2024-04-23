import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec

class Indexer:
    def __init__(self, documents):
        """
        Initialize the Indexer class with a list of documents.

        Parameters:
        documents (list): A list of strings, where each string is a document to be indexed.
        """
        self.documents = documents
        self.tfidf_vectorizer = TfidfVectorizer()
        """
        Initialize the TfidfVectorizer from scikit-learn to convert text documents to a matrix of TF-IDF features.
        """
        self.tfidf_matrix = None
        """
        Initialize the TF-IDF matrix to None. This will be populated with the TF-IDF matrix after it is built.
        """
        self.word2vec_model = None
        """
        Initialize the Word2Vec model to None. This will be populated with the Word2Vec model after it is trained.
        """
        self.word_embeddings = None

    def build_tfidf_index(self):
        """
        Build the TF-IDF index using the TfidfVectorizer.
        """
        self.tfidf_matrix = self.tfidf_vectorizer.fit_transform(self.documents)
        """
        Fit the TfidfVectorizer to the documents and transform them into a TF-IDF matrix.
        """

    def train_word2vec_model(self):
        """
        Train the Word2Vec model on the corpus of documents.
        """
        tokenized_documents = [doc.split() for doc in self.documents]
        self.word2vec_model = Word2Vec(tokenized_documents, vector_size=100, window=5, min_count=1, workers=4)
        self.word_embeddings = {word: self.word2vec_model.wv[word] for word in self.word2vec_model.wv.index_to_key}

    def save_tfidf_index(self, filename):
        """
        Save the TF-IDF index to a file using pickle.

        Parameters:
        filename (str): The name of the file to save the TF-IDF index to.
        """
        with open(filename, 'wb') as f:
            """
            Open the file in write-binary mode.
            """
            pickle.dump((self.tfidf_vectorizer, self.tfidf_matrix), f)
            """
            Dump the TF-IDF vectorizer and matrix to the file using pickle.
            """
    
    def save_word2vec_model(self, filename):
        """
        Save the Word2Vec model to a file using pickle.

        Parameters:
        filename (str): The name of the file to save the Word2Vec model to.
        """
        self.word2vec_model.save(filename)

    def calculate_cosine_similarity(self, query, use_word2vec=False):
        """
        Calculate the cosine similarity between a query and the indexed documents.

        Parameters:
        query (str): A string representing the query to calculate the cosine similarity for.
        use_word2vec (bool): Whether to use Word2Vec embeddings for calculating similarity.

        Returns:
        similarities (array): Array of cosine similarity scores.
        """
        if use_word2vec:
            query_embedding = self.get_embedding(query)
            similarities = [self.calculate_similarity(query_embedding, self.get_embedding(doc)) for doc in self.documents]
        else:
            self.build_tfidf_index()
            query_vector = self.tfidf_vectorizer.transform([query])
            similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        return similarities

    def get_embedding(self, text):
        """
        Get the Word2Vec embedding for a given text.

        Parameters:
        text (str): The input text.

        Returns:
        embedding (array): The Word2Vec embedding for the text.
        """
        words = text.split()
        vectors = [self.word_embeddings[word] for word in words if word in self.word_embeddings]
        if vectors:
            return sum(vectors) / len(vectors)
        else:
            return None

    def calculate_similarity(self, vec1, vec2):
        """
        Calculate cosine similarity between two vectors.

        Parameters:
        vec1 (array): First vector.
        vec2 (array): Second vector.

        Returns:
        similarity (float): Cosine similarity between the vectors.
        """
        if vec1 is None or vec2 is None:
            return 0
        return cosine_similarity([vec1], [vec2])[0][0]