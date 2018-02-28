# -*- coding: utf-8 -*-
"""
Created on Wed Jul 05 21:10:02 2017

@author: hp
"""

# -*- coding: utf-8 -*-
"""
Created on Mon May 09 23:05:09 2016

@author: ljk
"""
import wx.grid
import wx
import tushare as ts
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg as NavigationToolbar
import pylab
from matplotlib import pyplot
import matplotlib
class MPL_Panel_base(wx.Panel):
    def __init__(self,parent):
        wx.Panel.__init__(self,parent=parent, id=-1)
        self.Figure = matplotlib.figure.Figure(figsize=(4,3))
        self.axes = self.Figure.add_axes([0.1,0.1,0.8,0.8])
        self.FigureCanvas = FigureCanvas(self,-1,self.Figure)
        self.NavigationToolbar = NavigationToolbar(self.FigureCanvas)
        self.SubBoxSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.StaticText = wx.StaticText(self,-1,label='Show Help String')  
        self.SubBoxSizer.Add(self.NavigationToolbar,proportion =0, border = 2,flag = wx.ALL | wx.EXPAND)
        self.TopBoxSizer = wx.BoxSizer(wx.VERTICAL)
        self.TopBoxSizer.Add(self.SubBoxSizer,proportion =-1, border = 2,flag = wx.ALL | wx.EXPAND)
        self.TopBoxSizer.Add(self.FigureCanvas,proportion =-10, border = 2,flag = wx.ALL | wx.EXPAND)
        self.SubBoxSizer.Add(self.StaticText,proportion =-1, border = 2,flag = wx.ALL | wx.EXPAND)  
        self.SetSizer(self.TopBoxSizer)
        self.pylab=pylab
        self.pl=pylab
        self.pyplot=pyplot
        self.numpy=np
        self.np=np
        self.plt=pyplot
    def UpdatePlot(self):
        self.FigureCanvas.draw()
    def plot(self,*args,**kwargs):
        self.axes.plot(*args,**kwargs)
        self.UpdatePlot()
    def semilogx(self,*args,**kwargs):
        self.axes.semilogx(*args,**kwargs)
        self.UpdatePlot()
    def semilogy(self,*args,**kwargs):
        self.axes.semilogy(*args,**kwargs)
        self.UpdatePlot()
    def loglog(self,*args,**kwargs):
        self.axes.loglog(*args,**kwargs)
        self.UpdatePlot()
    def xlabel(self,XabelString="X"):
        self.axes.set_xlabel(XabelString)
    def ylabel(self,YabelString="Y"):
        self.axes.set_ylabel(YabelString)
    def legend(self,*args,**kwargs):
        self.axes.legend(*args,**kwargs)
    def xlim(self,x_min,x_max):
        self.axes.set_xlim(x_min,x_max)
    def ylim(self,y_min,y_max):
        self.axes.set_ylim(y_min,y_max)
    def savefig(self,*args,**kwargs):
        self.Figure.savefig(*args,**kwargs)
    def cla(self):
        self.axes.clear()
        self.Figure.set_canvas(self.FigureCanvas)
        self.UpdatePlot()
    def ShowHelpString(self,HelpString="Show Help String"):  
        self.StaticText.SetLabel(HelpString)
