# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:31:02 2017

@author: hp
"""

import socket
serverName='hostname'
serverPort =12000
clientSocket=socket(AF_INEF,SOCK_DGRAM)
message=raw_input('input lowercase sentence')
clientSocket=socket(message,(serverName,serverPort))
modifiefMessage,serverAddress=clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()
