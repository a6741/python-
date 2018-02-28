# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 19:26:22 2017

@author: hp
"""
import tkFileDialog
import xlrd
import quopri
from tkinter import *
from tkinter.ttk import *
import os
reload(sys)
sys.setdefaultencoding("utf-8")
def tovcf():
    listbox.delete(0,END)
    dic={}
    #path=r"C:\Users\hp\Desktop\新建.xls"
    try:
        path=e1.get()
        global path
        if u'\u202a' in path:
            path=re.split(u'\u202a',path)[1]
        data = xlrd.open_workbook(path)
        strs="BEGIN:VCARD\nVERSION:2.1\nFN;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE:{0}\nTEL;CELL;PREF:{1}\nEND:VCARD\n"
        dst=os.path.join(os.path.expanduser("~"), "Desktop")
        with open(dst+'\\all.vcf',"w") as f:
            for sheet in data.sheets():
                n=0
                global dic
                try:
                    while not dic.has_key('姓名') or not dic.has_key('电话'):
                            for col in range(sheet.ncols):
                                if sheet.cell(n,col).value==u'姓名':
                                    dic['姓名']=col
                                if sheet.cell(n,col).value==u'电话':
                                    dic['电话']=col
                            n+=1
                except:
                    dic['姓名']=0
                    dic['电话']=1
                    n=1
                for row in range(n,sheet.nrows):
                    try:
                        a=sheet.cell(row,dic['姓名']).value+'家长'
                        a=a.encode('utf-8')
                        name = quopri.encodestring(a)
                        tel=int(sheet.cell(row,dic['电话']).value)
                        f.write(strs.format(name,tel))
                    except:
                        g='第'+str(row+1)+'行出现错误'
                        listbox.insert(END, g)
        if os.path.getsize(dst+'\\all.vcf')!=0:
            listbox.insert(END, '*******************转换完成********************')
            listbox.insert(END, '已在桌面生成名为all.vcf的文件，将其导入手机通讯录即可')
            listbox.insert(END, '可通过数据线或者qq将vcf文件传至手机')
            listbox.insert(END, '不管手机什么系统，点击文件，打开方式选择通讯录导入')
            listbox.insert(END, '然后就可以看到导入成功的联系人名片了')
        else:
            os.remove(dst+'\\all.vcf')
            listbox.delete(0,END)
            listbox.insert(END, '该文件格式不规范')
            listbox.insert(END,"注意excel内姓名那列最顶上一格为 姓名")
            listbox.insert(END,"电话号码那列最顶上一格为 电话")
            listbox.insert(END,"如果还是不行，可以将姓名放第一列，电话放第二列再尝试")
    except:
        listbox.insert(END, '该文件并非excel文件')
def findroad():
    filename = tkFileDialog.askopenfilename(initialdir = 'E:/Python')
    sv.set(filename)
root=Tk()
root.title('excel生成vcf文件')
root.geometry('400x270')
sv=StringVar()
frm1=Frame(root,width=150,height=50).pack()
frm2=Frame(root,width=100,height=30).pack()
Label(frm1,text='excel文件路径:').place(x=20,y=20)
e1=Entry(frm1,textvariable=sv,width=35)
e1.place(x=110,y=20) 
Button(frm1,text='开始转换',command=tovcf).place(x=250,y=50)
Button(frm1,text='选择路径',command=findroad).place(x=110,y=50)
listbox=Listbox(frm2,width=50,height=10)
listbox.pack()
listbox.insert(END,"请在上方的方框内输入源excel文件地址,然后点击'开始转换'")
listbox.insert(END,"注意excel内姓名那列最顶上一格为 姓名")
listbox.insert(END,"电话号码那列最顶上一格为 电话")
listbox.insert(END,"点击'选择路径'以选择待转换excel文件路径")
root.mainloop()