# Importing the scrapy module
import scrapy

# Defining the ScrapyCrawlerItem class, which inherits from scrapy.Item
# This class is used to define the models for scraped items
class ScrapyCrawlerItem(scrapy.Item):
    # The scrapy.Field() function is used to define the fields for the item
    # These fields can be accessed using dictionary-like syntax, e.g. item['field_name']
    # In this example, no fields have been defined
    pass