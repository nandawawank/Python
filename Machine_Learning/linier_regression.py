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
print(boston_df.head())

# plt.hist(boston['target'],bins=50)
# plt.scatter(boston['data'][:,5],boston['target'])
# plt.xlabel('Prices in $1000s')
# plt.ylabel('Number of houses')
# plt.show()

sns.lmplot('RM','Price',data=boston_df)
plt.show()
