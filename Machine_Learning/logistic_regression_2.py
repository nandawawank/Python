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

occ_dummies = pd.get_dummies(df['occupation'])
occ_dummies.columns = ['occ1','occ2','occ3','occ4','occ5','occ6']

hus_occ = pd.get_dummies(df['occupation_husb'])
hus_occ.columns = ['hocc1','hocc2','hocc3','hocc4','hocc5','hocc6']

X = df.drop(['occupation','occupation_husb'],axis=1)
dummies = pd.concat([occ_dummies, hus_occ], axis=1)
X = pd.concat([X, dummies], axis=1)
Y = df.Had_Affair


