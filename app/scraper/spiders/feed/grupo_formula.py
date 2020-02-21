import scrapy
from datetime import datetime
from utils.text import remove_blank_lines
from scraper.items import Feed
import re

class GrupoFormulaFeedSpider(scrapy.Spider):
    name = 'GrupoFormula:Feed'

    allowed_domains = [
        'radioformula.com.mx'
    ]
    start_urls = [
        'https://www.radioformula.com.mx/noticias/'
    ]

    def set_config_values(self, items):
        items['name'] = 'Grupo Formula'
        items['domain'] = 'radioformula.com.mx'
        items['collection'] = 'Feed'
        items['createdAt'] = datetime.now()
        return items

    def get_category_from_class_attr(self, text):
        data = re.findall("category-\w+", text)
        result = " "
        data_cleaned = []
        x = ""
        for e in data:
            x = (re.sub("category-","",e))
            if x != "noticias":
                data_cleaned.append(x)
        result = result.join(data_cleaned)
        return  result


    def parse(self, response):
        items = Feed()

        news_content_selector = 'li.post'
        title_selector = 'h3.post-title>a::text'
        link_selector = 'a.more-link::attr("href")'
        tag_selector = 'li.post-item::attr("class")'

        next_page_selector = 'span.last-page a::attr("href")'
        next_page = response.css(next_page_selector).get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        for element in response.css(news_content_selector):
            items = self.set_config_values(items)
            items['hour'] = '00:00'
            items['title'] = element.css(title_selector).get()
            items['link'] = element.css(link_selector).get()
            items['tag'] = self.get_category_from_class_attr(element.css(tag_selector).get())
            yield items

        if next_page is not None:
            yield response.follow(next_page, self.parse)
        """
        for page in response.css(next_page_selector):
            yield response.follow(page, callback=self.parse)
        """
