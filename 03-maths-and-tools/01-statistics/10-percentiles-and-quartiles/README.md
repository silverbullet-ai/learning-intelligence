# Percentiles and Quartiles

## Overview

Percentiles and Quartiles are important statistical measures used to understand the **relative position of observations within a dataset**.

They are widely used in:

- Statistics
- Data Analysis
- Machine Learning
- Competitive Exams
- Medical Assessments
- Educational Assessments
- Salary Analysis
- Exploratory Data Analysis (EDA)

For example, when someone says:

> "I scored in the 99th percentile."

This does **not** mean that the person scored 99% marks.

It means their performance was higher than approximately 99% of the reference group.

---

## Percentage vs Percentile

Before understanding percentiles, it is important to distinguish between **percentage** and **percentile**. They are completely different concepts.

### Percentage

Percentage tells us **how much of the whole** something represents.

**Example**

Consider the set: `1, 2, 3, 4, 5, 6`

Odd numbers: `1, 3, 5`

- Number of odd values: **3**
- Total values: **6**

Formula:

```
Percentage = (Desired Values / Total Values) × 100
```

Therefore:

```
Percentage = (3 / 6) × 100
           = 50%
```

So, 50% of the values are odd.

### What is a Percentile?

A **Percentile** describes the relative position of a value within a dataset.

More formally:

> A percentile indicates the value below which a specified percentage of observations lies.

In simple terms:

```
Percentile → Relative Position
```

---

## Example Dataset

Consider the sorted dataset:

```
2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8, 9, 9, 10
```

Number of observations: **n = 14**

### Percentile Rank of a Value

Suppose we want to determine the percentile rank of **x = 9**.

A simple percentile-rank calculation is:

```
Percentile Rank = (Number of values below x / Total observations) × 100
```

**Step 1: Count values below 9**

```
2, 2, 3, 4, 5, 5, 6, 7, 8, 8, 8
```

Number of values: **11**

**Step 2: Calculate percentile rank**

```
Percentile Rank = (11 / 14) × 100
                ≈ 78.57%
```

Therefore, under this definition:

```
9 ≈ 78.57th percentile
```

This means approximately 78.57% of the observations are below 9.

> **Note:** Percentile-rank conventions can vary depending on the statistical definition or software being used, especially when ties are present.

---

## Finding the Value at a Given Percentile

Sometimes we know the percentile and want to find the corresponding value.

For example: *Find the 25th percentile.*

One commonly taught position formula is:

```
Position = (P / 100) × (n + 1)
```

where:
- `P` = Desired percentile
- `n` = Number of observations

### Example: 25th Percentile

Given: `P = 25`, `n = 14`

```
Position = (25 / 100) × (14 + 1)
         = 0.25 × 15
         = 3.75
```

The position is **3.75**, which lies between:

- Position 3 → value `3`
- Position 4 → value `4`

Using linear interpolation:

```
25th Percentile = 3.75
```

> **Note:** Percentile calculation methods differ between statistical software and conventions. NumPy, Pandas, Excel, R, and other tools may use different interpolation/quantile definitions. Therefore, the exact numerical result can vary.

### Interpolation

When a percentile position falls between two observations, interpolation can be used to estimate the corresponding value.

For example, `Position = 3.75` lies between positions 3 and 4.

If Position 3 = `3` and Position 4 = `4`, then the interpolated value is:

```
3 + 0.75 × (4 - 3) = 3.75
```

---

## Quartiles

Quartiles divide a sorted dataset into four sections.

The word **Quartile** comes from *Quarter = 1/4*.

The three main quartiles are:

| Quartile | Percentile      |
|----------|-----------------|
| Q1       | 25th percentile |
| Q2       | 50th percentile |
| Q3       | 75th percentile |

### First Quartile — Q1

`Q1 = 25th Percentile`

Q1 represents the point below which approximately 25% of the observations lie.

### Second Quartile — Q2

`Q2 = 50th Percentile`

Q2 is the **Median**. Therefore:

```
Q2 = Median = 50th Percentile
```

Approximately 50% of the observations lie below the median.

### Third Quartile — Q3

`Q3 = 75th Percentile`

Q3 represents the point below which approximately 75% of the observations lie.

