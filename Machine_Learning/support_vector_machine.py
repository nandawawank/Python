import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris['data']
Y = iris['target']

svm = SVC()
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, random_state=3)
svm.fit(X_train, Y_train)

predicted = svm.predict(X_test)
score = metrics.accuracy_score(Y_test, predicted)
print(score)





