# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 20:21:56 2017

@author: hp
"""
import requests 
from bs4 import BeautifulSoup
i=0
while i<=975:
    url='http://music.baidu.com/tag/%E6%B5%81%E8%A1%8C?start='+str(i)+'&size=25&third_type=0'
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    html=requests.get(url,headers=headers)
    html.encoding="utf-8"
    Soup=BeautifulSoup(html.text,'lxml')
    afind=Soup.find_all('span',class_="song-title")
    for a in afind:
        b=a.find('a')
        webs='http://music.baidu.com'+b['href']
        title=b.get_text()
        print(webs+title)
    i+=25