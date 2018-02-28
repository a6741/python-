# -*- coding: utf-8 -*-
"""
Created on Mon May 09 23:05:09 2016

@author: hp
"""

import wx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas.io.data as web

class IsPrimeFrame(wx.Frame):
    def __init__(self, superion):
        wx.Frame.__init__(self, parent=superion, title='Check Prime', size=(400,200))
        panel = wx.Panel(self)
        panel.SetBackgroundColour('White')
        wx.StaticText(parent=panel, label='Please input the stock code or input end to stop:', pos=(10,10))
        self.inputN = wx.TextCtrl(parent=panel, pos=(10,30))
        self.result = wx.StaticText(parent=panel, label='', pos=(10,50))
        self.buttonCheck = wx.Button(parent=panel, label='Check', pos=(70,90))
        self.Bind(wx.EVT_BUTTON, self.OnButtonCheck, self.buttonCheck)
        self.buttonQuit = wx.Button(parent=panel, label='Quit', pos=(150,90))
        self.Bind(wx.EVT_BUTTON, self.OnButtonQuit, self.buttonQuit)

    def OnButtonCheck(self, event):
        x=self.inputN.GetValue()
        try:
            DAX = web.DataReader(name=x, data_source='yahoo',start='2001-1-1')
            DAX.info()
            DAX['Close'].plot(figsize=(8, 5), grid=True) 
            plt.show()
            print DAX.tail()
            print DAX.describe()
        except:
            print 'wrong'
    def OnButtonQuit(self, event):
        dlg=wx.MessageDialog(self,'Really Quit?','Caution',\
                             wx.CANCEL|wx.OK|wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_OK:
            self.Destroy()
if __name__ == '__main__':
    app = wx.App()
    frame = IsPrimeFrame(None)
    frame.Show()
    app.MainLoop()
    del app
