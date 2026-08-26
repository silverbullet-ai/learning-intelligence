# Log-Normal Distribution

## Overview

A **Log-Normal Distribution** is a continuous probability distribution in which the **natural logarithm of the random variable follows a Normal Distribution**.

In simple terms, if:

$$
Y=\ln(X)
$$

and $Y$ follows a Normal Distribution, then $X$ follows a Log-Normal Distribution.

The relationship can be written as:

$$
Y=\ln(X)\sim N(\mu,\sigma^2)
$$

then:

$$
X\sim \operatorname{LogNormal}(\mu,\sigma^2)
$$

---

# Definition

A random variable $X$ follows a Log-Normal Distribution if its natural logarithm is Normally distributed.

That is:

$$
\ln(X)\sim N(\mu,\sigma^2)
$$

Equivalently:

$$
X=e^Y
$$

where:

$$
Y\sim N(\mu,\sigma^2)
$$

---

# Key Relationship

## Case 1 — Log-Normal to Normal

If:

$$
X\sim \operatorname{LogNormal}(\mu,\sigma^2)
$$

then:

$$
Y=\ln(X)
$$

follows:

$$
Y\sim N(\mu,\sigma^2)
$$

---

## Case 2 — Normal to Log-Normal

If:

$$
Y\sim N(\mu,\sigma^2)
$$

then:

$$
X=e^Y
$$

follows a Log-Normal Distribution:

$$
X\sim \operatorname{LogNormal}(\mu,\sigma^2)
$$

---

# Type

- Continuous Probability Distribution
- Continuous Random Variable
- Uses a **Probability Density Function (PDF)**

---

# Support

A Log-Normal random variable can only take **positive values**:

$$
X>0
$$

Therefore:

$$
P(X\leq0)=0
$$

This happens because:

$$
X=e^Y
$$

and the exponential function is always positive.

---

# Shape

The Log-Normal Distribution is typically:

- Right-skewed
- Asymmetric
- Positively valued
- Characterized by a long right tail

A typical shape looks approximately like:

```text
Probability Density
       |
       |       /\\
       |      /  \\
       |     /    \\
       |____/      \\________________
       |
       +--------------------------------> X
                         Long Right Tail
```

Unlike the Normal Distribution, the Log-Normal Distribution is **not symmetric**.

---

# Parameters

The Log-Normal Distribution is commonly represented as:

$$
X\sim\operatorname{LogNormal}(\mu,\sigma^2)
$$

where:

- $\mu$ = Mean of $\ln(X)$
- $\sigma^2$ = Variance of $\ln(X)$
- $\sigma$ = Standard deviation of $\ln(X)$

This distinction is important.

> $\mu$ and $\sigma^2$ describe the Normal Distribution of $\ln(X)$, not the arithmetic mean and variance of $X$.

---

# Probability Density Function

If:

$$
X\sim\operatorname{LogNormal}(\mu,\sigma^2)
$$

then its PDF is:

$$
f(x)=
\frac{1}{x\sigma\sqrt{2\pi}}
\exp\left(
-\frac{(\ln x-\mu)^2}{2\sigma^2}
\right)
$$

for:

$$
x>0
$$

and:

$$
f(x)=0
$$

for:

$$
x\leq0
$$

For learning and interviews, understanding the transformation and interpretation is generally more important than memorizing this formula.

---

# Transformation

The relationship between Normal and Log-Normal Distributions can be understood through two transformations.

## Log Transformation

```text
Log-Normal Distribution
          |
       ln(X)
          ↓
 Normal Distribution
```

Mathematically:

$$
Y=\ln(X)
$$

---

## Exponential Transformation

```text
Normal Distribution
          |
         e^Y
          ↓
Log-Normal Distribution
```

Mathematically:

$$
X=e^Y
$$

---

# Why Does the Log Transformation Work?

Suppose a variable $X$ has a strong right skew.

Taking the natural logarithm:

$$
Y=\ln(X)
$$

compresses large values much more than small values.

For example:

$$
\ln(10)\approx2.30
$$

while:

$$
\ln(1000)\approx6.91
$$

The large values are compressed, which can reduce right skewness and sometimes make the transformed data approximately Normal.

---

# Mean

If:

$$
\ln(X)\sim N(\mu,\sigma^2)
$$

then the arithmetic mean of $X$ is:

$$
\boxed{
E[X]=e^{\mu+\frac{\sigma^2}{2}}
}
$$

---

# Median

The median is:

$$
\boxed{
\operatorname{Median}(X)=e^\mu
}
$$

---

# Mode

The mode is:

$$
\boxed{
\operatorname{Mode}(X)=e^{\mu-\sigma^2}
}
$$

For a non-degenerate Log-Normal Distribution:

$$
\text{Mode}<\text{Median}<\text{Mean}
$$

This is consistent with its right-skewed shape.

---

# Variance

The variance is:

$$
\boxed{
\operatorname{Var}(X)
=
\left(e^{\sigma^2}-1\right)e^{2\mu+\sigma^2}
}
$$

---

# Standard Deviation

The standard deviation is:

$$
\boxed{
\sigma_X
=
\sqrt{
\left(e^{\sigma^2}-1\right)e^{2\mu+\sigma^2}
}
}
$$

Note that $\sigma_X$ is the standard deviation of $X$.

It is different from $\sigma$, which is the standard deviation of $\ln(X)$.

---

# Example

Suppose:

$$
Y\sim N(2,0.5^2)
$$

and:

$$
X=e^Y
$$

Then $X$ follows a Log-Normal Distribution:

$$
X\sim\operatorname{LogNormal}(2,0.5^2)
$$

---

## Mean

$$
E[X]
=
e^{2+\frac{0.5^2}{2}}
$$

