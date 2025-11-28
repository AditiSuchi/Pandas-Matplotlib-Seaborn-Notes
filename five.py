import pandas as pd
import numpy as np
from numpy.random import randn

# df =pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],columns=['one','two','three'])
# print(df)

# df = df.reindex(['a','b','c','d','e','f','g','h'])
# print(df)
# print(df.dropna())  # it del whole row if there is any nan on that row

# print(df.dropna(axis=1)) 
# print(df.dropna(thresh=1))
df1 =pd.DataFrame({'one':[10,20,30,40,50,2000],'two':[1000,0,30,40,50,60]})
print(df1)
print(df1.replace({1000:10,2000:60}))


