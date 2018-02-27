# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs 
import logging
from collections import OrderedDict
# 这里暂不下载图片
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
import pymssql
import pymongo

from DataAnalysisSpider.items import DataanalysisspiderItem,RelateOrgItem,SearchResItem

'''
   如何进行对不同的item分配对应的pipeline
    if isinstance(item, Aitem):
        pass
    elif isinstance(item, Bitem):
        pass
    else:
        pass
'''


# 导出为json文件
class DataanalysisspiderPipeline(object):

    def __init__(self, **kwargs):
        self.jsonfile = codecs.open('JsonData.json','w',encoding='utf-8',)
        self.relatedfile = codecs.open('relatedfile.json','w',encoding='utf-8')
        return super().__init__(**kwargs)

    def process_item(self, item, spider):
        if isinstance(item,RelateOrgItem):
            line = json.dumps(OrderedDict(item),ensure_ascii=False,sort_keys=False) + '\n'
            self.relatedfile.write(line)
        else:
            line = json.dumps(OrderedDict(item),ensure_ascii=False,sort_keys=False) + '\n'
            self.jsonfile.write(line)
        return item

    def close_spider(self,spider):
        self.jsonfile.close()
        self.relatedfile.close()

# 数据到mongodb 
class MongoDbPipelineX(object):

    def __init__(self, **kwargs):
        try:
            self.mongodb = pymongo.MongoClient(host='localhost',port=27017)
            self.db = self.mongodb['BaiduSearchDB']
            self.siteColl = self.db['WebsiteCollection']
        except Exception as ex:
            logging.error(str(ex))

    def process_item(self, item, spider):
        if isinstance(item,SearchResItem):
            self.siteColl.insert(dict(item))

    def close_spider(self,spider):
        self.mongodb.close()

# 数据到sqlserver
class MsSqlPipelineX(object):

    def __init__(self, **kwargs):
        try:
            self.mssqlConn = pymssql.connect(host='localhost\\NEOSQL',user='sa',password='iamneo',database='Spider')
            self.cursor = self.mssqlConn.cursor()    
        except Exception as ex:
            logging.error(str(ex)) 

    def process_item(self, item, spider):
        try:
            self.cursor.execute('')
            self.mssqlConn.commit()
        except Exception as ex:
            logging.error(str(ex))

    def close_spider(self,spider):
        self.mssqlConn.close()