# Covariance and Correlation

## Overview

Covariance and Correlation are statistical measures used to understand the relationship between two variables.

They help answer questions such as:

- Do two variables increase together?
- Does one variable increase while the other decreases?
- How strong is their relationship?
- Is the relationship linear or monotonic?

These concepts are widely used in:

- Statistics
- Data Analysis
- Exploratory Data Analysis (EDA)
- Machine Learning
- Feature Selection
- Feature Engineering

---

# Example

Suppose we have:

- **Hours Studied**
- **Exam Score**

We may want to know:

> If Hours Studied increases, does Exam Score also increase?

Covariance and Correlation help quantify this relationship.

---

# Covariance

## Definition

**Covariance** measures how two variables change together.

If:

```text
X increases → Y increases
```

the covariance is generally positive.

If:

```text
X increases → Y decreases
```

the covariance is generally negative.

If the variables do not show a consistent linear tendency together, covariance may be close to zero.

---

## Types of Covariance

### Positive Covariance

Both variables tend to move in the same direction.

```text
X ↑
Y ↑
```

Example:

```text
Hours Studied ↑
Exam Score   ↑
```

Therefore:

```text
Cov(X,Y) > 0
```

---

### Negative Covariance

The variables tend to move in opposite directions.

```text
X ↑
Y ↓
```

Example:

```text
Price ↑
Demand ↓
```

Therefore:

```text
Cov(X,Y) < 0
```

---

### Covariance Near Zero

There is little or no linear tendency for the variables to move together.

Important:

> Covariance near zero does not necessarily mean that there is no relationship. A nonlinear relationship may still exist.

---

# Sample Covariance Formula

For a sample:

```text
Cov(X,Y) = Σ[(Xi - X̄)(Yi - Ȳ)] / (n - 1)
```

Where:

| Symbol | Meaning |
|---|---|
| `Xi` | Individual observation of X |
| `Yi` | Individual observation of Y |
| `X̄` | Sample mean of X |
| `Ȳ` | Sample mean of Y |
| `n` | Sample size |

---

# Understanding the Formula

The formula calculates:

```text
(Xi - X̄)
```

which represents the deviation of X from its mean.

Similarly:

```text
(Yi - Ȳ)
```

represents the deviation of Y from its mean.

The deviations are multiplied:

```text
(Xi - X̄)(Yi - Ȳ)
```

Then the products are summed and divided by:

```text
n - 1
```

---

# Positive Covariance Example

Consider:

| X | Y |
|---:|---:|
| 2 | 3 |
| 4 | 5 |
| 6 | 7 |
| 8 | 9 |

As X increases:

```text
X ↑ → Y ↑
```

Therefore:

```text
Covariance > 0
```

The variables have a positive relationship.

---

# Negative Covariance Example

Consider:

| X | Y |
|---:|---:|
| 7 | 10 |
| 6 | 12 |
| 5 | 14 |
| 4 | 16 |

As X increases:

```text
X ↑ → Y ↓
```

Therefore:

```text
Covariance < 0
```

The variables have a negative relationship.

---

# Solved Covariance Example

Consider:

| Hours Studied (X) | Exam Score (Y) |
|---:|---:|
| 2 | 50 |
| 3 | 60 |
| 4 | 70 |
| 5 | 80 |
| 6 | 90 |

## Step 1: Calculate the Means

Mean of X:

```text
X̄ = (2 + 3 + 4 + 5 + 6) / 5

   = 4
```

Mean of Y:

```text
Ȳ = (50 + 60 + 70 + 80 + 90) / 5

   = 70
```

---

## Step 2: Calculate Deviations

| X | Y | X − X̄ | Y − Ȳ | Product |
|---:|---:|---:|---:|---:|
| 2 | 50 | -2 | -20 | 40 |
| 3 | 60 | -1 | -10 | 10 |
| 4 | 70 | 0 | 0 | 0 |
| 5 | 80 | 1 | 10 | 10 |
| 6 | 90 | 2 | 20 | 40 |

Sum of products:

```text
40 + 10 + 0 + 10 + 40 = 100
```

---

## Step 3: Divide by n − 1

```text
n = 5

n - 1 = 4
```

Therefore:

```text
Covariance = 100 / 4

           = 25
```

So:

```text
Cov(X,Y) = 25
```

Since covariance is positive, Hours Studied and Exam Score move in the same direction.

---

# Covariance and Variance

An important identity is:

```text
Cov(X,X) = Var(X)
```

Why?

Because:

```text
Cov(X,X)
```

becomes:

```text
Σ[(Xi - X̄)(Xi - X̄)] / (n - 1)
```

which is:

```text
Σ[(Xi - X̄)²] / (n - 1)
```

This is exactly the formula for sample variance.

Therefore:

```text
Cov(X,X) = Var(X)
```

---

# Limitation of Covariance

The major limitation of covariance is that it has **no fixed range**.

Covariance can theoretically range from:

```text
−∞ to +∞
```

Therefore, covariance values are difficult to compare directly.

For example:

```text
Cov(A,B) = 20

Cov(C,D) = 300
```

We cannot conclude that the second relationship is 15 times stronger.

The magnitude depends on the units and scale of the variables.

