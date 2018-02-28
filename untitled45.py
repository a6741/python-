# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 19:17:39 2017

@author: hp
"""
#服务器

from socket import *
servername='192.168.0.108'
serverport=12000
clientsocket=socket(socket.AF_INEF,SOCK_DGRAM)
message=raw_input('input lowercase sentence:')
clientsocket.sendto(message,(servername,serverport))
modifiedmessage,serveraddress=clientsocket.recvfrom(2048)
print modifiedmessage
clientsocket.close()