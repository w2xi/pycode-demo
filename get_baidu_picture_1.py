import re
import requests

def getHTML(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'

def getImage(html): # 获取真实的URL（被加密）
    reg = r'"objURL":"(.*?)"' # 最小匹配
    imgre = re.compile(reg) # 预编译
    imglist = re.findall(imgre, html) #list
    length = len(imglist)
    print(length)
    return imglist

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

def downLoad(urls, n, ini_url): # 下载并保存图片到本地(经测试，有 .jpeg 和 .jpg 的格式
    hd = {'user-agent':'chrome/10'}
    for url in urls:
        try:
            rq = requests.get(url, headers=hd)
            rq.raise_for_status()
            img_stream = rq.content
            
            picture_format = url.split('.')[-1]
            if picture_format in ['jpg', 'jpeg', 'png']:
                with open('D:/test/pic_7/img_' + str(n) + '.' + picture_format,\
                      'ab') as f:
                    f.write(img_stream)
            #else:
               # with open('D:/test/pic_5/img_' + str(n) + '.jpg',\
               #       'ab') as f:
               #     f.write(img_stream)
        except:
            print('error', url)
           
            continue
        n += 1
    return n

def main(word, file_num): #word: 搜索关键字； file_num: 文件数量 (每个文件有30张图片)
    
    initial_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn='
    
    keyword_url = initial_url.format(word=word)

    n = 1
    for i in range(file_num):
        url = keyword_url + str(30*i)
        
    
        data = getHTML(url)
        url_list = getImage(data)
        L = []
        for x in url_list:
            L.append(url_decoded(x))
        n = downLoad(L, n, url_list)

main('1366x768高清壁纸护眼', 3)
        
    
    
     
    
