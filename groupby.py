import numpy as np
import pandas as pd

# Aggregation- computing a summary statistic
# Transformation- perform some group-sepcific operation
# Filtration- discarding the data with some condition

ipl_data ={'Team':['Rider','Rider','Devils','Devils','Kings','Kings','Kings','Kings','Rider','Royals','Royals','Rider'],
           'Rank':[1,2,2,3,3,4,1,1,2,4,1,2],
           'Year':[2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
           'Points':[876,786,868,673,741,812,756,788,694,701,804,690]}


df = pd.DataFrame(ipl_data)
print(df)

# df1=df.groupby('Rank').groups
# print(df1)

# df2=df.groupby(['Rank','Year']).groups
# print(df2)
# print(df.max())

# df3 = df.groupby('Rank').max()
# print(df3)

# df4 =df.groupby('Rank').max()['Points']
# print(df4)


# find the higest rank of the each team in ipl data

df5 = df.groupby('Team').max()['Rank']
print(df5)