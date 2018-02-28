# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:17:39 2016

@author: hp
"""
import wx.grid
import wx
import numpy as np
import pandas as pd
import tushare as ts
import sys, random
from PyQt4 import QtGui, QtCore
class Stockdata(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='The stock data analysis', size=(1000,600))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        wx.StaticText(parent=panel, label='Please input the stock code:', pos=(10,10))
        self.input = wx.TextCtrl(parent=panel, pos=(10,30))
        self.result1 = wx.StaticText(parent=panel, label='', pos=(10,100))
        self.result2 = wx.StaticText(parent=panel, label='', pos=(500,10))
        self.buttonCheck = wx.Button(parent=panel, label='Check', pos=(10,70))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCheck, self.buttonCheck)
        self.buttonQuit = wx.Button(parent=panel, label='Quit', pos=(100,70))
        self.Bind(wx.EVT_BUTTON, self.OnButtonQuit, self.buttonQuit)

    def OnButtonCheck(self, event):
        code=self.input.GetValue()
        global code
        try:
            hist_data = ts.get_hist_data(code)
            des=hist_data.describe()
            des='*************A describe of this stock*************'+'\n'+str(des)
            head=hist_data.head()
            head='*************Recent trend of this stock*************'+'\n'+str(head)
        except:
            head='wrong'      
        self.result1.SetLabel(head)
        self.result2.SetLabel(des)
    def OnButtonQuit(self, event):
        dlg=wx.MessageDialog(self,'Really Quit?','Caution',\
                             wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            self.Destroy()

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        self.drawLines(qp)
        qp.end()
    def drawPoints(self, qp):
        hist_data = ts.get_hist_data('600000')
        h=700-hist_data['close'].max()*10-1
        l=700-hist_data['close'].min()*10+3
        qp.setPen(QtCore.Qt.blue)
        k=hist_data['close'].count()
        x1=k+1
        hist_data['return'] = np.log(hist_data['close'] / hist_data['close'].shift(1))
        h=hist_data['return'].max()*10
        l=hist_data['return'].min()*10
        
        for i in hist_data['close']:
            y = 700-i*10
            x1 = x1 - 1
            for u in range(0,10):
                y = y+0.2
                x = x1+0.1
                qp.drawPoint(x, y)
        global k,h,l
    def drawLines(self, qp):
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(k, l, k, h)
        qp.drawLine(0, l, k, l)
       


if __name__=='__main__':

    class MyFrame(wx.Frame):
      def __init__(self):
        wx.Frame.__init__(sd)
    class MyFrame2(wx.Frame):
      def __init__(self):
        wx.Frame.__init__(ex)        
    class MyApp(wx.App):
      def OnInit(self):
        self.myframe = MyFrame()
        self.myframe2 = MyFrame2()
        self.SetTopWindow(self.myframe)
        self.myframe.Show(True)
        self.myframe2.Show(True)
        return True
    app = MyApp(0)
    sd=Stockdata(None)
    ex=Example(None)
    app.MainLoop()