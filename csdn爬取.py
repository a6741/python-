# -*- coding: utf-8 -*-
"""
Created on Tue May 02 23:59:34 2017

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:34:39 2017

@author: hp
"""
import os
import requests 
import random
import re
from bs4 import BeautifulSoup
finded=[]
s = requests.session()
s.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 5
os.makedirs('C:\\Users\\hp\Desktop\\w\\')
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
def find(str):
 #   print str
    if str==None:
        return 0
    finded.append(str)
    url='http://my.csdn.net/'+str
    html=requests.get(url,headers=headers)
    html.encoding="utf-8"
    Soup=BeautifulSoup(html.text,'lxml')
    afind=Soup.find('img',class_="header")
    tet=Soup.find_all('a',class_='tit')
    print tet
    for t in tet:
        url2=t['href']
        html2=requests.get(url2,headers=headers)
        html2.encoding="utf-8"
        Soup2=BeautifulSoup(html2.text,'lxml')
        text=Soup2.find('div',id="article_details").get_text()
        os.makedirs('C:\\Users\\hp\Desktop\\w\\'+str)
        with open('C:\\Users\\hp\Desktop\\w\\'+str+t['title']+'.txt',"w") as f:
            f.write(text)
    img = requests.get(afind['src'], headers=headers)
    ps=Soup.find('div',class_='interested_con').find_all('img')
    ps+=Soup.find('div',class_='mod_relations').find_all('img')
    del(ps[0])
    f = open('C:\\Users\\hp\Desktop\\w\\'+str+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
    f.write(img.content) ##多媒体文件要是用conctent哦！
    f.close()
    for p in ps:
        if p['username'] not in finded:
            find(p['username'])
    return 0
find('notbaron')