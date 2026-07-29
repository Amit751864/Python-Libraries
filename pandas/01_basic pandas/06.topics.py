'''
1- how big is your dataset
2- what are the names of column ,access the name

SHAPE AND COLUMN

'''
import pandas as pd

data={
    "Name":["Ram","Amit",'Roshan','Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,21,23,32,23,43,43],
     "Salary":[30000,34422,32335,63232,43234,33443,3333,4444,33236,],
     "Performance Score":[85,76,87,67,87,87,65,99,87]
}

df = pd.DataFrame(data)
print(df)
print(f"Shape:{df.shape}")
print(f"Column Name: {df.columns}")



