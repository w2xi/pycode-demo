# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
#import requests
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem

'''
class MeizituPipeline(object):
    def process_item(self, item, spider):
        hd = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
              
        with open('E:/pycodes/MeiZiTu/MeiZiTu/pictures/' + item['desc'] + \
                  '.jpg', 'wb') as f:
            f.write(requests.get(item['image_url'], headers=hd).content)
        return item
'''
class MeizituPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item['image_url'])

    def item_completed(self, results, item, info):
        # 图片存储路径
        file_paths = [x['path'] for ok, x in results if ok]
        # 判断图片是否下载成功
        if not file_paths:
            raise DropItem('Item contains no files')
        #item['file_paths'] = file_paths
        return item
