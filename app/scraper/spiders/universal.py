import scrapy
from utils.text import remove_blank_lines


class ElUniversalSpider(scrapy.Spider):
    name = 'ElUniversal'

    def start_requests(self):
        base_url = 'https://www.eluniversal.com.mx/minuto-x-minuto?page={0}'
        urls = list()
        max_pages = 8
        for page_number in range(0, max_pages):
            urls.append(base_url.format(page_number))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        news_content_selector = 'div.view-content>div'
        title_selector = 'h2>a::text'
        link_selector = 'h2>a::attr(href)'
        tag_selector = 'h2>span>a::text'
        for element in response.css(news_content_selector):
            hour = element.css('::text').get()
            title = element.css(title_selector).get()
            link = element.css(link_selector).get()
            tag = element.css(tag_selector).get()
            yield {
                'hour': remove_blank_lines(hour),
                'title': title,
                'link': link,
                'tag': tag
            }