$$
=e^{2.125}
$$

$$
\approx8.37
$$

---

## Median

$$
\operatorname{Median}(X)=e^2
$$

$$
\approx7.39
$$

Notice:

$$
\text{Median}<\text{Mean}
$$

which is expected for a right-skewed distribution.

---

# Checking for a Log-Normal Distribution

A common approach is:

1. Examine the original data.
2. Apply a logarithmic transformation.
3. Examine the transformed data.
4. Use a Q-Q plot to compare the transformed data with a Normal Distribution.

If:

$$
Y=\ln(X)
$$

is approximately Normally distributed, then $X$ may reasonably be modeled as Log-Normal.

### Important

A Q-Q plot is a **diagnostic tool**, not absolute proof that a dataset follows a Log-Normal Distribution.

Other statistical tests and domain knowledge may also be useful.

---

# Real-World Applications

A Log-Normal Distribution can be useful for variables that:

- Are strictly positive
- Are strongly right-skewed
- Result from multiplicative processes

Examples include:

### Income and Wealth

Income and wealth distributions can sometimes be modeled approximately using Log-Normal or related heavy-tailed distributions.

### Dwell Time

Time spent by users on websites, articles, or applications can sometimes exhibit strong right skewness.

### Biological Measurements

Some biological measurements involving multiplicative growth processes may be approximately Log-Normal.

### Environmental Measurements

Certain positive environmental measurements can sometimes be modeled using Log-Normal distributions.

### Financial and Economic Variables

Some positive-valued economic quantities may be modeled approximately using Log-Normal distributions.

> The Log-Normal model is an approximation. Real-world datasets do not automatically follow a Log-Normal Distribution just because they are right-skewed.

---

# Normal vs Log-Normal Distribution

| Feature | Normal Distribution | Log-Normal Distribution |
|---|---|---|
| Type | Continuous | Continuous |
| Shape | Bell-shaped | Right-skewed |
| Symmetry | Symmetric | Asymmetric |
| Support | $-\infty < x < \infty$ | $x>0$ |
| Function | PDF | PDF |
| Transformation | Original scale | $\ln(X)$ is Normal |
| Mean = Median = Mode | Yes | No |
| Right tail | Balanced | Long right tail |

---

# Log Transformation vs Standardization

These two concepts are related to preprocessing but are **not the same operation**.

## Log Transformation

Transforms:

$$
X\rightarrow\ln(X)
$$

It is often used to reduce right skewness.

---

## Standardization

Transforms:

$$
X\rightarrow\frac{X-\mu}{\sigma}
$$

It changes the scale so that the transformed variable has mean approximately 0 and standard deviation approximately 1.

Therefore:

> **Log transformation changes the distribution's shape/skewness.**

> **Standardization changes the scale.**

---

# Applications in Data Science

Understanding Log-Normal Distributions is useful in:

- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Transformation
- Outlier Analysis
- Statistical Modeling
- Machine Learning preprocessing

A common workflow is:

```text
Original Feature
      |
      | Check distribution
      ↓
Strong Right Skew
      |
      | Apply log transformation
      ↓
ln(X)
      |
      | Check distribution
      ↓
Approximately Normal
```

---

# Key Takeaways

- Log-Normal Distribution is a **continuous probability distribution**.
- A Log-Normal random variable must satisfy:

$$
X>0
$$

- If:

$$
\ln(X)\sim N(\mu,\sigma^2)
$$

then:

$$
X\sim\operatorname{LogNormal}(\mu,\sigma^2)
$$

- It is generally **right-skewed**.
- The logarithm transforms a Log-Normal variable into a Normal variable.
- The exponential transformation converts a Normal variable into a Log-Normal variable.
- Q-Q plots can help diagnose whether log-transformed data is approximately Normal.
- Real-world datasets should not automatically be assumed to be Log-Normal simply because they are right-skewed.

---

# Interview Questions

1. What is a Log-Normal Distribution?
2. Why is it called "Log-Normal"?
3. Is a Log-Normal Distribution discrete or continuous?
4. What is the relationship between Normal and Log-Normal Distributions?
5. What transformation converts a Log-Normal variable into a Normal variable?
6. What transformation converts a Normal variable into a Log-Normal variable?
7. Why is a Log-Normal Distribution right-skewed?
8. Why can a Log-Normal random variable not be negative?
9. What are the parameters of a Log-Normal Distribution?
10. What is the PDF of a Log-Normal Distribution?
11. What is the median of a Log-Normal Distribution?
12. Why is the mean greater than the median for a Log-Normal Distribution?
13. How can you check whether data may follow a Log-Normal Distribution?
14. What is the difference between log transformation and standardization?
15. Give some real-world applications of the Log-Normal Distribution.

---

# Quick Revision

## Log-Normal Distribution

$$
X\sim\operatorname{LogNormal}(\mu,\sigma^2)
$$

if:

$$
\ln(X)\sim N(\mu,\sigma^2)
$$

### Transformation

$$
Y=\ln(X)
$$

### Reverse Transformation

$$
X=e^Y
$$

### Support

$$
X>0
$$

### Shape

**Right-skewed**

### Mean

$$
E[X]=e^{\mu+\frac{\sigma^2}{2}}
$$

### Median

$$
\operatorname{Median}(X)=e^\mu
$$

### Mode

$$
\operatorname{Mode}(X)=e^{\mu-\sigma^2}
$$

### Variance

$$
\operatorname{Var}(X)
=
\left(e^{\sigma^2}-1\right)e^{2\mu+\sigma^2}
$$

### Core Idea

> **Log-Normal → take $\ln$ → Normal**

> **Normal → take $e^x$ → Log-Normal**
