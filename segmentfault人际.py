# -*- coding: utf-8 -*-
"""
Created on Wed May 03 15:39:58 2017

@author: hp
"""

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
from bs4 import BeautifulSoup
finded=[]
i=0
k=0
s = requests.session()
s.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 5
os.makedirs('C:\\Users\\hp\Desktop\\w\\')
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
class Header:
    def __init__(self,**data):
        self.__dict__.update(data) 
def find(str):
    global i,k
    print str
    if str==None:
        return 0
    finded.append(str)
    url='https://segmentfault.com'+str+'/users/followed'
    html=requests.get(url,headers=headers)
    html.encoding="utf-8"
    Soup=BeautifulSoup(html.text,'lxml')
    pic=Soup.find('img',class_=" profile__heading--avatar")
    if pic==None:
        return 0
    if pic['src']=='https://static.segmentfault.com/v-590a963a/global/img/user-256.png' :        
        i+=1
        print i
    j=Header(fans=[],leader=pic['alt'])
    yd.append(j)
    dict1[pic['alt']]=k
    k+=1
    img = requests.get(pic['src'], headers=headers)
    f = open('C:\\Users\\hp\Desktop\\w\\'+pic['alt']+'.jpg', 'ab')
    f.write(img.content) 
    f.close()
    afind=Soup.find_all('div',class_="col-md-10")
    afind+=nex(Soup)
    if(afind==None):
        return 0
    del(afind[0])
    for a in afind:
        (yd[dict1[pic['alt']]].fans).append(a.find('a').get_text())
        if a.find('a')['href'] not in finded :
            find(a.find('a')['href'])
    return 0
def nex(Soup):
        if(Soup.find('li',class_="next")):
            url2='https://segmentfault.com/'+Soup.find('li',class_="next").find('a')['href']
            html2=requests.get(url2,headers=headers)
            html2.encoding="utf-8"
            Soup2=BeautifulSoup(html2.text,'lxml')
            find=Soup2.find_all('div',class_="col-md-10")
            find+=nex(Soup2)
            return find
        return []
def draw():
        import networkx as nx
        import matplotlib.pyplot as plt
        plt.figure(figsize=(250,250))         
        G = nx.DiGraph()
        q={'n':'y'}
        for i in yd:
            G.add_node(i.leader)
            q[dict1[i.leader]]=i.leader
        for fi in yd:
            for f in fi.fans:
                for qs in q:
                    if f==q[qs]:
                        G.add_edge(fi.leader,q[qs])
        nx.draw(G,with_labels=True,font_size=24,node_size=5000,node_color='y',pos=nx.random_layout(G),width=2.0)
        os.makedirs('C:\\Users\\hp\Desktop\\w\\show\\')        
        plt.savefig("C:\\Users\\hp\Desktop\\w\\show\\youxiangtu3.jpg")
        plt.show()
try:
    dict1 = { 'abc':'hi'}
    global dict1
    yd=[]
    global yd
    find('/u/dont')
finally :
    draw()
    with open('C:\\Users\\hp\Desktop\\w\\'+u'默认头像比例'+'.txt',"w") as f:
            f.write(str(i))