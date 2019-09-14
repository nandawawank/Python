import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.datasets import load_iris
from sklearn import linear_model, metrics
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

iris = load_iris()


X = iris.data
X = DataFrame(X, columns=['Sepal Lenght','Sepal Width','Petal Lenght','Petal Width'])
Y = iris.target
Y = np.ravel(Y)


logleg = LinearRegression()
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.4, random_state=3)

logleg.fit(X_train, Y_train)
Y_predict = logleg.predict(X_test)
Y_predict = Y_predict.astype(int)
score = metrics.accuracy_score(Y_test,Y_predict)
print('Logistict Regression :',score)

knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, Y_train)
Y_predict = knn.predict(X_test)
score = metrics.accuracy_score(Y_test,Y_predict)
print('K-Neightbord :',score)