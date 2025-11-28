import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# rs = np.random.RandomState(10)
# d = rs.normal(size=100)
# sns.histplot(d, kde=True, color="m")
# plt.show()

ty = sns.load_dataset('tips')
# print(ty)

# Displot
# sns.displot(ty['total_bill'],kde=True)

# Relplot
# sns.relplot(data=ty['total_bill'])

# Catplot 
# sns.catplot(x='day',y='tip',kind='swarm',data=ty)
# sns.catplot(x='day',y='tip',kind='strip',data=ty)
# sns.catplot(x='sex',y='total_bill',data=ty,kind='swarm')
# sns.catplot(x='sex',y='total_bill',data=ty,kind='violin')
# sns.catplot(x='day',y='tip',data=ty,hue='smoker')
# sns.catplot(y='total_bill',x='sex',kind='violin',hue='smoker',data=ty)
# sns.catplot(y='total_bill',x='sex',kind='violin',hue='day',data=ty)
# sns.catplot(y='total_bill',x='sex',kind='violin',hue='day',split=True,data=ty)



# Boxplot
# sns.boxplot(ty['tip'], color='r')   #univalent-- one attribute or single column
# sns.boxplot(ty['total_bill'])
# sns.catplot(y='total_bill',x='day',kind='box',data=ty)
# sns.catplot(y='total_bill',x='sex',kind='box',hue='day',data=ty)
# sns.catplot(y='total_bill',x='sex',kind='box',hue='smoker',data=ty)

# Barplot
# sns.catplot(x='smoker',y='tip',kind='bar',data=ty)
# sns.catplot(x='smoker',y='tip',hue='sex',kind='bar',data=ty)
# sns.catplot(x='smoker',y='tip',hue='sex',estimator=np.median,kind='bar',data=ty)
# sns.catplot(x='smoker',y='tip',hue='sex',estimator=np.std,kind='bar',data=ty)
# sns.catplot(x='smoker',y='tip',hue='sex',estimator=np.var,kind='bar',data=ty)



plt.show()