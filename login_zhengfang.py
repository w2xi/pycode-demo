import requests
from bs4 import BeautifulSoup
from PIL import Image

def get_post_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    # 找到 form 的验证参数
    __VIEWSTATE = soup.find('input', attrs={'name':'__VIEWSTATE'})['value']
    # 获取验证码的图片地址
    pic_url = 'http://172.16.65.99/' + soup.find('img', id='icode')['src']

    # 下载验证码图片
    pic = requests.get(pic_url).content
    with open('ver_pic.png', 'wb') as f:
        f.write(pic)

    # 打开验证码图片
    image = Image.open('C:/Python34/ver_pic.png')
    image.show()

    # 构造需要 post的参数表
    data = {'txtUserName': '15411200135',
            'TextBox2': '574632100.',
            'txtSecretCode': '',
            '__VIEWSTATE': '',
            # 这里将 radio 栏--学生 encode 成 gbk， 以符合数据的要求
            'RadioButtonList1': '\xd1\xa7\xc9\xfa',
            'Button1': '',
            'lbLanguage':'',
            'hidPdrs':'',
            'hidsc': ''
            }
    # 构造登录的post参数
    data['__VIEWSTATE'] = __VIEWSTATE
    #data['txtUserName'] = input('请输入学号:')
    #data['TextBox2'] = input('请输入密码:')
    data['txtSecretCode'] = input('请输入图片中的验证码:')

    return data

def login(url, data): # 登录教务系统
    # 通过requests库构造一个浏览器session, 这能帮我们自动，持久的管理cookies
    s = requests.session()
    s.post(url, data=data)
    return s

login_url = 'http://172.16.65.99/'
session_url = 'http://172.16.65.99/xs_main.aspx?xh=15411200135'

data = get_post_data(login_url)
print(data)
# 模拟登录教务系统
s = login(login_url, data)
rq = s.get(session_url)
print(rq.url)




    
