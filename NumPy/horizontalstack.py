import numpy as np

A = np.round(10*np.random.rand(2,3))
print(A)
print(A+3)

B= A*(np.arange(2).reshape(2,1)) #there will a colun that will be added
print(B)

c= np.round(10*np.random.rand(2,2))

print(c)

D = np.hstack