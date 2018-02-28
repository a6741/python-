# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:34:39 2017

@author: hp
"""
import os
import requests 
from bs4 import BeautifulSoup
i=1
u=0
while i<=1:
    url='http://www.dsb.cn/list-9-'+str(i)+'.html'
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    html=requests.get(url,headers=headers)
    html.encoding="utf-8"
    Soup=BeautifulSoup(html.text,'lxml')
    afind=Soup.find_all('div',class_="news_title")
    for a in afind:
        b=a.find('a')
        webs=b['href']
        title=b.get_text()
        print('**********'+title+'*********')
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        html=requests.get(webs,headers=headers)
        html.encoding="utf-8"
        Soup=BeautifulSoup(html.text,'lxml')
        pfind=Soup.find('div',class_="contents-con").find_all("p")
        for p in pfind:
            tet+='\n'+p.get_text().encode('utf-8')
            u+=1
        with open(str(u)+".txt","w") as f:
            f.write(tet)
        i+=1
