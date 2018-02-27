# -*- coding: utf-8 -*-

# Scrapy settings for DataAnalysisX project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'DataAnalysisX'

SPIDER_MODULES = ['DataAnalysisX.spiders']
NEWSPIDER_MODULE = 'DataAnalysisX.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'DataAnalysisX (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'zh-CN',
#   'Content-Type':'charset=UTF-8',
#   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DataAnalysisX.middlewares.DataanalysisxSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'DataAnalysisX.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'DataAnalysisX.pipelines.DataanalysisxPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
headersX = {
        "Connection": "keep-alive",
        "Accept-Language": "zh-CN",
        "Content-Type":"charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
}

page_x = { 
    'sj2037':['软件','网站架构设计师'],
    'sj2040':['软件','Java开发工程师'],
    'sj044':['软件','高级软件工程师'],
    'sj045':['软件','软件工程师'],
    'sj079':['软件','软件开发工程师'],
    'sj665':['软件','需求工程师'],
    'sj667':['软件','系统架构设计师'],
    'sj668':['软件','系统分析师'],
    'sj047':['软件','数据库开发工程师'],
    'sj048':['软件','ERP技术'],
    'sj3043':['软件','ERP开发应用'],
    'sj5124':['软件','安卓软件开发'],
    'sj5125':['软件','APP软件开发'],
    'sj5126':['软件','IOS软件开发'],
    'sj5127':['软件','JAVA软件开发'],
    'sj5128':['软件','敏捷开发'],
    'sj5129':['软件','手机软件开发'],
    'sj5130':['软件','游戏软件开发'],
    'sj5131':['软件','ERP软件开发'],
    'sj5132':['软件','C++软件开发'],
    'sj5133':['软件','GIS软件开发'],
    'sj5134':['软件','APK软件开发'],
    'sj5135':['软件','LINUX软件开发'],
    'sj5136':['软件','PHP软件开发'],
    'sj5137':['软件','OA软件开发'],
    'sj5138':['软件','C#软件开发'],
    'sj5139':['软件','VB软件开发'],
    'sj5140':['软件','.NET软件开发'],
    'sj5141':['软件','P2P软件开发'],
    'sj5142':['软件','DSP软件开发'],
    'sj5143':['软件','MAC软件开发'],
    'sj5147':['软件','游戏设计师'],
    'sj5148':['软件','手机游戏开发'],
    'sj5149':['软件','Html5游戏开发'],
    'sj5150':['软件','Unity3d游戏开发'],
    'sj5151':['软件','网络游戏开发'],
    'sj5152':['软件','游戏策划师'],
    'sj5153':['软件','软件界面设计'],
    'sj2034':['软件','算法工程师'],
    'sj2038':['软件','IOS开发工程师'],
    'sj2036':['软件','计算机辅助设计师'],
    'sj2041':['软件','PHP开发工程师'],
    'sj2043':['软件','脚本开发工程师'],
    'sj2039':['软件','Android开发工程师'],
    'sj2042':['软件','C语言开发工程师'],
    'sj2035':['软件','仿真应用工程师'],
    'sj672':['软件','游戏界面设计'],
    'sj040':['IT运维','信息技术经理'],
    'sj041':['IT运维','信息技术专员'],
    'sj058':['IT运维','IT技术支持经理'],
    'sj315':['IT运维','IT技术支持'],
    'sj1012':['IT运维','IT维护工程师'],
    'sj046':['IT运维','系统工程师'],
    'sj051':['IT运维','系统管理员'],
    'sj055':['IT运维','网络工程师'],
    'sj388':['IT运维','网络管理员'],
    'sj059':['IT运维','网络与信息安全工程师'],
    'sj389':['IT运维','数据库管理员'],
    'sj678':['IT运维','计算机硬件维护工程师'],
    'sj551':['IT运维','ERP实施顾问'],
    'sj690':['IT运维','IT技术文员'],
    'sj4024':['IT运维','IT技术助理'],
    'sj699':['IT运维','IT文档工程师'],
    'sj698':['IT运维','Helpdesk'],
    'sj840':['IT运维','算法工程师'],
    'sj6010':['IT运维','IT运维管理'],
    'sj6011':['IT运维','企业IT运维'],
    'sj6012':['IT运维','IT运维工程师'],
    'sj5157':['系统集成','系统集成项目管理工程师'],
    'sj666':['系统集成','系统集成工程师'],
    'sj5158':['系统集成','系统集成项目经理'],
    'sj5159':['系统集成','系统集成项目管理师'],
    'sj5160':['系统集成','系统集成项目工程师'],
    'sj5161':['系统集成','信息系统集成项目管理工程师'],
    'sj5162':['系统集成','系统集成管理工程师'],
    'sj5163':['系统集成','系统集成师'],
    'sj5164':['系统集成','系统集成'],
    'sj060':['系统集成','仿真应用工程师'],
    'sj052':['运营管理','网站运营管理'],
    'sj670':['运营管理','网站运营专员'],
    'sj1057':['运营管理','网络运营助理'],
    'sj056':['运营管理','网站编辑'],
    'sj552':['运营管理','搜索引擎优化'],
    'sj3041':['运营管理','网络营销'],
    'sj556':['运营管理','网络编辑'],
    'sj5174':['运营管理','运营管理'],
    'sj5175':['运营管理','企业运营管理'],
    'sj5177':['运营管理','电子商务运营管理'],
    'sj2064':['IT质量管理','游戏测试'],
    'sj2063':['IT质量管理','标准化工程师'],
    'sj693':['IT质量管理','IT质量管理经理'],
    'sj049':['IT质量管理','IT质量管理工程师'],
    'sj694':['IT质量管理','系统测试'],
    'sj695':['IT质量管理','软件测试'],
    'sj696':['IT质量管理','硬件测试'],
    'sj868':['IT质量管理','配置管理工程师'],
    'sj692':['IT质量管理','信息技术标准化工程师'],
    'sj561':['IT质量管理','故障分析工程师'],
    'sj6001':['IT质量管理','全面质量管理'],
    'sj6002':['IT质量管理','项目质量管理'],
    'sj2065':['IT质量管理','手机维修'],
    'sj053':['互联网开发','互联网软件工程师'],
    'sj679':['互联网开发','手机软件开发工程师'],
    'sj687':['互联网开发','嵌入式软件开发'],
    'sj863':['互联网开发','移动互联网开发'],
    'sj864':['互联网开发','WEB前端开发'],
    'sj317':['互联网开发','语音开发'],
    'sj4028':['互联网开发','视频开发'],
    'sj4029':['互联网开发','图形开发'],
    'sj669':['互联网开发','UI设计'],
    'sj861':['互联网开发','用户体验'],
    'sj4053':['互联网开发','UE设计'],
    'sj4054':['互联网开发','UX设计'],
    'sj054':['互联网开发','网页设计'],
    'sj4066':['互联网开发','网页制作'],
    'sj4067':['互联网开发','美工'],
    'sj057':['互联网开发','游戏设计'],
    'sj4083':['互联网开发','游戏开发'],
    'sj671':['互联网开发','游戏策划'],
    'sj867':['互联网开发','游戏界面设计'],
    'sj5156':['互联网开发','前端开发']
}


start_urls_x = [        
        'http://jobs.zhaopin.com/sj2037/',
        'http://jobs.zhaopin.com/sj665/',
        'http://jobs.zhaopin.com/sj667/',
        'http://jobs.zhaopin.com/sj668/',
        'http://jobs.zhaopin.com/sj047/',
        'http://jobs.zhaopin.com/sj048/',
        'http://jobs.zhaopin.com/sj3043/',
        'http://jobs.zhaopin.com/sj5124/',
        'http://jobs.zhaopin.com/sj5125/',
        'http://jobs.zhaopin.com/sj5126/',
        'http://jobs.zhaopin.com/sj5127/',
        'http://jobs.zhaopin.com/sj5128/',
        'http://jobs.zhaopin.com/sj5129/',
        'http://jobs.zhaopin.com/sj5130/',
        'http://jobs.zhaopin.com/sj5131/',
        'http://jobs.zhaopin.com/sj5132/',
        'http://jobs.zhaopin.com/sj5133/',
        'http://jobs.zhaopin.com/sj5134/',
        'http://jobs.zhaopin.com/sj5136/',
        'http://jobs.zhaopin.com/sj5138/',
        'http://jobs.zhaopin.com/sj5139/',
        'http://jobs.zhaopin.com/sj5140/',
        'http://jobs.zhaopin.com/sj5142/',
        'http://jobs.zhaopin.com/sj5143/',
        'http://jobs.zhaopin.com/sj5147/',
        'http://jobs.zhaopin.com/sj5148/',
        'http://jobs.zhaopin.com/sj5149/',
        'http://jobs.zhaopin.com/sj5150/',
        'http://jobs.zhaopin.com/sj5151/',
        'http://jobs.zhaopin.com/sj5152/',
        'http://jobs.zhaopin.com/sj5153/',
        'http://jobs.zhaopin.com/sj2034/',
        'http://jobs.zhaopin.com/sj2038/',
        'http://jobs.zhaopin.com/sj2036/',
        'http://jobs.zhaopin.com/sj2041/',
        'http://jobs.zhaopin.com/sj2043/',
        'http://jobs.zhaopin.com/sj2039/',
        'http://jobs.zhaopin.com/sj2042/',
        'http://jobs.zhaopin.com/sj2035/',
        'http://jobs.zhaopin.com/sj040/',
        'http://jobs.zhaopin.com/sj041/',
        'http://jobs.zhaopin.com/sj058/',
        'http://jobs.zhaopin.com/sj315/',
        'http://jobs.zhaopin.com/sj1012/',
        'http://jobs.zhaopin.com/sj046/',
        'http://jobs.zhaopin.com/sj051/',
        'http://jobs.zhaopin.com/sj055/',
        'http://jobs.zhaopin.com/sj388/',
        'http://jobs.zhaopin.com/sj059/',
        'http://jobs.zhaopin.com/sj389/',
        'http://jobs.zhaopin.com/sj678/',
        'http://jobs.zhaopin.com/sj551/',
        'http://jobs.zhaopin.com/sj690/',
        'http://jobs.zhaopin.com/sj4024/',
        'http://jobs.zhaopin.com/sj699/',
        'http://jobs.zhaopin.com/sj698/',
        'http://jobs.zhaopin.com/sj840/',
        'http://jobs.zhaopin.com/sj6010/',
        'http://jobs.zhaopin.com/sj6011/',
        'http://jobs.zhaopin.com/sj6012/',
        'http://jobs.zhaopin.com/sj5157/',
        'http://jobs.zhaopin.com/sj666/',
        'http://jobs.zhaopin.com/sj5158/',
        'http://jobs.zhaopin.com/sj5160/',
        'http://jobs.zhaopin.com/sj5162/',
        'http://jobs.zhaopin.com/sj5163/',
        'http://jobs.zhaopin.com/sj5164/',
        'http://jobs.zhaopin.com/sj060/',
        'http://jobs.zhaopin.com/sj052/',
        'http://jobs.zhaopin.com/sj670/',
        'http://jobs.zhaopin.com/sj1057/',
        'http://jobs.zhaopin.com/sj056/',
        'http://jobs.zhaopin.com/sj552/',
        'http://jobs.zhaopin.com/sj3041/',
        'http://jobs.zhaopin.com/sj556/',
        'http://jobs.zhaopin.com/sj5174/',
        'http://jobs.zhaopin.com/sj5175/',
        'http://jobs.zhaopin.com/sj5177/',
        'http://jobs.zhaopin.com/sj2064/',
        'http://jobs.zhaopin.com/sj2063/',
        'http://jobs.zhaopin.com/sj693/',
        'http://jobs.zhaopin.com/sj049/',
        'http://jobs.zhaopin.com/sj694/',
        'http://jobs.zhaopin.com/sj695/',
        'http://jobs.zhaopin.com/sj696/',
        'http://jobs.zhaopin.com/sj868/',
        'http://jobs.zhaopin.com/sj692/',
        'http://jobs.zhaopin.com/sj561/',
        'http://jobs.zhaopin.com/sj6001/',
        'http://jobs.zhaopin.com/sj6002/',
        'http://jobs.zhaopin.com/sj2065/',
        'http://jobs.zhaopin.com/sj053/',
        'http://jobs.zhaopin.com/sj679/',
        'http://jobs.zhaopin.com/sj687/',
        'http://jobs.zhaopin.com/sj863/',
        'http://jobs.zhaopin.com/sj864/',
        'http://jobs.zhaopin.com/sj317/',
        'http://jobs.zhaopin.com/sj4028/',
        'http://jobs.zhaopin.com/sj4029/',
        'http://jobs.zhaopin.com/sj669/',
        'http://jobs.zhaopin.com/sj861/',
        'http://jobs.zhaopin.com/sj4053/',
        'http://jobs.zhaopin.com/sj4054/',
        'http://jobs.zhaopin.com/sj054/',
        'http://jobs.zhaopin.com/sj4066/',
        'http://jobs.zhaopin.com/sj4067/',
        'http://jobs.zhaopin.com/sj057/',
        'http://jobs.zhaopin.com/sj4083/',
        'http://jobs.zhaopin.com/sj671/',
        'http://jobs.zhaopin.com/sj867/',
        'http://jobs.zhaopin.com/sj5156/'
    ]


'''
page_x_operation = {
    'sj040':['IT运维','信息技术经理'],
    'sj041':['IT运维','信息技术专员'],
    'sj058':['IT运维','IT技术支持经理'],
    'sj315':['IT运维','IT技术支持'],
    'sj1012':['IT运维','IT维护工程师'],
    'sj046':['IT运维','系统工程师'],
    'sj051':['IT运维','系统管理员'],
    'sj055':['IT运维','网络工程师'],
    'sj388':['IT运维','网络管理员'],
    'sj059':['IT运维','网络与信息安全工程师'],
    'sj389':['IT运维','数据库管理员'],
    'sj678':['IT运维','计算机硬件维护工程师'],
    'sj551':['IT运维','ERP实施顾问'],
    'sj690':['IT运维','IT技术文员'],
    'sj4024':['IT运维','IT技术助理'],
    'sj699':['IT运维','IT文档工程师'],
    'sj698':['IT运维','Helpdesk'],
    'sj840':['IT运维','算法工程师'],
    'sj6010':['IT运维','IT运维管理'],
    'sj6011':['IT运维','企业IT运维'],
    'sj6012':['IT运维','IT运维工程师'],
   
    
}

start_urls_x_operation = [
    'http://jobs.zhaopin.com/sj040/',
    'http://jobs.zhaopin.com/sj041/',
    'http://jobs.zhaopin.com/sj058/',
    'http://jobs.zhaopin.com/sj315/',
    'http://jobs.zhaopin.com/sj1012/',
    'http://jobs.zhaopin.com/sj046/',
    'http://jobs.zhaopin.com/sj051/',
    'http://jobs.zhaopin.com/sj055/',
    'http://jobs.zhaopin.com/sj388/',
    'http://jobs.zhaopin.com/sj059/',
    'http://jobs.zhaopin.com/sj389/',
    'http://jobs.zhaopin.com/sj678/',
    'http://jobs.zhaopin.com/sj551/',
    'http://jobs.zhaopin.com/sj690/',
    'http://jobs.zhaopin.com/sj4024/',
    'http://jobs.zhaopin.com/sj699/',
    'http://jobs.zhaopin.com/sj698/',
    'http://jobs.zhaopin.com/sj840/',
    'http://jobs.zhaopin.com/sj6010/',
    'http://jobs.zhaopin.com/sj6011/',
    'http://jobs.zhaopin.com/sj6012/'
]

page_x_integration = {
    'sj5157':['系统集成','系统集成项目管理工程师'],
    'sj666':['系统集成','系统集成工程师'],
    'sj5158':['系统集成','系统集成项目经理'],
    'sj5159':['系统集成','系统集成项目管理师'],
    'sj5160':['系统集成','系统集成项目工程师'],
    'sj5161':['系统集成','信息系统集成项目管理工程师'],
    'sj5162':['系统集成','系统集成管理工程师'],
    'sj5163':['系统集成','系统集成师'],
    'sj5164':['系统集成','系统集成'],
    'sj060':['系统集成','仿真应用工程师']
}

start_urls_x_integration = [
    'http://jobs.zhaopin.com/sj5157/',
    'http://jobs.zhaopin.com/sj666/',
    'http://jobs.zhaopin.com/sj5158/',
    'http://jobs.zhaopin.com/sj5159/',
    'http://jobs.zhaopin.com/sj5160/',
    'http://jobs.zhaopin.com/sj5161/',
    'http://jobs.zhaopin.com/sj5162/',
    'http://jobs.zhaopin.com/sj5163/',
    'http://jobs.zhaopin.com/sj5164/',
    'http://jobs.zhaopin.com/sj060/'
]

page_x_yunyin = {
    'sj052':['运营管理','网站运营管理'],
    'sj670':['运营管理','网站运营专员'],
    'sj1057':['运营管理','网络运营助理'],
    'sj056':['运营管理','网站编辑'],
    'sj552':['运营管理','搜索引擎优化'],
    'sj3041':['运营管理','网络营销'],
    'sj556':['运营管理','网络编辑'],
    'sj5174':['运营管理','运营管理'],
    'sj5175':['运营管理','企业运营管理'],
    'sj5177':['运营管理','电子商务运营管理']
}

start_urls_x_yunyin = [
    'http://jobs.zhaopin.com/sj052/',
    'http://jobs.zhaopin.com/sj670/',
    'http://jobs.zhaopin.com/sj1057/',
    'http://jobs.zhaopin.com/sj056/',
    'http://jobs.zhaopin.com/sj552/',
    'http://jobs.zhaopin.com/sj3041/',
    'http://jobs.zhaopin.com/sj556/',
    'http://jobs.zhaopin.com/sj5174/',
    'http://jobs.zhaopin.com/sj5175/',
    'http://jobs.zhaopin.com/sj5177/'
]

page_x_itzhil = {
    'sj2064':['IT质量管理','游戏测试'],
    'sj2063':['IT质量管理','标准化工程师'],
    'sj693':['IT质量管理','IT质量管理经理'],
    'sj049':['IT质量管理','IT质量管理工程师'],
    'sj694':['IT质量管理','系统测试'],
    'sj695':['IT质量管理','软件测试'],
    'sj696':['IT质量管理','硬件测试'],
    'sj868':['IT质量管理','配置管理工程师'],
    'sj692':['IT质量管理','信息技术标准化工程师'],
    'sj561':['IT质量管理','故障分析工程师'],
    'sj6001':['IT质量管理','全面质量管理'],
    'sj6002':['IT质量管理','项目质量管理'],
    'sj2065':['IT质量管理','手机维修']
}

start_urls_x_itzhil = [
    'http://jobs.zhaopin.com/sj2064/',
    'http://jobs.zhaopin.com/sj2063/',
    'http://jobs.zhaopin.com/sj693/',
    'http://jobs.zhaopin.com/sj049/',
    'http://jobs.zhaopin.com/sj694/',
    'http://jobs.zhaopin.com/sj695/',
    'http://jobs.zhaopin.com/sj696/',
    'http://jobs.zhaopin.com/sj868/',
    'http://jobs.zhaopin.com/sj692/',
    'http://jobs.zhaopin.com/sj561/',
    'http://jobs.zhaopin.com/sj6001/',
    'http://jobs.zhaopin.com/sj6002/',
    'http://jobs.zhaopin.com/sj2065/'
]

page_x_internetdev = {
    'sj053':['互联网开发','互联网软件工程师'],
    'sj679':['互联网开发','手机软件开发工程师'],
    'sj687':['互联网开发','嵌入式软件开发'],
    'sj863':['互联网开发','移动互联网开发'],
    'sj864':['互联网开发','WEB前端开发'],
    'sj317':['互联网开发','语音开发'],
    'sj4028':['互联网开发','视频开发'],
    'sj4029':['互联网开发','图形开发'],
    'sj669':['互联网开发','UI设计'],
    'sj861':['互联网开发','用户体验'],
    'sj4053':['互联网开发','UE设计'],
    'sj4054':['互联网开发','UX设计'],
    'sj054':['互联网开发','网页设计'],
    'sj4066':['互联网开发','网页制作'],
    'sj4067':['互联网开发','美工'],
    'sj057':['互联网开发','游戏设计'],
    'sj4083':['互联网开发','游戏开发'],
    'sj671':['互联网开发','游戏策划'],
    'sj867':['互联网开发','游戏界面设计'],
    'sj5156':['互联网开发','前端开发']
}

start_urls_x_internetdev = [
    'http://jobs.zhaopin.com/sj053/',
    'http://jobs.zhaopin.com/sj679/',
    'http://jobs.zhaopin.com/sj687/',
    'http://jobs.zhaopin.com/sj863/',
    'http://jobs.zhaopin.com/sj864/',
    'http://jobs.zhaopin.com/sj317/',
    'http://jobs.zhaopin.com/sj4028/',
    'http://jobs.zhaopin.com/sj4029/',
    'http://jobs.zhaopin.com/sj669/',
    'http://jobs.zhaopin.com/sj861/',
    'http://jobs.zhaopin.com/sj4053/',
    'http://jobs.zhaopin.com/sj4054/',
    'http://jobs.zhaopin.com/sj054/',
    'http://jobs.zhaopin.com/sj4066/',
    'http://jobs.zhaopin.com/sj4067/',
    'http://jobs.zhaopin.com/sj057/',
    'http://jobs.zhaopin.com/sj4083/',
    'http://jobs.zhaopin.com/sj671/',
    'http://jobs.zhaopin.com/sj867/',
    'http://jobs.zhaopin.com/sj5156/'
]
'''