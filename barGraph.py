import numpy as np
import matplotlib.pyplot as plt


# Vertical bars
# x = np.array(["A","B","C","D"])
# y= np.array([3,8,1,10])
# plt.bar(x,y,width=0.5,color='pink')
# plt.show()


# Horizontal Bar
# x = np.array(["A","B","C","D"])
# y= np.array([3,8,1,10])
# plt.barh(x,y,height=0.5,color='pink')
# plt.show()

y= np.array([3,8,1,10])
mylabels =['Apple','Banana','Cherries','Dates']
plt.subplot(1,2,1)
plt.pie(y,labels=mylabels)



y= np.array([3,8,1,10])
mylabels =['Apple','Banana','Cherries','Dates']
plt.subplot(1,2,2)
plt.pie(y,labels=mylabels)
plt.legend()
plt.show()