# _*_ coding:utf-8 _*_ 
import urllib2 
from bs4 import BeautifulSoup

 
url=('https://movie.douban.com/top250?start=25&filter=')
page = urllib2.urlopen(url) 
contents = page.read() 
soup = BeautifulSoup(contents, "lxml") 
namelist=soup.findAll("option",{'value'})
for name in namelist:
    print(name.get_text())

#fout = open('myOutput.json', 'w')  
#fout.write(soup.encode('utf-8') )
#fout.close
#
#fin = open( 'myOutput.json')
#soup=fin.read()

#soup = BeautifulSoup(soup, "lxml") 