#UPDATING VALUES
import pandas as pd
data={
    "Name":["Ram","Amit",'Roshan','Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,21,23,32,23,43,43],
     "Salary":[30000,34422,32335,63232,43234,33443,3333,4444,33236,],
     "Performance Score":[85,76,87,67,87,87,65,99,87]
}
df = pd.DataFrame(data)
print(df)
#.loc[]
#df.loc[row_index,"column name"] = new_value
#UPDATING A SINGLE VALUE
df.loc[0,"Salary"] = 25000
print(df)
#UPDATING MULTIPLE VALUE
df["Salary"] =df["Salary"]*1.05
print(df)