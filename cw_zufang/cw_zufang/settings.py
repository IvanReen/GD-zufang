# -*- coding: utf-8 -*-
BOT_NAME = 'cw_zufang'

SPIDER_MODULES = ['cw_zufang.spiders']
NEWSPIDER_MODULE = 'cw_zufang.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cw_zufang (+http://www.yourdomain.com)'
#item Pipeline同时处理item的最大值为100
# CONCURRENT_ITEMS=100
#scrapy downloader并发请求最大值为16
#CONCURRENT_REQUESTS=4
#对单个网站进行并发请求的最大值为8
#CONCURRENT_REQUESTS_PER_DOMAIN=2
#抓取网站的最大允许的抓取深度值
DEPTH_LIMIT=0
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
DOWNLOAD_TIMEOUT=10
DNSCACHE_ENABLED=True
#避免爬虫被禁的策略1，禁用cookie
# Disable cookies (enabled by default)
COOKIES_ENABLED = False
CONCURRENT_REQUESTS=4
#CONCURRENT_REQUESTS_PER_IP=2
#CONCURRENT_REQUESTS_PER_DOMAIN=2
#设置下载延时，防止爬虫被禁
DOWNLOAD_DELAY = 5
DOWNLOADER_MIDDLEWARES = {
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    "cw_zufang.proxy_mw.ProxyMiddleware":100,
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.chunked.ChunkedTransferMiddleware': 830,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'cw_zufang.timeout_mw.Timeout_Middleware':610,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': None,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 300,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': None,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 400,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': None,
    'cw_zufang.userAgent_mw.RotateUserAgentMiddleware':400,
    'cw_zufang.redirect_mw.Redirect_Middleware':500,

}
#使用scrapy-redis组件，分布式运行多个爬虫


#配置日志存储目录
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'
REDIS_URL = None
REDIS_HOST = '127.0.0.1' # 也可以根据情况改成 localhost
REDIS_PORT = '6379'
#LOG_FILE = "logs/scrapy.log"

