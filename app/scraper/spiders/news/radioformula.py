import scrapy 
import re 
from datetime import datetime
from utils.text import normalize_titles
from utils.text import unidecode_data
from utils.text import no_tags
from utils.text import remove_blank_lines
from scraper.items import News

class RadioFormulaNewsSpider(scrapy.Spider):
    name = 'RadioFormula:News'
    start_urls = [
        'radioformula.com.mx' 
    ]

    def __init__(self, link=None, *args, **kwargs):
        super(RadioFormulaNewsSpider, self).__init__(*args, **kwargs)
        self.start_urls = [link]

    def get_author(self, url):
        data = url.replace('https://www.radioformula.com.mx/author/','')
        data = data.replace('/','')
        data = data.replace('-',' ')
        return data

    def set_config_values(self, items):
        items['name'] = 'Radio Formula'
        items['domain'] = 'radioformula.com.mx'
        items['collection'] = 'News'
        items['createdAt'] = datetime.now()
        return items

    def parse(self, response):
        items = News()
        #item_selector = 'div.content'
        item_selector = 'div.background-overlay > div.tie-container > div.tie-wrapper >  div.content'
        title_selector = 'h1.post-title::text'
        subTitle_selector = 'h2.entry-sub-title::text'
        date_selector = 'span.date::text'
        author_selector = 'a.author-name::attr(href)'
        tag_selector = 'div.post-bottom-meta > span.tagcloud > a *::text'
        principalImage_selector = 'img.wp-post-image::attr(data-lazy-src)' 
        text_selector_all = 'article#the-post > div.entry-content >   div.css-1dbjc4n ' 

        
        items = self.set_config_values(items)
        items['link'] = str(response.request.url)
        items['title'] = normalize_titles(response.css(title_selector).get())
        items['subTitle']= normalize_titles(response.css(subTitle_selector).get())
        items['date'] =response.css(date_selector).get()
        items['hour']= '-1'
        items['author']= self.get_author(response.css(author_selector).get())
        items['tag']= response.css(tag_selector).getall()
        items['principalImage']= response.css(principalImage_selector).get()


        data = response.css(text_selector_all).getall() 
        if len(data) == 0  :
            text_selector_all = 'article#the-post > div.entry-content > p '
            data = response.css(text_selector_all).getall() 
        x = ""
        for e in data :
            x+=no_tags( remove_blank_lines( unidecode_data(e)) )

        items['text'] = x
        
        yield items