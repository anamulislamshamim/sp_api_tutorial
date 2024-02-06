import pandas as pd

my_data_set = {
    "cars": ["BMW", "Volvo", "Ford"],
    "passings": [3, 7, 2]
}

my_var = pd.DataFrame(my_data_set)

print(my_var)
# print the pandas version 
print(pd.__version__)