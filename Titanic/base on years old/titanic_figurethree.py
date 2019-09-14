import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

dataset = pd.read_csv('../dataset/train.csv')
flg = sns.FacetGrid(dataset,hue='Pclass',aspect=4)
flg.map(sns.kdeplot,'Age',shade=False)
oldset = dataset['Age'].max()
flg.set(xlim=(0,oldset))
flg.add_legend()
plt.show()