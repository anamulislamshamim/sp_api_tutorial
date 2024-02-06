""" 
wrong data does not mean empty or wrong format. If something is
unexpected then we can take it as a consideration and mark it
as wrong data. In this file row 7 in duration column has a value
450 is a wrong data! Why? If you look other data it is more than
our expectation 
"""
# for cleaning wrong format we can do two things
# 1. Remove that cells 
# 2. convert the column into the same format 

import pandas as pd 


df = pd.read_csv("cleaned_data.csv")

# fill the Null of calories with average value 
df["Calories"].fillna(format(df["Calories"].mean(), '.5g'), inplace=True)

# cleaning the format 
df.dropna(subset=['Date'], inplace=True)

# if data more than 2x than average value then replace it with
# average value 
avg = int(df["Duration"].mean())

# if duration is 2 * average_duration time then replace it with
# average duration value so that it will get you more specific vlaue

for x in df.index:
    if df.loc[x, "Duration"] > 2 * avg:
        df.loc[x, "Duration"] = avg
        
        
print(df.to_string())