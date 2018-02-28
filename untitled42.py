# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 21:53:20 2017

@author: hp
"""

# coding:utf-8
# 功能：打印163邮箱的未读邮件标题
# 首先输入用户,比如邮箱用户是test@163.com,则输入test
# 然后输入密码
# 按任意键每次显示自定义的未读邮件标题
import urllib2
import urllib
import cookielib
import getpass
import readline
import re
import thread
class Login163(object):
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.sid = ''
        self.enable = False
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:27.0) Gecko/20100101 Firefox/27.0'}
        self.cookie = cookielib.LWPCookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookie))
        urllib2.install_opener(opener)
        # 登录获取sid
    def login(self):
        postdata = {
            'savelogin':'0',
            'url2':'http://mail.163.com/errorpage/error163.htm',
            'username':self.username,
            'password':self.password,
        }
        postdata = urllib.urlencode(postdata)
        url = 'https://ssl.mail.163.com/entry/coremail/fcg/ntesdoor2?df=mail163_letter&from=web&funcid=loginone&iframe=1&language=-1&passtype=1&product=mail163&net=t&style=-1&race=-2_46_-2_hz&uid='+self.username+'@163.com'
        req = urllib2.Request(url=url,data=postdata,headers=self.headers)
        res = urllib2.urlopen(req).read()
        if 'sid' in res:
            match = re.search(r'sid=(.*?)"',res)
            self.sid = match.group(1)
        return self.sid
        # 获取未读邮件标题
        # 默认每次显示20条未读邮件标题
    def get_unread_mail(self,start=0,limit=20):
        self.enable = True
        while self.enable:
            postdata = {
                'var':'<?xml version="1.0"?><object><int name="fid">1</int><boolean name="skipLockedFolders">false</boolean><string name="order">date</string><boolean name="desc">true</boolean><int name="start">'+str(start)+'</int><int name="limit">'+str(limit)+'</int><boolean name="topFirst">false</boolean><object name="filterFlags"><boolean name="read">false</boolean></object><boolean name="returnTotal">true</boolean><boolean name="returnTag">true</boolean></object>'
            }
            postdata = urllib.urlencode(postdata)
            url = 'http://twebmail.mail.163.com/js5/s?sid='+self.sid+'&func=mbox:listMessages&deftabclick=t2&deftabclick=undefined&from=toolbar&type=unread&mboxentry=1'
            req = urllib2.Request(url=url,data=postdata,headers=self.headers)
            res = urllib2.urlopen(req).read()
            if 'subject' in res:
                unread = re.findall(r'<string name="subject">(.*?)</string>',res)
                for subject in unread:
                    print subject
                start += limit
                raw_input('')
            else:
                self.enable = False
def main():
    username = raw_input('Enter you email:')
    password = getpass.getpass('Enter you password:')
    login = Login163(username,password)
    sid = login.login()
    if sid:
        login.get_unread_mail(limit=5)
if __name__ == '__main__':
    main()