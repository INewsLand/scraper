import scrapy
from utils.text import remove_blank_lines
from ..items import ScraperUniversal


class ElUniversalSpider(scrapy.Spider):
    name = 'ElUniversal'
    allowed_domains = [
        'eluniversal.com.mx'
    ]
    start_urls = [
        'https://www.eluniversal.com.mx/minuto-x-minuto'
    ]

    def parse(self, response):
        items = ScraperUniversal()

        news_content_selector = 'div.view-content>div'
        title_selector = 'h2 > a::text'
        link_selector = 'h2 > a::attr(href)'
        tag_selector = 'h2 > span > a::text'

        for element in response.css(news_content_selector):
            items['name'] = 'El Universal'
            items['domain'] = 'eluniversal.com.mx'
            items['collection'] = 'Feed'
            items['hour'] = remove_blank_lines(element.css('::text').get())
            items['title'] = element.css(title_selector).get()
            items['link'] = element.css(link_selector).get()
            items['tag'] = element.css(tag_selector).get()
            yield items

        # next_page_selector = 'li.pager-next > a'
        # for page in response.css(next_page_selector):
        #     yield response.follow(page, callback=self.parse)
