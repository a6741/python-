# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 00:07:33 2017

@author: hp
"""
#服务器
import socket

address = ('218.66.152.254', 3150)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(address)

while True:
    data, addr = s.recvfrom(2048)
    if not data:
        print "client has exist"
        break
    print "received:", data, "from", addr

s.close()