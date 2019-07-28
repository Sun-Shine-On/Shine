# -*- coding: utf-8 -*-
import scrapy
from haodf.items import HaodfItem

class HdfSpider(scrapy.Spider):
    name = 'hdf'
    allowed_domains = ['zixun.haodf.com']
    # start_urls = ['http://zixun.haodf.com/']

    def start_requests(self):
        for i in range(1,4):
            yield scrapy.Request(url='https://zixun.haodf.com/dispatched/all.htm?p={}'.format(i),callback=self.parse)

    def parse(self, response):
        # item = HaodfItem()
        print('*'*100)
        titles = response.xpath('//*[@id="consult"]/div[5]/div[2]/div[2]/div/div[2]/div/ul/li/span[1]/a[2]/text()').extract()
        urls = response.xpath('//*[@id="consult"]/div[5]/div[2]/div[2]/div/div[2]/div/ul/li/span[1]/a[2]/@href').extract()
        for title,url in zip(titles,urls):
            item = HaodfItem()
            item['title']=title
            item['url']='https:'+url
            # item.save()
            yield item

        # print(ul_list)
        # for uls in ul_list:
        #     print('-'*100)
        #     title = uls.xpath('./li/span[1]/a[2]/text()').extract()
        #     url = uls.xpath('./li/span[1]/a[2]/@href').extract()
        #     print(url)
        # pass
