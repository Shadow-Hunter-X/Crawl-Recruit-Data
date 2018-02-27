# -*-coding:utf-8-*-

import re
import logging
import time

from scrapy.spider import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from DataAnalysisX.items import DataanalysisxItem
from DataAnalysisX.settings import *


logging.basicConfig(
    level = logging.DEBUG,
    filename = 'myblogspider.log',
    datefmt  = '%a %d %b %Y %H:%M:%S',
    format = '(asctime)s %(filename)s %(lineno)d %(message)s'
)

class SoftwareSpider(CrawlSpider):

    name = 'SoftwareSpider'

    allowed_doamins = [
        'jobs.zhaopin.com'
    ]

    def __init__(self, *a, **kw):
        self.first = True
        self.pages = 1
        self.current_page = 1 
        #self.page_url = page_url
        self.acmum = 0
        self.url_index = 120
        self.current_url_index = 0
        
    # 使用start_requests函数会使 start_urls失效
    def start_requests(self):
        logging.info('#---------- Start Spider -----------#')
        return [Request(url=start_urls_x[self.current_url_index],headers=headersX)]

    # 第一次进行解析时，读取页面数
    #def parse_start_url(self, response):
    #    return super().parse_start_url(response)

    # 只是完成
    def parse(self, response):
        sel = Selector(response = response)
        sign = 0
        # 首先获取页面总数
        if(self.first):
            try:
                total = sel.css('body > div.main > div.main-left-outer > form > div > div')
                if(total.xpath('input[1]') is not None):
                    self.pages = int(''.join(tuple(total.xpath('input[1]/@value').extract())))
                    if(self.pages >= 8):
                        self.acmum = 8 
                        sign = 1
                    else:
                        self.acmum = 0
                else:
                    self.acmum = 1
            except Exception as E:
                self.pages = 1
                logging.error(str(E))
                self.first = False

        
        index_num = 1
        if(sign == 1):
            job_li = sel.css('body > div.main > div.main-left-outer > form > div > ul > li')
            for div in job_li.xpath('div'):
                class_value = (''.join(tuple(div.xpath('@class').extract()))).strip()
                if class_value == 'details_container bg_container' or class_value == 'details_container  ':
                    item = DataanalysisxItem()
                    item['title_name'] = ''.join(tuple(div.xpath('span[1]/a/text()').extract()))
                    item['company_name'] = ''.join(tuple(div.xpath('span[2]/a/text()').extract()))
                    item['title_salary'] = ''.join(tuple(div.xpath('span[3]/text()').extract()))
                    item['company_address'] = ''.join(tuple(div.xpath('span[4]/a/text()').extract()))
                    item['issuer_date'] = '20'+''.join(tuple(div.xpath('span[5]/text()').extract()))
                    item['work_experience'] = ''.join(tuple(div.xpath('div/div[1]/span[1]/text()').extract()))
                    item['education_background'] = ''.join(tuple(div.xpath('div/div[1]/span[2]/text()').extract()))
                    item['company_scale'] = ''.join(tuple(div.xpath('div/div[1]/span[3]/text()').extract()))
                    item['company_type'] = ''.join(tuple(div.xpath('div/div[1]/span[4]/text()').extract()))
                    item['job_introuduce'] = ''.join(tuple(div.xpath('div/div[1]/p[1]/text()').extract()))

                    item['page_num'] = self.current_page
                    item['index_num'] = index_num
                    item['crawl_date'] = time.strftime("%Y/%m/%d %H:%M",time.localtime())
                
                    ar = response.url.split('/')
                    item['job_tag'] = page_x[ar[3]][0]
                    item['job_sub_tag'] = page_x[ar[3]][1]
                    url_z = ar[0] + "//" + ar[2] + "/" + ar[3]
                    index_num += 1
                    yield item

        if(self.current_page < self.acmum):
            self.current_page += 1
            now_url = url_z + "/p" + str(self.current_page) + "/"
            logging.info('#---- Request Url is : ' + now_url)
            yield Request(url=now_url,headers=headersX) 
        else:
            self.current_page = 1
            self.pages = 1
            self.first = True
            self.current_url_index += 1
            if(self.current_url_index <= self.url_index):
                yield Request(url=start_urls_x[self.current_url_index],headers=headersX)

    def jump_nextpage(self,url):
        if(self.current_page < self.pages):
            self.current_page += 1
            now_url = url + "/p" + str(self.current_page) + "/"
            logging.info('#---- Request Url is : ' + now_url)
            yield Request(url=now_url,headers=headersX,callback=self.parse) 

    def close(spider, reason):
        logging.info('#---------- Close Spider -----------#')

    