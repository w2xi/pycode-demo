# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class QiubaiPipeline(object):
    def process_item(self, item, spider):

        with open('E:/pycodes/qiubai/qiubai/duanzi.txt', 'a') as f:
            f.write('作者: {}\n段子: {}\n点赞: {}\t评论数: {}\n\n'.format(
                item['authpr'], item['body'], item['funNum'], item['comNum']))
            
        return item
