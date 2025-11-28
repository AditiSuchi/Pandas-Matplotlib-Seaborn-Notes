import pandas as pd
import numpy as np
from numpy.random import randn


df =pd.DataFrame(randn(5,2),index=[0,1,2,3,4],columns=['one','two'])
print(df)
print("Sum without isnull():",df['one'].sum())
print("sum with isnull function:",df['one'].isnull().sum())










