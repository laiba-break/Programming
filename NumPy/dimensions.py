import numpy as np

#a = np.array([[1,2,3],[4,5,6]])
#print(a.ndim)  #tells u the number of axes or dimensions in array
#print(a[0,2]) #basically this accesses the first array which is 0, and second element in whcih is 3
#print(a[1,2]) #prints 6 

#b = np.array([[1,2,3],[4,5,6],[1,2,3],[4,5,6]])
#print(b.ndim)

#print(b.shape[0],b.shape[1],b.shape[2])
#print([b[1,0,2]])

#B= np.array([[1,2,3],[2,4,5,9]])  #doesnt work since both arrays need to have same no of elements
#print(B.ndim)
B= np.array([[1,2,3],[2,4,5]])  #doesnt work since both arrays need to have same no of elements
print(B.ndim) #this works now since we got same leements
print(B[1,2])

C= np.array([[[1,2,3],[4,5,6],[0,0,-1]],[[-1,-2,-3],[-4,-5,-6],[0,0,1]]])
print(C.ndim) #is three 3d is has array of arrays and has 2d arrays 
print(C[1,0,2]) #1 means acess second arrays of arrays within that acess 0 which is first array or list
#and within that array access 2nd elemenr which is -3
print(type(C)) 