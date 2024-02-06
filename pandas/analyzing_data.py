import pandas as pd 
# viewing data 
# one of the most common method for getting overview of the 
# DataFrame is the head() and tail() method 

# head() will print top 5 rows 

df = pd.read_csv('data.csv')

print(df.head(10))

print(df.tail(3))


# Info about the data set 
# The DataFrame object has a method called info(), that gives you more 
# information about the data set 
print(df.info())