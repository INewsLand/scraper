from scrapy.crawler import CrawlerProcess
from scraper.spiders.universal import ElUniversalNewsSpider
from scraper.settings import settings

def main():
    spider_name = 'ElUniversalNews'
    spider_instance = None
    if spider_name == 'ElUniversalNews':
        spider_instance = ElUniversalNewsSpider

    process = CrawlerProcess(settings)
    process.crawl(spider_instance)
    process.start()

if __name__ == "__main__":
    main()
