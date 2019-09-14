import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn import linear_model
from sklearn.datasets import load_iris

iris = load_iris()

X = iris.data
Y = iris.target

iris_data = DataFrame(X, columns=['Sepal Lenght','Sepal Width','Petal Lenght','Petal Width'])
iris_target = DataFrame(Y, columns=['Species'])

def flower(num):
    if num == 0:
        return 'Setosa'
    elif num == 1:
        return 'Versicolour'
    else:
        return 'Virginica'

iris_target['Species'] = iris_target['Species'].apply(flower)
iris = pd.concat([iris_data, iris_target], axis = 1)

# sns.pairplot(iris, hue='Species', size=2)
sns.factorplot('Petal Lenght', data=iris, hue='Species', size=10, kind='count')
plt.show()