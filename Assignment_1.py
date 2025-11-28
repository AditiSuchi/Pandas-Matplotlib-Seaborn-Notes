import numpy as np
import pandas as pd

p = pd.read_csv('C:\\Users\\aditi\\OneDrive\\Desktop\\Pandas\\Pands\\lowest_ranked_movies_data.csv')
# print(p)
# print(type(p))

# WAP to get the columns of the dataframe
print(p.columns)

# WAP to get the  of the information dataframe
# print(p.info())

# WAP to get the details of the third movie of the dataframe
# print(p.iloc[2])

# WAP to count the number of row and columns of the dataframe
# print(p.count())
# print(p.count)
# print(p.shape)

# WAP to get the Details of the columns name and genres of the detaframe
# print(p[['name','genre']])

#WAP toget d details of d movie with name 'Grumpier Old Men'
# print(p[p['name']  == 'Birdemic: Shock and Terror'])

# WAP to get the detail of the fifth movie of the DataFrame
# print(p.iloc[4])

# WAP to creat a smaller DataFrame with a subset of all Features
# p1 =p[['name','duration','director']]
# print(p1)

# WAP to display the first 10 rows of the DataFrame
# print(p.head(10))


# WAP to sort the DataFrame based on release_date
# print(p.sort_values('duration'))

# WAP to access those movies, released after 2010
# print(p[p['year']>2010][['name','year']])

# WAP tp sort movies on runtime in descending order
# print(p.sort_values('year'),False)


# WAP to get those movies whose revenue more than 2 million and spent less than 1 million

# WAP to get the movies name with start with