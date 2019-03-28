# -*- coding: utf-8 -*-
import scrapy


class MeiwenzhanSpider(scrapy.Spider):
    name = 'meiwenzhan'
    allowed_domains = ['interface.meiriyiwen.com']
    base_url = 'https://interface.meiriyiwen.com/article/random?dev=1'
    start_urls = [base_url]

    def parse(self, response):
         douyu_data = json.loads(response.body)['data']
         print('......................', douyu_data['title'])
        yield scrapy.Request(self.base_url, callback=self.parse)
