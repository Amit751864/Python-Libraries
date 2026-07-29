#multiple column sort
#syntax df.sort_values(by=["Age","salary"]) 
import pandas as pd
data = {
    "Name":["Arun","Varun","Amit"],
    "Age":[20,19,25],
    "Salary":[20000,15000,30000]

}
df = pd.DataFrame(data)
print(df)
df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True) 
print(df)
