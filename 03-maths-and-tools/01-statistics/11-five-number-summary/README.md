
# Five Number Summary

## Overview

The **Five Number Summary** is a statistical summary used to describe the distribution and spread of a dataset using five important values.

The five values are:

1. Minimum
2. First Quartile (Q1)
3. Median (Q2)
4. Third Quartile (Q3)
5. Maximum

The Five Number Summary is widely used in:

- Statistics
- Data Analysis
- Exploratory Data Analysis (EDA)
- Outlier Detection
- Box Plots
- Machine Learning Preprocessing
- Data Cleaning

---

## The Five Numbers

| Statistic   | Description          |
| ----------- | -------------------- |
| Minimum     | Smallest observation |
| Q1          | 25th Percentile      |
| Median (Q2) | 50th Percentile      |
| Q3          | 75th Percentile      |
| Maximum     | Largest observation  |

Together, these five values provide a compact description of the dataset.

---

## Example Dataset

Consider:

```text
1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 27
```

Notice that `27` is much larger than the majority of the observations. This makes it a potential outlier.

### Step 1: Calculate Quartiles

Number of observations: **n = 19**

Using the percentile position formula introduced earlier:

```
Position = (P / 100) × (n + 1)
```

**First Quartile — Q1**

Q1 corresponds to the 25th percentile.

```
Position = (25 / 100) × (19 + 1)
         = 0.25 × 20
         = 5
```

The 5th observation is `3`. Therefore:

```
Q1 = 3
```

**Third Quartile — Q3**

Q3 corresponds to the 75th percentile.

```
Position = (75 / 100) × (19 + 1)
         = 0.75 × 20
         = 15
```

The 15th observation is `7`. Therefore:

```
Q3 = 7
```

### Step 2: Calculate the IQR

The Interquartile Range (IQR) measures the spread of the middle 50% of the dataset.

Formula:

```
IQR = Q3 - Q1
```

Calculation:

```
IQR = 7 - 3
    = 4
```

Therefore: `IQR = 4`

### Step 3: Calculate the Lower Fence

```
Lower Fence = Q1 - 1.5 × IQR
```

Substitute the values:

```
Lower Fence = 3 - (1.5 × 4)
            = 3 - 6
            = -3
```

Therefore: `Lower Fence = -3`

### Step 4: Calculate the Upper Fence

```
Upper Fence = Q3 + 1.5 × IQR
```

Calculation:

```
Upper Fence = 7 + (1.5 × 4)
            = 7 + 6
            = 13
```

Therefore: `Upper Fence = 13`

### Step 5: Identify Outliers

The IQR rule states:

```
Value < Lower Fence → Outlier
Value > Upper Fence → Outlier
```

For this dataset:

```
Lower Fence = -3
Upper Fence = 13
```

The dataset contains `27`. Since `27 > 13`, **27 is identified as an outlier** using the 1.5 × IQR rule.

---

## The Five Number Summary

The Five Number Summary should be calculated from the dataset under analysis.

For the given dataset, using the convention demonstrated in this lesson:

```
Minimum = 1
Q1      = 3
Median  = 5
Q3      = 7
Maximum = 27
```

| Statistic   | Value |
| ----------- | ----- |
| Minimum     | 1     |
| Q1          | 3     |
| Median (Q2) | 5     |
| Q3          | 7     |
| Maximum     | 27    |

Notice that the maximum is 27 because the Five Number Summary describes the original dataset. The fact that 27 is an outlier is recorded separately through the IQR analysis.

### Median

There are 19 observations, so the median is the middle observation.

`n = 19`

Median position:

```
(n + 1) / 2
= 20 / 2
= 10
```

The 10th observation is `5`. Therefore:

```
Median = 5
```

---

## Five Number Summary Visualization

The five values can be represented as:

```text
Minimum       Q1       Median       Q3       Maximum

   1           3          5           7          27
   |-----------|----------|-----------|-----------|
```

This compact representation allows us to understand:

- The center of the data
- The spread of the middle 50%
- The overall range
- Potential outliers

---

## Interquartile Range

The IQR represents the range containing the middle 50% of observations.

Formula:

```
IQR = Q3 - Q1
```

For this dataset:

```
IQR = 7 - 3
    = 4
```

The IQR is resistant to extreme values and is therefore useful when working with datasets containing outliers.

---

## Outlier Detection Using IQR

The standard IQR method uses:

```
Lower Fence = Q1 - 1.5 × IQR
Upper Fence = Q3 + 1.5 × IQR
```

Any observation outside these boundaries is considered a potential outlier.

