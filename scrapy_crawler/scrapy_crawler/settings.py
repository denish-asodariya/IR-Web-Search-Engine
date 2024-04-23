# Scrapy settings for scrapy_crawler project

# The name of the bot
BOT_NAME = "scrapy_crawler"

# The module where the spiders are defined
SPIDER_MODULES = ["scrapy_crawler.spiders"]

# The module where the new spiders are defined
NEWSPIDER_MODULE = "scrapy_crawler.spiders"

# Whether to obey robots.txt rules
ROBOTSTXT_OBEY = True

# The maximum number of concurrent requests performed by Scrapy
#CONCURRENT_REQUESTS = 32

# The delay for requests for the same website
#DOWNLOAD_DELAY = 3

# The maximum number of concurrent requests per domain
#CONCURRENT_REQUESTS_PER_DOMAIN = 16

# The maximum number of concurrent requests per IP
#CONCURRENT_REQUESTS_PER_IP = 16

# Whether to enable cookies
#COOKIES_ENABLED = False

# Whether to enable the Telnet Console
#TELNETCONSOLE_ENABLED = False

# The default request headers
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# The spider middlewares
#SPIDER_MIDDLEWARES = {
#    "scrapy_crawler.middlewares.ScrapyCrawlerSpiderMiddleware": 543,
#}

# The downloader middlewares
#DOWNLOADER_MIDDLEWARES = {
#    "scrapy_crawler.middlewares.ScrapyCrawlerDownloaderMiddleware": 543,
#}

# The extensions
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# The item pipelines
#ITEM_PIPELINES = {
#    "scrapy_crawler.pipelines.ScrapyCrawlerPipeline": 300,
#}

# The AutoThrottle extension
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

# The HTTP caching
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# The request fingerprinter implementation
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"

# The Twisted reactor
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

# The feed export encoding
FEED_EXPORT_ENCODING = "utf-8"