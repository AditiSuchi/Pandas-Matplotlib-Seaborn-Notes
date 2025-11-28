import pandas as pd
import numpy as np
from numpy.random import randn


df = pd.DataFrame(randn(6,3),columns=["col1","col2","col3"])

print(df)
print(df['col1'].sum())