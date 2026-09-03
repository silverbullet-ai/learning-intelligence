# P-Value and Significance Level (α)

## Overview

The **P-value** and **Significance Level (α)** are important concepts in **Inferential Statistics** and **Hypothesis Testing**.

They help us decide whether the evidence from sample data is strong enough to **reject the Null Hypothesis (H₀)**.

---

## What is a P-Value?

A **P-value** is a number calculated from a statistical test that describes how compatible the observed result is with the **Null Hypothesis (H₀)**.

In simple terms:

> The P-value measures how surprising the observed result would be if the Null Hypothesis were true.

### Interpretation

- **Small P-value** → The observed result is relatively unusual under H₀.
- **Large P-value** → The observed result is relatively compatible with H₀.

> **Important:** The P-value is **not** the probability that H₀ is true.

---

# P-Value Intuition

Consider a fair coin tossed many times.

If the coin is fair:

$$
P(\text{Head}) = 0.5
$$

For 100 tosses, we expect approximately:

$$
50 \text{ Heads}
$$

Suppose we observe:

- 60 Heads, 40 Tails → This could reasonably happen by chance.
- 70 Heads, 30 Tails → This provides stronger evidence that the coin may not be fair.

Hypothesis testing helps determine whether the observed difference is statistically significant.

---

# Hypothesis Testing Setup

### Null Hypothesis

The Null Hypothesis represents the default assumption.

For a fair coin:

$$
H_0: p = 0.5
$$

### Alternate Hypothesis

For a two-tailed test:

$$
H_1: p \neq 0.5
$$

The statistical test then produces a P-value.

---

# Significance Level (α)

The **Significance Level**, represented by **α (alpha)**, is the threshold selected before making the statistical decision.

A commonly used value is:

$$
\alpha = 0.05
$$

This represents a **5% significance level**.

The value of α should be selected based on the problem, risk, and domain context.

---

# Confidence Level

The relationship between significance level and confidence level is:

$$
\text{Confidence Level} = 1 - \alpha
$$

For:

$$
\alpha = 0.05
$$

we get:

$$
1 - 0.05 = 0.95
$$

Therefore:

$$
\text{Confidence Level} = 95\%
$$

---

# Rejection Region

For a two-tailed test with:

$$
\alpha = 0.05
$$

the total rejection probability is 5%.

Since the test has two tails:

$$
\frac{\alpha}{2}
=
\frac{0.05}{2}
=
0.025
$$

Therefore:

- Left tail = 0.025
- Right tail = 0.025
- Middle region = 0.95

For the standard normal distribution, the corresponding critical values are approximately:

$$
z = -1.96
$$

and:

$$
z = 1.96
$$

---

# Relationship Between P-Value and α

After performing a statistical test, compare the P-value with the Significance Level.

## Case 1: P-value < α

$$
p < \alpha
$$

### Decision

**Reject H₀**

The observed result provides sufficient evidence against the Null Hypothesis at the chosen significance level.

---

## Case 2: P-value ≥ α

$$
p \geq \alpha
$$

### Decision

**Fail to Reject H₀**

There is insufficient evidence against the Null Hypothesis at the chosen significance level.

> We generally say **"Fail to Reject H₀"** instead of **"Accept H₀"**, because a hypothesis test does not prove that H₀ is true.

---

# Decision Rule

$$
p < \alpha
\Rightarrow
\text{Reject } H_0
$$

$$
p \geq \alpha
\Rightarrow
\text{Fail to Reject } H_0
$$

---

# Example 1

Suppose a statistical test produces:

$$
p = 0.03
$$

and:

$$
\alpha = 0.05
$$

Since:

$$
0.03 < 0.05
$$

we **Reject H₀**.

### Interpretation

The result is statistically significant at the 5% significance level.

---

# Example 2

Suppose:

$$
p = 0.08
$$

and:

$$
\alpha = 0.05
$$

Since:

