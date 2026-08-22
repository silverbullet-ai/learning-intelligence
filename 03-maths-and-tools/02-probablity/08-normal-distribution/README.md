# Normal (Gaussian) Distribution

## Overview

The **Normal Distribution**, also called the **Gaussian Distribution**, is one of the most important continuous probability distributions in statistics and machine learning.

It describes data that is distributed symmetrically around a central value, producing the familiar **bell-shaped curve**.

The Normal Distribution is widely used in:

- Statistics
- Data Analysis
- Machine Learning
- Data Visualization
- Feature Analysis
- Quality Control
- Research

---

## Definition

A **Normal (Gaussian) Distribution** is a continuous probability distribution for a continuous random variable where the data is distributed symmetrically around the mean.

It is represented as:

$$
X \sim N(\mu, \sigma^2)
$$

where:

- $\mu$ = Mean
- $\sigma^2$ = Variance
- $\sigma$ = Standard Deviation

---

## Type

- **Continuous Probability Distribution**
- Used for **Continuous Random Variables**
- Uses **Probability Density Function (PDF)**

---

## Characteristics

A Normal Distribution has the following characteristics:

- Bell-shaped curve
- Symmetric about the mean
- Continuous distribution
- Mean = Median = Mode
- Total area under the curve = 1
- 50% of the probability lies on each side of the mean

---

## Important Property

For a Normal Distribution:

$$
\text{Mean} = \text{Median} = \text{Mode}
$$

This happens because the distribution is perfectly symmetric around the mean.

---

## Parameters

A Normal Distribution is defined by two parameters:

### Mean ($\mu$)

The mean determines the **center** of the distribution.

Changing $\mu$ shifts the entire bell curve left or right.

### Variance ($\sigma^2$)

Variance determines how spread out the distribution is.

A larger variance produces a wider and flatter curve.

A smaller variance produces a narrower and taller curve.

### Standard Deviation ($\sigma$)

Standard deviation is the square root of variance:

$$
\sigma = \sqrt{\sigma^2}
$$

It represents the typical spread of observations around the mean.

---

## Probability Density Function (PDF)

The PDF of a Normal Distribution is:

$$
f(x) =
\frac{1}{\sigma\sqrt{2\pi}}
e^{-\frac{(x-\mu)^2}{2\sigma^2}}
$$

where:

- $x$ = Continuous random variable
- $\mu$ = Mean
- $\sigma$ = Standard deviation
- $\sigma^2$ = Variance
- $\pi \approx 3.14159$
- $e \approx 2.71828$

The PDF describes the **density of probability** at different values of $x$.

> **Note:** For interviews, understand what the formula represents. There is usually no need to memorize the complete formula because statistical libraries calculate it directly.

---

## Probability and Area Under the Curve

For a continuous random variable, probability is represented by the **area under the PDF curve**.

For example:

$$
P(a \leq X \leq b)
$$

represents the area under the Normal Distribution curve between $a$ and $b$.

The total area under the curve is always:

$$
\int_{-\infty}^{\infty} f(x)\,dx = 1
$$

Therefore, the total probability is always 1.

---

## Effect of Variance

Variance controls the spread of the Normal Distribution.

### Large Variance

When variance increases:

- Data becomes more spread out.
- The bell curve becomes wider.
- The curve becomes flatter.

### Small Variance

When variance decreases:

- Data becomes more concentrated around the mean.
- The bell curve becomes narrower.
- The curve becomes taller.

---

## Effect of Mean

The mean controls the **location** of the distribution.

For example:

$$
N(0,1)
$$

has mean $0$.

If we change the mean:

$$
N(5,1)
$$

the curve shifts to the right while maintaining the same spread.

Therefore:

> **Mean controls location, while variance controls spread.**

---

# Empirical Rule

The **68–95–99.7 Rule** describes how data is distributed around the mean in a Normal Distribution.

---

## Within 1 Standard Deviation

Approximately **68%** of the data lies between:

$$
\mu-\sigma
\leq X \leq
\mu+\sigma
$$

Therefore:

$$
P(\mu-\sigma \leq X \leq \mu+\sigma)
\approx 0.68
$$

---

## Within 2 Standard Deviations

Approximately **95%** of the data lies between:

$$
\mu-2\sigma
\leq X \leq
\mu+2\sigma
$$

Therefore:

$$
P(\mu-2\sigma \leq X \leq \mu+2\sigma)
\approx 0.95
$$

---

## Within 3 Standard Deviations

Approximately **99.7%** of the data lies between:

$$
\mu-3\sigma
\leq X \leq
\mu+3\sigma
$$

Therefore:

$$
P(\mu-3\sigma \leq X \leq \mu+3\sigma)
\approx 0.997
$$

---

## Empirical Rule Summary

| Range | Approximate Percentage |
|---|---:|
| $\mu \pm 1\sigma$ | 68% |
| $\mu \pm 2\sigma$ | 95% |
| $\mu \pm 3\sigma$ | 99.7% |

---

## Probability Interpretation

