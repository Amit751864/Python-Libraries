# Question 4: Data Transformation & Feature Engineering
# Transform raw data into meaningful features.
# Cover:
# apply()	Apply a custom function to each value or row
# map()	Replace or transform values in a single column
# replace()	Replace selected values while leaving all others unchanged
# String Operations (.str)	Clean and manipulate text data
# np.where()	Create a new column based on a condition
# pd.cut() (Binning)	Convert continuous numerical data into categories
# New Feature Creation	Build new columns from existing data to improve analysis or machine learning
import pandas as pd
import numpy as np
df =pd.read_csv("ques3.csv")
print(df)
print("Apply ")
df["Salary"]  = df["Salary"].apply(lambda x:x*1.10)
print(df)
print("MAP")
#map function are used single column values rename ya transform
#  and ya column value na mile par Nan print hota uske jagha par
# df["Department"] = df["Department"].map({
#     "IT":"Information Technology",
#     "HR":"Human Resource",
#     "Sales":"Sales Team",
#     "Finance":"Finance Team"
# })
# print(df)
#replace function are used column values old values replace with new value but 
# but jiska new value hota uska he replace hota nhii thhu old value he rha jata (ma
# me aisa nhii hota new value nhiii milega thhu uska old value replace karke Nan Print ka dega uske jagha)
df["Department"] = df["Department"].replace({
    "IT":"Information Technology",
    "HR":"Human Resource",
    "Sales":"Sales Team",
    "Finance":"Finance Team"
})
print(df)
print("STRINgG OPERATION")
print(df["Name"].str.upper())
print(df["Name"].str.lower())
print(df["Department"].str.len())
print(df["Name"].str.startswith("R"))# means kon kon R se start hua ha
print(df["Name"].str.contains("a")) # kon kon name a contain haa
print(df["Name"].str.strip())
print(df["Name"].str.replace("a","@"))
# print(df["Email"].str.split("@"))
print(df["Name"].str.capitalize())
# condition just like sql
df["Bonus"] =np.where(
    df["Salary"]>40000,
    "YES",
    "NO"
)
print(df)
# Binning 
df["Annual_Salary"] = df["Salary"]*12
print(df)

# binning used 

bins =[0,25,35,100]
labels=["Young","Adult","Senior"]
df["Age_Group"] =pd.cut(
    df["Age"] ,
    bins=bins,
    labels=labels
)
print(df)
df[["Salary","Annual_Salary"]]= (df[["Salary","Annual_Salary"]].astype("int"))
print(df)
df["Name"] =df["Name"].str.capitalize()
print(df)
df.to_csv("ques4.csv",index=False)
print(df)