class MPL_Frame(wx.Frame):
    def __init__(self,title="Pictures",size=(800,500)):
        wx.Frame.__init__(self,parent=None,title = title,size=size)
        self.MPL = MPL_Panel_base(self)
        self.FlexGridSizer=wx.FlexGridSizer( rows=9, cols=1, vgap=5,hgap=5)
        self.FlexGridSizer.SetFlexibleDirection(wx.BOTH)
        self.RightPanel = wx.Panel(self,-1)
        self.Button1 = wx.Button(self.RightPanel,-1,"Code Trend",size=(100,40),pos=(10,10))
        self.Button1.Bind(wx.EVT_BUTTON,self.Button1Event)
        self.FlexGridSizer.Add(self.Button1,proportion =0, border = 5,flag = wx.ALL | wx.EXPAND)
        self.Button2 = wx.Button(self.RightPanel,-1,"Return Rate",size=(100,40),pos=(10,10))  
        self.Button2.Bind(wx.EVT_BUTTON,self.Button2Event)  
        self.FlexGridSizer.Add(self.Button2,proportion =0, border = 5,flag = wx.ALL | wx.EXPAND)  
        self.Button3 = wx.Button(self.RightPanel,-1,"The Turnover",size=(100,40),pos=(10,10))  
        self.Button3.Bind(wx.EVT_BUTTON,self.Button3Event)  
        self.FlexGridSizer.Add(self.Button3,proportion =0, border = 5,flag = wx.ALL | wx.EXPAND)
        self.RightPanel.SetSizer(self.FlexGridSizer)
        self.BoxSizer=wx.BoxSizer(wx.HORIZONTAL)
        self.BoxSizer.Add(self.MPL,proportion =-10, border = 2,flag = wx.ALL | wx.EXPAND)
        self.BoxSizer.Add(self.RightPanel,proportion =0, border = 2,flag = wx.ALL | wx.EXPAND)        
        self.SetSizer(self.BoxSizer)	
        self.StatusBar()
        self.Centre(wx.BOTH)  
        self.MPL.ShowHelpString("It maybe a little slow, don't be hurry"+'\n'+"If the picture isn't clear,please use the 'zoom' to zoom in it ")  
    def Button1Event(self,event):
        self.MPL.cla()
        hist_data = ts.get_hist_data(code)
        x=hist_data['close'].count()
        x= np.arange(x,0,-1)
        y=hist_data['close'][x-1]
        x=max(x)-x+1
        self.MPL.plot(x,y,'--*g')
        self.MPL.UpdatePlot()
    def Button2Event(self,event):
        self.MPL.cla()
        hist_data = ts.get_hist_data(code)
        hist_data['return'] = np.log(hist_data['close'] / hist_data['close'].shift(1))
        x=hist_data['return'].count()
        x= np.arange(x,0,-1)
        y=hist_data['return'][x-1]
        x=max(x)-x+1
        self.MPL.plot(x,y,'--*g')
        self.MPL.UpdatePlot()
    def Button3Event(self,event):
        self.MPL.cla()
        hist_data = ts.get_hist_data(code)
        x=hist_data['turnover'].count()
        x= np.arange(x,0,-1)
        y=hist_data['turnover'][x-1]
        x=max(x)-x+1
        self.MPL.plot(x,y,'--*g')
        self.MPL.UpdatePlot()
    def StatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-2, -2, -1])
class Stockdata(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='The stock data analysis', size=(1000,600))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        wx.StaticText(parent=panel, label='Please input the stock code:', pos=(10,10))
        self.input = wx.TextCtrl(parent=panel, pos=(10,30))
        self.result1 = wx.StaticText(parent=panel, label='', pos=(10,100))
        self.result2 = wx.StaticText(parent=panel, label='', pos=(500,10))
        self.buttonCheck = wx.Button(parent=panel, label='Informations', pos=(10,70))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCheck, self.buttonCheck)
        self.buttonQuit = wx.Button(parent=panel, label='Quit', pos=(195,70))
        self.Bind(wx.EVT_BUTTON, self.OnButtonQuit, self.buttonQuit)
        self.buttonShowPicture = wx.Button(parent=panel, label='ShowPicture', pos=(105,70))
        self.Bind(wx.EVT_BUTTON, self.OnButtonPicture, self.buttonShowPicture)
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
            head='wrong!'
            des=''
        self.result1.SetLabel(head)
        self.result2.SetLabel(des)

    def OnButtonQuit(self, event):
        dlg=wx.MessageDialog(self,'Really Quit?','Caution',\
                             wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            self.Destroy()
    def OnButtonPicture(self, event):
        code=self.input.GetValue()
        global code
        try:
                if ts.get_hist_data(code) .all!=False:
                    frame =MPL_Frame()
                    frame.Center()
                    frame.Show()
        except:
                head='wrong!'
                self.result1.SetLabel(head)
                des=''  
                self.result2.SetLabel(des)
if __name__ == '__main__':
    app = wx.App()
    frame = Stockdata(None)
    frame.Show()
    app.MainLoop()
    del app