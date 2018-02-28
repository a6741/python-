# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:01:31 2017

@author: hp
"""

#coding=gbk  
import urllib2  
  
HEADERS = {'cookie':'pgv_pvid=4312036325; pgv_pvi=733492224; RK=7Otiow8rT8; pgv_si=s1008726016; ptui_loginuin=172832763; ptisp=cnc; ptcz=ef1a94703144380db6ff72d0710615fce0b4a828a2448cf00c42b1a0e1c2d0c5; pt2gguin=o0172832763; uin=o0172832763; p_uin=o0172832763; p_skey=Xv31MXidD1Dkr0fMLiUlSGx6uV-Ufh0FVMCZG3aVpMI_; pt4_token=m5zt3efwMDPvkKB9Lnup-Hs*u4*i4JxV0BoKFSh*mAY_; qm_sid=42b6cd589baef6ddf7e066914b3b9281,qWHYzMU1YaWREMURrcjBmTUxpVWxTR3g2dVYtVWZoMEZWTUNaRzNhVnBNSV8.; reader_mail_cur_page=; qm_ptsk=172832763&@37gR1wa1j; wimrefreshrun=0&; qm_flag=0; qqmail_alias=172832763@qq.com; sid=172832763&42b6cd589baef6ddf7e066914b3b9281,qWHYzMU1YaWREMURrcjBmTUxpVWxTR3g2dVYtVWZoMEZWTUNaRzNhVnBNSV8.; qm_username=172832763; qm_domain=https://mail.qq.com; foxacc=674153814&0|172832763&0; ssl_edition=sail.qq.com; edition=mail.qq.com; qm_loginfrom=674153814&wsk|172832763&wsk; username=172832763&172832763; CCSHOW=000000; new_mail_num=674153814&0|172832763&0; webp=1'}
url = 'https://mail.qq.com/'  
req = urllib2.Request(url, headers=HEADERS)  
text = urllib2.urlopen(req).read()    
print "登陆成功!"  
print "登录失败!" 