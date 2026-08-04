# Measures of Dispersion

## Overview

Measures of Dispersion are statistical techniques used to measure how spread out data points are around their central value (mean).

While Measures of Central Tendency (Mean, Median, and Mode) describe the center of a dataset, Measures of Dispersion describe the variability or spread within the dataset.

The two most common measures of dispersion are:

- Variance
- Standard Deviation

This chapter focuses on **Variance**, which forms the foundation for understanding Standard Deviation.

---

# Why Do We Need Measures of Dispersion?

Consider the following two datasets:

**Distribution 1**

```text
2, 2, 4, 4
```

**Distribution 2**

```text
1, 1, 5, 5
```

The mean of both datasets is:

```text
(2 + 2 + 4 + 4) / 4 = 3

(1 + 1 + 5 + 5) / 4 = 3
```

Both datasets have the same mean:

```text
Mean = 3
```

However, they are clearly different.

- Distribution 1 is closely clustered around the mean.
- Distribution 2 is more spread out.

Therefore, the mean alone cannot fully describe the data.

Measures of Dispersion help quantify this spread.

---

# Variance

## Definition

Variance measures the average squared distance of each observation from the mean.

A larger variance indicates greater variability.

A smaller variance indicates that observations are closer to the mean.

---

# Interpretation

```text
Higher Variance

↓

Greater Spread

↓

More Variability
```

```text
Lower Variance

↓

Less Spread

↓

More Consistent Data
```

---

# Population Variance

Population Variance is represented by:

```text
σ² (Sigma Squared)
```

Formula

```text
            Σ (Xi − μ)²
σ² =  -----------------------
                N
```

Where:

- σ² = Population Variance
- Xi = Observation
- μ = Population Mean
- N = Population Size

---

# Example 1

Dataset

```text
2, 2, 4, 4
```

### Step 1

Calculate the Mean.

```text
μ = (2 + 2 + 4 + 4) / 4

μ = 3
```

---

### Step 2

Calculate the squared deviations.

| Xi | μ | (Xi − μ)² |
|---:|---:|---:|
|2|3|1|
|2|3|1|
|4|3|1|
|4|3|1|

---

### Step 3

Sum the squared deviations.

```text
1 + 1 + 1 + 1 = 4
```

---

### Step 4

Divide by N.

```text
Variance = 4 / 4

Variance = 1
```

Result

```text
σ² = 1
```

---

# Example 2

Dataset

```text
1, 1, 5, 5
```

### Step 1

Mean

```text
μ = 3
```

---

### Step 2

Squared deviations.

| Xi | μ | (Xi − μ)² |
|---:|---:|---:|
|1|3|4|
|1|3|4|
|5|3|4|
|5|3|4|

---

### Step 3

Sum

```text
4 + 4 + 4 + 4 = 16
```

---

### Step 4

Divide by N.

```text
Variance = 16 / 4

Variance = 4
```

Result

```text
σ² = 4
```

---

# Interpretation

Dataset 1

```text
Variance = 1
```

Dataset 2

```text
Variance = 4
```

Since

```text
4 > 1
```

Dataset 2 is much more spread out.

---

# Sample Variance

When working with a sample rather than the entire population, Sample Variance is used.

Sample Variance is represented by:

```text
s²
```

Formula

```text
            Σ (Xi − X̄)²
s² = --------------------------
             n − 1
```

Where

- s² = Sample Variance
- X̄ = Sample Mean
- n = Sample Size

---

# Population vs Sample Variance

| Population Variance | Sample Variance |
|---------------------|-----------------|
| Uses μ | Uses X̄ |
| Divide by N | Divide by n − 1 |
| Entire population | Sample only |

---

# Why Square the Differences?

Variance uses squared differences because:

- Positive and negative deviations cancel each other.
- Squaring makes every deviation positive.
- Larger deviations receive greater emphasis.

---

# Variance Summary

## Low Variance

```text
2, 2, 4, 4

Variance = 1
```

The observations are close to the mean.

---

## High Variance

```text
1, 1, 5, 5

Variance = 4
```

The observations are farther from the mean.

---

# Symbols

| Symbol | Meaning |
|---------|---------|
| μ | Population Mean |
| X̄ | Sample Mean |
| σ² | Population Variance |
| s² | Sample Variance |
| N | Population Size |
| n | Sample Size |

---

# Applications

Variance is widely used in:

- Machine Learning
- Data Science
- Risk Analysis
- Financial Modeling
- Statistical Analysis
- Scientific Research
- Quality Control

---

# Interview Questions

### What is Variance?

Variance is a measure of dispersion that quantifies how far observations are spread around the mean.

---

### Why do we square the differences?

To prevent positive and negative deviations from cancelling each other and to emphasize larger deviations.

---

### Why is Variance important?

Two datasets can have the same mean but completely different variability.

Variance helps distinguish between them.

---

### What is the difference between Population Variance and Sample Variance?

Population Variance divides by **N**, whereas Sample Variance divides by **n − 1**.

---

# Key Takeaways

- Measures of Dispersion describe the spread of data.
- Variance measures the average squared distance from the mean.
- Higher variance indicates greater variability.
- Lower variance indicates more consistent observations.
- Population Variance uses **N**.
- Sample Variance uses **n − 1**.
- Variance is fundamental to many Machine Learning and Data Science algorithms.

---

# What's Next?

In the next chapter, we'll study **Standard Deviation**, which is the square root of Variance and provides a more interpretable measure of dispersion.