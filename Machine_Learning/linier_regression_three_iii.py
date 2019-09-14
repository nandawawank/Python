import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import Series, DataFrame
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

sns.set_style('whitegrid')
boston = load_boston()
boston_df = DataFrame(boston['data'])
boston_df.columns = boston['feature_names']
boston_df['Price'] = boston['target']

lreg = LinearRegression()

X_multi = boston_df.drop('Price',1)
Y_target = boston_df.Price

lreg.fit(X_multi,Y_target)

print('The estimated intercept coefficient is %.2f'  % lreg.intercept_)
print('The number of coefficient used was %d' % len(lreg.coef_))

X = boston_df.RM
X = [
        [value, 1] for value in X
    ]

x_train, x_test, y_train, y_test = train_test_split(X, boston_df.Price)
lreg.fit(x_train,y_train)

pred_train = lreg.predict(x_train)
pred_test = lreg.predict(x_test)

print('Fit a model x_train and calculate the MSE with y_train: %.2f' % (np.mean(y_train - pred_train)**2))
print('Fit a model x_train and calculate the MSE with x_test and y_test: %.2f' % (np.mean(y_test - pred_test)**2))

train  = plt.scatter(pred_train, (pred_train - y_train), c='b', alpha=0.5)
test = plt.scatter(pred_test, (pred_test - y_test), c='r', alpha=0.5)

plt.hlines(y=0, xmin=10, xmax=40)
plt.legend((train, test), ('Training', 'Test'), loc='lower left')
plt.title('Residual Plot')
plt.show()
