from __future__ import division
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series,DataFrame
from pandas_datareader import DataReader
from datetime import datetime

sns.set_style('whitegrid')
tech_list = ['AAPL','GOOG','MSFT','AMZN']
end = '2018-01-01'
start = '2017-01-01'

for stock in tech_list:
    globals()[stock] = DataReader(stock,data_source='yahoo',start=start,end=end)

AAPL.describe()
AAPL['Daily Return'] = AAPL['Adj Close'].pct_change()
AAPL['Daily Return'].plot(figsize=(10,4),legend=True,linestyle='--',marker='o')
plt.show()