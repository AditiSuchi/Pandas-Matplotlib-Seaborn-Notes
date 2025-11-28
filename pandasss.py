import pandas as pd
import numpy as np
from numpy.random import randn

df =pd.DataFrame(randn(5,4),['a','b','c','d','e'],['x','y','z','w'])
print(df)

print(df.reset_index())

