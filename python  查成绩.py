# -*- coding: utf-8 -*-
import re
import requests
from tkinter import *
from tkinter.ttk import *
def foo():
    s=requests.session()
    payload={'Login.Token1':e1.get(),'Login.Token2':e2.get()}
    s.post('http://ssfw.xmu.edu.cn/cmstar/userPasswordValidate.portal',data=payload)
    r=s.get('http://ssfw.xmu.edu.cn/cmstar/index.portal?.pn=p1201_p3535')
    rs=re.findall(r'<tr>\s+<td width="260px">\s+<font color="">(.+?)</font>&nbsp;\s+</td>\s+<td>\s+<font color="">.+?</font>&nbsp;\s+</td>\s+<td>\s+<font color="">.+?</font>&nbsp;\s+</td>\s+<td>\s+<font color="">.+?</font>&nbsp;\s+</td>\s+<td>\s+<font color="">(.+?)</font>&nbsp;\s+</td>\s+<td>\s+<font color=""></font>&nbsp;\s+</td>\s+<td width="70px">\s+<font color="">\s+.+?\s+</font>&nbsp;\s+</td>\s+</tr>',r.text)
    for i in range(0,len(rs)): 
        listbox.insert(END, rs[i])

root=Tk()
root.title('厦大成绩查询')
root.geometry('500x500+400+200')
frm1=Frame(root,width=150,height=50).pack()
frm2=Frame(root,width=150,height=200).pack()
Label(frm1,text='学号').place(x=20,y=20)
e1=Entry(frm1)
e1.place(x=80,y=20)
Label(frm1,text='密码').place(x=20,y=50)
e2=Entry(frm1)
e2['show'] = '*'
e2.place(x=80,y=50)
Button(frm1,text='查询成绩',command=foo).place(x=300,y=35)
Label(frm2,text='查询结果').pack()
sv=StringVar()
listbox=Listbox(frm2,width=30)
listbox.pack()
root.mainloop()