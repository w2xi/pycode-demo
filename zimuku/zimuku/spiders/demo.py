# -*- coding: utf-8 -*-
import scrapy

from zimuku.items import ZimukuItem

class DemoSpider(scrapy.Spider):
    name = 'demo'
    allowed_domains = ['zimuku.cn']
    start_urls = ['http://zimuku.cn/']

    def parse(self, response):
        # we want to inspect one specific response
        if 'cn' in response.url:
            from scrapy.shell import inspect_response
            inspect_response(response, self)
        # rest of parsing code.
        name = response.xpath('//b/text()').extract()[1]

        items = {}
        items['第一个'] = name

        return items
