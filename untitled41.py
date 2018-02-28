# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 20:56:58 2017

@author: hp
"""

import smtplib
from email.mime.text  import  MIMEText
from  email.header  import Header
Sender ="a674153814@163.com"       # 发件人Email地址
AuthorizationCode='ljk674153814'     # 授权码，163邮箱开启SMTP服务时授权第三方登陆邮箱的授权码
receiver ="a674153814@163.com"    # 收件人地址
smtp_server ='smtp.163.com'             # SMTP服务器地址
msg.MIMEText('你好！我是Python发邮测试！','plain','utf-8')       #邮件正文
msg['Subject']=Header('测试','utf-8')        #邮件主题
msg['From']=formataddr(['***',Sender])    #发件人，显示在收件人界面上
msg['To']=formataddr(['',receiver])            #收件人
smtpObj = smtplib.SMTP()
smtpObj.connect(smtp_server,25)              # 25 为 SMTP 端口号
smtpObj.login(Sender,AuthorizationCode)   #登陆邮箱
smtpObj.sendmail(Sender, receiver, msg.as_string())  #发送邮件
smtpObj.quit()