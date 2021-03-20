import os

#directory = 'D:/pycodes'
#os.chdir(directory)

def deleteFile(dir):
    os.chdir(dir)   # 切换到 dir 目录
    files = os.listdir(os.getcwd()) #列出 dir 目录下的文件 array
    for file in files:
        os.remove(file) # 删除文件
        print(file + ' is deleted')

    return

def main():
    directory = 'E:\\pycodes\\MeiZiTu\\MeiZiTu\\images\\full'
    deleteFile(directory)
    

main()


#print('ok')
