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

closing_df = DataReader(tech_list,data_source='yahoo',start=start,end=end)['Adj Close']
tech_rets = closing_df.pct_change()

sns.heatmap(tech_rets, square=True, linecolor="lightgray", linewidths=1)
plt.show()