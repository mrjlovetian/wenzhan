# -*- coding: utf-8 -*-
import scrapy
import json
import pymysql
import datetime


class MeiwenzhanSpider(scrapy.Spider):
    name = 'meiwenzhan'
    allowed_domains = ['interface.meiriyiwen.com']
    offsize = 0
    alldays = []
    base_url = 'https://interface.meiriyiwen.com/article/day'
    start_urls = [base_url]       
    alldays = self.get_nday_list(2000)
    
    def get_nday_list(n):
        before_n_days = []
        for i in range(1, n + 1)[::-1]:
            before_n_days.append((datetime.date.today() - datetime.timedelta(days=i)).strftime("%Y%m%d"))
        return before_n_days

    def parse(self, response):
        douyu_data = json.loads(response.body)['data']
    
        author = pymysql.escape_string(douyu_data['author'])
        title = pymysql.escape_string(douyu_data['title'])
        digest = pymysql.escape_string(douyu_data['digest'])
        content = pymysql.escape_string(douyu_data['content'])
        print('......................', author)
        print('......................', title)
        print('......................', digest)
        print('......................', content)
        if (len(content) < 20000):
            db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
            cursor = db.cursor()
            sql = """INSERT INTO wenzhan values ('%s', '%s', '%s', '%s')"""%(author, title, digest, content)
            cursor.execute(sql)
            db.commit()
            db.close()
       
        self.offsize += 1
        yield scrapy.Request(self.base_url +'?date='+ str(self.alldays[self.offsize]), callback=self.parse)
