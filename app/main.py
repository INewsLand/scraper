from scrapy.crawler import CrawlerProcess
from scraper.spiders.universal import ElUniversalSpider
from scraper.settings import settings

def main():
    process = CrawlerProcess(settings)
    process.crawl(ElUniversalSpider)
    process.start()

if __name__ == "__main__":
    main()
