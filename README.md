[![](https://img.shields.io/badge/python-3.6.3-orange.svg)](https://www.python.org/downloads/release/python-363/)
[![](https://img.shields.io/badge/scrapy-1.7.3-green.svg)](https://docs.scrapy.org/en/latest/news.html)
[![](https://img.shields.io/badge/scrapy—redis-0.6.8-blue.svg)](https://scrapy-redis.readthedocs.io/en/latest/)
[![](https://img.shields.io/badge/pymongo-3.9.0-mauve.svg)](https://pypi.org/project/pymongo/)

# scrapy分布式爬虫项目---淘车项目

## 主要功能

 - **使用redis数据库队列**
 - **使用scrapy框架运行多个spider**
 - **MongoDB数据库存储**
 - **master主机分配队列，载入任务，数据处理**
 - **多个slaver从机运行爬，结果交由主机**

