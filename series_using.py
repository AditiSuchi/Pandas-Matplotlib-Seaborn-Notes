import numpy as np
import pandas as pd

a =[1,3,4,]
d = pd.Series(a)
print(d)

dic ={"A":1,"B":2}
c =pd.Series(dic)
print(c)

e =pd.Series(np.linspace(2,9,4))
print(e)

ser =np.arange(10,15)
serobj = pd.Series(data=ser*5,index=ser)
print(serobj)




