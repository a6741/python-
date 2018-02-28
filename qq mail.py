# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 23:36:17 2017

@author: hp
"""

import smtplib
import poplib
from email.mime.text import MIMEText
_user = "@qq.com"
_pwd  = ""
_to   = "@qq.com"

msg = MIMEText("Test")
msg["Subject"] = "hey man fuck u"
msg["From"]    = _user
msg["To"]      = _to 


try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    print s
    s.login(_user, _pwd)
    print s
    s.mail
    s.sendmail(_user, _to, msg.as_string())
    print s    
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e 
