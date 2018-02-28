# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:25:20 2017

@author: hp
"""
import xlrd
import xlwt
import requests 
import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import time
#driver=webdriver.Chrome(executable_path="C://Program Files (x86)//Google//Chrome//Application//chrome.exe")
driver = webdriver.PhantomJS(executable_path="D://phantomjs-2.1.1-windows//bin//phantomjs.exe")
driver.maximize_window()
def get_mail(path):
    fileform={}
    global fileform
    driver.get('https://mail.qq.com')
    time.sleep(2)
    try:
        driver.find_element_by_id('loginform')
        a = True
    except:
        a = False
        print 'FALSE'
        return 0
    if a == True:
        driver.switch_to.frame('login_frame')
        driver.find_element_by_id('switcher_plogin').click()
        driver.find_element_by_id('u').clear()#选择用户名框
        driver.find_element_by_id('u').send_keys(raw_input('user:'))
        driver.find_element_by_id('p').clear()
        driver.find_element_by_id('p').send_keys(raw_input('password:'))
        driver.find_element_by_id('login_button').click()
        time.sleep(3)
    if 1 == True:
        driver.find_element_by_id('folder_1').click()
        want=raw_input('search:').decode('gbk')
        start=raw_input('date start from(eg:2017.6.1)')
        global start
        year=int(re.split('\.',start)[0])
        month=int(re.split('\.',start)[1])
        day=int(re.split('\.',start)[2])
        sd=year*10000+month*100+day
        flag=''
        page={}
        pdict1={}
        pnum=1
        global pdict1
        driver.switch_to.frame('mainFrame')
        print '\n查找到以下邮件\n'
        while flag!='end':
            pdict1[pnum]={}
            pages = driver.page_source
            soup = BeautifulSoup(pages,'lxml')
            page[pnum]=soup.find_all('table',class_="i M")
            page[pnum]+=soup.find_all('table',class_="i F")
            for uf in page[pnum]:
                date=uf.find('td',class_='dt').find('div').get_text()
                try:
                    mailmon=re.search(u'\d+(?=月)',date).group(0)
                    mailday=re.search(u'(?<=月)\d+',date).group(0)
                    myear=time.localtime().tm_year
                except:
                    try:                    
                        mailmon=re.search('(?<=/)\d+',date).group(0)
                        mailday=re.search('(?<=/)\d+$',date).group(0)
                        myear=re.search('\d+(?=/)',date).group(0)
                    except:
                        myear=time.localtime().tm_year
                        mailmon=time.localtime().tm_mon
                        mailday=time.localtime().tm_mday
                md=int(myear)*10000+int(mailmon)*100+int(mailday)
                if md<sd:
                    flag='end'
                    break
                title=uf.find('u',tabindex="0").get_text()
                i=1
                if want in title:
                    if title in pdict1[pnum]:
                        while title+str(i) in pdict1[pnum]:
                            i+=1
                        title+=str(i)
                    print title,'\n'
                    (pdict1[pnum])[title]=(page[pnum]).index(uf)
            try:
                driver.find_element_by_id('nextpage1').click()
                pnum+=1
            except:
                flag='end'
        driver.find_element_by_xpath("//*[@id='frm']/table/tbody/tr/td[6]/div/a").click()
        driver.find_element_by_xpath("//*[@id='frm']/table/tbody/tr/td[6]/div/a").click()  
        cookie = driver.get_cookies()
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        global headers
        cookie_dict = {}
        for c in cookie:
            cookie_dict[c['name']]=c['value']
        global cookie_dict
        if os.path.exists(path)==False:
            os.makedirs(path)
        for p in pdict1:
            for i in pdict1[p]:
                find()
                print "\n=========="+i+"================"
                try:
                    clickon(let[pdict1[p][i]],i,path)
                except:
                    print '未知错误，自动退出'
                    break
            try:
                driver.find_element_by_id('nextpage1').click()
            except:
                pass
        print("==========完成================")
        makeexcel(path)
    driver.close()
    driver.quit()
def clickon(uid,title,path):
    uid.click()
    cpages = driver.page_source
    csoup = BeautifulSoup(cpages,'lxml')
    wr=csoup.find('div',id='mailContentContainer')
    try:
        print re.split('.qmbox style',wr.get_text())[0]
    except:
        print '无法提取该格式内容'
    try:    
        downurl='https://mail.qq.com'+csoup.find('div',class_='down_big').find('a')['href']
        files=requests.get(downurl,headers=headers,cookies=cookie_dict)
        fname=csoup.find('div',class_='name_big').find('span').get_text()
        fform=(re.search('.\w+$',fname)).group(0)
        fileform[title+fform]=fform
        with open(path+"\\"+title+fform,"wb") as f:
            f.write(files.content)
        print '附件下载成功'
    except:
        print '无附件'
    driver.find_element_by_xpath("//a[@class='btn_gray btn_space btn_back left']").click()
def find():
    let=driver.find_elements_by_xpath("//table[@class='i M']/tbody/tr/td[3]")
    let+=driver.find_elements_by_xpath("//table[@class='i F']/tbody/tr/td[3]")
    global let            
def makeexcel(path):
    summary=xlwt.Workbook()
    hang=1
    #b=[]
    #b.append(raw_input().decode('gbk'))
    b=[u'获奖名称',u'姓名']
    sumsheet=summary.add_sheet(u'统计')
    for i in b:
        sumsheet.write(0,b.index(i),i)
    global b
    global hang
    global sumsheet
    for i in fileform:
        if u'.dos' in fileform[i]:
            solveword(path+'\\'+i)
        elif u'xls' in fileform[i]:
            solveexcel(path+'\\'+i)
        else:
            print '暂不支持此格式文件'
    summary.save(path+'\\'+'summary.xls')
            
def solveexcel(files):
    data = xlrd.open_workbook(files)
    loc={}
    global hang,b
    for sheet in data.sheets():
        loc[sheet.name]={}
        for col in range(sheet.ncols):
            for bs in b:
                if bs==sheet.cell(1,col).value:
                    loc[sheet.name][sheet.cell(1,col).value]=col
                    break
    for sheet in data.sheets():
        for row in range(2,sheet.nrows):
                for i in loc[sheet.name]:
                    sumsheet.write(hang,b.index(i),sheet.cell(row,loc[sheet.name][i]).value)
                if len(loc[sheet.name])!=0:
                    hang+=1
                    print len(loc[sheet.name]),loc[sheet.name]
#def solveword():
if __name__ == '__main__':
    get_mail(r'C:\Users\hp\Desktop\mail')