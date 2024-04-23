# This is the ScrapyCrawlerPipeline class which is used as a pipeline for items in Scrapy.
class ScrapyCrawlerPipeline:
    # This method is called for each item that goes through the pipeline.
    def process_item(self, item, spider):
        # It returns the item without modifying it.
        return item