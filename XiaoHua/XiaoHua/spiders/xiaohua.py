# -*- coding: utf-8 -*-
import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['mmonly.cc']
    start_urls = ['http://mmonly.cc/']

    def parse(self, response):
        pass
