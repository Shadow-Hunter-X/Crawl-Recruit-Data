# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DataanalysisxItem(scrapy.Item):
    title_name = scrapy.Field()
    company_name = scrapy.Field()
    title_salary = scrapy.Field()
    company_address = scrapy.Field()
    issuer_date = scrapy.Field()
    work_experience = scrapy.Field()
    education_background = scrapy.Field()
    company_scale = scrapy.Field()
    company_type = scrapy.Field()
    job_introuduce = scrapy.Field()

    job_tag = scrapy.Field()
    job_sub_tag = scrapy.Field()
    page_num = scrapy.Field()
    index_num = scrapy.Field()
    crawl_date = scrapy.Field()