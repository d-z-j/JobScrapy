# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql
import re

# Connect to the database


import scrapy

class MycrawlingItem(scrapy.Item):
    job = scrapy.Field()
    address = scrapy.Field()
    workage = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    skill = scrapy.Field()
    education = scrapy.Field()
    pass

class MycrawlingItem2(scrapy.Item):
    job = scrapy.Field()
    address = scrapy.Field()
    workage = scrapy.Field()
    salary = scrapy.Field()
    city = scrapy.Field()
    skill = scrapy.Field()
    education = scrapy.Field()
    pass
