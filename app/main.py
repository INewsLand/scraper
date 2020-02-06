from scrapy.crawler import CrawlerProcess
from scraper.spiders.universal_feed import ElUniversalFeedSpider
from scraper.settings import settings

def main():
    spider_name = 'ElUniversalFeed'
    spider_instance = None
    if spider_name == 'ElUniversalFeed':
        spider_instance = ElUniversalFeedSpider

    process = CrawlerProcess(settings)
    process.crawl(spider_instance)
    process.start()

if __name__ == "__main__":
    main()
