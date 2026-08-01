


# 📊 Matplotlib Complete Guide

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Matplotlib](https://img.shields.io/badge/Library-Matplotlib-orange)
![Status](https://img.shields.io/badge/Level-Beginner_to_Advanced-success)

A complete guide to **Matplotlib** covering all important graphs, charts, theory, syntax, customization, and real-world use cases.

---

# Table of Contents

1. What is Matplotlib?
2. Why Use Matplotlib?
3. Installation
4. Importing Library
5. Basic Plot Structure
6. Line Chart
7. Scatter Plot
8. Bar Chart
9. Horizontal Bar Chart
10. Histogram
11. Pie Chart
12. Box Plot
13. Area Chart
14. Stem Plot
15. Step Plot
16. Error Bar Plot
17. Stack Plot
18. Hexbin Plot
19. Violin Plot
20. Event Plot
21. Polar Plot
22. Contour Plot
23. Filled Contour Plot
24. Heatmap
25. Image Plot
26. 3D Plots
27. Multiple Plots (Subplots)
28. Plot Customization
29. Saving Figures
30. Real-World Applications
31. Interview Questions

---

# What is Matplotlib?

Matplotlib is one of the most popular Python libraries used for creating data visualizations. It converts numerical data into graphical representations, making data easier to understand and analyze.

Developed by **John D. Hunter**.

---

# Why Use Matplotlib?

- Easy to learn
- High-quality graphs
- Works with NumPy and Pandas
- Fully customizable
- Supports 2D and 3D graphs
- Widely used in Data Analysis, Machine Learning, and Research

---

# Installation

```bash
pip install matplotlib
```

---

# Import Library

```python
import matplotlib.pyplot as plt
import numpy as np
```

---

# Basic Plot Structure

```python
import matplotlib.pyplot as plt

x=[1,2,3,4]
y=[2,4,6,8]

plt.plot(x,y)

plt.title("Simple Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()
```

---

# 1. Line Chart

## Theory

A line graph connects data points using straight lines.

### Best Used For

- Trends
- Time Series
- Growth Analysis

```python
plt.plot(x,y)
```

Parameters

- color
- linestyle
- linewidth
- marker

---

# 2. Scatter Plot

## Theory

Shows relationship between two variables.

Best For

- Correlation
- Outlier Detection

```python
plt.scatter(x,y)
```

Useful Parameters

- color
- s
- alpha
- marker

---

# 3. Bar Chart

## Theory

Compares different categories.

```python
plt.bar(category,values)
```

Applications

- Sales
- Population
- Revenue

---

# 4. Horizontal Bar Chart

```python
plt.barh(category,values)
```

Best when labels are long.

---

# 5. Histogram

## Theory

Shows frequency distribution.

```python
plt.hist(data,bins=10)
```

Parameters

- bins
- color
- edgecolor

Applications

- Age Distribution
- Salary Distribution
- Marks Distribution

---

# 6. Pie Chart

## Theory

Shows percentage contribution.

```python
plt.pie(values,
labels=labels,
autopct="%1.1f%%")
```

Applications

- Market Share
- Budget Allocation

---

# 7. Box Plot

## Theory

Displays

- Minimum
- Q1
- Median
- Q3
- Maximum
- Outliers

```python
plt.boxplot(data)
```

Applications

- Detect Outliers
- Compare Distributions

---

# 8. Area Chart

```python
plt.fill_between(x,y)
```

Best for cumulative values.

---

# 9. Stem Plot

```python
plt.stem(x,y)
```

Useful for discrete signals.

---

# 10. Step Plot

```python
plt.step(x,y)
```

Used in

- Digital Signals
- Algorithms

---

# 11. Error Bar Plot

Shows uncertainty.

```python
plt.errorbar(x,y,yerr=error)
```

Applications

Scientific Research

---

# 12. Stack Plot

Shows cumulative trends.

```python
plt.stackplot(x,y1,y2,y3)
```

Applications

Revenue Breakdown

---

# 13. Hexbin Plot

For large scatter datasets.

```python
plt.hexbin(x,y)
```

---

# 14. Violin Plot

Shows distribution and density.

```python
plt.violinplot(data)
```

---

# 15. Event Plot

Visualizes events occurring over time.

```python
plt.eventplot(data)
```

---

# 16. Polar Plot

Circular graph.

```python
plt.polar(theta,r)
```

Applications

- Wind Direction
- Compass Data

---

# 17. Contour Plot

Shows 3D surface in 2D.

```python
plt.contour(X,Y,Z)
```

Applications

Topographic Maps

---

# 18. Filled Contour Plot

```python
plt.contourf(X,Y,Z)
```

Better visualization than contour.

---

# 19. Heatmap

```python
plt.imshow(data,cmap="viridis")
plt.colorbar()
```

Applications

- Correlation Matrix
- Image Analysis

---

# 20. Image Plot

```python
plt.imshow(image)
```

Displays images.

---

# 21. 3D Scatter Plot

```python
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection="3d")

ax.scatter(x,y,z)
```

---

# 22. 3D Surface Plot

```python
ax.plot_surface(X,Y,Z)
```

Applications

Scientific Visualization

---

# 23. Multiple Plots (Subplots)

```python
plt.subplot(2,2,1)
```

or

```python
fig,ax=plt.subplots(2,2)
```

---

# Plot Customization

## Title

```python
plt.title("Sales Report")
```

---

## X Label

```python
plt.xlabel("Months")
```

---

## Y Label

```python
plt.ylabel("Sales")
```

---

## Grid

```python
plt.grid(True)
```

---

## Legend

```python
plt.legend()
```

---

## Figure Size

```python
plt.figure(figsize=(10,6))
```

---

## Colors

```python
plt.plot(x,y,color="red")
```

---

## Line Styles

```python
'-'
'--'
':'
'-.'
```

---

## Markers

```python
'o'
's'
'^'
'x'
'D'
```

---

## Transparency

```python
alpha=0.5
```

---

## Save Figure

```python
plt.savefig("graph.png")
```

---

# Common Color Maps

- viridis
- plasma
- inferno
- magma
- coolwarm
- jet
- rainbow

---

# Real-World Applications

## Business

- Sales Analysis
- Revenue Dashboard
- Profit Visualization

---

## Finance

- Stock Prices
- Profit Trends

---

## Healthcare

- Patient Data
- Disease Distribution

---

## Machine Learning

- Loss Curve
- Accuracy Curve
- Feature Importance

---

## Data Analysis

- Missing Value Analysis
- Distribution Analysis
- Outlier Detection
- Correlation Matrix

---

## Scientific Research

- Signal Processing
- Weather Analysis
- Simulation

---

# Common Interview Questions

### Why use Matplotlib?

For creating static, animated, and interactive visualizations.

---

### Difference between Plot and Scatter?

Plot connects points using lines.

Scatter shows independent points.

---

### Difference between Histogram and Bar Chart?

Histogram

- Continuous data
- Frequency distribution

Bar Chart

- Categorical data
- Category comparison

---

### Difference between Box Plot and Histogram?

Histogram shows frequency.

Box Plot shows distribution and outliers.

---

### What is Figure?

The complete window containing one or more plots.

---

### What is Axes?

The area where graphs are drawn.

---

### What is pyplot?

A module used for plotting graphs.

---

### Why use subplot()?

To display multiple graphs in one figure.

---

### How to save a graph?

```python
plt.savefig("figure.png")
```

---

# Cheat Sheet

| Function       | Purpose         |
| -------------- | --------------- |
| plot()         | Line Graph      |
| scatter()      | Scatter Plot    |
| bar()          | Vertical Bar    |
| barh()         | Horizontal Bar  |
| hist()         | Histogram       |
| pie()          | Pie Chart       |
| boxplot()      | Box Plot        |
| fill_between() | Area Chart      |
| stem()         | Stem Plot       |
| step()         | Step Plot       |
| errorbar()     | Error Bar       |
| stackplot()    | Stack Plot      |
| hexbin()       | Hexbin Plot     |
| violinplot()   | Violin Plot     |
| eventplot()    | Event Plot      |
| polar()        | Polar Plot      |
| contour()      | Contour Plot    |
| contourf()     | Filled Contour  |
| imshow()       | Image/Heatmap   |
| subplot()      | Multiple Graphs |
| savefig()      | Save Figure     |
| grid()         | Grid            |
| legend()       | Legend          |
| xlabel()       | X-axis Label    |
| ylabel()       | Y-axis Label    |
| title()        | Title           |

---

# Conclusion

Matplotlib is the foundation of Python data visualization. Learning these charts helps in:

- Data Analysis
- Machine Learning
- Data Science
- Research
- Dashboard Development
- Business Analytics
- Interview Preparation

Master these plots along with NumPy and Pandas to become proficient in Python-based data analysis.

⭐ If you found this repository useful, don't forget to give it a star!
