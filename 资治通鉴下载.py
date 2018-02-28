# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 12:55:31 2017

@author: hp
"""
import requests 
from bs4 import BeautifulSoup

b=450
while(b<=743):
    
    tet=''
    url='http://so.gushiwen.org/guwen/bookv_'+str(b)+'.aspx'
    headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    html=requests.get(url,headers=headers)
    html.encoding="utf-8"
    Soup=BeautifulSoup(html.text,'lxml')
    title=Soup.find('div',class_="main3").find('div',class_="son1").get_text().replace('\n','')
    afind=Soup.find('div',class_="bookvson2").find_all('p')
    for a in afind:
        tet+=a.get_text().encode('utf-8').replace("　　",'\n　　')+'\n'
    with open(title+'.doc',"w") as f:
        f.write(tet)
    b+=1