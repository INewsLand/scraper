# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class Feed(scrapy.Item):
    name = scrapy.Field()
    domain = scrapy.Field()
    collection = scrapy.Field()
    createdAt = scrapy.Field()
    hour = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    tag = scrapy.Field()

class News(scrapy.Item):
    name = scrapy.Field()
    domain = scrapy.Field()
    collection = scrapy.Field()
    createdAt = scrapy.Field()
    hour = scrapy.Field()
    date = scrapy.Field()
    author = scrapy.Field()
    title = scrapy.Field()
    subTitle = scrapy.Field()
    principalImage = scrapy.Field()
    text = scrapy.Field()
    link = scrapy.Field()
    tag = scrapy.Field()
    tags = scrapy.Field()
