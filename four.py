import pandas as pd
import numpy as np

df =pd.DataFrame({'A':[1,2,np.nan],'B':['a',np.nan,'c'],'C':[10,np.nan,np.nan]})
print(df)
# print(df.fillna('a'))
# print("----------------")
# print(df.fillna(5))

# print(df['A'].fillna(df['A'].mean()))
# print(df.fillna(df['A'].mean()))


# print(df.fillna(value=df['A'].mean()))
# print(df.fillna(value=df.mean()))
# print(df.fillna(value=df['A'].mean()))
# print(df.fillna(df['A'].sum()))
# print(df['A'].fillna(value=df.sum()))
# print(df.fillna(value=df["A"].sum()))
print()



