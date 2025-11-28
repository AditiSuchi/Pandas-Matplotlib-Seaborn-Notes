import pandas as pd

# data ={
#     "Student": ["Aditi","Baiju","Manisha","Guddu Bhaiya"],
#     "marks":[100,99,89,82]
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.loc[0])
# print(df.loc[[2,3]])


# df = pd.DataFrame(data,index=['rank-1','rank-2','rank-3','rank-4'])
# # print(df)
# print(df.loc[['rank-1','rank-2']])

# dic_data =[{'a':1,'b':2},{'a':5,'b':10,'c':20}]
# df1= pd.DataFrame(dic_data)
# print(df1)
# df1= pd.DataFrame(dic_data,index=['first','second'])
# print(df1)

d={'one':pd.Series([1,2,3],index=['a','b','c']),
   'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df2=pd.DataFrame(d)
print(df2)

# d={'one':pd.Series([1,2,3],index=['a','b','c']),
#    'two':pd.Series([1,2,3,4],index=['x','y','z','w'])}
# df2=pd.DataFrame(d)
# print(df2)

# d={'one':pd.Series([1,2,3],index=['a','b','c']),
#    'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
# df2=pd.DataFrame(d)
# print(df2['one'])

d={'one':pd.Series([1,2,3],index=['a','b','c']),
   'two':pd.Series([1,2,3,4],index=['a','b','c','d'])}
df2=pd.DataFrame(d)

# df2['three']=pd.Series([10,20,30],index=['a','b','c'])
# print(df2)

# df2['four']=df2['one']+df2['two']
# print(df2)

# df2['five']=df2['one']+False
# df2['five']=df2['one']+True

print(df2)


d={'one':pd.Series([1,2,3],index=['a','b','c']),
   'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
   'three':pd.Series([10,20,30],index=['a','b','c'])}

df=pd.DataFrame(d)
print(df)


del df['one']
print(df)
df.pop('two')
print(df)



