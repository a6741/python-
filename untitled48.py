# -*- coding: utf-8 -*-
"""
Created on Mon May 08 21:31:37 2017

@author: hp
"""
import xlrd
from xlutils.copy import copy
 
data = xlrd.open_workbook('C:\\Users\\hp\Desktop\\shit.xls')
tmpData = copy(data)
tmpData.get_sheet(0).write(1,1,'sb')
tmpData.save("C:\\Users\\hp\Desktop\\shitfu.xls")