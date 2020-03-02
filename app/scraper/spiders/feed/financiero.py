import scrapy
from datetime import datetime
from utils.text import remove_blank_lines
from utils.text import normalize_titles
from scraper.items import Feed


class ElFinancieroFeedSpider(scrapy.Spider):
    name = 'ElFinanciero:Feed'
    allowed_domains = [
        'elfinanciero.com.mx'
    ]
    start_urls = [
        'https://www.elfinanciero.com.mx/bloomberg-businessweek',
        'https://www.elfinanciero.com.mx/economia',
        'https://www.elfinanciero.com.mx/empresas',
        'https://www.elfinanciero.com.mx/mercados',
        'https://www.elfinanciero.com.mx/nacional',
        'https://www.elfinanciero.com.mx/tech'
    ]

    def set_config_values(self, items):
        items['name'] = 'El Financiero'
        items['domain'] = 'elfinanciero.com.mx'
        items['collection'] = 'Feed'
        items['createdAt'] = datetime.now()
        return items

    def get_tag(self,url=""):
        url = url.split('\x2f')
        #print("URL _ " , url)
        return url[1]

    def parse(self, response):
        items = Feed()

        news_content_selector = 'div.feed'
        title_selector = 'div.no-padding-left > p.head::text'
        link_selector = 'a::attr(href)'
        tag_selector = link_selector

        for element in response.css(news_content_selector):
            items = self.set_config_values(items)
            items['hour'] = remove_blank_lines(element.css('::text').get())
            items['title'] = normalize_titles(element.css(title_selector).get())
            items['link'] = element.css(link_selector).get()
            items['tag'] = self.get_tag( element.css(tag_selector).get())
            yield items

            

        next_page_selector = 'button.load-more'
        for page in response.css(next_page_selector):
            yield response.follow(page, callback=self.parse)
