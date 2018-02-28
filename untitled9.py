


import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hist_data = ts.get_hist_data('600000')

hist_data['close'].plot(figsize=(8, 5), grid=True) 
from Tkinter import *
root=Tk()
b=Button(root,text='tu',command=plt.show()).pack()
root.mainloop()
