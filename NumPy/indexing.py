#more indexing 
import numpy as np

A = np.arange(100)

B=A[[3,5,6]]
print(B)
print(A)

B=A[A<40] #accesses all ele,ents less then 40
print(B)

B= A[(A<40) & (A>30)]
print(B)

#& -used when left and side or arrays and normal is used then normal objects are used 
# and is used for single objects
# #or /
# not ~

 