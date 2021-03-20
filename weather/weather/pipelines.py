# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import requests
import json
import codecs
#import pymysql

class WeatherPipeline(object):
    
    def process_item(self, item, spider):
        return item
        '''
        #处理每一个从 ZhuZtiqnqi
        #传过来的 item
        
        
        # 获取当前工作目录
        #base_dir = os.getcwd() #E:\pycodes\weather\weather
        # 文件存在 data 目录下的 weather.txt 文件内
        filename = 'E:/pycodes/weather/weather/data/weather.txt'
        # 从内存以追加的方式打开文件， 并写入对应的数据
        
        with open(filename, 'a') as f:
            f.write(item['city_name'] + ' ' +  item['date'] + ' ' + item['week'] + \
                    ' ' + item['weather']  + ' ' + item['temperature'] + \
                    ' ' + item['wind'] + '\n')
            
        # 下载图片
        with open('E:/pycodes/weather/weather/data/' + item['city_name'] + \
                   ' ' + item['date'] + '.png', 'wb') as f:
            f.write(requests.get('http://www.tianqi.com' + item['img']).content)
                
        return item

class W2json(object):
    def process_item(self, item, spider):
        '''
       # 将爬取的信息保存为 json 格式
       # 方便其他程序员调用
        '''

        filename = 'E:/pycodes/weather/weather/data/weather.json'
        with open(filename, 'a') as f:
            line = json.dumps(dict(item), ensure_ascii=False) + '\n'
            f.write(line)
        return item
            
'''
