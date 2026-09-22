# 📦 Box Plot with Python

A box plot is a statistical visualization used to understand the distribution of numerical data, identify its central tendency and spread, and detect potential outliers.

This topic covers:

- Five-number summary
- Quantiles
- Q1 and Q3
- Median
- Interquartile Range (IQR)
- Lower and upper fences
- Outlier detection
- Box plots using Seaborn

---

## 1. Five-Number Summary

A box plot is based on five important statistical values:

1. **Minimum**
2. **Q1** — 25th percentile
3. **Median** — 50th percentile
4. **Q3** — 75th percentile
5. **Maximum**

Together, these form the **five-number summary**.

```text
Minimum → Q1 → Median → Q3 → Maximum
```

---

## 2. Calculating Quantiles with NumPy

NumPy provides the `np.quantile()` function for calculating quantiles.

```python
import numpy as np
```

Example dataset:

```python
marks = [
    45, 32, 56, 75, 89, 54, 32, 89,
    90, 87, 67, 54, 45, 98, 99, 67, 74
]
```

We can calculate the five-number summary with:

```python
minimum, q1, median, q3, maximum = np.quantile(
    marks,
    [0, 0.25, 0.50, 0.75, 1.0]
)
```

### Quantile Mapping

| Quantile | Meaning |
|---:|---|
| `0` | Minimum |
| `0.25` | Q1 / 25th percentile |
| `0.50` | Median / 50th percentile |
| `0.75` | Q3 / 75th percentile |
| `1.0` | Maximum |

---

## 3. Five-Number Summary Example

For the given dataset:

```text
Minimum = 32
Q1      = 54
Median  = 67
Q3      = 89
Maximum = 99
```

Therefore:

```text
Minimum → 32
Q1      → 54
Median  → 67
Q3      → 89
Maximum → 99
```

> **Note:** Quantile values can depend on the quantile calculation method. NumPy's default method is used here.

---

## 4. Interquartile Range (IQR)

The **Interquartile Range (IQR)** represents the spread of the middle 50% of the data.

### Formula

```text
IQR = Q3 − Q1
```

For the example:

```text
IQR = 89 − 54
    = 35
```

So, the middle 50% of the data spans **35 units**.

---

## 5. Lower Fence

The lower fence is used to identify potential lower-side outliers.

### Formula

```text
Lower Fence = Q1 − 1.5 × IQR
```

Using:

```text
Q1  = 54
IQR = 35
```

we get:

```text
Lower Fence = 54 − 1.5 × 35
            = 54 − 52.5
            = 1.5
```

Therefore:

```text
Lower Fence = 1.5
```

Any observation below `1.5` is considered a potential outlier under the standard IQR rule.

---

## 6. Upper Fence

The upper fence is used to identify potential upper-side outliers.

### Formula

```text
Upper Fence = Q3 + 1.5 × IQR
```

For the example:

```text
Upper Fence = 89 + 1.5 × 35
            = 89 + 52.5
            = 141.5
```

Therefore:

```text
Upper Fence = 141.5
```

Any observation above `141.5` is considered a potential outlier under the standard IQR rule.

For the original dataset, there are no values below `1.5` or above `141.5`, so there are no potential outliers according to this rule.

---

## 7. Outlier Detection Rule

The standard IQR rule identifies observations outside the fences as potential outliers.

### Lower-side outlier

```text
x < Q1 − 1.5 × IQR
```

### Upper-side outlier

```text
x > Q3 + 1.5 × IQR
```

Conceptually:

```text
Value < Lower Fence
        ↓
Potential Outlier
```

or:

```text
Value > Upper Fence
        ↓
Potential Outlier
```

---

## 8. Creating a Box Plot with Seaborn

Seaborn can be used to create a box plot.

```python
import seaborn as sns
```

Then:

```python
sns.boxplot(x=marks)
```

Seaborn calculates the statistics required for the box plot and displays potential outliers as individual points.

---

## 9. Understanding the Box Plot

A simplified vertical box plot looks like this:

