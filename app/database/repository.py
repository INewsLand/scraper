import os
import pymongo

class MongoRepository:

    def __init__(self):
        self.url = os.environ['SCRAPER_DATABASE_URL']
        self.databse_name = os.environ['SCRAPER_DATABASE_NAME']

    def check_if_exists(self, collection, item):
        query = {
            'link': item['link']
        }
        return self.__get_connect(collection).find_one(query)

    def insert_one(self, collection, item):
        if self.check_if_exists(collection, item) is None:
            self.__get_connect(collection).insert(item)

    def __get_connect(self, collection):
        return pymongo.MongoClient(self.url)[self.databse_name][collection]
