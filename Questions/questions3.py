# Question 3: Data Selection & Cleaning
# Clean a dataset for machine learning.
# Cover:
# loc, iloc
# filtering
# multiple conditions
# query()
# sort_values()
# duplicated()
# drop_duplicates()
# isnull()
# fillna(mean/median/mode)
# forward fill
# backward fill
# interpolation
# group-wise median
# dropna()
import pandas as pd
data={
    "Name":["Ram","Amit",'Rajesh','Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,None,23,32,None,43,43],
     "Salary":[30000,34422,None,63232,43234,33443,333388,None,33236],
     "Performance_Score":[85,76,None,67,87,87,65,None,87]
}
df = pd.DataFrame(data)
print(df)
print(df.loc[0:4])
print(df.iloc[0:4])
#filtering
print(df[df["Age"]>25 ])
# multiple condition
print("Multiple Condition")
print(df[(df["Age"]>25) | (df["Salary"] >40000)])
print("Query")
print(df.query("Age>30"))
print("Sort Values")
print(df.sort_values("Age"))
print("Duplicate Values")
print(df.duplicated())
print("REMOVE DUPLICATE VALUES")
print(df.drop_duplicates())
print("How Many Missing Values in Your Data")
print(df.isnull())
print(df.isnull().sum())

# ALL function used in below is performed the filled the missing values

# print("Fill THE MISSING VALUES")

# df[["Age", "Salary", "Performance_Score"]] = (
#     df[["Age", "Salary", "Performance_Score"]]
#     .fillna(df[["Age", "Salary", "Performance_Score"]].mean())
# )
# print(df)

# print("FORWARD FILL")
# df[["Age", "Salary", "Performance_Score"]] =  (df[["Age", "Salary", "Performance_Score"]].ffill())
# print(df)

# print("Backward Fill")
# df[["Age", "Salary", "Performance_Score"]] = (df[["Age", "Salary", "Performance_Score"]].bfill())
# print(df)

print("Interpolation")
df[["Age", "Salary", "Performance_Score"]] =( df[["Age", "Salary", "Performance_Score"]].interpolate())
print(df)

df.to_csv("ques3.csv",index=False)
print(df)