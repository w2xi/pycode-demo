# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem

class DxdlspiderSpider(scrapy.Spider):
    name = 'dxdlspider'
    allowed_domains = ['xicidaili.com']
    #提供了代理的 API
    start_urls = ['http://api.xicidaili.com/free2016.txt']

    def parse(self, response):
        item = ProxyItem()
        # 因为直接调用网站的API，本身get下来的就是一个text文本
        # 我们直接把文本传给item, 再交给 pipeline处理就好
        item['addr'] = response.text
        return item
    
