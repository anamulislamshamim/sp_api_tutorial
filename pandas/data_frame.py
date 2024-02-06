# what is data sets in pandas ?
# Data sets in Pandas are usually multi-dimensional tables, called 
# DataFrames 

"""
DataFrame is actually 2 dimensional array or like 
table with row and column.

   calories  duration
0       420        50
1       380        40
2       390        45
"""

import pandas as pd 


data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45],
    "food": ["Rice", "Meat", "Egg"]
}

df = pd.DataFrame(data)

print(df)


# for printing any row pandas use loc attrubute 
"""
calories     420
duration      50
food        Rice
Name: 0, dtype: object
"""
print(df.loc[0])
print(df.loc[0]["food"]) # will print Rice

# print row 0 to 1 
print(df.loc[[0, 1]])
print(df.loc[[0, 1]]["food"])