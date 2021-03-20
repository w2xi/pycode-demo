# -*- coding: utf-8 -*-
import scrapy
from getpictures.items import GetpicturesItem
import json
import re

class GetpicSpider(scrapy.Spider):
    name = 'getpic'
    allowed_domains = ['image.baidu.com']
    start_urls = []

    ini_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word={word}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&cg=wallpaper&pn='       

    # 搜索关键字
    keyword = ''

    # 文件数量
    file_num = ''
    
    objurl = ini_url.format(word=keyword)
    
    for i in range(file_num):
        start_urls.append('https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=壁纸%20卡通动漫%20名侦探柯南&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word=壁纸%20卡通动漫%20名侦探柯南&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&cg=wallpaper&pn=' + str(30*i))        
        
    def parse(self, response):
        # 实例化 item
        item = GetpicturesItem()
        datas = json.loads(response.body.decode())
        content = datas['data']
        
        f = { "w": "a", "k": "b", "v": "c", "1": "d", "j": "e", "u": "f", "2": "g",\
      "i": "h", "t": "i", "3": "j", "h": "k", "s": "l", "4": "m", "g": "n",\
      "5": "o", "r": "p", "q": "q", "6": "r", "f": "s", "p": "t", "7": "u",\
      "e": "v", "o": "w", "8": "1", "d": "2", "n": "3", "9": "4", "c": "5",\
      "m": "6", "0": "7", "b": "8", "l": "9", "a": "0", "_z2C$q": ":",\
      "_z&e3B": ".", "AzdH3F": "/" }

        for value in content:
            i = value['objURL']
            s = ''
            lst = re.findall(r'AzdH3F|_z2C\$q|_z&e3B|AzdH3F|[a-z\d]|[-_=?]', i, re.I)
            for j in lst:
                if j in f:
                    s += f[j]
                else:
                    s += j
            item['url'] = s
            #item['number'] = value['pageNum']
            #item['pic_format'] = value['type']
            yield item
