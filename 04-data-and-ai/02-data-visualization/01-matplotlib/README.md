# Matplotlib

## Overview

Matplotlib is one of the most widely used Python libraries for data visualization.

It is used to create:

- Line Plots
- Bar Charts
- Histograms
- Scatter Plots
- Pie Charts
- Subplots

Matplotlib is a foundational library for:

- Data Analysis
- Exploratory Data Analysis (EDA)
- Machine Learning
- Data Science
- Analytics

The most commonly used module is:

```python
import matplotlib.pyplot as plt
```

---

## Installation

```bash
pip install matplotlib
```

---

## Topics Covered

### Line Plots

- `plt.plot()`
- Line styles
- Colors
- Markers
- Grid customization

### Bar Charts

- `plt.bar()`
- Category comparison

### Histograms

- `plt.hist()`
- Data distribution
- Bins

### Scatter Plots

- `plt.scatter()`
- Relationship analysis
- Correlation visualization

### Pie Charts

- `plt.pie()`
- Percentage contribution
- Explode effect
- Percent labels

### Subplots

- `plt.subplot()`
- `plt.figure()`
- Multiple visualizations in one figure

---

## Key Concepts

| Plot Type    | Primary Use              |
| ------------ | ------------------------ |
| Line Plot    | Trends over time         |
| Bar Chart    | Category comparison      |
| Histogram    | Data distribution        |
| Scatter Plot | Relationship analysis    |
| Pie Chart    | Percentage contribution  |
| Subplots     | Multiple charts together |

---

## Common Functions

| Function      | Purpose        |
| ------------- | -------------- |
| plt.plot()    | Line plot      |
| plt.bar()     | Bar chart      |
| plt.hist()    | Histogram      |
| plt.scatter() | Scatter plot   |
| plt.pie()     | Pie chart      |
| plt.figure()  | Create figure  |
| plt.subplot() | Create subplot |
| plt.xlabel()  | X-axis label   |
| plt.ylabel()  | Y-axis label   |
| plt.title()   | Plot title     |
| plt.grid()    | Display grid   |
| plt.show()    | Render chart   |

---

## Real-World Applications

Matplotlib is commonly used for:

- Sales Analysis
- Business Dashboards
- Exploratory Data Analysis
- Machine Learning Model Evaluation
- Trend Analysis
- Reporting

---

## Practice Assignment (Solved)

### Problem

Create a line chart showing the square of numbers from 1 to 5.

### Solution

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(
    x,
    y,
    marker="o"
)

plt.xlabel("Number")
plt.ylabel("Square")
plt.title("Squares of Numbers")

plt.grid(True)

plt.show()
```

### Expected Result

A line chart showing:

- X-axis → Numbers
- Y-axis → Their squares
- Grid enabled
- Circular markers

---

## Key Takeaways

- Matplotlib is the foundation of Python visualization.
- Line plots are used for trends.
- Bar charts compare categories.
- Histograms show distributions.
- Scatter plots reveal relationships.
- Pie charts show proportions.
- Subplots allow multiple visualizations in one figure.
