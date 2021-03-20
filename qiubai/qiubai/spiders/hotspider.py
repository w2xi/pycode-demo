# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem

class HotspiderSpider(scrapy.Spider):
    name = 'hotspider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    # 我们爬取 13 页的全部热门段子
    for i in range(1, 14):
        start_urls.append('https://www.qiushibaike.com/8hr/page/' + \
                          str(i) + '/')
    
    def parse(self, response):
        item = QiubaiItem()

        #找到热门段子主体
        main = response.xpath('//div[@id="content-left"]/div')

        for div in main:
            item['author'] = div.xpath('.//h2/text()').extract()[0]
            # 观察网页，知道 span标签下的不单单是一行str，
            #我们将它连接起来
            item['body'] = ''.join(div.xpath('.//div[@class="content"]/span/text()').extract())
            item['funNum'] = div.xpath('.//span[@class="stats-vote"]/i/text()').extract()[0]
            item['comNum'] = div.xpath('.//span[@class="stats-comments"]/a/i/text()').extract()[0]
            yield item
