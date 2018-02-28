# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 17:42:22 2017

@author: hp
"""
import re
with open(r'C:\Users\hp\Desktop\123.txt','r') as f:
    a=f.read().decode('gbk')
    b=re.search('(?<=z)\w+',a).group()[1]
    print b