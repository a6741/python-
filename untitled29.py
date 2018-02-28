# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 14:37:37 2017

@author: hp
"""

from urllib import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("https://segmentfault.com"+articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    return bsObj.find("li", {"class":"widget-links__item"}).findAll("a", href=re.compile("^(/q/)((?!:).)*$"))
links = getLinks("/q/1010000004966001")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    newArticle= "/q/"+str(int(newArticle.replace("/q/",''))+1)
    print("https://segmentfault.com"+newArticle)
    links = getLinks(newArticle)
    if len(links) < 0:
            newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
            newArticle= "/q/"+str(int(newArticle.replace("/q/",''))+1)
            links = getLinks(newArticle)
        