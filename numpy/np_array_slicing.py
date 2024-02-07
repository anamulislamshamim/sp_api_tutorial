# slicing in python means taking elements from one given
# index to another given index 

import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7])


# print [2, 3, 4, 5] from above arr 
print(arr[1:5]) # it will print index 1 till 4
# notice it is include index 5 

# I did not provide step. Default step 1
print(arr[1:5:2])

# Negative slicing 
print(arr[-3:-1])

print(arr[::2])
print(arr[::-2])


# slicing 2-D array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr[1, 1:4])

# from the both elements return index 2
print(arr[0:2, 2])

print(arr[0:2, 1:4])

print(arr.dtype)