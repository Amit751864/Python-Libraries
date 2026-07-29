import pandas as pd
from openpyxl.workbook import Workbook

data ={

    "Name":['RAm','shyam','amit'],
    "Age":[10,20,30],
    "city":['nagpur','manipur','delhi']

}
df = pd.DataFrame(data)
print(df)

df.to_csv("output.csv",index=False)
df.to_json("output.json",indent=4,index=False)
df.to_excel("output.xlsx")
print(df.info())

