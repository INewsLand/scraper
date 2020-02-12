from scrapy.crawler import CrawlerProcess
from scraper.spiders.feed.grupo_formula import GrupoFormulaFeedSpider
from scraper.settings import settings

def main():
    process = CrawlerProcess(settings)
    process.crawl(GrupoFormulaFeedSpider)
    process.start()

if __name__ == "__main__":
    main()
