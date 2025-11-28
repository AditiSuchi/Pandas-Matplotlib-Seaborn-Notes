import pandas as pd
import numpy as np
from numpy.random import randn

outer =['a','a','a','b','b','b']
inner =[1,2,3,1,2,3]
h_index = list(zip(outer,inner))
h_index = pd.MultiIndex.from_tuples(h_index)
print(h_index)

df1=pd.DataFrame(randn(6,2))
df2=pd.DataFrame(randn(6,2),h_index)
df3=pd.DataFrame(randn(6,2),h_index,['A','B'])
print(df1)
print(df2)
print(df3)