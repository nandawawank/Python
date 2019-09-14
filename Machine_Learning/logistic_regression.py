#Data imports
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

#Math
import math

#Plot imports
import matplotlib.pyplot as plt
import seaborn as sns

#Machine learning import
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

#For evaluation our ML result
import statsmodels.api as sm

df = sm.datasets.fair.load_pandas().data

def affair_check(x):
    if x != 0:
        return 1
    else:
        return 0

df['Had_Affair'] = df['affairs'].apply(affair_check)
df_groupby = df.groupby('Had_Affair').mean()

sns.factorplot('age',data=df,hue='Had_Affair',palette='coolwarm',kind='count')
# sns.catplot('age',data=df.dropna(),hue='Had_Affair',palette='coolwarm')
plt.show()
