# head(),tail()
#head(n) #  first n row print kargega
#tail(n) # last n row print karega

import pandas as pd
df = pd.read_json("sample_Data.json")
print("Display 10 rows of first")
print(df.head(10))# by chance tum value pass nhii kiya tu starting ke five display
print("display 10 row of last")
print(df.tail(10))#by chance tum value pass nhii kiya tu ending ke five display

'''
info() is method to find given points
numbers of rows and cloumns
column name
int64,float64 object
non null counts
memory usage of the data frame
'''