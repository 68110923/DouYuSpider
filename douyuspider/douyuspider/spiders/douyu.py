# -*- coding: utf-8 -*-
import scrapy
import json
from douyuspider.items import DouyuspiderItem


class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']
    offset = 0
    url = 'http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset='
    start_urls = [url]

    def parse(self, response):
        data = json.loads(response.text)["data"]
        print('ls:',len(data))
        for each in data:
            item = DouyuspiderItem()
            item['name'] = each["nickname"]
            item['img_url']=each["vertical_src"]
            yield  item

        self.offset+=20
        if self.offset <= 300:
            yield scrapy.Request(self.url + str(self.offset),callback=self.parse)

