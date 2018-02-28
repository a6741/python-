# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 17:43:09 2016

@author: hp
"""

# _*_ coding:utf-8 _*_ 
import urllib2 
from bs4 import BeautifulSoup

 
url=('http://movie.douban.com/top250?format=text')
page = urllib2.urlopen(url) 
contents = page.read()
soup = BeautifulSoup(contents, "lxml") 
namelist=soup.findAll("span",{'class':"title"})
print namelist