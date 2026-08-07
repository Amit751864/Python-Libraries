# Question 6: GroupBy, Pivot & Combining Data

# Analyze business data from multiple tables.

# Cover:
# groupby() → Make groups.
# agg() → Calculate many statistics together.
# transform() → Give every row its group's result.
# filter() → Remove or keep whole groups.
# pivot_table() → Summarize data like an Excel Pivot Table.
# crosstab() → Count combinations of categories.
# merge() → SQL-style join using common columns.
# join() → Merge mainly using indexes.
# concat() → Stack DataFrames (rows or columns).
import pandas as pd
import numpy as np
df = pd.read_csv("ques4.csv")
print(df)
print(df.groupby("Department")[["Salary","Performance_Score"]].mean())
print(df.groupby("Department")[["Salary","Performance_Score"]].agg(["min","mean","max"]))
df["Dept_Avg_Sal"] = (df.groupby("Department")["Salary"].transform("mean"))
print(df)
print("Filter")
print(df.groupby("Department").filter(lambda x: x["Salary"].mean()>60000)) 
print(pd.pivot_table(df,
                     values='Salary',
                     index = 'Department',
                     aggfunc='mean'))
print("Crosstab")
print(pd.crosstab(
    df["Department"],
    df["Age"]
))

df.to_csv("ques6.csv",index=False)
print(df)
# merge
# join
# concate
