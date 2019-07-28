# -*- coding: utf-8 -*-
from scrapy_redis.spiders import RedisSpider
from ..items import HaodfItem1,HaodfItem
# from haodf.spiders.hdf import item

class HdfjxSpider(RedisSpider):
    name = 'hdfjx'
    redis_key = 'urls'

    def parse(self, response):
        # id = item.save()
        item = HaodfItem1()
        lists = []
        datail = response.xpath('//div[@class="h_s_info_cons"]/div/text()').extract()
        print('*'*100)
        print('------',id)
        detail = ''.join(datail)
        print(detail)
        lists.append(detail)
        for i,j in enumerate(lists):
            print('-'*100)
            print(i,j)
        item['detail'] =detail
        item['con'] =id
        item.save()
        yield item
