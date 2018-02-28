# -*- coding: utf-8 -*-
"""
Created on Sun May 14 13:46:19 2017

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
sht.write(0,0,u'昵称')
sht.write(0,1,u'学校')
sht.write(0,2,u'粉丝')
class Header:
    def __init__(self,**data):
        self.__dict__.update(data)
class Stack: 
    """模拟栈""" 
    def __init__(self): 
        self.items = [] 

    def isEmpty(self): 
        return len(self.items)==0  

    def push(self, item): 
        self.items.append(item) 

    def pop(self): 
        return self.items.pop()  

    def peek(self): 
        if not self.isEmpty(): 
            return self.items[len(self.items)-1] 

    def size(self): 
        return len(self.items) 
def find(str):
    s666=Stack()
    k=1
    ks=1
    dict1 = { 'abc':'hi'}
    del dict1['abc']
    yd=[]
    global yd
    global dict1
    while(s666.isEmpty()==0 or k==1):
        print str   
        if str!=None:
            if str not in finded :
                num=0
                url='https://segmentfault.com'+str+'/users/followed'
                html=requests.get(url,headers=headers)
                html.encoding="utf-8"
                Soup=BeautifulSoup(html.text,'lxml')
                stat=Soup.find('div',class_="col-md-5 col-sm-9 col-xs-9")
                if stat!=None:
                    finded.append(str)
                    [s.extract() for s in stat('small')]
                    j=Header(fans=[],leader=stat.find('h2',class_="profile__heading--name").get_text())
                    sht.write(ks,0,j.leader)
                    school=stat.find('span',class_="profile__school")
                    [s.extract() for s in school('span')]
                    school=school.get_text()
                    sht.write(ks,1,school)
                    yd.append(j)
                    dict1[j.leader]=k
                    k+=1
                    ks+=1
                    afind=Soup.find_all('div',class_="col-md-10")
                    afind+=nex(Soup)
                    if(afind!=None):
                        del(afind[0])
                        wri=ks-1
                        for a in afind:
                            print ('write in',wri+(afind.index(a))/254)
                            (yd[dict1[j.leader]-1].fans).append(a.find('a').get_text())
                            try:                            
                                sht.write(wri+(afind.index(a))/254,2+afind.index(a)-((afind.index(a)/254))*254,a.find('a').get_text())
                            except:
                                ks+=1
                                wri=ks
                                sht.write(wri+(afind.index(a))/254,2+afind.index(a)-((afind.index(a)/254))*254,a.find('a').get_text())
                            kj=(2+afind.index(a))/256
                            print 2+afind.index(a)-((2+afind.index(a))/255)*255
                            num+=1
                            s666.push(a.find('a')['href'])
                        ks+=kj
        str=s666.pop()
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
    plt.figure(figsize=(100,100))                
    G = nx.DiGraph()
    q={'n':'y'}
    del q[-1]
    big=[]
    for i in yd:
        if i.leader in dict1.keys():
            G.add_node(i.leader)
            q[dict1[i.leader]]=i.leader
            big.append((math.sqrt(len(i.fans)))*5000+5000)
    for fi in yd:
        for f in fi.fans:
            for qs in q:
                if f==q[qs].strip():
                    G.add_edge(fi.leader,q[qs])
    nx.draw(G,with_labels=True,font_size=26,node_size=big,node_color='y',pos=nx.spring_layout(G),width=2.0,edge_color='b')
    os.makedirs(path)        
    plt.savefig(path+"youxiangtu3.jpg")        
try:
    find('/u/dont')
finally :
    book.save('C:\\Users\\hp\Desktop\\ws\\shit.xls')
    draw('C:\\Users\\hp\Desktop\\ws\\show\\')

