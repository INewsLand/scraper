from scrapy.crawler import CrawlerProcess
from scraper.spiders.news.universal import ElUniversalNewsSpider
from scraper.settings import settings

def main():
    process = CrawlerProcess(settings)
    process.crawl(ElUniversalNewsSpider)
    process.start()

if __name__ == "__main__":
    main()
