import pandas as pd
# read  data from CSV file into a dataframe
#df = pd.read_csv("simpled_data.csv",encoding="latin1")
#df = pd.read_excel("SampleSuperstore.xlsx",encoding="latin1")
df = pd.read_json("sample_Data.json",encoding="utf-8")
print(df)

#cloud gcsfs


