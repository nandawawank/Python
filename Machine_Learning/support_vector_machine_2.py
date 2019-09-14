import numpy as np
import matplotlib.pyplot as plt

from sklearn import svm
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

X = iris['data'][:,:2]
Y = iris['target']
C = 1.0

svc = svm.SVC(kernel='linear',C=C).fit(X,Y)
rbf = svm.SVC(kernel='rbf',C=C,gamma='auto').fit(X,Y)
poly = svm.SVC(kernel='poly',C=C,degree=3).fit(X,Y)
linier = svm.LinearSVC(C=C).fit(X,Y)

h = 0.02
x_min = X[:,0].min() - 1
x_max = X[:,0].max() + 1
y_min = X[:,1].min() - 1
y_max = X[:,1].max() + 1

xx, yy = np.meshgrid(np.arange(x_min, x_max), np.arange(y_min, y_max, h))
title = [
    'SVC with linier kernel',
    'LinierSVC (linier kernal)',
    'SVC with RBF kernel',
    'SVC with Polynomial (deggre 3) kernel'
]

for i, clf in enumerate((svc, linier, rbf, poly)):
    plt.figure(figsize=(15,15))
    plt.subplot(2,2,i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.5)
    plt.scatter(X[:,0], X[:,1], c=Y)

    plt.xlabel('Sepal lenght')
    plt.ylabel('Sepal width')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.xticks(())
    plt.yticks(())
    plt.title(title[i])
    plt.show