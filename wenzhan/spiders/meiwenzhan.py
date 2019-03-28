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
        
        author = pymysql.escape_string(ouyu_data['author'])
        title = pymysql.escape_string(ouyu_data['title'])
        digest = pymysql.escape_string(ouyu_data['digest'])
        content = pymysql.escape_string(ouyu_data['content'])
        print('......................', author)
        print('......................', title)
        print('......................', digest)
        print('......................', content)
        db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
        cursor = db.cursor()
        sql = """INSERT INTO wenzhan values ('%s', '%s', '%s', '%s')"""%(author, title, digest, content)
        cursor.execute(sql)
        db.commit()
        db.close()

        self.offsize += 1
        yield scrapy.Request(self.base_url + str(self.offsize), callback=self.parse)
