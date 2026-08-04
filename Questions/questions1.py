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
data={
    "Name":["Ram","Amit",None,'Ankit','Auysh',"Raj","rishi","ajay","vijay"],
     "Age":[22,21,32,None,23,32,23,43,43],
     "Salary":[30000,34422,None,63232,43234,33443,3333,4444,33236],
     "Performance Score":[85,76,None,67,87,87,65,99,87]
}
df = pd.DataFrame(data)
print(df)
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.size)
print("Rename Column")
df.rename(columns={"Name":"First_name"},inplace=True)
print(df)
print(df.dtypes)
df["Age"] = df["Age"].astype("int") # convert to data type
print(df)