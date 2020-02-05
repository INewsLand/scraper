from scrapy.crawler import CrawlerProcess
from scraper.spiders.universal import ElUniversalSpider

def main():
    print('Running Crawlers')
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'ITEM_PIPELINES': {
            'scraper.pipelines.MongoPipeline': 100,
        }
    })
    process.crawl(ElUniversalSpider)
    process.start()

if __name__ == "__main__":
    main()