For this example:

```
Q1 = 3
Q3 = 7
IQR = 4
```

Therefore:

```
Lower Fence = -3
Upper Fence = 13
```

Since `27 > 13`, **27 is an outlier**.

### Why 1.5 × IQR?

The multiplier **1.5** is a widely used statistical rule for identifying observations that are unusually far from the central portion of the data.

The rule is strongly associated with **John Tukey** and is widely used in exploratory data analysis and box plots.

It is a practical rule for identifying potential outliers and does not require assuming a specific probability distribution.

---

## Five Number Summary and Box Plot

The Five Number Summary forms the foundation of a **Box Plot**.

A box plot uses:

- Minimum
- Q1
- Median
- Q3
- Maximum

along with the IQR-based rule to identify potential outliers.

Conceptually:

```text
        Q1       Median       Q3
         |          |          |
         ↓          ↓          ↓

────────[==========|==========]────────

         <--- IQR --->
```

Potential outliers are plotted separately outside the whiskers.

> Box plots will be explored in more detail in a later lesson.

---

## Why is the Five Number Summary Useful?

The Five Number Summary provides a compact way to understand a dataset. It helps identify:

**Center**
The median tells us where the center of the data lies.

**Spread**
Q1 and Q3 show the middle 50% of the observations.

**Range**
Minimum and maximum show the overall range.

**Outliers**
The IQR can be used to identify potential outliers.

---

## Five Number Summary vs Mean and Standard Deviation

Mean and standard deviation are useful statistical measures, but they can be strongly affected by extreme values.

The Five Number Summary relies heavily on:

- Median
- Quartiles
- IQR

These are more resistant to extreme observations.

Therefore, the Five Number Summary is particularly useful for **skewed datasets** and **exploratory data analysis**.

---

## Important Formulas

**Interquartile Range**

```
IQR = Q3 - Q1
```

**Lower Fence**

```
Lower Fence = Q1 - 1.5 × IQR
```

**Upper Fence**

```
Upper Fence = Q3 + 1.5 × IQR
```

**Outlier Rule**

```
Value < Lower Fence → Potential Outlier
Value > Upper Fence → Potential Outlier
```

---

## Important Note About Outliers

An observation identified by the IQR rule is considered a **potential** outlier. It should not automatically be deleted.

An outlier may represent:

- Measurement error
- Data-entry error
- Rare event
- Genuine extreme observation
- Important business case

The decision to remove an outlier should depend on the context and the reason behind the observation.

---

## Applications

Five Number Summaries are commonly used in:

- Exploratory Data Analysis
- Data Cleaning
- Outlier Detection
- Box Plot Construction
- Feature Analysis
- Machine Learning Preprocessing
- Business Analytics
- Statistical Reporting

---

## Summary

```text
Dataset
   ↓
Sort Data
   ↓
Calculate Q1
   ↓
Calculate Median
   ↓
Calculate Q3
   ↓
Five Number Summary
   ↓
Calculate IQR
   ↓
Calculate Fences
   ↓
Identify Potential Outliers
```

---

## Interview Questions

1. **What is a Five Number Summary?**
   A Five Number Summary is a statistical summary consisting of: Minimum, Q1, Median, Q3, and Maximum.
2. **What is IQR?**
   IQR stands for Interquartile Range. It measures the spread of the middle 50% of observations: `IQR = Q3 - Q1`.
3. **How are outliers detected using IQR?**
   First calculate `IQR = Q3 - Q1`. Then calculate `Lower Fence = Q1 - 1.5 × IQR` and `Upper Fence = Q3 + 1.5 × IQR`. Observations outside these fences are considered potential outliers.
4. **Why is IQR useful?**
   IQR is less affected by extreme values than measures such as range, variance, and standard deviation.
5. **What are the five values in a Five Number Summary?**
   Minimum, Q1, Median, Q3, Maximum.
6. **Where is the Five Number Summary used?**
   It is commonly used in EDA, box plots, outlier detection, data cleaning, and machine learning preprocessing.

---

## Key Takeaways

- A Five Number Summary describes a dataset using five values.
- The five values are Minimum, Q1, Median, Q3, and Maximum.
- Q1 is the 25th percentile.
- Median/Q2 is the 50th percentile.
- Q3 is the 75th percentile.
- IQR = Q3 − Q1.
- The IQR rule uses 1.5 × IQR to identify potential outliers.
- Outliers should not automatically be removed.
- Five Number Summaries form the foundation of Box Plots.
- They are particularly useful for Exploratory Data Analysis and datasets containing extreme values.
