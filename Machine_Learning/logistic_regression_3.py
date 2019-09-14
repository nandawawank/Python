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
from sklearn.metrics import accuracy_score

#For evaluation our ML result
import statsmodels.api as sm

df = sm.datasets.fair.load_pandas().data

def affair_check(x):
    if x != 0:
        return 1
    else:
        return 0

df['Had_Affair'] = df['affairs'].apply(affair_check)

occ_dummies = pd.get_dummies(df['occupation'])
occ_dummies.columns = ['occ1','occ2','occ3','occ4','occ5','occ6']

hus_occ = pd.get_dummies(df['occupation_husb'])
hus_occ.columns = ['hocc1','hocc2','hocc3','hocc4','hocc5','hocc6']

Y = df['Had_Affair']
X = df.drop(['occupation','occupation_husb','Had_Affair'],axis=1)

dummies = pd.concat([occ_dummies, hus_occ], axis=1)
X = pd.concat([X, dummies], axis=1)
Y = np.ravel(Y)

log_model = LogisticRegression()
log_model.fit(X,Y)
score = log_model.score(X,Y)

coef_df = DataFrame(zip(X.columns, np.transpose(log_model.coef_)))

X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

log_model2 = LogisticRegression()
log_model2.fit(X_train,Y_train)

class_predict = log_model2.predict(X_test)

print(score)
print(accuracy_score(Y_test, class_predict))

