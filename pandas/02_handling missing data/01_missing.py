import pandas as pd
data={
    "Name":["Ram","Amit",None,'Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,None,23,32,23,43,43],
     "Salary":[30000,34422,None,63232,43234,33443,3333,4444,33236],
     "Performance Score":[85,76,None,67,87,87,65,99,87]
}
df = pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.isnull().sum())