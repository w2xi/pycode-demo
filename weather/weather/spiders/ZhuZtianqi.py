# -*- coding: utf-8 -*-
import scrapy
# 将 item 导入进来， 这样数据才能在各个模块之间流转
from weather.items import WeatherItem


class ZhuztianqiSpider(scrapy.Spider):
    name = 'ZhuZtianqi'
    allowed_domains = ['www.tianqi.com']
    start_urls = ['http://www.tianqi.com/zhuzhou',
                  'http://www.tianqi.com/changsha',
                  'http://www.tianqi.com/shanghai']

    def parse(self, response):

        #建立一个列表，用来保存每天的天气信息
        items = []

        
        # 找到包裹着每天天气信息的 div
        day7 = response.xpath('//div[@class="day7"]')

        # 循环筛选出每天的信息
        for i in range(1, 8):
            # 先申请一个 weatheritem 的类型来保存结果
            item = WeatherItem()
            
            item['city_name'] = response.xpath('//dd[@class="name"]/h2/text()').extract()[0]
        
            item['date'] = day7.xpath('./ul[@class="week"]/li/b/text()').extract()[i-1]
            item['week'] = day7.xpath('./ul[@class="week"]/li/span/text()').extract()[i-1]
            item['img'] = day7.xpath('./ul[@class="week"]/li/img/@src').extract()[i-1]              
            item['weather'] = day7.xpath('./ul[@class="txt txt2"]/li/text()').extract()[i-1]
            
            tq1 = day7.xpath('./div[@class="zxt_shuju"]/ul/li/span/text()').extract()[i-1]
            tq2 = day7.xpath('./div[@class="zxt_shuju"]/ul/li/b/text()').extract()[i-1]
            # 将 tq 里的 str 连接起来
            item['temperature'] = '-'.join([tq2, tq1])
            item['wind'] = day7.xpath('./ul[@class="txt"]/li/text()').extract()[i-1]
            items.append(item)
        
        return items

        
