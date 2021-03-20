'''
通过这个脚本来判断抓取到的IP是否可用

采用 requests 库 及 多线程
'''

import requests
# 引入这个库来获得 map 函数的并发版本
from multiprocessing.dummy import Pool as ThreadPool

# 定义全局变量
alive_ip = []

def test_ip(proxy):
    '''
    通过一个简单的函数，使用代理访问百度，
    筛选通过的代理保存在 alive_ip 中
    '''
    
    global alive_ip
    
    # 设置代理头
    proxies = {'http': proxy}
    print('正在测试: {}'.format(proxies))
    try:
        r = requests.get('http://www.baidu.com', proxies=proxies, timeout=5)
        if r.status_code == 200:
            print('该代理: {}, 成功存活'.format(proxy))
            alive_ip.append(proxy)
    except:
        print('该代理: {}, 失效!'.format(proxy))


def saveToFile(path):
    # 写入符合要求的代理 ip

    with open(path + 'ip.txt', 'w') as f:
        for i in alive_ip:
            f.write(i + '\n')
        print('所有存活的ip都已经写入文件!')
        
def main():
    
    file_path = 'E:/pycodes/proxy/proxy/doc/'
    # 使得 map 并发， 实例化 pool 对象
    pool = ThreadPool()
    # 设置并发数量
    pool = ThreadPool(20)

    with open(file_path + 'kdl.txt', 'r') as f:
        # 从文件中读入所有行，以每行为元素形成一个列表
        lines = f.readlines()
        # 我们去掉lines中每个元素后面的 \n\r 之类的空格
        # 生成一个新的列表
        proxys = list(map(lambda x: x.strip(), lines))

        # 一行代码解决多线程
        pool.map(test_ip, proxys)

    saveToFile(file_path)

main()
        
                  
