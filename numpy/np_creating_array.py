import numpy as np 

# creating numpy ndarray object 
# what is ndarray stands for? ans: N Dimentional Array Object
# N can be 0...n

# arr = np.array([[[1, 2, 3, 4, 5], [1, 2, 3, 4, 5]], [[1, 2, 3, 4, 5],[1, 2, 3, 4, 5]]])
# 0-D array
# arr = np.array(117)
# 1-D array 
# arr = np.array((1, 2, 3, 4, 5))

# 2-D array: An array that has 1-D array as an element!
# arr = np.array([[1,2], [1,2]])

# Higher dimensions array
# you can create any number of dimensions when the array is created. you can define ndim
# argument 
arr = np.array([1, 2, 3, 4, 5], ndmin=5)

print(arr)

print(type(arr))

print(arr.ndim)