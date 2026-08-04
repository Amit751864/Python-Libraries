import pandas as pd
import matplotlib.pyplot as plt

df =pd.read_csv("netflix_titles.csv",encoding="latin1")
print(df)

print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())