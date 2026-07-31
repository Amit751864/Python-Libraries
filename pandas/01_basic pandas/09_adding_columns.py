#adding column
import pandas as pd

data={
    "Name":["Ram","Amit",'Roshan','Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,21,23,32,23,43,43],
     "Salary":[30000,34422,32335,63232,43234,33443,3333,4444,33236,],
     "Performance Score":[85,76,87,67,87,87,65,99,87]
}
df = pd.DataFrame(data)
print(df)

#adding new column
df["Bonus"] = df["Salary"]*0.1
print(df)

#using insert() specific position
#df.insert(loc,"column name",some data)
df.insert(0,"Employee ID",[10,20,30,40,50,60,70,80,90])
print(df)
df.to_csv("output1.csv",index=False)
