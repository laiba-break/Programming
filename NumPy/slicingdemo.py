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

#print(A[::5]) #print every 5th element
#print(A[::-5]) #prints every 5th in revser 
#print(A[::-1])
print(A)
#so now i want to find the numbe -1200 that changed
#to find elements in numpy aarray
idx = np.argwhere(A==-1200)[0][0] #finds the index position where this element is 
print(idx)
A[idx] = 2 #this way we replace -1200 with 2
print(A)

A= np.round(10*np.random.rand(5,4)) #random no generated
#scales up value to values to then round uses to round it to integer
print(A)
print(A[1,2])
print(A[:,1]) 
print(A[1:3,2:4]) #1st row 3rd column adn 2nd row 4th colm
print(A.T) #t is tranpose

import numpy.linalg as la
#this has many mathematical functions this library related to matrixes and 2d 
la.inv(np.random.rand(3,3))
A.sort(axis=0) # every column is sorted indivually 

