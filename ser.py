import pandas as pd
import numpy as np
from numpy.random import randn

# ser = pd.Series(data=[1,2,3,np.nan,5])
# print(ser)
# print(ser.dropna())

df = pd.DataFrame([1,3,5,np.nan],[2,4,5,12],[6,4,2,1],[0,5,2,7])

print(df)
print(df.dropna())
