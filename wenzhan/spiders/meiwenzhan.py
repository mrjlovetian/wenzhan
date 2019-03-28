# -*- coding: utf-8 -*-
import scrapy
import json
import pymysql

class MeiwenzhanSpider(scrapy.Spider):
    name = 'meiwenzhan'
    allowed_domains = ['interface.meiriyiwen.com']
    offsize = 1
    base_url = 'https://interface.meiriyiwen.com/article/random?dev='+str(offsize)
    start_urls = [base_url]
    

    def parse(self, response):
        douyu_data = json.loads(response.body)['data']
        print('......................', douyu_data['author'])
        print('......................', douyu_data['title'])
        print('......................', douyu_data['digest'])
        print('......................', douyu_data['content'])

        db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
        cursor = db.cursor()
        sql = """INSERT INTO wenzhan values ('%s', '%s', '%s', '%s')"""%(douyu_data['author'], douyu_data['title'], douyu_data['digest'], douyu_data['content'])
        cursor.execute(sql)
        db.commit()
        db.close()

        self.offsize += 1
        yield scrapy.Request(self.base_url + str(self.offsize), callback=self.parse)
