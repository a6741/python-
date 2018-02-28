# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 18:14:11 2017

@author: hp
"""

import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import random
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
a_url='http://baike.baidu.com/link?url=nyjqLnZK4qbQ6Akd_1hU62OdYMyDsGPT87OfIxQw3zcfGgOYaoqpn9zEZmdWPTj0tYmQXx3BpT49hVpPaioJklYWmh5mL2uHwB2AwTUjy4_kA8yqQTNFrrcfWMjZl01D'
by=a_url
while len(a_url)!=19:
    a=requests.get(a_url,headers)
    sa=BeautifulSoup(a.text,'lxml')
    sa0=sa.find('div',class_="main-content")
    while str(type(sa0))=="<type 'NoneType'>" or a_url=='http://baike.baidu.com/feedback':
        a=requests.get(by,headers)
        sa=BeautifulSoup(a.text,'lxml')
        sa0=sa.find('div',class_="main-content")
    sa1=sa0.find_all('a',target="_blank")       
    c1=sa1[random.randint(0, sa1.index(max(sa1)))]
    q=str(c1)
    title=sa.find('dd',class_="lemmaWgt-lemmaTitle-title").find('h1').get_text()
    while ((('href' in q)==False )or ('/pic/' in c1['href'])):
        c1=sa1[random.randint(0, sa1.index(max(sa1)))]
        q=str(c1)
    if((('http://baike.baidu.com/' in c1['href'])==False)):
        if 'http://' in c1['href']==False:
            c1['href']=c1['href'].replace('http:/','')
        a_url='http://baike.baidu.com'+c1['href']
    else:
        a_url=c1['href']
    sad=title.encode('unicode_escape')
    print(sad.encode('utf-8'),a_url)