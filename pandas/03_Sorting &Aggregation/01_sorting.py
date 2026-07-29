#sorting data
#sorting data 1 column sort_values()
#synatx  df.sort_values(by="column name",True/false,inplace=True)
#true = ascending, false = desceding order
import pandas as pd
data = {
    "Name":["Arun","Varun","Amit"],
    "Age":[20,19,25],
    "Salary":[20000,15000,30000]

}
df = pd.DataFrame(data)
print(df)
#single column sort
df.sort_values(by="Age",ascending=True,inplace=True)
print(df)