```text
          Maximum
             │
        ─────┤
             │
          ┌──┴──┐
          │     │
          │     │  ← Q3
          │     │
          ├─────┤  ← Median
          │     │
          │     │  ← Q1
          │     │
          └──┬──┘
             │
        ─────┤
             │
          Minimum
```

### Main Components

| Component | Meaning |
|---|---|
| Minimum / lower whisker | Lowest non-outlier observation |
| Q1 | 25th percentile |
| Median | 50th percentile |
| Q3 | 75th percentile |
| Maximum / upper whisker | Highest non-outlier observation |
| Box | Middle 50% of the data |
| Whiskers | Extend to the most extreme non-outlier observations |
| Dots | Potential outliers |

> **Important:** In a standard Seaborn box plot, the whiskers do **not necessarily reach the dataset's absolute minimum and maximum**. They extend to the most extreme observations within the 1.5 × IQR limits. Values beyond those limits are shown separately as potential outliers.

---

## 10. What Happens When Outliers Exist?

Suppose extreme values such as:

```text
-100
-200
```

are added to the dataset.

These values may fall outside the lower fence. When the box plot is generated, Seaborn displays them as individual points beyond the whiskers.

Conceptually:

```text
       •  ← Potential outlier
       │
       │
     ┌───┐
     │   │
     │   │
     ├───┤  ← Median
     │   │
     │   │
     └───┘
       │
       │
       •  ← Potential outlier
```

### Important

**Dots outside the whiskers represent potential outliers according to the box plot's IQR-based rule.**

---

## 11. Seaborn and Automatic Box Plot Calculation

You do not need to manually calculate Q1, Q3, IQR, and the fences just to create a box plot.

```python
sns.boxplot(x=marks)
```

handles the statistical calculations required to construct the visualization.

However, manually calculating these values is important for understanding:

- How a box plot is constructed
- How the box represents the middle 50% of the data
- How whiskers are determined
- How potential outliers are identified

---

## 12. Complete Example

```python
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


marks = [
    45, 32, 56, 75, 89, 54, 32, 89,
    90, 87, 67, 54, 45, 98, 99, 67, 74
]


# Five-number summary
minimum, q1, median, q3, maximum = np.quantile(
    marks,
    [0, 0.25, 0.50, 0.75, 1.0]
)


# Interquartile Range
IQR = q3 - q1


# Fences
lower_fence = q1 - 1.5 * IQR
upper_fence = q3 + 1.5 * IQR


# Display statistics
print("Minimum:", minimum)
print("Q1:", q1)
print("Median:", median)
print("Q3:", q3)
print("Maximum:", maximum)
print("IQR:", IQR)
print("Lower Fence:", lower_fence)
print("Upper Fence:", upper_fence)


# Create box plot
sns.boxplot(x=marks)

plt.show()
```

---

## 13. Quick Revision

### Five-Number Summary

```text
Minimum, Q1, Median, Q3, Maximum
```

### Q1

```text
25th percentile
```

### Median

```text
50th percentile
```

### Q3

```text
75th percentile
```

### IQR

```text
IQR = Q3 − Q1
```

### Lower Fence

```text
Lower Fence = Q1 − 1.5 × IQR
```

### Upper Fence

```text
Upper Fence = Q3 + 1.5 × IQR
```

### Potential Outlier

```text
Below Lower Fence → Potential Outlier
Above Upper Fence → Potential Outlier
```

### Python

Calculate quantiles:

```python
np.quantile()
```

Create a box plot:

```python
sns.boxplot()
```

---

## 14. Key Takeaways

- A **box plot** summarizes the distribution of numerical data.
- The **five-number summary** consists of Minimum, Q1, Median, Q3, and Maximum.
- **Q1** represents the 25th percentile.
- **Median** represents the 50th percentile.
- **Q3** represents the 75th percentile.
- **IQR = Q3 − Q1** represents the spread of the middle 50% of the data.
- The **1.5 × IQR rule** is commonly used to identify potential outliers.
- Seaborn can automatically calculate and visualize the required statistics.
- In a standard box plot, whiskers generally extend to the most extreme **non-outlier** observations rather than necessarily reaching the absolute minimum and maximum.