Suppose:

$$
\mu = 100
$$

and

$$
\sigma = 10
$$

Then:

### Within 1 Standard Deviation

$$
100-10 \leq X \leq 100+10
$$

$$
90 \leq X \leq 110
$$

Approximately **68%** of observations lie between 90 and 110.

### Within 2 Standard Deviations

$$
80 \leq X \leq 120
$$

Approximately **95%** of observations lie between 80 and 120.

### Within 3 Standard Deviations

$$
70 \leq X \leq 130
$$

Approximately **99.7%** of observations lie between 70 and 130.

---

# Standard Normal Distribution

A special case of the Normal Distribution is the **Standard Normal Distribution**.

It has:

$$
\mu = 0
$$

and

$$
\sigma = 1
$$

Therefore:

$$
X \sim N(0,1)
$$

The corresponding random variable is commonly represented using:

$$
Z
$$

and is called the **Z-score** or **standard score**.

---

## Z-Score

A Z-score tells us how many standard deviations a value is away from the mean.

The formula is:

$$
Z = \frac{X-\mu}{\sigma}
$$

where:

- $X$ = Observed value
- $\mu$ = Mean
- $\sigma$ = Standard deviation
- $Z$ = Standardized value

### Interpretation

If:

$$
Z=0
$$

the observation is exactly at the mean.

If:

$$
Z=1
$$

the observation is one standard deviation above the mean.

If:

$$
Z=-2
$$

the observation is two standard deviations below the mean.

---

# Real-Life Examples

Many real-world measurements can approximately follow a Normal Distribution.

Examples include:

- Heights of students
- Weights of people
- Measurement errors
- Manufacturing measurements
- Test scores under certain conditions
- Biological measurements

### Iris Dataset

Some numerical features in the Iris dataset can be analyzed using Normal Distribution concepts:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

However, not every real-world dataset or feature follows a Normal Distribution exactly.

---

# Applications

Normal Distribution is widely used in:

### Data Analysis

Understanding the distribution and spread of numerical features.

### Machine Learning

Used in:

- Statistical assumptions
- Feature analysis
- Standardization
- Gaussian-based models
- Probabilistic modeling

### Quality Control

Detecting unusually high or low measurements.

### Statistics

Used extensively in:

- Confidence intervals
- Hypothesis testing
- Sampling theory
- Statistical inference

---

# Normal Distribution and Outliers

The Normal Distribution can also help identify unusual observations.

Using the empirical rule:

- Values beyond approximately $\mu \pm 2\sigma$ are relatively uncommon.
- Values beyond approximately $\mu \pm 3\sigma$ are very uncommon under a Normal model.

However, this should not automatically mean that every observation beyond 3 standard deviations is an error or an outlier.

Context matters.

---

# Quick Revision

| Property | Description |
|---|---|
| Type | Continuous |
| Random Variable | Continuous |
| Function | PDF |
| Shape | Bell-shaped |
| Symmetry | Symmetric |
| Mean | $\mu$ |
| Variance | $\sigma^2$ |
| Standard Deviation | $\sigma$ |
| Relationship | Mean = Median = Mode |
| Total Area | 1 |
| 1 Standard Deviation | 68% |
| 2 Standard Deviations | 95% |
| 3 Standard Deviations | 99.7% |

---

# Key Takeaways

- **Normal Distribution** is a continuous probability distribution.
- It has a **bell-shaped and symmetric curve**.
- It is represented as:

$$
X \sim N(\mu,\sigma^2)
$$

- $\mu$ controls the **center/location**.
- $\sigma^2$ controls the **spread**.
- $\sigma$ represents the standard deviation.
- Mean = Median = Mode.
- Total area under the PDF is 1.
- Approximately **68%** of observations lie within $\pm1\sigma$.
- Approximately **95%** lie within $\pm2\sigma$.
- Approximately **99.7%** lie within $\pm3\sigma$.
- The Standard Normal Distribution has $\mu=0$ and $\sigma=1$.
- Z-score standardizes observations using:

$$
Z = \frac{X-\mu}{\sigma}
$$

---

# Interview Questions

1. What is a Normal Distribution?
2. Is Normal Distribution discrete or continuous?
3. Why does Normal Distribution use a PDF?
4. What are the parameters of a Normal Distribution?
5. What is the relationship between Mean, Median, and Mode?
6. What happens when variance increases?
7. What happens when variance decreases?
8. Explain the 68–95–99.7 rule.
9. What is a Standard Normal Distribution?
10. What is a Z-score?
11. What does a Z-score of 2 mean?
12. What is the difference between variance and standard deviation?
13. Why is Normal Distribution important in Machine Learning?
14. Give some real-world examples of approximately Normal data.
15. What does the area under a Normal Distribution curve represent?

---

## Related Topics

This topic connects directly to:

- Probability Distribution Functions
- Standard Normal Distribution
- Z-Score
- Central Limit Theorem
- Sampling Distributions
- Inferential Statistics
- Hypothesis Testing
- Confidence Intervals