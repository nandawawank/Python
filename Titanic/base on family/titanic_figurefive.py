import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import Series, DataFrame

generation = [10,20,40,60,80]
dataset = pd.read_csv('../dataset/train.csv')
# sns.lmplot('Age','Survived',data=dataset,palette='Set1')
# sns.lmplot('Age','Survived',hue='Pclass',data=dataset,palette='winter')
# sns.lmplot('Age','Survived',hue='Pclass',data=dataset,palette='winter',x_bins=generation)
sns.lmplot('Age','Survived',hue='Sex',data=dataset,palette='winter',x_bins=generation)
plt.show()