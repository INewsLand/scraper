import scrapy
from datetime import datetime
from utils.text import remove_blank_lines
from scraper.items import Feed


class ElUniversalFeedSpider(scrapy.Spider):
    name = 'ElUniversalFeed'
    allowed_domains = [
        'eluniversal.com.mx'
    ]
    start_urls = [
        'https://www.eluniversal.com.mx/minuto-x-minuto'
    ]

    def set_config_values(self, items):
        items['name'] = 'El Universal'
        items['domain'] = 'eluniversal.com.mx'
        items['collection'] = 'Feed'
        items['createdAt'] = datetime.now()
        return items

    def parse(self, response):
        items = Feed()

        news_content_selector = 'div.view-content>div'
        title_selector = 'h2 > a::text'
        link_selector = 'h2 > a::attr(href)'
        tag_selector = 'h2 > span > a::text'

        for element in response.css(news_content_selector):
            items = self.set_config_values(items)
            items['hour'] = remove_blank_lines(element.css('::text').get())
            items['title'] = element.css(title_selector).get()
            items['link'] = element.css(link_selector).get()
            items['tag'] = element.css(tag_selector).get()
            yield items

        next_page_selector = 'li.pager-next > a'
        for page in response.css(next_page_selector):
            yield response.follow(page, callback=self.parse)
