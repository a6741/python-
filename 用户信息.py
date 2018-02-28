# -*- coding: utf-8 -*-
"""
Created on Wed May 10 21:51:36 2017

@author: hp
"""

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
import xlwt as xl
import requests 
from bs4 import BeautifulSoup
finded=[]
k=0
book=xl.Workbook()
sht=book.add_sheet('fuck')
s = requests.session()
s.keep_alive = False
requests.adapters.DEFAULT_RETRIES = 5
os.makedirs('C:\\Users\\hp\Desktop\\ws\\')
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
class Header:
    def __init__(self,**data):
        self.__dict__.update(data) 
def find(str):
    global k
    print str
    if str==None:
        return 0
    url='https://segmentfault.com'+str+'/users/followed'
    html=requests.get(url,headers=headers)
    html.encoding="utf-8"
    Soup=BeautifulSoup(html.text,'lxml')
    stat=Soup.find('div',class_="col-md-5 col-sm-9 col-xs-9")
    if stat==None:
        return 0
    finded.append(str)
    [s.extract() for s in stat('small')]
    j=Header(fans=[],leader=stat.find('h2',class_="profile__heading--name").get_text())
    sht.write(k,0,j.leader)
    school=stat.find('span',class_="profile__school")
    [s.extract() for s in school('span')]
    school=school.get_text()
    sht.write(k,1,school)
    yd.append(j)
    dict1[j.leader]=k
    k+=1
    afind=Soup.find_all('div',class_="col-md-10")
    afind+=nex(Soup)
    if(afind==None):
        return 0
    del(afind[0])
    for a in afind:
        (yd[dict1[j.leader]].fans).append(a.find('a').get_text())
        sht.write(dict1[j.leader],2+afind.index(a),a.find('a').get_text())
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
def draw(path):
        import networkx as nx
        import matplotlib.pyplot as plt
        import math
        #plt.figure(figsize=(250,250))
        plt.figure(figsize=(200,200))                
        G = nx.DiGraph()
        q={'n':'y'}
        big=[]
        egecol=[]
        for i in yd:
            if i.leader in dict1.keys():
                G.add_node(i.leader)
                q[dict1[i.leader]]=i.leader
                big.append(math.sqrt(len(i.fans))*5000+5000)
        for fi in yd:
            for f in fi.fans:
                for qs in q:
                    if f==q[qs].strip():
                        #if len(fi.fans)>num[q[qs]]:                           
                        G.add_edge(fi.leader,q[qs])
                        if len(fi.fans)>100:
                            egecol.append('r')
                        elif len(fi.fans)>50:
                            egecol.append('g')
                        elif len(fi.fans)>10:
                            egecol.append('b')
                        else:
                            egecol.append('black')
        del egecol[-1]
        nx.draw(G,with_labels=True,font_size=26,node_size=big,node_color='y',pos=nx.random_layout(G),width=2.0,edge_color='y')
        os.makedirs(path)        
        plt.savefig(path+"youxiangtu3.jpg")
try:
    dict1 = { 'abc':'hi'}
    del dict1['abc']
    global dict1
    yd=[]
    global yd
    find('/u/dont')
finally :
    book.save('C:\\Users\\hp\Desktop\\ws\\shit.xls')
    draw('C:\\Users\\hp\Desktop\\ws\\show\\')