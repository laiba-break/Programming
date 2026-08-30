import numpy as np

A = np.arange(100)

b = A[3:10]
#print(b)

#b[0]=-1200

#print(b)  #now you have replaced the element

#print(A) #now number also changed in A

#b = A[3:10].copy() #now b is a different copy from A to avoid this issue

b[0] = -1200
print(b)

print(A[::5]) #print every 5th element
print(A[::-5]) #prints every 5th in revser 
print(A[::-1])

#so now i want to find the numbe -1200 that changed

B = (A == -1200)*np.arange(A.size)

