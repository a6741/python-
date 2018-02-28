# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:07:09 2017

@author: hp
"""
#客户端
import socket

address = ('110.83.78.98', 31500)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = raw_input()
    if not msg:
        break
    s.sendto(msg, address)

s.close()