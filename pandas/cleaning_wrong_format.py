""" 
In our Data Frame, we have two cells with the wrong format. Check out row 22 and 26, the 'Date' column should be a string that represents a date:
"""
# for cleaning wrong format we can do two things
# 1. Remove that cells 
# 2. convert the column into the same format 

import pandas as pd 
import matplotlib.pyplot as plt 


df = pd.read_csv("cleaned_data.csv")

# fill the Null of calories with average value 
df["Calories"].fillna(format(df["Calories"].mean(), '.5g'), inplace=True)

# cleaning the format 
df.dropna(subset=['Date'], inplace=True)

print(df.to_string())
print(df.duplicated())
# drop duplicate values 
df.drop_duplicates(inplace=True)
print(df.to_string())

df.plot()
plt.show()