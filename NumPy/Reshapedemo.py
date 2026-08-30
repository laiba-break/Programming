import numpy as np

#A = np.random.rand(1000)
#print(A)

import matplotlib.pyplot as plt

#plt.hist(A)
#plt.show()  #shows u the graph

#B = np.random.randn(10000)
#plt.hist(B,bins=200)
#plt.show() #gives bell shaped curve
#np.random helps this way

#print(B.ndim)
D = np.arange(100)
print(D)

D = np.arange(100).reshape(4,25)
print(D) #changes from 1 row and 100 columsn to 4 rows 25 columns
#reshape basically changes the rows and columns
#only needs to match same elements
print(D.shape)  

D = np.arange(100).reshape(4,5,5)
print(D.shape)
#print(np.zeros([3,4])) #prints 3 rows 4 columns of zero
#print(np.ones([2,3])) #prints ones 
