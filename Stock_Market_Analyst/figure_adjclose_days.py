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
ma_day = [10,20,50]
for ma in ma_day:
    column_name = "MA for %s days" % (str(ma))
    AAPL[column_name] = AAPL['Adj Close'].rolling(ma).mean()

AAPL[['Adj Close','MA for 10 days','MA for 20 days','MA for 50 days']].plot(subplots=False,figsize=(10,4))
plt.show()