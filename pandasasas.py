import pandas as pd
import numpy as np
from numpy.random import randn

df = pd.DataFrame(randn(6,3),columns=["col1","col2","col3"])
print(df)
print("After renaming the Rows and Columns: ")
df1=df.rename(columns={"col1":"c1","col2":"c2"},index={0:"apple",1:'banana',2:"durian"})
print(df1)
