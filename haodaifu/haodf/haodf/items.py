# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from app1.models import answer,content

# class HaodfItem(scrapy.Item):
class HaodfItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # title = scrapy.Field()
    # url = scrapy.Field()
    django_model = answer
    pass

class HaodfItem1(DjangoItem):
    # detail = scrapy.Field()
    django_model = content
    pass
