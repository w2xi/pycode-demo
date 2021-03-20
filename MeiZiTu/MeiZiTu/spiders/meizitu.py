# -*- coding: utf-8 -*-
import scrapy
from MeiZiTu.items import MeizituItem

class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['meizitu.com']
    start_urls = ['http://meizitu.com/']

    def parse(self, response):
        for a in response.xpath('//div[@class="tags"]/span/a'):
            href = a.xpath('./@href').extract()[0]
            request = scrapy.Request(href, callback=self.parse_item1)
            yield request

    def parse_item1(self, response):
        for li in response.xpath('//ul[@class="wp-list clearfix"]/li'):
            href = li.xpath('.//h3[@class="tit"]/a/@href').extract()[0]
            request = scrapy.Request(href, callback=self.parse_item2)
            yield request
            
        all_li = response.xpath("//div[@class='navigation']/div[@id='wp_page_numbers']/ul/li")
        next_page = all_li[-2].xpath('./a/@href').extract()[0]
        if  next_page:
            request = scrapy.Request('http://www.meizitu.com/a/' + next_page,\
                                     callback=self.parse_item1)
            yield request
    
    def parse_item2(self, response):
        item = MeizituItem()
        for img in response.xpath('//div[@id="picture"]/p/img'):       
            #item['desc'] = img.xpath('./@alt').extract()[0]
            item['image_url'] = img.xpath('./@src').extract()[0]
            yield item
            
