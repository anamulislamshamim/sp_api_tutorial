import numpy as np 

# the best way to convert data type of an arr is to used astype() method 

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(arr)
print(arr.dtype)
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)