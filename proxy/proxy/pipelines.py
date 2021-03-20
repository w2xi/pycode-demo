# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        '''
        这里我们通过对 spider name 的判断来分清楚
        item 是哪一个spider 传来的， 从而做出相应的处理方式
        '''

        if spider.name == 'kdlspider':
            #content = item['addr'].split('\r\n') # 没必要这样嘞. yield 生成
            with open('E:/pycodes/proxy/proxy/doc/kdl.txt', 'a') as f:
                #for line in content:
                f.write(item['addr'] + '\n')
        elif spider.name == 'dxdlspider':
            # 直接把传过来的 addr 写入文本
            with open('E:/pycodes/proxy/proxy/doc/dxdl.txt', 'a') as f:
                f.write(item['addr'] + '\n')
                
        return item
