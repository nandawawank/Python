import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

levels = []
dataset = pd.read_csv('../dataset/train.csv')
deck = dataset['Cabin'].dropna()
for level in deck:
    levels.append(level[0])

cabin_def = DataFrame(levels)
cabin_def.columns = ['Cabin']
# cabin_def = cabin_def[cabin_def.Cabin != 'T']
#factorplot soon in new release seaborn will bee rename catplot and default kind will bee rename strip
sns.factorplot('Cabin',data=cabin_def,kind='count',palette='winter_d')
plt.show()