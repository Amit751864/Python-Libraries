# Question 1: Dataset Exploration

# Using any real-world dataset (Titanic, Customer Churn, House Prices, etc.):

# Perform a complete exploratory analysis by:

# Load CSV/Excel
# Display head(), tail()
# Check shape, size
# View columns
# Check dtypes
# Use info()
# Use describe()
# Calculate memory usage
# Change data types where necessary
# Rename columns
import pandas as pd
df = pd.read_csv("test.csv")
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.size)
print("Rename Column")
df.rename(columns={"Sex":"Gender"},inplace=True)
print(df)
print(df.dtypes)
df["Age"] = df["Age"].astype("int") # convert to data type
print(df)