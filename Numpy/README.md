
# 🔢 NumPy Complete Guide (README.md)

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![NumPy](https://img.shields.io/badge/Library-NumPy-013243?logo=numpy)
![Status](https://img.shields.io/badge/Level-Beginner_to_Advanced-success)

A complete guide to **NumPy (Numerical Python)** covering theory, arrays, indexing, slicing, mathematical operations, statistics, linear algebra, random module, broadcasting, and interview questions.

---

# 📚 Table of Contents

1. What is NumPy?
2. Why Use NumPy?
3. Installation
4. Import NumPy
5. NumPy Arrays
6. Creating Arrays
7. Array Attributes
8. Data Types
9. Indexing
10. Slicing
11. Reshaping Arrays
12. Joining Arrays
13. Splitting Arrays
14. Copy vs View
15. Iterating Arrays
16. Array Operations
17. Mathematical Functions
18. Statistical Functions
19. Universal Functions (ufuncs)
20. Broadcasting
21. Sorting Arrays
22. Searching Arrays
23. Filtering Arrays
24. Linear Algebra
25. Random Module
26. Input & Output
27. Performance Comparison
28. Real-World Applications
29. Frequently Used Functions
30. Interview Questions
31. Cheat Sheet

---

# What is NumPy?

NumPy (Numerical Python) is an open-source Python library used for fast numerical computing. It provides the powerful **ndarray (N-dimensional array)** object and a collection of mathematical functions.

NumPy is the foundation of many Python libraries like:

- Pandas
- Matplotlib
- Scikit-Learn
- TensorFlow
- SciPy

---

# Why Use NumPy?

- Faster than Python Lists
- Less Memory Usage
- Mathematical Operations
- Matrix Computation
- Scientific Computing
- Machine Learning
- Data Analysis

---

# Installation

```bash
pip install numpy
```

---

# Import Library

```python
import numpy as np
```

---

# NumPy Array

A NumPy array is a homogeneous collection of elements stored in contiguous memory.

```python
arr = np.array([10,20,30,40])
print(arr)
```

---

# Creating Arrays

## 1D Array

```python
np.array([1,2,3,4])
```

---

## 2D Array

```python
np.array([[1,2],[3,4]])
```

---

## 3D Array

```python
np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
```

---

## Zeros

```python
np.zeros((3,3))
```

---

## Ones

```python
np.ones((2,4))
```

---

## Identity Matrix

```python
np.eye(4)
```

---

## Empty Array

```python
np.empty((2,2))
```

---

## Full Array

```python
np.full((3,3),5)
```

---

## Range

```python
np.arange(1,10,2)
```

---

## Evenly Spaced Numbers

```python
np.linspace(0,10,5)
```

---

# Array Attributes

```python
arr.shape
```

Number of rows and columns.

```python
arr.ndim
```

Dimensions.

```python
arr.size
```

Total elements.

```python
arr.dtype
```

Data type.

```python
arr.itemsize
```

Size of one element.

---

# Data Types

```python
arr.astype(float)
```

Common Types

- int
- float
- bool
- complex
- str

---

# Indexing

```python
arr[0]
```

```python
arr[1]
```

2D

```python
arr[1,0]
```

---

# Slicing

```python
arr[1:5]
```

```python
arr[:4]
```

```python
arr[::-1]
```

2D

```python
arr[0:2,1:3]
```

---

# Reshaping Arrays

```python
arr.reshape(2,3)
```

Flatten

```python
arr.flatten()
```

Ravel

```python
arr.ravel()
```

Transpose

```python
arr.T
```

---

# Joining Arrays

Vertical

```python
np.vstack((a,b))
```

Horizontal

```python
np.hstack((a,b))
```

Concatenate

```python
np.concatenate((a,b))
```

---

# Splitting Arrays

```python
np.split(arr,2)
```

```python
np.hsplit(arr,2)
```

```python
np.vsplit(arr,2)
```

---

# Copy vs View

Copy

```python
copy = arr.copy()
```

View

```python
view = arr.view()
```

---

# Iterating Arrays

```python
for x in arr:
    print(x)
```

Multi-dimensional

```python
for x in np.nditer(arr):
    print(x)
```

---

# Array Operations

Addition

```python
a+b
```

Subtraction

```python
a-b
```

Multiplication

```python
a*b
```

Division

```python
a/b
```

Power

```python
a**2
```

---

# Mathematical Functions

Square Root

```python
np.sqrt(arr)
```

Square

```python
np.square(arr)
```

Absolute

```python
np.abs(arr)
```

Exponential

```python
np.exp(arr)
```

Log

```python
np.log(arr)
```

Trigonometry

```python
np.sin(arr)
np.cos(arr)
np.tan(arr)
```

---

# Statistical Functions

Mean

```python
np.mean(arr)
```

Median

```python
np.median(arr)
```

Standard Deviation

```python
np.std(arr)
```

Variance

```python
np.var(arr)
```

Minimum

```python
np.min(arr)
```

Maximum

```python
np.max(arr)
```

Sum

```python
np.sum(arr)
```

Product

```python
np.prod(arr)
```

---

# Universal Functions (ufuncs)

```python
np.add(a,b)
```

```python
np.subtract(a,b)
```

```python
np.multiply(a,b)
```

```python
np.divide(a,b)
```

```python
np.power(a,b)
```

---

# Broadcasting

Broadcasting allows NumPy to perform arithmetic operations on arrays of different shapes.

```python
arr + 10
```

```python
matrix + vector
```

Advantages

- Faster
- Less Memory
- Cleaner Code

---

# Sorting Arrays

```python
np.sort(arr)
```

2D

```python
np.sort(arr,axis=0)
```

---

# Searching Arrays

```python
np.where(arr==5)
```

```python
np.argmax(arr)
```

```python
np.argmin(arr)
```

---

# Filtering Arrays

```python
arr[arr>5]
```

```python
arr[arr%2==0]
```

---

# Linear Algebra

Matrix Multiplication

```python
np.dot(a,b)
```

or

```python
a @ b
```

Inverse

```python
np.linalg.inv(matrix)
```

Determinant

```python
np.linalg.det(matrix)
```

Eigen Values

```python
np.linalg.eig(matrix)
```

---

# Random Module

Random Integer

```python
np.random.randint(1,10)
```

Random Float

```python
np.random.rand(3,3)
```

Normal Distribution

```python
np.random.randn(3,3)
```

Choice

```python
np.random.choice([1,2,3])
```

Shuffle

```python
np.random.shuffle(arr)
```

Seed

```python
np.random.seed(42)
```

---

# Input & Output

Save

```python
np.save("array.npy",arr)
```

Load

```python
np.load("array.npy")
```

Text File

```python
np.savetxt("array.txt",arr)
```

Read Text

```python
np.loadtxt("array.txt")
```

---

# Performance Comparison

Python List

```python
numbers=[1,2,3,4]
```

NumPy

```python
numbers=np.array([1,2,3,4])
```

NumPy Advantages

- Faster execution
- Lower memory usage
- Vectorized operations

---

# Real-World Applications

## Data Analysis

- Data Cleaning
- Numerical Analysis

---

## Machine Learning

- Feature Engineering
- Matrix Operations

---

## Artificial Intelligence

- Neural Networks
- Tensor Operations

---

## Scientific Computing

- Simulations
- Numerical Methods

---

## Image Processing

- Pixel Manipulation
- Image Transformation

---

## Finance

- Stock Analysis
- Risk Modeling

---

# Frequently Used Functions

| Function      | Purpose               |
| ------------- | --------------------- |
| array()       | Create Array          |
| zeros()       | Zeros Array           |
| ones()        | Ones Array            |
| eye()         | Identity Matrix       |
| arange()      | Range                 |
| linspace()    | Equal Intervals       |
| reshape()     | Change Shape          |
| flatten()     | Convert to 1D         |
| transpose()   | Matrix Transpose      |
| concatenate() | Join Arrays           |
| split()       | Split Arrays          |
| sort()        | Sorting               |
| where()       | Search                |
| mean()        | Average               |
| median()      | Median                |
| std()         | Standard Deviation    |
| var()         | Variance              |
| min()         | Minimum               |
| max()         | Maximum               |
| sum()         | Sum                   |
| dot()         | Matrix Multiplication |
| random.rand() | Random Values         |

---

# Common Interview Questions

### What is NumPy?

NumPy is a Python library used for numerical computing and efficient array operations.

---

### Difference between Python List and NumPy Array?

| Python List             | NumPy Array           |
| ----------------------- | --------------------- |
| Slower                  | Faster                |
| More Memory             | Less Memory           |
| Mixed Data Types        | Homogeneous Data      |
| Limited Math Operations | Vectorized Operations |

---

### What is ndarray?

`ndarray` is the core data structure of NumPy that stores homogeneous data in multiple dimensions.

---

### What is Broadcasting?

Broadcasting allows NumPy to perform operations on arrays with different shapes without making unnecessary copies.

---

### Difference between reshape() and flatten()?

- `reshape()` changes the shape without changing data.
- `flatten()` creates a 1D copy of the array.

---

### Difference between copy() and view()?

- `copy()` creates a new independent array.
- `view()` shares memory with the original array.

---

### What are Universal Functions (ufuncs)?

Vectorized functions that operate element-wise on arrays, such as `np.add()`, `np.sqrt()`, and `np.sin()`.

---

### Why is NumPy faster than Python Lists?

- Contiguous memory allocation
- Vectorized operations
- Optimized C implementation
- Reduced memory overhead

---

# Cheat Sheet

| Task                  | Function          |
| --------------------- | ----------------- |
| Create Array          | `np.array()`    |
| Shape                 | `.shape`        |
| Dimensions            | `.ndim`         |
| Size                  | `.size`         |
| Data Type             | `.dtype`        |
| Reshape               | `reshape()`     |
| Flatten               | `flatten()`     |
| Indexing              | `[]`            |
| Slicing               | `:`             |
| Sort                  | `sort()`        |
| Search                | `where()`       |
| Mean                  | `mean()`        |
| Median                | `median()`      |
| Std Dev               | `std()`         |
| Variance              | `var()`         |
| Sum                   | `sum()`         |
| Matrix Multiplication | `dot()` / `@` |
| Inverse               | `linalg.inv()`  |
| Determinant           | `linalg.det()`  |
| Random Numbers        | `random.rand()` |
| Save Array            | `save()`        |
| Load Array            | `load()`        |

---

# Conclusion

NumPy is the backbone of Python's scientific computing ecosystem. It provides fast and memory-efficient array operations, making it indispensable for **Data Analysis, Machine Learning, Artificial Intelligence, Scientific Computing, Image Processing, and Finance**.

By mastering NumPy concepts like arrays, indexing, slicing, broadcasting, vectorization, statistics, and linear algebra, you'll build a solid foundation for advanced libraries such as **Pandas, Matplotlib, SciPy, Scikit-learn, TensorFlow, and PyTorch**.

⭐ If you found this repository useful, don't forget to give it a **Star**!

Happy Coding! 🚀
