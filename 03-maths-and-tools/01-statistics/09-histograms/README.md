# Histograms

## Overview

A **Histogram** is one of the most important visualization tools in Statistics.

It helps us understand how numerical data is distributed by showing the **frequency (count)** of observations within specific intervals called **bins**.

Histograms are widely used in:

- Statistics
- Data Analysis
- Machine Learning
- Deep Learning
- Exploratory Data Analysis (EDA)

Histograms also provide an important foundation for understanding **Probability Density Functions (PDFs)**.

---

## What is a Histogram?

A histogram is a graphical representation of the **frequency distribution of numerical data**.

Instead of displaying every observation individually, a histogram:

1. Divides the data into intervals called bins.
2. Counts the observations within each bin.
3. Represents those counts using adjacent bars.

Unlike a bar chart, histogram bars normally **touch each other**, because the intervals represent continuous numerical ranges.

---

# Example Dataset

Consider the following age data:

```python
ages = [23, 24, 25, 30, 34, 36, 40, 50, 60, 75, 80]
```

Instead of looking at every value individually, we can group the values into intervals.

---

# Creating Bins

Suppose we choose a bin size of 10.

```text
0–10
10–20
20–30
30–40
40–50
50–60
60–70
70–80
```

These intervals are called **bins**.

### Bin

A **bin** is an interval used to group numerical observations together.

---

# Frequency Distribution

We count how many observations fall into each interval.

| Bin | Frequency |
|-----|----------:|
| 0–10 | 0 |
| 10–20 | 0 |
| 20–30 | 3 |
| 30–40 | 2 |
| 40–50 | 1 |
| 50–60 | 1 |
| 60–70 | 1 |
| 70–80 | 2 |

> **Note:** The exact boundary treatment depends on how the bins are defined by the histogram implementation.

The histogram is a visual representation of this frequency distribution.

---

# Understanding a Histogram

Each histogram bar represents:

```text
Width  → Bin Interval

Height → Frequency
```

For example:

```text
20–30 → 3 observations

30–40 → 2 observations

40–50 → 1 observation
```

This allows us to understand the distribution without examining every individual observation.

---

# What are Bins?

A bin is simply a range used to group numerical data.

Example:

```text
Bin Size = 10

0–10
10–20
20–30
30–40
...
```

The choice of bin size has a significant effect on the appearance of a histogram.

---

# Changing the Bin Size

We can use different bin sizes for the same dataset.

### Bin Size = 20

```text
0–20
20–40
40–60
60–80
```

### Bin Size = 5

```text
20–25
25–30
30–35
35–40
...
```

Changing the bin size changes the appearance and level of detail of the histogram.

---

# Why is Bin Size Important?

If the bins are too large:

```text
Too few bins
    ↓
Less detail
    ↓
Important patterns may disappear
```

If the bins are too small:

```text
Too many bins
    ↓
More detail
    ↓
Distribution may appear noisy
```

Therefore, an appropriate bin size is important when interpreting a histogram.

---

# Continuous vs Discrete Data

Histograms are primarily associated with **numerical data**, especially continuous data.

Examples of continuous data:

- Height
- Weight
- Age
- Salary
- Temperature

Example:

```text
150.2
152.7
158.5
160.1
175.8
```

These values can take many possible values within a range.

---

# Discrete Numerical Data

Discrete numerical data consists of countable values.

Example:

```text
Number of Children

0
1
2
3
4
```

Although histograms can sometimes be used for discrete numerical data, **bar charts are often more appropriate** when the values represent separate categories or counts.

---

# Histogram vs Bar Chart

| Histogram | Bar Chart |
|-----------|-----------|
| Numerical data | Categorical data |
| Usually continuous measurements | Categories |
| Bars touch | Bars have gaps |
| X-axis contains intervals/bins | X-axis contains categories |
| Shows frequency distribution | Compares categories |

---

# Why Do Histogram Bars Touch?

Histogram bars represent adjacent numerical intervals.

For example:

```text
20–30
30–40
40–50
```

There is no conceptual gap between these numerical ranges.

Therefore, the bars are drawn next to one another.

A bar chart, on the other hand, represents separate categories:

