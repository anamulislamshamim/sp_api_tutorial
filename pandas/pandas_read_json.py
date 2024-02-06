# Big data sets are often stored, or extracted as JSON

# JSON is a plain text, but has the format of an object, and is 
# well known in the world of programming, including Pandas 

import pandas as pd 

# df = pd.read_csv("data.csv")

df = pd.read_json('data.json')

print(df.corr())