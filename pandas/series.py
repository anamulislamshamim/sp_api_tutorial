# what is series ?
# Pandas series is like a column in a table. It is one dimensional
# array holding any type of data. 

import pandas as pd 


a = [1, 7, 2] # a is a series 

myVar = pd.Series(a)

print(myVar)
# Notice: pd.Series convert the 'a' array into a column 
"""
 index  value
    0    1
    1    7
    2    2
    dtype: int64
"""

# Labels: If nothing else is specified, the values are labeled 
# with their index number.

# create my own labels 
import pandas as pd 

a = [1, 7, 2]

myVar = pd.Series(a, index=["x", "y", "z"])

print(myVar)

"""
 index value
    x    1
    y    7
    z    2
    dtype: int64
"""
# Notice: not Series labeled with x, y and z

# you print value by refering their label
print(myVar["x"])

# you can also use a key/value object like map or dictionary,
# when creating a Series 
calories = {"day1": 420, "day2": 380, "day3": 390}

myVar = pd.Series(calories)

print(myVar)
print(myVar["day1"])
# Notice: The key of the dictionary become label of the Series

# To select only some of the items in the dictionary, use the 
# index argument and specify only the items that you want to 
# include in the series 

calories = {"day1": 420, "day2": 380, "day3": 390}
myVar = pd.Series(calories, index=["day1", "day2", "day3", "day4"])

print(myVar)
