import scrapy
from datetime import datetime 
from utils.text import normalize_titles
from scraper.items import Feed


class SDPNoticiasFeedSpider(scrapy.Spider):
    name = 'SDPNoticias:Feed'
    allowed_domains = [
        'www.sdpnoticias.com'
    ]
    start_urls = [
        'https://www.sdpnoticias.com/internacional',
        'https://www.sdpnoticias.com/nacional',
        'https://www.sdpnoticias.com/deportes',
        'https://www.sdpnoticias.com/negocios',
        'https://www.sdpnoticias.com/tecnologia',
        'https://www.sdpnoticias.com/estilo-de-vida',
        'https://www.sdpnoticias.com/sexxion',
        'https://www.sdpnoticias.com/diversidad',
        'https://www.sdpnoticias.com/geek',
        'https://www.sdpnoticias.com/sorprendente'
    ]

    def get_tag(self,url=""):
        url = url.split('\x2f')
        print("URL _ " , url)
        return url[1]

    def set_config_values(self, items):
        items['name'] = 'SDP Noticias'
        items['domain'] = 'sdpnoticias.com'
        items['collection'] = 'Feed'
        items['createdAt'] = datetime.now()
        return items

    def get_tag(self,url=""):
        url = url.split('\x2f')
        return url[1]


    def parse(self, response):
        items = Feed()
        news_content_selector = 'article.articleModule' 
        title_selector = 'h2.title::text'
        link_selector = 'a.page-link::attr(href)'
        tag_selector = link_selector
        next_page_selector = 'li.see-more>a::attr("href")'
        
        for element in response.css(news_content_selector): 
            items = self.set_config_values(items)
            items['hour'] = '-1'
            title = element.css(title_selector).get()
            if title != " " :
                items['title'] = title
            else:
                items['title'] = element.css('h2.title *::text').getall()[1]

            items['link'] = element.css(link_selector).get()
            items['tag'] = self.get_tag( element.css(tag_selector).get())
            yield items
 
        for page in response.css(next_page_selector):
            yield response.follow(page, callback=self.parse)
        