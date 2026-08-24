# Standard Normal Distribution

## Overview

The **Standard Normal Distribution** is a special case of the **Normal (Gaussian) Distribution** with:

$$
\mu = 0
$$

and

$$
\sigma = 1
$$

It is commonly represented by the random variable:

$$
Z \sim N(0,1)
$$

The transformation used to convert an observation into a standardized value is called the **Z-score** or **standard score**.

---

## Definition

A Standard Normal Distribution is a Normal Distribution whose:

- Mean = `0`
- Standard Deviation = `1`
- Variance = `1`

Therefore:

$$
Z \sim N(0,1)
$$

It is a **continuous probability distribution** and uses a **Probability Density Function (PDF)**.

---

## Why Do We Need the Standard Normal Distribution?

Different datasets can have:

- Different means
- Different standard deviations
- Different units
- Different numerical scales

For example:

| Feature | Unit |
|---|---|
| Age | Years |
| Height | Centimeters |
| Weight | Kilograms |
| Salary | Rupees / Dollars |

A value of `70` could mean 70 kg, 70 years, or ₹70, depending on the feature.

Standardization converts values to a common scale based on their distance from the feature's mean.

---

# Z-Score

The **Z-score** tells us how many standard deviations an observation is away from the mean.

The formula is:

$$
Z = \frac{X-\mu}{\sigma}
$$

where:

- $X$ = Observed data value
- $\mu$ = Mean
- $\sigma$ = Standard deviation
- $Z$ = Z-score

---

## Interpretation of Z-Score

### Z = 0

The value is exactly at the mean.

### Z > 0

The value is above the mean.

### Z < 0

The value is below the mean.

### Larger |Z|

A larger absolute Z-score means the observation is farther from the mean.

For example:

$$
Z=2
$$

means the observation is **2 standard deviations above the mean**.

Similarly:

$$
Z=-1.5
$$

means the observation is **1.5 standard deviations below the mean**.

---

# Example 1

Suppose:

- Mean = `4`
- Standard deviation = `1`
- Data value = `4.25`

Using:

$$
Z = \frac{X-\mu}{\sigma}
$$

we get:

$$
Z = \frac{4.25-4}{1}
$$

$$
Z=0.25
$$

### Interpretation

The value `4.25` is **0.25 standard deviations above the mean**.

---

# Example 2

Suppose:

- Mean = `4`
- Standard deviation = `1`
- Data value = `2.5`

Then:

$$
Z = \frac{2.5-4}{1}
$$

$$
Z=-1.5
$$

### Interpretation

The value `2.5` is **1.5 standard deviations below the mean**.

---

# Converting Values to Z-Scores

Suppose we have:

```text
1   2   3   4   5
```

with:

```text
Mean = 3
Standard Deviation = 1
```

Applying:

$$
Z = \frac{X-\mu}{\sigma}
$$

gives:

```text
X:  1   2   3   4   5

Z: -2  -1   0   1   2
```

The transformed values have:

```text
Mean = 0
Standard Deviation = 1
```

This is the essence of **standardization**.

> Important: Standardization makes the mean 0 and standard deviation 1, but it does **not** make a non-Normal dataset Normal.

---

# Standardization

**Standardization** is the process of transforming numerical features so that they have:

$$
\text{Mean} = 0
$$

and:

$$
\text{Standard Deviation} = 1
$$

The transformation is:

$$
Z = \frac{X-\mu}{\sigma}
$$

This is also called **Z-score standardization**.

---

## Example

Suppose a feature contains:

```text
10, 20, 30, 40, 50
```

After calculating its mean and standard deviation, each observation can be transformed into its corresponding Z-score.

The resulting feature will have approximately:

```text
Mean = 0
Standard Deviation = 1
```

---

# Why Is Standardization Useful?

Real-world datasets often contain features with very different scales.

For example:

| Feature | Example Scale |
|---|---|
| Age | 20–60 |
| Height | 140–200 |
| Salary | 20,000–200,000 |
| Experience | 0–30 |

Without scaling, algorithms that depend on distances or gradient-based optimization may be affected by these different scales.

Standardization can:

- Make numerical features comparable.
- Prevent large-scale features from dominating distance calculations.
- Improve optimization and convergence in many models.
- Make some model coefficients easier to compare.
- Improve the numerical stability of certain algorithms.

---

# Machine Learning Algorithms and Standardization

Standardization is especially useful for algorithms that are sensitive to feature scale.

Examples include:

- K-Means Clustering
- K-Nearest Neighbors (KNN)
- Support Vector Machines (SVM)
- Logistic Regression
- Linear Regression
- Principal Component Analysis (PCA)
- Neural Networks

### Important Note

These algorithms do not all **require** standardization.

For example, Linear Regression can mathematically work without scaling.

However, standardization can still be useful for:

- Gradient-based optimization
- Comparing feature coefficients
- Improving numerical behavior

Distance-based algorithms such as K-Means and KNN are particularly sensitive to feature scale.

