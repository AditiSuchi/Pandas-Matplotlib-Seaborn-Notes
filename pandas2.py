import numpy as np
import pandas as pd

se = pd.Series([2,4,6])
ser =pd.Series([3,5,7,9])

series =pd.concat([se,ser],axis=1)
print(series)
series =pd.concat([se,ser],axis=0)
print(series)




