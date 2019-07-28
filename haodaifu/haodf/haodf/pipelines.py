# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from redis import StrictRedis

class HaodfPipeline(object):
    def open_spider(self,spide):
        self.con = StrictRedis(host='localhost',port=6379,db=0,password='')
        pass
    def process_item(self, item, spider):
        self.res = self.con.lpush('urls',item['url'])
        return item
    def close_spider(self,spider):
        pass

from pymongo import MongoClient
class HaodfPipeline1(object):
    def open_spider(self,spide):
        self.con = MongoClient('localhost', 27017)
        self.db = self.con.hdf
        self.collection = self.db.hdf
        pass
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
    def close_spider(self,spider):
        self.con.close()
        pass