```text
Python     Java     C++
```

Therefore, gaps are normally used between the bars.

---

# What Can a Histogram Tell Us?

Histograms help us understand:

- Distribution of data
- Concentration of observations
- Spread of data
- Skewness
- Possible outliers
- Shape of the distribution
- Frequency of observations

Instead of examining thousands of observations individually, we can obtain a visual summary of the dataset.

---

# Histogram and Probability Density Function

Histograms are an important stepping stone toward understanding the **Probability Density Function (PDF)**.

A histogram represents observed frequencies.

A PDF represents the underlying probability density of a continuous random variable.

Conceptually:

```text
Observed Data
      ↓
Histogram
      ↓
Estimate Underlying Distribution
      ↓
Probability Density Function
```

---

# Kernel Density Estimation (KDE)

A histogram uses rectangular bins.

We can instead estimate a smooth distribution using **Kernel Density Estimation (KDE)**.

Conceptually:

```text
Histogram
    ↓
Kernel Density Estimation
    ↓
Smooth Density Curve
```

KDE provides a smooth estimate of the distribution of the data.

> KDE is an estimation technique. A PDF describes the probability density of a continuous random variable. They are related, but they are not exactly the same thing.

---

# Python Histogram

A histogram can be created using Matplotlib.

```python
import matplotlib.pyplot as plt

ages = [
    23, 24, 25, 30, 34,
    36, 40, 50, 60, 75, 80
]

plt.hist(
    ages,
    bins=8,
    edgecolor="black"
)

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Histogram of Ages")

plt.show()
```

---

# Histogram Workflow

```text
Raw Data
   ↓
Choose Bins
   ↓
Group Observations
   ↓
Count Frequency
   ↓
Draw Histogram
   ↓
Analyze Distribution
```

---

# Example Interpretation

Suppose a histogram shows a large concentration of observations between:

```text
20–40
```

and relatively few observations between:

```text
60–80
```

We can conclude that the dataset contains more observations around the lower age range.

The histogram allows us to identify this pattern immediately.

---

# Advantages of Histograms

- Easy to understand
- Clearly shows data distribution
- Helps identify skewness
- Helps identify potential outliers
- Summarizes large datasets
- Useful during Exploratory Data Analysis
- Provides intuition for probability distributions

---

# Limitations

- Appearance depends on bin size
- Exact individual values cannot be recovered easily
- Not suitable for categorical variables
- Different bin choices can lead to different visual interpretations

---

# Important Terms

| Term | Meaning |
|------|---------|
| Histogram | Graph showing frequency distribution |
| Bin | Interval used to group observations |
| Frequency | Number of observations in a bin |
| Bin Size | Width of each interval |
| KDE | Smooth estimate of the underlying distribution |
| PDF | Probability density function |

---

# Interview Questions

### 1. What is a Histogram?

A histogram is a graphical representation of the frequency distribution of numerical data using adjacent bars.

---

### 2. What is a Bin?

A bin is an interval used to group numerical observations together.

---

### 3. What does the height of a histogram bar represent?

The height generally represents the **frequency**, or number of observations, within that bin.

---

### 4. Why do Histogram bars touch each other?

Because histogram bins represent adjacent numerical intervals, particularly for continuous numerical data.

---

### 5. What is the difference between a Histogram and a Bar Chart?

A histogram is primarily used for numerical distributions and uses bins, while a bar chart is generally used to compare separate categories.

---

### 6. What is Kernel Density Estimation?

Kernel Density Estimation (KDE) is a statistical technique used to create a smooth estimate of the underlying distribution of numerical data.

---

# Key Takeaways

- A **Histogram** visualizes the frequency distribution of numerical data.
- Data is divided into **bins**.
- Each bin represents an interval.
- The bar height represents the frequency of observations.
- Histogram bars normally touch because the intervals are adjacent.
- Bin size affects the appearance and interpretation of a histogram.
- Histograms help identify distribution, spread, skewness, and potential outliers.
- Histograms provide intuition for understanding probability distributions.
- **KDE** can be used to create a smooth estimate of an underlying distribution.
- Histograms are an important foundation for learning **PDFs and CDFs**.