
# 🐼 Pandas Complete Guide 

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas)
![Status](https://img.shields.io/badge/Level-Beginner_to_Advanced-success)

A complete guide to **Pandas**, covering theory, syntax, data manipulation, cleaning, analysis, visualization, and interview questions.

---

# 📚 Table of Contents

1. What is Pandas?
2. Why Use Pandas?
3. Installation
4. Importing Pandas
5. Pandas Data Structures
6. Series
7. DataFrame
8. Reading Data
9. Writing Data
10. Viewing Data
11. Selecting Data
12. Filtering Data
13. Sorting Data
14. Handling Missing Values
15. Removing Duplicates
16. Renaming Columns
17. Changing Data Types
18. Creating Columns
19. Updating Values
20. String Operations
21. Date & Time Functions
22. GroupBy
23. Aggregation Functions
24. Merge
25. Join
26. Concatenate
27. Pivot Table
28. Crosstab
29. Apply Function
30. Map Function
31. Replace Values
32. Value Counts
33. Unique Values
34. Correlation
35. Descriptive Statistics
36. Exporting Data
37. Performance Tips
38. Real-World Applications
39. Interview Questions
40. Cheat Sheet

---

# What is Pandas?

Pandas is an open-source Python library used for **data manipulation, cleaning, transformation, and analysis**.

It provides powerful data structures such as **Series** and **DataFrame** to work efficiently with structured data.

---

# Why Use Pandas?

- Easy to read datasets
- Fast data manipulation
- Powerful filtering
- Data cleaning
- Statistical analysis
- Works with NumPy
- Supports Excel, CSV, JSON, SQL

---

# Installation

```bash
pip install pandas
```

---

# Import Library

```python
import pandas as pd
```

---

# Pandas Data Structures

## 1. Series

A **Series** is a one-dimensional labeled array.

```python
import pandas as pd

s = pd.Series([10,20,30,40])
print(s)
```

Applications

- Single column data
- Time series
- Labels

---

## 2. DataFrame

A DataFrame is a **2-dimensional table** consisting of rows and columns.

```python
data={
    "Name":["Amit","Rahul"],
    "Age":[22,23]
}

df=pd.DataFrame(data)
```

Applications

- Excel-like tables
- CSV files
- SQL tables

---

# Reading Data

## CSV

```python
df=pd.read_csv("students.csv")
```

---

## Excel

```python
df=pd.read_excel("students.xlsx")
```

---

## JSON

```python
df=pd.read_json("students.json")
```

---

## SQL

```python
pd.read_sql(query,connection)
```

---

# Writing Data

```python
df.to_csv("output.csv",index=False)
```

```python
df.to_excel("output.xlsx")
```

```python
df.to_json("output.json")
```

---

# Viewing Data

## First Rows

```python
df.head()
```

---

## Last Rows

```python
df.tail()
```

---

## Shape

```python
df.shape
```

---

## Columns

```python
df.columns
```

---

## Index

```python
df.index
```

---

## Information

```python
df.info()
```

---

## Summary Statistics

```python
df.describe()
```

---

# Selecting Data

## Single Column

```python
df["Age"]
```

---

## Multiple Columns

```python
df[["Name","Age"]]
```

---

## Row Selection

```python
df.loc[0]
```

```python
df.iloc[0]
```

---

# Filtering Data

```python
df[df["Age"]>20]
```

```python
df[df["City"]=="Delhi"]
```

---

# Sorting Data

Ascending

```python
df.sort_values("Age")
```

Descending

```python
df.sort_values("Age",ascending=False)
```

---

# Handling Missing Values

Check Missing Values

```python
df.isnull()
```

Count Missing Values

```python
df.isnull().sum()
```

Remove Missing Values

```python
df.dropna()
```

Fill Missing Values

```python
df.fillna(0)
```

Fill with Mean

```python
df.fillna(df["Age"].mean())
```

Fill with Median

```python
df.fillna(df["Age"].median())
```

Fill with Mode

```python
df.fillna(df["City"].mode()[0])
```

---

# Removing Duplicates

```python
df.drop_duplicates()
```

---

# Renaming Columns

```python
df.rename(columns={"Age":"Student_Age"})
```

---

# Changing Data Types

```python
df["Age"]=df["Age"].astype(int)
```

---

# Creating New Columns

```python
df["Bonus"]=df["Salary"]*0.10
```

---

# Updating Values

```python
df.loc[0,"Age"]=25
```

---

# String Operations

```python
df["Name"].str.upper()
```

```python
df["Name"].str.lower()
```

```python
df["Name"].str.contains("A")
```

```python
df["Name"].str.replace("A","X")
```

---

# Date & Time

```python
df["Date"]=pd.to_datetime(df["Date"])
```

Extract Year

```python
df["Date"].dt.year
```

Month

```python
df["Date"].dt.month
```

Day

```python
df["Date"].dt.day
```

---

# GroupBy

```python
df.groupby("Department")["Salary"].mean()
```

Applications

- Department wise salary
- Category analysis

---

# Aggregation Functions

```python
df.mean()
```

```python
df.max()
```

```python
df.min()
```

```python
df.sum()
```

```python
df.count()
```

```python
df.std()
```

```python
df.var()
```

---

# Merge

```python
pd.merge(df1,df2,on="ID")
```

Types

- Inner
- Left
- Right
- Outer

---

# Join

```python
df1.join(df2)
```

---

# Concatenate

```python
pd.concat([df1,df2])
```

---

# Pivot Table

```python
pd.pivot_table(df,
index="Department",
values="Salary",
aggfunc="mean")
```

---

# Crosstab

```python
pd.crosstab(df["Gender"],df["Department"])
```

---

# Apply Function

```python
df["Salary"]=df["Salary"].apply(lambda x:x+1000)
```

---

# Map Function

```python
df["Gender"]=df["Gender"].map({
"M":"Male",
"F":"Female"
})
```

---

# Replace Values

```python
df.replace("Delhi","New Delhi")
```

---

# Value Counts

```python
df["City"].value_counts()
```

---

# Unique Values

```python
df["City"].unique()
```

```python
df["City"].nunique()
```

---

# Correlation

```python
df.corr(numeric_only=True)
```

---

# Descriptive Statistics

```python
df.describe()
```

Includes

- Mean
- Median
- Std
- Min
- Max
- Quartiles

---

# Export Data

CSV

```python
df.to_csv("file.csv")
```

Excel

```python
df.to_excel("file.xlsx")
```

JSON

```python
df.to_json("file.json")
```

---

# Performance Tips

✔ Use vectorized operations

✔ Avoid unnecessary loops

✔ Use `.loc[]` and `.iloc[]`

✔ Convert repeated strings to `category`

✔ Read only required columns using `usecols`

✔ Use `chunksize` for large files

---

# Real-World Applications

## Data Analysis

- Data Cleaning
- Data Transformation
- Data Exploration

---

## Business

- Sales Dashboard
- Customer Analysis
- Revenue Reports

---

## Finance

- Stock Market Analysis
- Expense Tracking

---

## Healthcare

- Patient Records
- Disease Analysis

---

## Machine Learning

- Data Preprocessing
- Feature Engineering
- Missing Value Handling

---

## Data Science

- EDA
- Feature Selection
- Data Wrangling

---

# Frequently Used Functions

| Function          | Purpose                 |
| ----------------- | ----------------------- |
| head()            | First rows              |
| tail()            | Last rows               |
| info()            | Dataset information     |
| describe()        | Statistics              |
| shape             | Rows & Columns          |
| columns           | Column names            |
| dtypes            | Data types              |
| isnull()          | Missing values          |
| fillna()          | Fill missing values     |
| dropna()          | Remove missing values   |
| duplicated()      | Duplicate check         |
| drop_duplicates() | Remove duplicates       |
| sort_values()     | Sorting                 |
| groupby()         | Group data              |
| merge()           | Merge tables            |
| concat()          | Combine tables          |
| pivot_table()     | Pivot table             |
| value_counts()    | Frequency               |
| unique()          | Unique values           |
| nunique()         | Number of unique values |
| corr()            | Correlation             |
| apply()           | Apply function          |
| map()             | Map values              |
| replace()         | Replace values          |
| astype()          | Change data type        |
| rename()          | Rename columns          |
| to_csv()          | Export CSV              |
| to_excel()        | Export Excel            |

---

# Common Interview Questions

### What is Pandas?

A Python library used for data manipulation and analysis.

---

### Difference between Series and DataFrame?

| Series        | DataFrame        |
| ------------- | ---------------- |
| 1D            | 2D               |
| Single column | Multiple columns |
| Homogeneous   | Heterogeneous    |

---

### Difference between loc[] and iloc[]?

- `loc[]` → Label-based indexing
- `iloc[]` → Position-based indexing

---

### Difference between merge() and concat()?

- `merge()` combines datasets using common keys.
- `concat()` stacks datasets vertically or horizontally.

---

### Difference between apply() and map()?

- `apply()` works on Series or DataFrames.
- `map()` works only on a Series.

---

### How do you handle missing values?

- `dropna()`
- `fillna()`
- Mean
- Median
- Mode
- Forward Fill
- Backward Fill

---

### What is GroupBy?

GroupBy splits data into groups, applies aggregation functions, and combines the results.

---

### What is Pivot Table?

A pivot table summarizes and aggregates data for easier analysis.

---

# Cheat Sheet

| Task              | Function                    |
| ----------------- | --------------------------- |
| Read CSV          | `read_csv()`              |
| Read Excel        | `read_excel()`            |
| View Data         | `head()`                  |
| Information       | `info()`                  |
| Statistics        | `describe()`              |
| Select Columns    | `[]`                      |
| Filter Rows       | `loc[]`, Boolean Indexing |
| Missing Values    | `isnull()`, `fillna()`  |
| Remove Duplicates | `drop_duplicates()`       |
| Sort Data         | `sort_values()`           |
| Group Data        | `groupby()`               |
| Merge Tables      | `merge()`                 |
| Join Tables       | `join()`                  |
| Combine Data      | `concat()`                |
| Pivot Table       | `pivot_table()`           |
| Correlation       | `corr()`                  |
| Export CSV        | `to_csv()`                |
| Export Excel      | `to_excel()`              |

---

# Conclusion

Pandas is one of the most essential Python libraries for **Data Analysis, Data Science, Machine Learning, and Business Intelligence**. Mastering Pandas enables you to efficiently clean, transform, analyze, and prepare datasets for real-world applications.

⭐ If this guide helped you, consider giving the repository a star and continue practicing with real datasets to strengthen your skills.
