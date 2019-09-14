import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import DataFrame, Series

dataset = pd.read_csv('../dataset/train.csv')
dataset['Alone'] = dataset.SibSp + dataset.Parch
dataset['Alone'].loc[dataset['Alone'] > 0] = 'With Family'
dataset['Alone'].loc[dataset['Alone'] == 0] = 'Alone'
sns.factorplot('Alone',data=dataset,kind='count',palette='Blues')
plt.show()
