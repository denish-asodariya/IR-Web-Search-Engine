from scrapy.crawler import CrawlerProcess  # Import CrawlerProcess class from scrapy.crawler
from scrapy_crawler.scrapy_crawler.spiders.crawling_spider import CrawlingSpider  # Import CrawlingSpider class from scrapy_crawler.scrapy_crawler.spiders.crawling_spider
from indexer.indexer import Indexer  # Import Indexer class from indexer.indexer
from processor.processor import app  # Import app instance from processor.processor

# Initialize CrawlerProcess
process = CrawlerProcess()

# Start crawling using the CrawlingSpider
process.crawl(CrawlingSpider)

# Start the crawling process
process.start()

# Initialize CrawlingSpider
crawler = CrawlingSpider()

# Get documents from the crawling process
documents = crawler.documents

# Check if documents are retrieved
if not documents:
    # Print message if no documents are retrieved
    print("No documents retrieved. Check the crawling process.")
else:
    # Initialize Indexer
    indexer = Indexer(documents)

    # Build TF-IDF index
    indexer.build_tfidf_index()

    # Save TF-IDF index as "tfidf_index.pkl"
    indexer.save_tfidf_index("tfidf_index.pkl")

    # Load TF-IDF index from "tfidf_index.pkl"
    indexer.load_tfidf_index("tfidf_index.pkl")

# Run Flask app
app.run(debug=True)