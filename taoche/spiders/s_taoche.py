# -*- coding: utf-8 -*-
import scrapy
import re
from taoche.spiders.city import CITY_CODE,CAR_CODE_LIST
from lxml import etree
from taoche.items import TaocheItem
from scrapy_redis.spiders import RedisSpider # 导入RedisSpider
# 城市编码
city_code = CITY_CODE
# 车 品牌列表
car_code_list = CAR_CODE_LIST
# for city in city_code:
#     for car in car_code_list:
#         url = f'https://{city}.taoche.com/{car}/?page='
#         print(url)
# print(len(city_code)*len(car_code_list))

# class STaocheSpider(scrapy.Spider):
class STaocheSpider(RedisSpider):
    name = 's_taoche'
    redis_key = 'taoche:start_urls'
    # allowed_domains = ['taoche.com']
    # start_urls = ['https://beijing.taoche.com/all/?page=1']
    # https://beijing.taoche.com/all/?page=2
    # https://beijing.taoche.com/audi/?page=2#pagetag
    # 暂时没有找到符合条件的二手车
    # 'class="pages-next"'
    # 'class="pages-next pages-disabled"'
    def parse(self, response):
        # print("----",response.url)
        # html = response.body.decode('utf-8')
        page = response.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()').extract()
        if len(page) > 0:
            page = page[0]
        else:
            page = 1
        # tree = etree.HTML(response.body.decode('utf-8'))
        # page = tree.xpath('//div[@class="paging-box the-pages"]/div/a[last()-1]/text()')
        # print("========",page)
        for p in range(1,int(page)+1):
            url = response.url + '?page=%s'%p
            # print("+++++++++",url)
            yield scrapy.Request(url=url,callback=self.parse_list)





    def parse_list(self, response):
        # with open('taoche.html','w',encoding='utf-8')as fp:
        #     fp.write(response.body.decode('utf-8'))
        # li_list = response.xpath('//div[@id="container_base"]/ul/li')
        # html = response.body.decode('utf-8')
        tree = etree.HTML(response.body.decode('utf-8'))
        # 判断列表页是否有数据
        data = tree.xpath('//div[@id="container_base"]')
        if data:
            # tree = etree.HTML(response.body.decode('utf-8'))
            # 汽车信息盒子列表
            li_list = tree.xpath('//div[@id="container_base"]/ul/li')
            print("-------",len(li_list))
            for li in li_list:
                # 实例化item
                item = TaocheItem()
                # -----列表页
                # 标题
                title = li.xpath('./div[@class="gongge_main"]/a/span/text()')[0]
                print("-------",title)
                # 上牌日期
                reg_date = li.xpath('./div[@class="gongge_main"]/p/i[1]/text()')[0]
                print("-------", reg_date)
                # 公里数
                mile = li.xpath('./div[@class="gongge_main"]/p/i[2]/text()')[0]
                print("-------", mile)
                # 优惠价格
                price = li.xpath('.//div[@class="price"]/i[@class="Total brand_col"]//text()')
                price = ''.join(price)
                print("-------", price)
                # 全款价格
                all_price = li.xpath('.//div[@class="price"]/i[@class="onepaynor"]/text()')[0]
                all_price = re.findall(r'原价(.*)',all_price)[0]
                print("-------", all_price)
                # 详情页url
                detail_url = li.xpath('./div[@class="gongge_main"]/a/@href')[0]
                detail_url = 'https:' + detail_url
                print("-------", detail_url)

                # item数据
                item['title'] = title
                item['reg_date'] = reg_date
                item['mile'] = mile
                item['price'] = price
                item['all_price'] = all_price
                item['detail_url'] = detail_url

                yield scrapy.Request(
                    url=detail_url,
                    callback=self.parse_detail,
                    meta={'data':item},
                    dont_filter=False
                )
            else:
                pass

    def parse_detail(self, response):
        # 继承上面的item
        item = response.meta['data']
        # with open('car_detail.html','w',encoding='utf-8')as fp:
        #     fp.write(response.body.decode('utf-8'))
        tree = etree.HTML(response.body.decode('utf-8'))
        # 城市名称
        city_name = tree.xpath('//div[@class="summary-attrs"]/dl[last()]/dd/text()')[0]
        print("-------", city_name)
        # 图片
        pic = tree.xpath('//ul[@id="taoche-details-piclist"]/li/img/@data-src')
        # print("-------", pic)
        # 排量
        displace = tree.xpath('//div[@class="summary-attrs"]/dl[3]/dd/text()')[0]
        displace = re.findall(r'(.*?)/.*?',displace)[0]
        print("-------", displace)
        # 车源号
        source_id = tree.xpath('//span[@class="car-number"]/text()')[0]
        source_id = re.findall(r'车源号：(\d+)',source_id)[0]
        print("-------", source_id)

        item['city_name'] = city_name
        item['pic'] = pic
        item['displace'] = displace
        item['source_id'] = source_id
        item['name'] = 'zz'
        yield item
