import numpy as np
import pandas as pd

d= pd.Series(range(1,11))
print(d)
print(d[7:10])
print(d[-1:-4:-1])

data ={"a":1,"b":2,"c":3}
s = pd.Series(data,index=["b","c","d","a"])
print(s)
