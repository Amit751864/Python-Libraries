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
import numpy as np
df = pd.read_csv("test.csv")
print(df)
print(df.duplicated())
print(df.drop_duplicates())
print(df.isnull().sum())
print