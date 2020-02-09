import scrapy
from datetime import datetime
from utils.text import remove_blank_lines
from utils.text import unidecode_data
from scraper.items import News


class ElUniversalNewsSpider(scrapy.Spider):
    name = 'El Universal News'
    allowed_domains = [
        'eluniversal.com.mx'
    ]
    start_urls = [
        'https://www.eluniversal.com.mx/cartera/twitter-se-dispara-en-wall-street-tras-anunciar-aumento-de-usuarios'
    ]

    def set_config_values(self, items):
        items['name'] = 'El Universal'
        items['domain'] = 'eluniversal.com.mx'
        items['collection'] = 'News'
        items['createdAt'] = datetime.now()
        return items

    def parse(self, response):
        items = News()

        title_selector = 'div.pane-content > h1::text'
        subTitle_selector = 'div.field.field-name-field-resumen.field-type-text-long.field-label-hidden::text'
        date_selector = 'div.fechap::text'
        hour_selector = 'div.hora::text'
        author_selector = 'div.field-item.even::text'
        tag_selector = 'span.inline.even > a::text'
        principalImage_selector = 'div.field.field-name-field-image.field-type-image.field-label-hidden > img::attr(src)'
        text_selector = 'div.pane-content > div.field.field-name-body.field-type-text-with-summary.field-label-hidden'
        tags_selector = 'div.field-content > a'

        items = self.set_config_values(items)
        items['link'] = str(response.request.url)
        items['title'] = response.css(title_selector).get()
        items['subTitle'] = response.css(subTitle_selector).get()
        items['date'] = response.css(date_selector).get()
        items['hour'] = response.css(hour_selector).get()
        items['author'] = response.css(author_selector).get()
        items['tag'] = response.css(tag_selector).get()
        items['principalImage'] = response.css(principalImage_selector).get()
        items['text'] = unidecode_data(response.css(text_selector).get())
        tags = []
        for tag in response.css(tags_selector):
            tags.append(tag.css('::text').get())
        items['tags'] = tags

        yield items
