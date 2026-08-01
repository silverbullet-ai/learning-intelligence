# Measures of Central Tendency

## Overview

Measures of Central Tendency are statistical techniques used to determine the central or typical value of a dataset.

Instead of analyzing every individual observation, these measures summarize the dataset using a single representative value.

The three primary measures of central tendency are:

- Mean
- Median
- Mode

These measures are widely used in Statistics, Data Science, Machine Learning, Artificial Intelligence, Business Analytics, and Scientific Research.

---

# Why Do We Need Measures of Central Tendency?

Consider the following dataset:

```text
1, 3, 4, 5
```

Instead of examining each value individually, we often want a single value that best represents the dataset.

Measures of central tendency provide that representative value.

---

# 1. Mean (Average)

## Definition

The **Mean** is the arithmetic average of all observations in a dataset.

It is calculated by adding all observations and dividing by the total number of observations.

---

## Population Mean

The population mean is represented by:

```text
μ (Mu)
```

Formula:

```text
        ΣXi
μ =  ----------
          N
```

Where:

- μ = Population Mean
- N = Population Size
- Xi = Individual Observation

---

## Sample Mean

The sample mean is represented by:

```text
x̄ (X Bar)
```

Formula:

```text
        ΣXi
x̄ = ----------
         n
```

Where:

- x̄ = Sample Mean
- n = Sample Size

---

## Example

Dataset:

```text
1, 3, 4, 5
```

Calculation:

```text
(1 + 3 + 4 + 5) / 4

= 13 / 4

= 3.25
```

**Mean = 3.25**

---

# Outliers and Mean

The mean is highly sensitive to outliers.

## Example

Dataset:

```text
1, 3, 4, 5, 100
```

Calculation:

```text
(1 + 3 + 4 + 5 + 100) / 5

= 113 / 5

= 22.6
```

Originally:

```text
Mean = 3.25
```

After adding one extreme value:

```text
Mean = 22.6
```

The outlier significantly changes the average.

---

# What is an Outlier?

An outlier is an observation that is significantly different from the rest of the dataset.

Example:

```text
1, 3, 4, 5, 100
              ↑
          Outlier
```

Outliers can heavily influence the mean.

---

# 2. Median

## Definition

The **Median** is the middle value of a dataset after arranging the observations in ascending order.

Unlike the mean, the median is much less affected by outliers.

---

# Steps to Calculate Median

1. Arrange the observations in ascending order.
2. Find the middle value.

---

## Example (Odd Number of Observations)

Dataset:

```text
4, 3, 1, 5, 100
```

After sorting:

```text
1, 3, 4, 5, 100
```

Middle value:

```text
1, 3, [4], 5, 100
```

**Median = 4**

---

## Example (Even Number of Observations)

Dataset:

```text
1, 3, 4, 5, 100, 200
```

Middle values:

```text
1, 3, [4, 5], 100, 200
```

Calculation:

```text
(4 + 5) / 2

= 4.5
```

**Median = 4.5**

---

# Median Rules

## Odd Number of Elements

Choose the middle value.

Example:

```text
1, 3, 4, 5, 100

Median = 4
```

---

## Even Number of Elements

Take the average of the two middle values.

Example:

```text
1, 3, 4, 5, 100, 200

Median = (4 + 5) / 2

Median = 4.5
```

---

# Advantages of Median

- Resistant to outliers
- Suitable for skewed distributions
- Represents the center more accurately when extreme values exist

---

# 3. Mode

## Definition

The **Mode** is the value that appears most frequently in a dataset.

---

## Example

Dataset:

```text
4, 3, 2, 1, 1, 4, 4, 5, 2, 100
```

Frequency Table

| Value | Frequency |
|------:|----------:|
| 1 | 2 |
| 2 | 2 |
| 3 | 1 |
| 4 | 3 |
| 5 | 1 |
|100|1|

The highest frequency is:

```text
4 → 3 times
```

**Mode = 4**

---

# Why Mode Works Well

Mode depends only on frequency.

Even though:

```text
100
```

is an outlier, it appears only once and therefore does not affect the mode.

---

# Mean vs Median vs Mode

| Measure | Definition | Affected by Outliers? |
|----------|------------|-----------------------|
| Mean | Arithmetic Average | Yes |
| Median | Middle Value | Very Little |
| Mode | Most Frequent Value | Generally No |

---

# Example Comparison

Dataset:

```text
1, 3, 4, 5, 100
```

| Measure | Value |
|---------|------:|
| Mean | 22.6 |
| Median | 4 |
| Mode | No Mode |

---

Dataset:

```text
1, 1, 2, 4, 4, 4, 5, 100
```

| Measure | Result |
|---------|--------|
| Mean | Influenced by Outlier |
| Median | Stable |
| Mode | 4 |

---

# When Should You Use Each?

## Mean

Use when:

- Data has no significant outliers.
- Distribution is approximately normal.

---

## Median

Use when:

- Dataset contains outliers.
- Distribution is skewed.

Examples:

- Salaries
- House Prices
- Income Distribution

---

## Mode

Use when:

- Finding the most common value.
- Working with categorical data.

Examples:

- Most Sold Product
- Most Common Shoe Size
- Most Common Age Group

---

# Important Symbols

| Symbol | Meaning |
|---------|---------|
| μ | Population Mean |
| x̄ | Sample Mean |
| N | Population Size |
| n | Sample Size |

---

# Interview Questions

### What are Measures of Central Tendency?

Measures of Central Tendency are statistical techniques used to identify the central value of a dataset.

---

### What are the three Measures of Central Tendency?

- Mean
- Median
- Mode

---

### Which measure is most affected by outliers?

Mean.

---

### Which measure is least affected by outliers?

Median.

---

### When is Mode useful?

Mode is useful when identifying the most frequently occurring value or category.

---

# Key Takeaways

- Mean is the arithmetic average of observations.
- Median is the middle value after sorting the data.
- Mode is the most frequently occurring observation.
- Mean is sensitive to outliers.
- Median is resistant to outliers.
- Mode is useful for frequency analysis.
- Choosing the correct measure depends on the nature of the dataset.

---

# What's Next?

In the next chapter, we'll study **Measures of Dispersion**, including:

- Range
- Variance
- Standard Deviation

These measures help us understand how spread out the data is around its center.