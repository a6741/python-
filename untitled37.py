# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:30:38 2017

@author: hp
"""

# -*- coding: utf-8 -*-
import requests
import re
import sys
# import urllib2
reload(sys)
sys.setdefaultencoding('gb18030')
type=sys.getfilesystemencoding()

class spider(object):
    def __init__(self):
        print u"开始喽"
    def getsource(self,url):
        zz=requests.get(url)
        return zz.text
    def changepage(self,url,total_page):
        now_page=int(re.search('list_23_(\d)',url,re.S).group(1))

        page_group=[]
        for i in range(now_page,total_page+1):
            link=re.sub('list_23_(\d+)','list_23_%s'%i,url,re.S)
            page_group.append(link)
        return page_group
    def geteverymoive(self,url):
        movieposition=re.findall('<table width="100%"(.*?)</table>',url,re.S)
        return movieposition
    def gettitle(self,everylink,ensure_ascii=False):
        title=re.findall('class="ulink">(.*?)<',everylink,re.S)
        for each in title:
            print each
            return title
if __name__=='__main__':
    moiveinfo=[]
    url='http://www.ygdy8.net/html/gndy/dyzz/list_23_1.html'
    yaospider=spider()
    all_links=yaospider.changepage(url,10)
    for each in all_links:
        print u'正在处理页面：'+each
        html=yaospider.getsource(each)
        everymoive=yaospider.geteverymoive(html)
        for each in everymoive:
            title=yaospider.gettitle(each)