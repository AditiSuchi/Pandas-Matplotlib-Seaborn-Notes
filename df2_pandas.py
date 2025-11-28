import pandas as pd
import numpy as np

df =pd.DataFrame({'A':[1,2,np.nan],'B':['a',np.nan,'c'],'C':[10,np.nan,np.nan]})

# print(df)
print(df[:].isnull())
print(df[:].notnull())











