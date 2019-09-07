# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class TaochePipeline(object):
    def process_item(self, item, spider):
        return item

class TaocheMongoPipeline(object):
    def __init__(self):
        # 创建客户端
        # self.client = pymongo.MongoClient(host='10.10.21.184',port=27017)
        self.client = pymongo.MongoClient(host='127.0.0.1',port=27017)
        # 创建数据库
        self.db = self.client['taoche']
        # 创建集合
        self.collection = self.db['car']
    def process_item(self, item, spider):
        print("="*30)
        self.collection.insert(dict(item))
        return item
