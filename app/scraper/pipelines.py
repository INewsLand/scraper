# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from database.repository import MongoRepository

class MongoPipeline(object):

    def __init__(self):
        self.db_client = MongoRepository()

    def process_item(self, item, spider):
        document = self.verify_values(dict(item))
        self.db_client.insert_one(item['collection'], document)
        return item

    def verify_values(self, document):
        if document.get('tag', None) == None:
            document['tag'] = 'Unidentified'
        return document
