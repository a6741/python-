# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 14:01:39 2017

@author: hp
"""
import re
import requests
from bs4 import BeautifulSoup
headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",'Cookie':'pgv_pvid=4312036325; pgv_pvi=733492224; RK=7Otiow8rT8; _qpsvr_localtk=0.3596759034211734; pgv_si=s3768910848; pgv_info=ssid=s1838601306; ptui_loginuin=172832763; ptisp=cnc; ptcz=ef1a94703144380db6ff72d0710615fce0b4a828a2448cf00c42b1a0e1c2d0c5; pt2gguin=o0172832763; uin=o0172832763; skey=@GDx02oLGG; p_uin=o0172832763; p_skey=GWmAZsK3FCK24gkLjBcUAv9HG49i6n3UmBi0E6WLPBo_; pt4_token=Wy3i-oJHl16T0LCUzKQITEeKD-JNRa0UTHgdcYGi7E4_; wimrefreshrun=0&; qm_flag=0; qqmail_alias=172832763@qq.com; sid=172832763&e843f7d67afd1e6050409bd09b5eeb0b,qR1dtQVpzSzNGQ0syNGdrTGpCY1VBdjlIRzQ5aTZuM1VtQmkwRTZXTFBCb18.; qm_username=172832763; qm_domain=https://mail.qq.com; qm_ptsk=172832763&@GDx02oLGG; foxacc=172832763&0; ssl_edition=sail.qq.com; edition=mail.qq.com; qm_loginfrom=172832763&wpt; username=172832763&172832763; new_mail_num=172832763&0; webp=1; CCSHOW=000000'}
s=requests.session()
#login={'u':raw_input(),'p':raw_input()}
r=s.get('https://mail.qq.com/',headers=headers)
print r
Soup=BeautifulSoup(r.text,'lxml')
print Soup