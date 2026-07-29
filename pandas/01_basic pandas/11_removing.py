import pandas as pd
data={
    "Name":["Ram","Amit",'Roshan','Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,21,23,32,23,43,43],
     "Salary":[30000,34422,32335,63232,43234,33443,3333,4444,33236,],
     "Performance Score":[85,76,87,67,87,87,65,99,87]
}
df = pd.DataFrame(data)
print(df)
#df.drop(columns == ["column name"],inplace = True)
#single column remove
df.drop(columns= ["Performance Score"],inplace =True)
print(df)
#multiple column remove
df.drop(columns=["Performance Score", "Age"],errors="ignore",inplace=True)
print(df)