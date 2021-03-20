import requests
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''

def parseHTML(lst, html):
    try:
        soup = BeautifulSoup(html, 'html.parser')
        ol = soup.find('ol', attrs={'class':'grid_view'})
        for li in ol.find_all('li'):
            rank = li.find('em').string
            name = li.find('img').attrs['alt']
            try:
                quote = li.find('span', attrs={'class':'inq'}).string
            except:
                quote = 'error(no quote)'
            lst.append([rank, name, quote])
        #with open('C:\Python34\learning_2\DouBanTop250.txt', 'a') as f:
           # f.write(str(lst) + '\n')
    except:
        return ''
     
def printText(lst):
    print('豆瓣Top250'+'\n')
    for i in lst:
        print('[{1:^5}]{2:{0}<15}{3:{0}<30}'.format(chr(12288), i[0], i[1], i[2]))

def main():
    depth = 10
    Top250_list = []
    start_url = 'https://movie.douban.com/top250?start='
    for page in range(depth):
        try:
            url = start_url + str(25*page)
            html = getHTMLText(url)     
            parseHTML(Top250_list, html) #???
        except:
            continue
    printText(Top250_list)

main()



