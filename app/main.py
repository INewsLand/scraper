from scrapy.crawler import CrawlerProcess
from scraper.spiders.feed.universal import ElUniversalFeedSpider
from scraper.settings import settings

def main():
    process = CrawlerProcess(settings)
    process.crawl(ElUniversalFeedSpider)
    process.start()

if __name__ == "__main__":
    main()
