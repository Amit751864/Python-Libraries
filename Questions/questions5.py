# Question 5: Statistical Analysis & NumPy Operations

# Perform statistical analysis using NumPy and Pandas.

# Cover:
# mean
# median
# std
# variance
# min/max
# argmin/argmax/idxmax/idxmin
# unique()
# value_counts()
# quantiles
# percentiles
# element-wise operations
# broadcasting
# normalization
# standardization
import pandas as pd
import numpy as np 
df = pd.read_csv("ques4.csv")
print(df)

print("MEAN")
print(f"Age:{df["Age"].mean():.2f}")
print(f"Salary:{df["Salary"].mean():.2f}")
print(f"Performance_Score:{df["Performance_Score"].mean():.2f}")
# print(df.mean(numeric_only=True))

print("MEDIAN")
print(f"Age:{df["Age"].median():.2f}")
print(f"Salary:{df["Salary"].median():.2f}")
print(f"Performance_Score:{df["Performance_Score"].median():.2f}")

print("STANDARD DEVIATION")
print(f"Age:{df["Age"].std():.2f}")
print(f"Salary:{df["Salary"].std():.2f}")
print(f"Performance_Score:{df["Performance_Score"].std():.2f}")

print("VARIANCE")
print(f"Age:{df["Age"].var():.2f}")
print(f"Salary:{df["Salary"].var():.2f}")
print(f"Performance_Score:{df["Performance_Score"].var():.2f}")

print("maximun")
print(f"Age:{df["Age"].max()}")
print(f"Salary:{df["Salary"].max()}")
print(f"Performance_Score:{df["Performance_Score"].max()}")

print("minmun")
print(f"Age:{df["Age"].min()}")
print(f"Salary:{df["Salary"].min()}")
print(f"Performance_Score:{df["Performance_Score"].min()}")

print("idxmax")
print(f"Age:{df["Age"].idxmax()}")
print(f"Salary:{df['Salary'].idxmax()}")
print(f"Performance_Score: {df['Performance_Score'].idxmax()}") 

print("idxmin")
print(f"Age:{df["Age"].idxmin()}")
print(f"Salary:{df['Salary'].idxmin()}")
print(f"Performance_Score: {df['Performance_Score'].idxmin()}") 

print("UNIQUE")
print(f"Unique Value:{df['Age'].unique()}")
print(f"Value Count:{df['Department'].value_counts()}")

print(f"quantiles:{df['Age'].quantile([0.25,0.50,0.75])}")

print(np.percentile(df['Salary'],10))

print("Element Wise Operation")

df["Salary"] = df["Salary"] +5000
print(df)

df["Performance_Score"] = df["Performance_Score"] + 5
print(df)

