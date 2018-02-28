# -*- coding: utf-8 -*-
"""
Created on Sun May 08 23:31:06 2016

@author: hp
"""

import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

hist_data = ts.get_hist_data('600000')
hist_data['close'].plot(figsize=(8, 5), grid=True) 
plt.show()
hist_data['return'] = np.log(hist_data['close'] / hist_data['close'].shift(1))
hist_data['return'].plot( figsize=(8, 5), grid=True)
plt.show()
hist_data['close'].plot(figsize=(8, 5), grid=True)

plt.show()