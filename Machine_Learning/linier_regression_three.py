import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from sklearn.datasets import load_boston

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
boston = load_boston()
boston_df = DataFrame(boston['data'])
boston_df.columns = boston['feature_names']
boston_df['Price'] = boston['target']

X = boston_df.RM

Y = boston_df.Price
X = np.array([ 
                [value, 1] for value in X
            ])        

# m, b = np.linalg.lstsq(X,Y,rcond=None)[0]

# plt.plot(boston_df.RM,boston_df.Price,'o')
# x = boston_df.RM
# plt.plot(x, m * x + b, 'r', label='Best Fit Line')
# plt.show()

result = np.linalg.lstsq(X,Y,rcond=None)
error_result = result[1]
rmse = np.sqrt(error_result/len(X))

print('The root mean squared error was %.2f' % rmse)