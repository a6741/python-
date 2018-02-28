# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 18:23:41 2017

@author: hp
"""

import string
import poplib
import StringIO, rfc822

servername = "mail.qq.com"
username = "3207029428@qq.com"
passwd = "密码，这边就不贴了"

#连接 登录 服务器
pop = poplib.POP3(servername)
pop.set_debuglevel(1)            #会打印出debug信息
pop.user(username)
pop.pass_(passwd)

#列出邮件信息
num,total_size = pop.stat()

#取得最新的邮件
hdr,text,octet=pop.retr(num)

#对邮件进行操作
text = string.join(text,"n")
file = StringIO.StringIO(text)

message = rfc822.Message(file)

for k, v in message.items():
    print k+"="+v
print message.fp.read()