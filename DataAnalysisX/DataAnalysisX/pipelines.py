# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import logging
import pymssql
import pymongo

class DataanalysisxPipeline(object):

    def __init__(self, **kwargs):
        # 连接，初始化sqlserver client
        self.mssqlClient = pymssql.connect(host='localhost\\neosql',user='sa',password='iamneo',database='ZhaopinSpiderData')
        self.sqlCursor = self.mssqlClient.cursor()
        # 连接，初始化 mongodb client
        self.mongo = pymongo.MongoClient()
        self.db = self.mongo['zhaopin']
        self.coll = self.db['jobInfor']

    def process_item(self, item, spider):
        try:
            # mssql 存储数据
            self.sqlCursor.execute("INSERT INTO JobInformation(title_name,company_name,title_salary,\
                                    company_address,issuer_date,work_experience,education_background,\
                                    company_scale,company_type,job_introuduce,job_tag,page_num,index_num,crawl_date,job_sub_tag)\
                                   VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d,%d,%s,%s)",
            (item['title_name'],item['company_name'],item['title_salary'],item['company_address'],item['issuer_date'],item['work_experience'],
             item['education_background'],item['company_scale'],item['company_type'],item['job_introuduce'],item['job_tag'],item['page_num'],item['index_num'],item['crawl_date'],item['job_sub_tag']))
            self.mssqlClient.commit()

            # mongodb存储数据
            self.coll.insert(dict(item))            

        except Exception as e:
            logging.error("store data error:" + str(e))

    def close_spider(self,spider):
        self.mssqlClient.close() 
        self.mongo.close()
