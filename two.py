import pandas as pd
import numpy as np

df =pd.DataFrame({'A':[1,2,np.nan],'B':['a',np.nan,'c'],'C':[10,np.nan,np.nan]})

print(df)
print(df['A'].isnull())
print(df[:].notnull())
print(df[:].notnull().sum())
print(df['c'].count())  #2 ans comes
print(df['C'].notnull().count())  #3 ans comes as it makes temp 




