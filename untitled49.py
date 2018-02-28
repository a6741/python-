# -*- coding: utf-8 -*-
"""
Created on Sun May 14 23:51:31 2017

@author: hp
"""

import socket
   
def parse(content):
    header_end=content.find(b'\r\n\r\n')
    if header_end<=0: 
        print("Cannot find http header")
        return 0, content
    head_str=content[:header_end]
    print(head_str)    
    
    if b'200' in head_str and b'OK' in head_str:
        hlines=head_str.split(b'\r\n')
        hs=[ line.split(b': ') for line in hlines[1:]]        
        headers=dict(hs)
        print(hs)        
        return eval(headers[b'Content-Length']),content[header_end+4:]
    raise "Cannot find html"
    return 0, content


host,port='www.xmu.edu.cn',80


msg_head={
    'Host': host,
    'Connection': 'closed',
    'Accept':'*/*',
    'Accept-Encoding': 'gzip,deflate',
    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.154 Safari/537.36'
    #'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4'
    }

msg='Get / HTTP/1.1\r\n'+'\r\n'.join([':'.join(i) for i in msg_head.items()] )+'\r\n\r\n'

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))
sock.sendall(msg.encode())
resp=sock.recv(4096)

length,html=parse(resp)
print(length,len(html))
while length>len(html):    
    html+=sock.recv(4096)
    #print(len(html))
open('resp.html.zip','wb').write(html)
sock.close()