# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaocheItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 列表页
    title = scrapy.Field()  # 标题
    reg_date = scrapy.Field()  # 上牌日期
    mile = scrapy.Field()  # 公里数
    price = scrapy.Field()  # 优惠价格
    all_price = scrapy.Field()  # 全款价格
    detail_url = scrapy.Field()  # 详情url
    # 详情页
    city_name = scrapy.Field()  # 城市名称
    pic = scrapy.Field()  # 图片
    displace = scrapy.Field()  # 排量
    source_id = scrapy.Field()  # 车源号
    name = scrapy.Field()


