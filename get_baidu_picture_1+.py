 import re
import requests
import json
import random
from multiprocessing.dummy import Pool as ThreadPool

# 实例化 pool 对象
pool = ThreadPool(15)

def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'
'''
def getImage(html): # 获取 URL（被加密）
    reg = r'"objURL":"(.*?)"' # 最小匹配
    imgre = re.compile(reg) # 预编译
    imglist = re.findall(imgre, html) #list
    length = len(imglist)
    print(length)
    return imglist
'''

def getImage(html):
    lst = []
    datas = json.loads(html)['data']
    for i in datas:
        if i:
            lst.append([i['objURL'], i['pageNum'], i['type']])
    return lst
            
def url_decoded(url_): # 对URL解密
    s = ''
    f = { "w": "a", "k": "b", "v": "c", "1": "d", "j": "e", "u": "f", "2": "g",\
      "i": "h", "t": "i", "3": "j", "h": "k", "s": "l", "4": "m", "g": "n",\
      "5": "o", "r": "p", "q": "q", "6": "r", "f": "s", "p": "t", "7": "u",\
      "e": "v", "o": "w", "8": "1", "d": "2", "n": "3", "9": "4", "c": "5",\
      "m": "6", "0": "7", "b": "8", "l": "9", "a": "0", "_z2C$q": ":",\
      "_z&e3B": ".", "AzdH3F": "/" }
    
    #lst = re.findall(r'[a-w\d]|-|_z2C\$q|_z&e3B|AzdH3F', url_) 不能满足需求
    lst = re.findall(r'AzdH3F|_z2C\$q|_z&e3B|AzdH3F|[a-z\d]|[-_=?]', url_, re.I)
    for i in lst:
        if i in f:
            s += f[i]
        else:
            s += i
    return s

def downLoad(lst):
    hd = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}
    '''ip = ['101.4.136.34:81', 
          '222.186.32.227:8118',
          '118.193.107.36:80',
          '118.193.107.222:80',
          '118.193.107.115:80',
          '118.193.107.184:80',
          '101.4.136.34:81']
     '''     
    #proxies = {'http': random.choice(ip)}
    pic_url = url_decoded(lst[0])
    try:
        rq = requests.get(pic_url, headers=hd)# proxies=proxies, timeout=5)
        rq.raise_for_status()
        
        with open('D:/动漫图片/img_' + str(lst[1]) + '.' + lst[2], 'wb') as f:
            f.write(rq.content)
    except:
        print('error', pic_url)

def main(word, file_num): #word: 搜索关键字； file_num: 文件数量 (每个文件有30张图片)
    
    initial_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='   
    keyword_url = initial_url.format(word=word)
    
    for i in range(file_num):
        url = keyword_url + str(30*i)            
        html = getHTML(url)
        pic_datas = getImage(html) # objURL pageNum type

        pool.map(downLoad, pic_datas)
        
main('动漫图片 二次元', 300)
        
