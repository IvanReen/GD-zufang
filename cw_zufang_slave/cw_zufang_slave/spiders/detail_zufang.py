import re

from scrapy import Selector
from scrapy_redis.spiders import RedisSpider

from cw_zufang_slave.items import CwZufangSlaveItem

from cw_zufang_slave.utils.result_parse import list_first_item


class CwzufangSpider(RedisSpider):
    name = 'cwzufang'
    redis_key = 'cwzufang_cw:requests'

    def parse(self, response):
        cwzufangItem = CwZufangSlaveItem()
        response_url = re.findall('^http\:\/\/\w+\.58\.com', response.url)
        response_selector = Selector(response)

        raw_title = list_first_item(response_selector.xpath('//div[contains(@class,"house-title")]/h1[contains(@class,"c_333 f20")]/text()').extract())
        if raw_title:
            cwzufangItem['title'] = raw_title.encode('utf8')

        raw_time = list_first_item(response_selector.xpath('//div[contains(@class,"house-title")]/p[contains(@class,"house-update-info c_888 f12")]/text()').extract())
        try:
            cwzufangItem['pub_time'] = re.findall('\d+\-\d+\-\d+\s+\d+\:\d+\:\d+', raw_time)[0]
        except:
            cwzufangItem['pub_time'] = 0

        cwzufangItem['money'] = list_first_item(response_selector.xpath('//div[contains(@class,"house-pay-way f16")]/span[contains(@class,"c_ff552e")]/b[contains(@class,"f36")]/text()').extract())

        raw_method = list_first_item(response_selector.xpath('//ul[contains(@class,"f14")]/li[1]/span[2]/text()').extract())
        try:
            cwzufangItem['method'] = raw_method.encode('utf8')
        except:
            cwzufangItem['method'] = 0

        try:
            area = response_selector.xpath('//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[1]
        except:
            area = ''
        if area:
            area = area
        try:
            area2 = response_selector.xpath('//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[2]
        except:
            area2 = ''
        raw_area = area + '-' + area2
        if raw_area:
            raw_area = raw_area.encode('utf8')
        cwzufangItem['area'] = raw_area if raw_area else None

        try:
            raw_community = response_selector.xpath('//ul[contains(@class,"f14")]/li/span/a[contains(@class,"c_333")]/text()').extract()[0]
            if raw_community:
                raw_community = raw_community.encode('utf8')
            cwzufangItem['community'] = raw_community if raw_community else None
        except:
            cwzufangItem['community'] = 0

        cwzufangItem['targeturl'] = response.url

        cwzufangItem['city'] = response.url.split('//')[1].split('.')[0]

        try:
            cwzufangItem['phone'] = response_selector.xpath('//div[contains(@class,"house-fraud-tip")]/span[1]/em[contains(@class,"phone-num")]/text()').extract()[0]
        except:
            cwzufangItem['phone'] = 0

        try:
            cwzufangItem['img1'] = response_selector.xpath('//ul[contains(@class,"pic-list-wrap pa")]/li[1]/@data-src').extract()[0]
        except:
            cwzufangItem['img1'] = 0

        try:
            cwzufangItem['img2'] = response_selector.xpath('//ul[contains(@class,"pic-list-wrap pa")]/li[2]/@data-src').extract()[0]
        except:
            cwzufangItem['img2'] = 0
        yield cwzufangItem