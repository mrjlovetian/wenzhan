# -*- coding: utf-8 -*-
import scrapy


class MeiwenzhanSpider(scrapy.Spider):
    name = 'meiwenzhan'
    allowed_domains = ['interface.meiriyiwen.com']
    start_urls = ['http://interface.meiriyiwen.com/']

    def parse(self, response):
        pass