### Quartile Visualization

```text
0%          25%          50%          75%          100%
|------------|------------|------------|------------|
             Q1           Q2           Q3
                          Median
```

The dataset is divided into approximately four sections:

- 0–25% → First Quarter
- 25–50% → Second Quarter
- 50–75% → Third Quarter
- 75–100% → Fourth Quarter

### Relationship Between Median and Quartiles

```
Q1 = 25th Percentile
Q2 = 50th Percentile = Median
Q3 = 75th Percentile
```

Therefore:

```text
Mean
  ↓
Average

Median
  ↓
Middle Value

Quartiles
  ↓
Divide Data into Four Parts
```

---

## Percentage vs Percentile (Comparison)

| Percentage                          | Percentile                        |
|--------------------------------------|------------------------------------|
| Measures a proportion                | Measures relative position         |
| Expressed as a percentage            | Describes position in a dataset    |
| Based on part-to-whole relationship  | Based on relative standing         |
| Example: 80% marks                   | Example: 80th percentile           |
| Measures amount/performance          | Measures rank/position             |

---

## Applications of Percentiles

Percentiles are commonly used for:

- Competitive examination rankings
- Student performance analysis
- Medical growth charts
- Salary comparisons
- Credit score analysis
- Machine Learning feature analysis
- Data Analysis
- Performance benchmarking

## Applications of Quartiles

Quartiles are particularly useful for:

- Understanding data distribution
- Measuring relative position
- Constructing box plots
- Detecting outliers
- Calculating the Interquartile Range (IQR)
- Exploratory Data Analysis

---

## Interquartile Range

Quartiles provide the foundation for the **Interquartile Range (IQR)**.

The IQR measures the spread of the middle 50% of observations.

Formula:

```
IQR = Q3 - Q1
```

For example, if `Q1 = 25` and `Q3 = 75`, then:

```
IQR = 75 - 25 = 50
```

> IQR and box plots will be covered in more detail in a later lesson.

---

## Summary

```text
Dataset
   ↓
Sort the Data
   ↓
Determine Relative Position
   ↓
Calculate Percentiles
   ↓
25% → Q1
50% → Q2 → Median
75% → Q3
```

---

## Key Formulas

**Percentage**

```
Percentage = (Desired Values / Total Values) × 100
```

**Percentile Rank**

A simple percentile-rank definition is:

```
Percentile Rank = (Number of Values Below x / n) × 100
```

**Pth Percentile Position**

One commonly used method is:

```
Position = (P / 100) × (n + 1)
```

where:
- `P` = Desired percentile
- `n` = Number of observations

**Interquartile Range**

```
IQR = Q3 - Q1
```

---

## Interview Questions

1. **What is a percentile?**
   A percentile indicates the relative position of a value within a dataset and represents the point below which a specified percentage of observations lie.

2. **What is the difference between percentage and percentile?**
   - Percentage measures a proportion out of 100.
   - Percentile describes the relative position of an observation within a dataset.

3. **What is the 50th percentile?**
   The 50th percentile is `Q2 = Median`.

4. **What are Quartiles?**
   Quartiles divide a sorted dataset into four approximately equal parts.

5. **What are Q1, Q2, and Q3?**
   - Q1 → 25th Percentile
   - Q2 → 50th Percentile → Median
   - Q3 → 75th Percentile

6. **Why are Quartiles important?**
   Quartiles help us understand the distribution and spread of data and form the basis for:
   - IQR
   - Box plots
   - Outlier detection
   - Exploratory Data Analysis

7. **What is IQR?**
   IQR stands for Interquartile Range. It measures the spread of the middle 50% of observations: `IQR = Q3 - Q1`.

---

## Key Takeaways

- Percentage and Percentile are different concepts.
- Percentage measures a part-to-whole relationship.
- Percentile describes the relative position of a value within a dataset.
- Q1 = 25th percentile.
- Q2 = 50th percentile = Median.
- Q3 = 75th percentile.
- Quartiles divide a sorted dataset into four approximately equal sections.
- Percentiles are useful for ranking and relative comparisons.
- Quartiles are useful for understanding data spread.
- Quartiles form the foundation of IQR and box plots.
- Percentile calculations can vary depending on the statistical convention or software implementation.