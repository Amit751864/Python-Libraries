import pandas as pd
data = {
    "Name":["Arun","Varun","Amit","Karun","Marun"],
    "Age":[20,34,20,34,35],
    "Salary":[20000,15000,30000,35000,40000]


}
df = pd.DataFrame(data)
print(df)
#single column implement  group by
print("single")
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)
print("multi")
#mutliple column implement group by
grouped1 =df.groupby(["Age","Name"])["Salary"].sum()
print(grouped1) 