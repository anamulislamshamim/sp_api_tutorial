import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# convert 1-D array to 2-D array 
newarr = arr.reshape(4, 3)

print(arr)
print(newarr)

# reshape into 3-D array
newarr = arr.reshape(2, 3, 2)

print(newarr)