import numpy as np 

# 1-D array indexing as similar as python list 
# access 1-D array
arr = np.array([0, 1, 2, 3, 4, 5])

print(arr[0])

# access 2-D array 
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

# print the 2nd element on 1st row: 
print(arr[0, 1])

# here 0 is first element of 2-D array in this case [1, 2, 3, 4, 5]
# here 1 is the second element of 1-D array 2

# access 3-D array 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# print the third element of the second array of the first array
print(arr[0, 1, 2])
