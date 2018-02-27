# -*-coding:utf-8 -*-

import re
import logging

from scrapy.spiders import CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
