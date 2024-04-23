import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.item import Item, Field

class DocumentItem(Item):
    url = Field()
    html_content = Field()

class CrawlingSpider(CrawlSpider):
    name = 'crawling'  # Name of the spider
    allowed_domains = ['books.toscrape.com']  # Domains allowed for crawling
    start_urls = ["http://books.toscrape.com/"]  # Starting URLs for crawling
    max_pages = 10  # Maximum number of pages to crawl
    max_depth = 3  # Maximum depth for crawling

    documents = []  # List to store crawled documents

    def __init__(self, *args, **kwargs):
        super(CrawlingSpider, self).__init__(*args, **kwargs)
        self.documents = []  # Initialize documents list

    rules = (
        Rule(LinkExtractor(allow='catalogue/category')),  # Rule for category links
        Rule(LinkExtractor(allow='catalogue', deny="category"), callback='parse_item'),  # Rule for catalog links
    )

    def parse_item(self, response):
        if response.meta.get('depth', 0) <= self.max_depth:
            item = DocumentItem()
            item['url'] = response.url  # Set URL for the item
            item['html_content'] = response.text  # Set HTML content for the item
            self.documents.append(response.text)  # Append HTML content to documents list
            yield item

    def parse(self, response):
        if len(response.meta.get('redirect_urls', [])) <= self.max_pages:
            return super().parse(response)  # Call the parent class parse method