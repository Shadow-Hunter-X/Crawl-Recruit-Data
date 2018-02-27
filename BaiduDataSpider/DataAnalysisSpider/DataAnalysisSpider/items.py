# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DataanalysisspiderItem(scrapy.Item):
    org_url = scrapy.Field()
    org_title = scrapy.Field()
    org_description = scrapy.Field()
    org_keyword = scrapy.Field()
    org_footer = scrapy.Field()

class RelateOrgItem(scrapy.Item):
    relation_url = scrapy.Field()
    relation_name = scrapy.Field()

class SearchResItem(scrapy.Item):
    res_info = scrapy.Field()
    res_page_num = scrapy.Field()
    res_page_location = scrapy.Field()