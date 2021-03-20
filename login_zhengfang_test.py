import requests
from lxml import etree
from PIL import Image

login_url = 'http://172.16.65.99/'
#session_url = 'http://172.16.65.99/xs_main.aspx?xh=15411200135'

s = requests.session() # 保持一个会话
r = s.get(login_url)
print(r.url)

tree = etree.HTML(r.text)

pic_url = login_url + tree.xpath('//img[@id="icode"]/@src')[0]
with open('pic.png', 'wb') as fp:
    fp.write(s.get(pic_url).content)
image = Image.open('pic.png')
image.show()

__viewstate = tree.xpath('//input[@name="__VIEWSTATE"]/@value')[0]

data = {"__VIEWSTATE":"",
        "txtUserName":"15411200135",
        "TextBox2":"574632100.",
        "txtSecretCode":"",
        "RadioButtonList1":"\xd1\xa7\xc9\xfa",
        "Button1":"",
        "lbLanguage":"",
        "hidPdrs":"",
        "hidsc":""
        }
data["__VIEWSTATE"] = __viewstate
data["txtSecretCode"] = input("请输入验证码:")
#print(data)
'''
hd = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection':'keep-alive',
            'Cookie':'ASP.NET_SessionId=yj0w1y45kwwqvxbifo3vqa55',
            'Host':'172.16.65.99',
            'Referer':'http://172.16.65.99/',
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
           }
'''
r2 = s.post(login_url, data=data) # login 
print(r2.status_code, r2.url)

r3 = s.get(r2.url)# headers=hd)  get htmltext
print(r3.url)
sel = etree.HTML(r2.text)
login_name = sel.xpath('//span[@id="xhxm"]/text()')[0]
print(login_name) # 王集岗同学
