import numpy as np

b = np.array([[[1,2,3],[4,5,6],[1,2,3],[4,5,6]]])
print(b.ndim)
print (b.shape) #prints the number of arrays of arrays which is 2,
#then tells u the number of arrays in one array which is 2 and then tellss you the n
#the number of elements in each #0-1, 0-3, 3 so 1, 4,3
print(b.shape[0],b.shape[1],b.shape[2]) #shape[0] tells u total no fo arrays in first array
# of arrays which is 2 and 1 will done
A = np.array([2]) #you can define two array of arrays
print(A.ndim) 
#size
print(b.size) #no of elements

