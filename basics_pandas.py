import numpy as np
import pandas as pd

s=pd.Series(10,index=[0,1,2])
print(s)
s=pd.Series("d",index=[0,1,2])
print(s)
d = pd.Series(np.arange(5))
print(d)

d = pd.Series(np.arange(5),index=["a","b","c","d","e"])
print(d)

