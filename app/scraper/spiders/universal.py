import scrapy
from utils.text import remove_blank_lines


class ElUniversalSpider(scrapy.Spider):
    name = 'ElUniversal'
    start_urls = [
        'https://www.eluniversal.com.mx/minuto-x-minuto'
    ]

    def parse(self, response):
        news_content_selector = 'div.view-content>div'
        title_selector = 'h2 > a::text'
        link_selector = 'h2 > a::attr(href)'
        tag_selector = 'h2 > span > a::text'
        for element in response.css(news_content_selector):
            yield {
                'hour': remove_blank_lines(element.css('::text').get()),
                'title': element.css(title_selector).get(),
                'link': element.css(link_selector).get(),
                'tag': element.css(tag_selector).get()
            }

        next_page_selector = 'li.pager-next > a'
        for page in response.css(next_page_selector):
            yield response.follow(page, callback=self.parse)