This is where correlation becomes useful.

---

# Correlation

## Definition

**Correlation** is a normalized measure of the relationship between two variables.

Unlike covariance, correlation always lies between:

```text
−1 and +1
```

Therefore, correlation is easier to interpret and compare.

---

# Pearson Correlation

The most common correlation measure is the:

**Pearson Correlation Coefficient**

Formula:

```text
r = Cov(X,Y) / (σX × σY)
```

Where:

| Symbol | Meaning |
|---|---|
| `Cov(X,Y)` | Covariance between X and Y |
| `σX` | Standard deviation of X |
| `σY` | Standard deviation of Y |
| `r` | Pearson correlation coefficient |

The standard deviations normalize covariance and place the result in the range:

```text
−1 ≤ r ≤ +1
```

---

# Interpreting Correlation

| Correlation | Interpretation |
|---:|---|
| +1 | Perfect positive linear relationship |
| +0.8 | Strong positive relationship |
| +0.5 | Moderate positive relationship |
| 0 | No linear relationship |
| -0.5 | Moderate negative relationship |
| -0.8 | Strong negative relationship |
| -1 | Perfect negative linear relationship |

> These values are useful guidelines rather than strict universal categories.

---

# Perfect Positive Correlation

Example:

```text
X = 1, 2, 3, 4, 5

Y = 2, 4, 6, 8, 10
```

As X increases, Y increases perfectly linearly.

Therefore:

```text
r = +1
```

---

# Perfect Negative Correlation

Example:

```text
X = 1, 2, 3, 4, 5

Y = 10, 8, 6, 4, 2
```

As X increases, Y decreases perfectly linearly.

Therefore:

```text
r = -1
```

---

# Correlation Near Zero

A Pearson correlation close to zero indicates that there is little or no **linear** relationship between the variables.

However:

```text
Correlation ≈ 0
```

does not necessarily mean:

```text
No relationship exists
```

A nonlinear relationship may still exist.

---

# Pearson Correlation Limitation

Pearson correlation measures **linear relationships**.

Consider:

```text
Y = X²
```

The variables have a strong nonlinear relationship.

However, Pearson correlation may not fully represent this relationship, especially when the data is symmetric around zero.

Therefore:

> Pearson correlation should be interpreted in the context of the relationship being analyzed.

---

# Spearman Rank Correlation

Another important correlation measure is:

**Spearman Rank Correlation**

Spearman correlation works with the **ranks** of observations rather than directly using their raw values.

For example:

```text
Values:

20, 50, 80, 100

Ranks:

1, 2, 3, 4
```

Spearman correlation then measures the relationship between the ranks.

---

# When to Use Spearman Correlation?

Spearman correlation is useful when:

- Data is ordinal or naturally ranked.
- The relationship is monotonic.
- The relationship is not necessarily linear.
- Outliers make Pearson correlation less appropriate.
- The actual distances between values are less important than their ordering.

A **monotonic relationship** means that as one variable increases, the other generally moves in one direction, even if the rate of change is not constant.

---

# Pearson vs Spearman

| Feature | Pearson | Spearman |
|---|---|---|
| Uses | Actual values | Ranks |
| Measures | Linear relationship | Monotonic relationship |
| Range | -1 to +1 | -1 to +1 |
| Outlier sensitivity | More sensitive | Often more robust |
| Nonlinear monotonic relationship | May not capture well | Can capture |
| Ordinal data | Usually inappropriate | Appropriate |

---

# Covariance vs Correlation

| Feature | Covariance | Correlation |
|---|---|---|
| Measures | Direction of joint variation | Direction and standardized strength |
| Range | −∞ to +∞ | −1 to +1 |
| Scale dependent | Yes | No |
| Unit dependent | Yes | No |
| Easy to compare | No | Yes |
| Common use | Statistical calculations | Relationship analysis |

---

# Real-World Example: Feature Selection

Suppose we want to predict:

```text
House Price
```

Available features:

- House Size
- Number of Rooms
- Location
- Number of People Living
- House is Haunted

We can investigate their correlation with house price.

For example:

| Feature | Relationship with Price |
|---|---|
| House Size | Strong Positive |
| Number of Rooms | Positive |
| Location | Positive |
| Number of People | Weak |
| House is Haunted | Negative |

Correlation analysis can help identify potentially useful features.

However:

> Correlation does not prove that a feature causes the target to change.

Feature selection should also consider:

- Domain knowledge
- Model performance
- Multicollinearity
- Other statistical techniques

---

# Correlation and Machine Learning

Correlation is commonly used during:

## Exploratory Data Analysis

To understand relationships between variables.

## Feature Selection

To identify potentially useful features.

## Multicollinearity Detection

Highly correlated input features may contain redundant information.

## Data Analysis

To identify patterns and relationships.

---

# Important Warning: Correlation Does Not Mean Causation

Suppose:

```text
Ice Cream Sales ↑

and

Swimming Accidents ↑
```

Both may be correlated.

This does not mean:

```text
Ice Cream Sales → Swimming Accidents
```

A third variable, such as:

```text
Temperature
```

may influence both.

Therefore:

> **Correlation indicates association, not causation.**
