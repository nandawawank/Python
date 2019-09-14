import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

dataset = pd.read_csv('../dataset/train.csv')
sns.factorplot('Sex',data=dataset, kind="count")
plt.show()