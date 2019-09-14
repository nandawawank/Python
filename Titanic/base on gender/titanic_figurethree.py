import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

dataset = pd.read_csv('../dataset/train.csv')
sns.factorplot('Pclass',data=dataset,kind='count',hue='Sex')
plt.show()
