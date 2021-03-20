# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
'''
class GetpicturesPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        file_path = 'E:/pycodes/getpictures/getpictures/images/pic_1/'
        with open(file_path + 'img_' +  str(item['number']) + '.' +  item['pic_format'], 'wb') as f:
            f.write(requests.get(item['url']).content)     
        return item
'''
class GetpicturesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['url'])

    def item_completed(self, results, item, info):
        # 图片存储路径
        file_path = [x['path'] for ok, x in results if ok]
        # 判断图片是否下载成功
        if not file_path:
            raise DropItem('Item contains no filed')
        return item
    
