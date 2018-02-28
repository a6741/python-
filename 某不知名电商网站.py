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
i=1
u=0
tet=''
os.makedirs('C:\\Users\\hp\Desktop\\w\\')
list=[]
while i<=800:
    url='http://www.dsb.cn/list-9-'+str(i)+'.html'
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    html=requests.get(url,headers=headers)
    html.encoding="utf-8"
    Soup=BeautifulSoup(html.text,'lxml')
    afind=Soup.find_all('div',class_="news_title")
    for a in afind:
        b=a.find('a')
        webs=b['href']
        list.append(webs)
        title=b['title'].replace('?','').replace('"','').replace(':','').replace('/','').replace("\\",'').replace('*','').replace('>','').replace('<','').replace('|','')
        print('**********'+title+'*********')
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        html=requests.get(webs,headers=headers)
        html.encoding="utf-8"
        Soupp=BeautifulSoup(html.text,'lxml')
        pfind=Soupp.find('div',class_="contents-con")
        pfind=pfind.find_all('p')
        for p in pfind:
            tet+=p.get_text().encode('utf-8')+'\n'
        with open('C:\\Users\\hp\Desktop\\w\\'+title+'.txt',"w") as f:
            f.write(tet)
        tet=''
    i+=1
