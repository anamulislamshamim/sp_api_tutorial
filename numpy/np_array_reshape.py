import numpy as np 

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

# convert 1-D array to 2-D array 
newarr = arr.reshape(4, 3)

print(arr)
print(newarr)

# reshape into 3-D array
newarr = arr.reshape(2, 3, 2)

print(newarr)

print(newarr.base)

print(arr.reshape(3, 2, -1))


# flattening the arrays 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[9, 10, 11], [12, 13, 14]]])

newarr = arr.reshape(-1)

print(arr)
print(newarr)

for i in newarr:
    print(i, end=" ")

print("\n")

for x in arr:
    print(x)
    
    
for x in arr:
    for y in x:
        for z in y:
            print(z, end= " ")
            
print("\n")
          
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x, end=" ")

print("\n")
# iterating with different Step size 
for x in np.nditer(arr[:, ::2]):
    print(x, end=" ")

print("\n")

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x in np.ndenumerate(arr):
    print(idx, " : ", x, end=" ")