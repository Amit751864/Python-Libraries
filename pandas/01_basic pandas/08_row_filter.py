import pandas as pd

data={
    "Name":["Ram","Amit",'Roshan','Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,21,23,32,23,43,43],
     "Salary":[30000,34422,32335,63232,43234,33443,3333,4444,33236,],
     "Performance Score":[85,76,87,67,87,87,65,99,87]
}
df = pd.DataFrame(data)
print(df)

#single condition
high_salary = df[(df["Salary"]<50000)]
print(high_salary)

#multiple condition
#using and ya isme dono shii hona chayiye
subset = df[(df["Salary"]<50000) & (df["Age"]>25)]
print(subset)

#using or isme kio bhi aak shii hojaye
filtered_or = df[(df["Salary"]<50000) | (df["Age"]>25)]
print(filtered_or)
