from taoche.spiders.city import CITY_CODE,CAR_CODE_LIST

from redis import Redis
# import sys
# sys.path.append("..")
class Redis_url():

    def __init__(self):
        #1.连接客户端，
        self.re = Redis("localhost", 6379)

    def add(self,url):
        #讲url,利用lpush方法，添加到"taoche:start_urls"中
        self.re.lpush("taoche:start_urls",url)

rd = Redis_url()

# 先将redis中的requests全部清空
# flushdbRes = rd.flushdb()
for city in CITY_CODE:
    for car_code in CAR_CODE_LIST:
        rd.add( "https://{}.taoche.com/{}/".format(city, car_code))

