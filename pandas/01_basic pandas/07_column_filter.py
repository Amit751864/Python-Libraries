'''
1- select the specific column
2- filter rows
3- combine multiple coditions

4 - select the column in square brackets the access
5-  rows ko fliter karna haa thuu boolean condition


6- selecting columns 
*kya return single series
*dataframe multiple columns of data

 column = df["column name"]
 how to access multiple column 
 subset = df["column1",column2,"...."]


7- FILTERING ROWS
specific condition
boolean indexing use kar kage

# filter base  on a single condition ya syntax haa
filtered_rows = df[df["column name"]>50000]

#combine a multiple condition 
filtered_row =df[(df[salary]>5555) & (df[column2]>32332)]
'''

#describe() DataFrame ya Series ka summary statistics deta hai.
#step 1. create  a samplle data frame
import pandas as pd
data={
    "Name":["Ram","Amit",'Roshan','Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,21,23,32,23,43,43],
     "Salary":[30000,34422,32335,63232,43234,33443,3333,4444,33236,],
     "Performance Score":[85,76,87,67,87,87,65,99,87]
}
df = pd.DataFrame(data)
print("Sample DataFrame")
print(df)
print("Name (single column returns series)")
name = df["Name"]
print(name)
#selecting a multiple column
subset = df[["Name","Salary"]]
print("\n subset with Name and Salary")
print(subset)
