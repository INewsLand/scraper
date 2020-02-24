import scrapy
from datetime import datetime 
from utils.text import normalize_titles
from scraper.items import Feed


class SDPNoticiasFeedSpider(scrapy.Spider):
    name = 'SDPNoticias:Feed'
    allowed_domains = [
        'sdpnoticias.com/'
    ]
    start_urls = [
        'https://www.sdpnoticias.com/internacional'
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

    def parse(self, response):
        items = Feed()

        news_content_selector = 'div.main.container > div.category-boards > div#m20-18-21'
        
        title_selector = 'div.articleDetails > div.title-container > h2.title::text'
        link_selector = 'a.link-container::attr(href)'
        tag_selector = link_selector
        """
        title_selector = 'div.articleDetails > div.title-container > h2::text'
        link_selector = 'a.link-container::attr(href)'
        tag_selector = link_selector
        """
       # print((response.css(news_content_selector).getall()[0]))
        for element in response.css(news_content_selector):
            print("TITULOS")
            print((element.css(title_selector).getall()))

            items = self.set_config_values(items)
            items['hour'] = '-1'
            items['title'] = (element.css(title_selector).get())
            items['link'] = element.css(link_selector).get()
            items['tag'] = ( element.css(tag_selector).get())
            yield items

            
        next_page_selector = 'li.see-more>a::attr("href")'

        for page in response.css(next_page_selector):
            yield response.follow(page, callback=self.parse)
