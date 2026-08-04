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
df =pd.read_csv("ques3.csv")
print(df)
print("Apply ")
df["Salary"]  = df["Salary"].apply(lambda x:x*1.10)
print(df)
print("MAP")
