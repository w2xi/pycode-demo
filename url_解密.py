# 对url解码

import re

'''
f = { "w": "a", "k": "b", "v": "c", "1": "d", "j": "e", "u": "f", "2": "g",\
      "i": "h", "t": "i", "3": "j", "h": "k", "s": "l", "4": "m", "g": "n",\
      "5": "o", "r": "p", "q": "q", "6": "r", "f": "s", "p": "t", "7": "u",\
      "e": "v", "o": "w", "8": "1", "d": "2", "n": "3", "9": "4", "c": "5",\
      "m": "6", "0": "7", "b": "8", "l": "9", "a": "0", "_z2C$q": ":",\
      "_z&e3B": ".", "AzdH3F": "/" }
'''

f = { "w": "a", "k": "b", "v": "c", "1": "d", "j": "e", "u": "f", "2": "g",\
      "i": "h", "t": "i", "3": "j", "h": "k", "s": "l", "4": "m", "g": "n",\
      "5": "o", "r": "p", "q": "q", "6": "r", "f": "s", "p": "t", "7": "u",\
      "e": "v", "o": "w", "8": "1", "d": "2", "n": "3", "9": "4", "c": "5",\
      "m": "6", "0": "7", "b": "8", "l": "9", "a": "0", "_z2C$q": ":",\
      "_z&e3B": ".", "AzdH3F": "/" }


def func(url):
    s = ''
    #lst = re.findall(r'[a-w\d]|-|_z2C\$q|_z&e3B|AzdH3F', url) #不能满足需求
    lst = re.findall(r'AzdH3F|_z2C\$q|_z&e3B|AzdH3F|[a-z\d]|[-_=?]', url, re.I)
    for i in lst:
        if i in f:
            s += f[i]
        else:
            s += i

    return s

url = 'ippr_z2C$qAzdH3FAzdH3Fooo_z&e3B0lg_z&e3BvgAzdH3F7rs5w1fAzdH3Fwsst42AzdH3F8camabAzdH3F8-8camaPa8mam_z&e3B3r2'
print(func(url))
        
            
