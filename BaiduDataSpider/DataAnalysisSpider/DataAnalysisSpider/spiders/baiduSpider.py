# -*- coding:utf-8 -*-

# builid-in module
import re
import logging
import time,random

# scrapy module
from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.http import Request

# selenium Moduel 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# spider
from DataAnalysisSpider import settings
from DataAnalysisSpider.items import DataanalysisspiderItem,RelateOrgItem,SearchResItem

# 是用了Phantomjs后，对于Scrapy的框架的整体就是无法使用了，但在yield的时候,浏览器就是关闭了
# 也就是甚至连item都不需要使用了 
import json
import codecs
from collections import OrderedDict
import pymssql
import pymongo


logging.basicConfig(
    level = logging.DEBUG,
    filename = 'SpiderLog.log',    
    format = '%(funcName)s %(lineno)d %(message)s'
)

'''

   1 针对phantomjs中出现的 : Element is not currently visible and may not be manipulated exception问题，无法找到相应的元素

     可以尝试的结局方法为设置浏览器的窗口大小: browser.set_window_size(1124, 850)

   2 使用 PhantomJS时，对框架Scrapy的问题

   3 

'''

class BaiduSpider(CrawlSpider):

    name = 'BaiduSearchSpider'

    start_urls = [
        'https://www.baidu.com',
    ]

    def __init__(self, *a, **kw):
        logging.info('#------------ Spider Start ------------#')
        self.current_page = 1
        # file
        self.jsonfile = codecs.open('JsonData.json','w',encoding='utf-8',)
        self.relatedfile = codecs.open('relatedfile.json','w',encoding='utf-8')
        # mongodb
        self.mongodb = pymongo.MongoClient(host='localhost',port=27017)
        self.db = self.mongodb['BaiduSearchSpider']
        self.siteColl = self.db['BaiduSearchDbColl']
        # mssql
        self.mssqlConn = pymssql.connect(host='localhost\\NEOSQL',user='sa',password='iamneo',database='BaiduSpiderData')
        self.cursor = self.mssqlConn.cursor()    
        # browser
        self.browser_driver = webdriver.Chrome()
        self.browser_driver = webdriver.Chrome()

        # 设置 PhantomJS的请求头
        #webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = settings.headersX['User-Agent'] #'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        #webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Language'] = settings.headersX['Accept-Language']#'zh-CN,zh;q=0.8'
        #webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Connection'] = settings.headersX['Connection'] #'keep-alive'
        #webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept'] = settings.headersX['Accept']#'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        #webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.Accept-Encoding'] = settings.headersX['Accept-Encoding']#'gzip, deflate, br'

    def start_requests(self):
        return [Request(url="https://www.baidu.com",headers=settings.headersX)] 

    def parse(self, response):
        if(response.request.url == 'https://www.baidu.com'):
            self.search_results('https://www.baidu.com','IT教育')

    def close(self,spider, reason):
        time.sleep(random.randint(3,6))
        self.browser_driver.close()
        self.jsonfile.close()
        self.relatedfile.close()
        self.mongodb.close()
        self.mssqlConn.close()
        logging.info('#----------- Spider close ------------# reason : ' + str(reason))

    def search_results(self,url,keyWord):
        self.browser_driver.get(url)
        try:
            search_input = self.browser_driver.find_element_by_css_selector('#kw')
            search_button = self.browser_driver.find_element_by_css_selector('#su')
        except Exception as ex:
            logging.error('########### find elememt error : ' +  str(ex)) 
            raise
        search_input.clear()
        search_input.send_keys(keyWord)
        search_button.click()

        WebDriverWait(self.browser_driver,20).until(EC.presence_of_element_located((By.CSS_SELECTOR,'#page > a.n')))
        try:
            relate_button = self.browser_driver.find_element_by_xpath('//*[@id="con-ar"]/div[1]/div/div/div[1]/a/i')
            relate_button.click()
        except Exception as ex:
            logging.error('########### find elememt error: ' +  str(ex)) 
            raise
        time.sleep(random.randint(1,10))

        print('--------------------------------- 刮一刮 ---------------------------------')
        self.get_releation_org()
        self.get_page_results()

    def get_releation_org(self):
        try:
            relation_orgs = Selector(text=self.browser_driver.page_source).xpath('//*[@id="con-ar"]/div[1]/div/div/div[2]')
            div_1_orgs = relation_orgs.xpath('div[1]')
            div_2_orgs = relation_orgs.xpath('div[2]')
        except Exception as ex:
            logging.error('########### find relation_orgs element error:' + str(ex))
            raise

        for div in div_1_orgs.xpath('div'):
            info = div.xpath('div[2]/a') 
            dat = dict(relation_name=''.join(tuple(info.xpath('@title').extract())),relation_url=''.join(tuple(info.xpath('@href').extract())))
            line = json.dumps(OrderedDict(dat),ensure_ascii=False,sort_keys=False) + '\n'
            self.relatedfile.write(line)

        for div in div_2_orgs.xpath('div'):
            infos = div.xpath('div') 
            for e in infos:
                x = e.xpath('div[2]/a')
                dat = dict(relation_name=''.join(tuple(x.xpath('@title').extract())),relation_url=''.join(tuple(x.xpath('@href').extract())) )
                line = json.dumps(OrderedDict(dat),ensure_ascii=False,sort_keys=False) + '\n'
                self.relatedfile.write(line)

    def get_page_results(self):
        content_left_sel = Selector(text=self.browser_driver.page_source).css('#content_left')
        div_list = content_left_sel.xpath('div[@class="result c-container "]')
        current_search_number = 1 
        for div in div_list:
            dat = ''.join( tuple(div.xpath('div[1]/div[2]/div[@class="f13"]/div[1]/@data-tools').extract()) )
            z = self.current_page
            q = current_search_number
            try:
                if len(dat) > 1 :
                    self.cursor.execute("INSERT INTO SearchResItem(res_info,res_page_num,res_page_location) VALUES (%s ,%s ,%s)",(dat,z,q) ) 
                    self.mssqlConn.commit()
            except pymssql.Error as e:
                logging.info("pymssql error: " + str(e))
                raise
            current_search_number += 1
        try:
            next_page = self.browser_driver.find_element_by_xpath('//*[@id="page"]/a[last()]')
            if self.current_page <= 200:
                self.current_page += 1
                next_page.click()
                WebDriverWait(self.browser_driver,46).until(EC.presence_of_element_located((By.XPATH,'//*[@id="page"]/a[last()]')))
                self.browser_driver.refresh()
                time.sleep(random.randint(3,6))
                self.get_page_results()
        except Exception as ex:
            logging.error('########## find elemet of next_page fail: ' + str(ex))
            raise
