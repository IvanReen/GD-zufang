# -*- coding: utf-8 -*-
from scrapy import Selector
from scrapy_redis.spiders import RedisSpider


class testSpider(RedisSpider):
    name = 'iptest'
    redis_key = 'iptest'
    def parse(self, response):
        response_selector = Selector(response)
        code = response_selector.xpath('//div[contains(@class,"well")]/p[1]/code/text()')
        print(code)