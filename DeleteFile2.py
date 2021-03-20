import os

from multiprocessing.dummy import Pool

def deleteFile(file):
    os.remove(file)
    print(file + ' is deleted')

def main():
    dir = 'E:\\pycodes\\MeiZiTu\\MeiZiTu\\images\\meizitu\\full'
    os.chdir(dir)
    files = os.listdir(os.getcwd()) # array

    pool = Pool(15)
    pool.map(deleteFile, files)
    #pool.close()
    #pool.join()

main()
