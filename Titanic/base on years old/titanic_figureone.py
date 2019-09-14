import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

dataset = pd.read_csv('../dataset/train.csv')
def male_fimale_child(pessanger):
    age, sex = pessanger
    if age < 16:
        return 'child'
    else:
        return sex
dataset['person'] = dataset[['Age','Sex']].apply(male_fimale_child,axis=1)
sns.factorplot('Pclass',data=dataset,kind='count',hue='person')
plt.show()
        