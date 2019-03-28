# -*- coding: utf-8 -*-
import scrapy
import json

class MeiwenzhanSpider(scrapy.Spider):
    name = 'meiwenzhan'
    allowed_domains = ['interface.meiriyiwen.com']
    offsize = 1
    base_url = 'https://interface.meiriyiwen.com/article/random?dev='+str(offsize)
    start_urls = [base_url]
    

    def parse(self, response):
        douyu_data = json.loads(response.body)['data']
        print('......................', douyu_data['title'])
        self.offsize += 1
        yield scrapy.Request(self.base_url + str(self.offsize), callback=self.parse)
