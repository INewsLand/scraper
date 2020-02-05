import os
import pymongo

class MongoRepository:

    def __init__(self):
        self.url = os.environ['SCRAPER_DATABASE_URL']
        self.databse_name = os.environ['SCRAPER_DATABASE_NAME']

    def insert_one(self, collection, item):
        self.__get_connect(collection).insert(item)

    def __get_connect(self, collection):
        return pymongo.MongoClient(self.url)[self.databse_name][collection]
