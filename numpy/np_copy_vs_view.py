import numpy as np 

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)
""" 
[42  2  3  4  5]
[1 2 3 4 5]
"""
# Notice: if you copy arr and make any changes into the 
# main array it will not affect the copy array

# view 
arr = np.array([100, 110, 120, 130, 140, 150])
x = arr.view()
arr[0] = 1000

print(arr)
print(x)

""" 
[1000  110  120  130  140  150]
[1000  110  120  130  140  150]
"""

# notice the view affected the change that made in the 
# original array 

# check if the array owns it's data 
print(arr.base)
print(x.base)