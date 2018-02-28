# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 18:42:28 2016

@author: hp


x='s'
if isinstance(x,str):
  x=input('')
  x=x.lower()
  a=list(x)
  if a[0] in ['a','e','i','o','u']:
     s=x+'hay'
  elif a[0]=='q' and a[1]=='u':
     s=x[2:]+'quay'
  else:
     k=[]
     if a[0] not in ['a','e','i','o','u']:
       k+=a[0]
       a=a[1:]
       a=a+k
       s=''.join(a)+'ay'
  print s