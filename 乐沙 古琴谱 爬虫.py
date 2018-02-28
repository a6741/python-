# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 20:01:19 2017

@author: hp
"""

import requests ##导入requests
from bs4 import BeautifulSoup ##导入bs4中的BeautifulSoup
import os
dst=os.path.join(os.path.expanduser("~"), "Desktop")
os.mkdir(dst+'/yue')

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
c=1
while c<=8:
    all_url="http://www.yuesha.com/forum-115-"+str(c)+".html"
    shtml=requests.get(all_url,headers=headers)
    Soup=BeautifulSoup(shtml.text,'lxml')
    all_a = Soup.find('table',summary='forum_115',cellspacing='0',cellpadding='0',id='threadlisttableid').find_all('tbody') ##使用BeautifulSoup解析网页过后就可以用找标签呐！（find_all是查找指定网页内的所有标签的意思，find_all返回的是一个列表。）
    del(all_a[0])
    for a in all_a:
        title = a.find('th').get_text().replace('\n','')
        href = a.find('a')['href']
        pichtml='http://www.yuesha.com/'+href
        pic=requests.get(pichtml,headers=headers)
        picsoup=BeautifulSoup(pic.text,'lxml')
        pics=picsoup.find_all('div',class_="mbn savephotop")
        k=1
        for p in pics:
            pic=p.find('img')['file']
            img_url='http://www.yuesha.com/'+pic
            name = title ##取URL 倒数第四至第九位 做图片的名字
            img = requests.get(img_url, headers=headers)
            f = open(dst+'/yue/'+name+str(k)+'.jpg', 'ab')##写入多媒体文件必须要 b 这个参数！！必须要！！
            f.write(img.content) ##多媒体文件要是用conctent哦！
            f.close()
            k+=1
    c+=1
    