$$
0.08 \geq 0.05
$$

we **Fail to Reject H₀**.

### Interpretation

There is insufficient evidence to reject H₀ at the 5% significance level.

---

# Relationship with Confidence Interval

For a two-sided hypothesis test:

$$
\text{Confidence Level} = 1 - \alpha
$$

Examples:

| Significance Level (α) | Confidence Level |
|---:|---:|
| 0.10 | 90% |
| 0.05 | 95% |
| 0.01 | 99% |

For α = 0.05, the extreme 5% of the reference distribution forms the rejection regions.

---

# P-Value and Statistical Significance

A result is commonly called **statistically significant** when:

$$
p < \alpha
$$

However, statistical significance does **not automatically mean practical significance**.

A very small P-value can occur with a very large sample even when the actual effect is small.

Therefore, statistical significance should be interpreted together with:

- Effect size
- Confidence interval
- Sample size
- Domain context

---

# How is the P-Value Obtained?

The P-value is calculated from a statistical test.

Common statistical tests include:

- Z-Test
- T-Test
- Chi-Square Test
- ANOVA
- F-Test

The exact calculation depends on the statistical test and the alternative hypothesis.

---

# Important Points

- The **P-value** is calculated from sample data through a statistical test.
- The P-value describes how compatible the observed result is with H₀.
- **α** is the preselected significance threshold.
- A common value is **α = 0.05**.
- Confidence Level is $1 - \alpha$.
- If $p < \alpha$ → **Reject H₀**.
- If $p \geq \alpha$ → **Fail to Reject H₀**.
- The P-value is **not** the probability that H₀ is true.
- Statistical significance does not necessarily imply practical significance.

---

# Flow of Decision Making

```text
Write H₀
   │
   ▼
Write H₁
   │
   ▼
Perform Statistical Test
   │
   ▼
Calculate P-Value
   │
   ▼
Choose Significance Level (α)
   │
   ▼
Compare P-Value with α
   │
   ├───────────────┐
   ▼               ▼
p < α             p ≥ α
   │               │
   ▼               ▼
Reject H₀      Fail to Reject H₀
```

---

# Summary Table

| Concept | Meaning |
| --- | --- |
| **P-value** | Measures how surprising the observed result is under H₀ |
| **Significance Level (α)** | Threshold used for statistical decision-making |
| **Confidence Level** | $1 - \alpha$ |
| **Small P-value** | Stronger evidence against H₀ |
| **Large P-value** | Insufficient evidence against H₀ |
| **p < α** | Reject H₀ |
| **p ≥ α** | Fail to Reject H₀ |
| **Rejection Region** | Extreme region(s) of the reference distribution |

---

# Applications

P-values and significance levels are used in:

- Hypothesis Testing
- Data Analysis
- Machine Learning
- Scientific Research
- A/B Testing
- Medical Research
- Quality Control
- Experimental Studies
- Business Analytics

---

# Interview Questions

1. What is a P-value?
2. What does a P-value represent?
3. Is the P-value the probability that H₀ is true?
4. What is the Significance Level (α)?
5. What is a commonly used value of α?
6. What is the relationship between α and confidence level?
7. What happens when P-value < α?
8. What happens when P-value ≥ α?
9. Why do we say "Fail to Reject H₀" instead of "Accept H₀"?
10. What is a rejection region?
11. Why is α divided by two in a two-tailed test?
12. What is the difference between statistical significance and practical significance?

---

# Quick Revision

- **P-value** → Measures how surprising the observed result is assuming H₀ is true.
- **α** → Preselected significance threshold.
- **Common α** → 0.05.
- **Confidence Level** → $1 - \alpha$.
- **α = 0.05** → **95% confidence level**.
- **p < α** → Reject H₀.
- **p ≥ α** → Fail to Reject H₀.
- **Small P-value** → Stronger evidence against H₀.
- **P-value ≠ Probability that H₀ is true.**
