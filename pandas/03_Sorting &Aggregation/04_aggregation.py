'''Data Analyst Interview Topics
Data ko summarize karne ke liye aggregate functions use karte hain.
df["column name"].sum()
sum()
mean() average
max()
min()
count()
median()
std() (Standard Deviation)
var() (Variance)
agg()
groupby()
Ye Pandas ke sabse important aggregation functions hain.'''
import pandas as pd
data = {
    "Name":["Arun","Varun","Amit"],
    "Age":[20,19,25],
    "Salary":[20000,15000,30000]

}
df = pd.DataFrame(data)
print(df)
sum_of_salary =df["Salary"].sum()
print(sum_of_salary)

