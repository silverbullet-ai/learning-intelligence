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

# Why Do We Divide Sample Variance by (n − 1)?

One of the most common interview questions in Statistics is:

> **Why do we divide Sample Variance by (n − 1) instead of n?**

The answer lies in the fact that a **sample is only an estimate of the population**, not the complete dataset.

---

## Understanding the Problem

Suppose we have a very large population.

```text
Population
┌───────────────────────────┐
│ Thousands of observations │
└───────────────────────────┘
```

Instead of collecting every observation, we select a sample.

```text
Population

        ↓

Sample
```

The goal is to estimate:

- Population Mean (μ)
- Population Variance (σ²)

using only the sample.

---

## Case 1: A Good Random Sample

Imagine the population is evenly distributed.

```text
          Population

              μ

      . . . . | . . . .
```

Now suppose the sample is collected from all regions of the population.

```text
Sample

x   x   x   x   x
```

In this case:

```text
Sample Mean (X̄)

≈

Population Mean (μ)
```

and

```text
Sample Variance

≈

Population Variance
```

The sample provides a good estimate of the population.

---

## Case 2: A Poor Sample

Suppose the sample is collected only from one side of the population.

```text
Population

. . . . . . . . . . . . .

            μ

Sample

x x x x
```

Now,

```text
Sample Mean (X̄)

≠

Population Mean (μ)
```

Since all selected observations are close together,

```text
Sample Variance

<

Population Variance
```

The variance is underestimated.

---

## Why Dividing by n Causes Underestimation

Suppose

```text
Σ(X − X̄)² = 100

n = 10
```

Using **n**

```text
100 / 10 = 10
```

Using **n − 1**

```text
100 / 9 = 11.11
```

Notice that

```text
11.11 > 10
```

Dividing by **n − 1** produces a slightly larger estimate that compensates for the tendency of samples to underestimate the true population variance.

This adjustment is known as **Bessel's Correction**.

---

# Bessel's Correction

Using

```text
n − 1
```

instead of

```text
n
```

when calculating Sample Variance is called **Bessel's Correction**.

Its purpose is to provide a less biased estimate of the population variance.

---

# Degree of Freedom (DOF)

Another way interviewers explain this concept is using **Degrees of Freedom**.

For Sample Variance,

```text
DOF = n − 1
```

### Why?

Suppose:

```text
Sample Size = 4

Mean = 10
```

Three observations are:

```text
8

10

12
```

Their total is:

```text
30
```

Since the total of all observations must be:

```text
40
```

the fourth observation must be:

```text
10
```

Only **three values were free to vary**.

Therefore,

```text
DOF = 4 − 1 = 3
```

---

# Population vs Sample Variance (Quick Recap)

| Population Variance | Sample Variance |
|---------------------|-----------------|
| Uses μ | Uses X̄ |
| Divide by N | Divide by n − 1 |
| Exact variance | Estimate of variance |
| No correction required | Uses Bessel's Correction |

---

# Memory Trick

```text
Population knows everything

↓

Divide by N
```

```text
Sample only estimates

↓

Divide by n − 1
```

---

# Interview Question

### Why do we divide Sample Variance by (n − 1) instead of n?

Using **n** tends to underestimate the true population variance because the sample mean is calculated from the same sample.

Dividing by **n − 1** (Bessel's Correction) compensates for this bias and produces a better estimate of the population variance.

The quantity **n − 1** is also known as the **Degree of Freedom (DOF)**.

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