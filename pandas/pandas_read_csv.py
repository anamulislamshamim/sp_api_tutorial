# What is csv file? Ans: CSV stands for Comma Separated Value
# CSV file is simple way to store big data sets 

import pandas as pd

df = pd.read_csv('data.csv')

print(df)
# you can check your system's maximum rows with the pd.options.display.max_rows
print(pd.options.display.max_rows)
print(pd.options.display.max_columns)