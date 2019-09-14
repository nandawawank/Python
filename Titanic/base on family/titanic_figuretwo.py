import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

dataset = pd.read_csv('../dataset/train.csv')
dataset['Survivor'] = dataset.Survived.map({0:'no',1:'yes'})
sns.factorplot('Survivor',data=dataset,kind='count',palette='Set1')
plt.show()