---

# Standardization vs Normalization

Standardization and normalization are not the same thing.

### Standardization

Uses:

$$
Z = \frac{X-\mu}{\sigma}
$$

and produces:

```text
Mean ≈ 0
Standard Deviation ≈ 1
```

### Min-Max Normalization

A common normalization method transforms values to a fixed range, often `[0, 1]`:

$$
X' = \frac{X-X_{\min}}{X_{\max}-X_{\min}}
$$

The choice between standardization and normalization depends on the dataset and algorithm.

---

# Standard Normal Distribution

After standardization, if the original variable is normally distributed:

$$
X \sim N(\mu,\sigma^2)
$$

then its standardized version:

$$
Z = \frac{X-\mu}{\sigma}
$$

follows:

$$
Z \sim N(0,1)
$$

This is the **Standard Normal Distribution**.

---

# Standard Normal Distribution vs Normal Distribution

| Feature | Normal Distribution | Standard Normal Distribution |
|---|---|---|
| Mean | Any value $\mu$ | 0 |
| Standard Deviation | Any $\sigma > 0$ | 1 |
| Variance | $\sigma^2$ | 1 |
| Shape | Bell-shaped | Bell-shaped |
| Distribution | Continuous | Continuous |
| PDF | Yes | Yes |
| Z-score | Not necessarily standardized | Standardized |

The Standard Normal Distribution is therefore a **specific Normal Distribution**, not a completely different family of distributions.

---

# Standard Normal Distribution and Z-Scores

Consider:

$$
X \sim N(100,10^2)
$$

For an observation:

$$
X=120
$$

the Z-score is:

$$
Z = \frac{120-100}{10}
$$

$$
Z=2
$$

Therefore, `120` is **2 standard deviations above the mean**.

---

# Probability and Z-Scores

Z-scores allow us to convert observations from different Normal Distributions to the common Standard Normal scale.

For example:

$$
P(X \le x)
$$

can be transformed into:

$$
P(Z \le z)
$$

where:

$$
z = \frac{x-\mu}{\sigma}
$$

Statistical software can then calculate the corresponding probability using the Standard Normal CDF.

---

# Typical Z-Score Range

For data that is approximately Normally distributed:

- About 68% lies between `-1` and `+1`.
- About 95% lies between `-2` and `+2`.
- About 99.7% lies between `-3` and `+3`.

Therefore, values outside:

$$
-3 \le Z \le 3
$$

may be unusual under a Normal model.

However:

> A Z-score outside `[-3, 3]` does **not automatically mean that the observation is an outlier**.

The distribution of the data and the application context must also be considered.

---

# Applications

Standardization and Z-scores are used in:

- Data Preprocessing
- Feature Scaling
- Exploratory Data Analysis
- Outlier Analysis
- Statistical Analysis
- Machine Learning
- Distance-Based Algorithms
- Gradient-Based Optimization
- Principal Component Analysis

---

# Key Takeaways

- Standard Normal Distribution is a special case of the Normal Distribution.
- It has:

$$
\mu = 0,\qquad \sigma = 1
$$

- Its variance is therefore:

$$
\sigma^2 = 1
$$

- The Z-score formula is:

$$
Z = \frac{X-\mu}{\sigma}
$$

- Positive Z → Above the mean.
- Negative Z → Below the mean.
- Z = 0 → Exactly at the mean.
- Larger `|Z|` → Farther from the mean.
- Standardization converts features to a common scale.
- Standardization does **not** automatically make data Normally distributed.
- For approximately Normal data, most observations lie between approximately `-3` and `+3`.
- Standardization is particularly useful for scale-sensitive Machine Learning algorithms.

---

# Interview Questions

1. What is a Standard Normal Distribution?
2. What are the mean and standard deviation of a Standard Normal Distribution?
3. What is a Z-score?
4. Write the Z-score formula.
5. What does a positive Z-score indicate?
6. What does a negative Z-score indicate?
7. What does `Z = 0` mean?
8. What does `Z = 2` mean?
9. Why is standardization useful in Machine Learning?
10. Which Machine Learning algorithms are sensitive to feature scale?
11. What is the difference between standardization and normalization?
12. Does standardization make data Normally distributed?
13. What is the relationship between a Normal Distribution and a Standard Normal Distribution?
14. Why can values beyond ±3 be considered unusual for approximately Normal data?
15. What happens to the mean and standard deviation after Z-score standardization?

---

# Quick Revision

### Standard Normal Distribution

$$
\mu = 0,\qquad \sigma = 1
$$

### Z-Score

$$
Z = \frac{X-\mu}{\sigma}
$$

### Interpretation

```text
Z > 0  → Above the mean
Z < 0  → Below the mean
Z = 0  → At the mean
```

### Standardization

```text
Original Feature
       ↓
Calculate Mean and Standard Deviation
       ↓
Z = (X - μ) / σ
       ↓
Standardized Feature
       ↓
Mean ≈ 0
Standard Deviation ≈ 1
```
