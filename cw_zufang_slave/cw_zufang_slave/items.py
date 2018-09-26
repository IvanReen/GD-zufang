# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CwZufangSlaveItem(scrapy.Item):
    # 标题
    title = scrapy.Field()
    # 金额
    money = scrapy.Field()
    # 整租、合租
    method = scrapy.Field()
    # 区域
    area = scrapy.Field()
    # 小区
    community = scrapy.Field()
    # 详情url
    targeturl = scrapy.Field()
    # 发布时间
    pub_time = scrapy.Field()
    # 城市
    city = scrapy.Field()
    # 电话
    phone = scrapy.Field()
    # 图片1
    img1 = scrapy.Field()
    # 图片2
    img2 = scrapy.Field()
