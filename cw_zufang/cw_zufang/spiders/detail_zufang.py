# -*- coding: utf-8 -*-
import re

from scrapy import Selector
from scrapy_redis.spiders import RedisSpider

# 继承自RedisSpider，则start_urls可以从redis读取
# 继承自BaseSpider，则start_urls需要写出来
from cw_zufang.utils.result_parse import list_first_item

from cw_zufang.utils.InsertRedis import inserintotc, inserintota


class CwzufnagSpider(RedisSpider):
    name = 'cwzufang'
    # start_urls=(
    #     'http://dg.58.com/chuzu/',
    #     'http://sw.58.com/chuzu/',
    #     'http://sz.58.com/chuzu/',
    #     'http://gz.58.com/chuzu/',
    #     'http://fs.58.com/chuzu/',
    #     'http://zs.58.com/chuzu/',
    #     'http://zh.58.com/chuzu/',
    #     'http://huizhou.58.com/chuzu/',
    #     'http://jm.58.com/chuzu/',
    #     'http://st.58.com/chuzu/',
    #     'http://zhanjiang.58.com/chuzu/',
    #     'http://zq.58.com/chuzu/',
    #     'http://mm.58.com/chuzu/',
    #     'http://jy.58.com/chuzu/',
    #     'http://mz.58.com/chuzu/',
    #     'http://qingyuan.58.com/chuzu/',
    #     'http://yj.58.com/chuzu/',
    #     'http://sg.58.com/chuzu/',
    #     'http://heyuan.58.com/chuzu/',
    #     'http://yf.58.com/chuzu/',
    #     'http://chaozhou.58.com/chuzu/',
    #     'http://taishan.58.com/chuzu/',
    #     'http://yangchun.58.com/chuzu/',
    #     'http://sd.58.com/chuzu/',
    #     'http://huidong.58.com/chuzu/',
    #     'http:// boluo.58.com/chuzu/',
    # )
    # redis_key = 'tczufangCrawler:start_urls'
    # 解析从start_urls下载返回的页面
    # 页面页面有两个目的：
    # 第一个：解析获取下一页的地址，将下一页的地址传递给爬虫调度器，以便作为爬虫的下一次请求
    # 第二个：获取详情页地址，再对详情页进行下一步的解析
    redis_key = 'start_urls'
    def parse(self, response):
        # 获取所访问的url
        response_url = re.findall('^http\:\/\/\w+\.58\.com', response.url)
        response_selector = Selector(response)
        next_link = list_first_item(response_selector.xpath('//div[contains(@class,"pager")]/a[contains(@class,"next")]/@href').extract())
        detail_link = response_selector.xpath('//div[contains(@class,"listBox")]/ul[contains(@class,"listUl")]/li/@logr').extract()
        if next_link and detail_link:
            inserintotc(next_link, 1)
            print(
                f'#########[success] the next link {next_link} is insert into the redis queue#########'
            )

        for detail_link in response_selector.xpath('//div[contains(@class,"listBox")]/ul[contains(@class,"listUl")]/li/@logr').extract():
            print(detail_link.split('_')[3])
            detail_link = 'https://dg.58.com/zufang/' + detail_link.split('_')[3] + 'x.shtml'
            print(detail_link)
            if detail_link:
                inserintota(detail_link, 2)
                print(
                    f'[success] the detail link {detail_link} is insert into the redis queue'
                )