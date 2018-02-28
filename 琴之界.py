# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 20:22:28 2017

@author: hp
"""

import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os
os.makedirs('C:\\Users\\hp\Desktop\\w\\')
all_url='https://weidian.com/item_classes.html?userid=1203049980&c=100664114&wfr=wx'
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
htmla=requests.get(all_url,headers=headers)
soup=BeautifulSoup(htmla.text,'lxml')
book=soup.find_all('a',class_='for_gaq')
#del book[0]
#book.pop()
for b in book:
    name=b.find('p',class_='i_txt ')
    xz='https://weidian.com/'+b['href']
    print(name+str(xz))
    htmlb=requests.get(xz,headers=headers)
    soupb=BeautifulSoup(htmlb.text,'lxml')
    pics=soupb.find_all('img',class_='detail_img lazy')
    i=0
    for p in pics:
        f= open('C:\\Users\\hp\Desktop\\w\\'+name+i+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
        f.write(p.content) ##多媒体文件要是用conctent哦！
        f.close()
        i+=1