# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import traceback

from pymongo import MongoClient
from scrapy.exceptions import DropItem


class CwZufangSlavePipeline(object):
    MONGODB_SERVER = "127.0.0.1"
    MONGODB_PORT = 27017
    MONGODB_DB = "zufang_cw"

    def __init__(self):
        # 连接mongodb
        try:
            client = MongoClient(self.MONGODB_SERVER, self.MONGODB_PORT)
            self.db = client[self.MONGODB_DB]
        except Exception as e:
            traceback.print_exc()

    @classmethod
    def from_crawler(cls, crawler):
        cls.MONGODB_SERVER = crawler.settings.get('SingleMONGODB_SERVER', '127.0.0.1')
        cls.MONGODB_PORT = crawler.settings.get('SingleMONGODB_PORT', 27017)
        cls.MONGODB_DB = crawler.settings.get('SingleMONGODB_DB', 'zufang_cw')
        pipe = cls()
        pipe.crawler = crawler
        return pipe

    def process_item(self, item, spider):
        if item['pub_time'] == 0:
            raise DropItem(f"Duplicate item found: {item}")
        if item['method'] == 0:
            raise DropItem(f"Duplicate item found: {item}")
        if item['community']==0:
            raise DropItem(f"Duplicate item found: {item}")
        if item['money']==0:
            raise DropItem(f"Duplicate item found: {item}")
        if item['area'] == 0:
            raise DropItem(f"Duplicate item found: {item}")
        if item['city'] == 0:
            raise DropItem(f"Duplicate item found: {item}")
        # if item['phone'] == 0:
        #     raise DropItem("Duplicate item found: %s" % item)
        # if item['img1'] == 0:
        #     raise DropItem("Duplicate item found: %s" % item)
        # if item['img2'] == 0:
        #     raise DropItem("Duplicate item found: %s" % item)
        zufang_detail = {
            'title': item.get('title'),
            'money': item.get('money'),
            'method': item.get('method'),
            'area': item.get('area', ''),
            'community': item.get('community', ''),
            'targeturl': item.get('targeturl'),
            'pub_time': item.get('pub_time', ''),
            'city':item.get('city',''),
            'phone':item.get('phone',''),
            'img1':item.get('img1',''),
            'img2':item.get('img2',''),
        }
        result = self.db['zufang_detail'].insert(zufang_detail)
        print('[success] the '+item['targeturl']+'wrote to MongoDB database')
        return item
