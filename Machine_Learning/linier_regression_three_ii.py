import sklearn
import seaborn as sns

from pandas import Series, DataFrame
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

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

coef_df = DataFrame(boston_df.columns)
coef_df.columns = ['Features']

coef_df['Coefficient Estimate'] = Series(lreg.coef_)
print(coef_df)