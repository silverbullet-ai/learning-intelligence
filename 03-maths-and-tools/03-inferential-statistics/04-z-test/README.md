# Z-Test

## Overview

A **Z-Test** is a statistical hypothesis test used to determine whether a sample provides sufficient evidence about a population mean or proportion.

For the classical **one-sample Z-test for a population mean**, the population standard deviation $\sigma$ is known.

The Z-test is closely connected to:

- Hypothesis Testing
- P-Values
- Significance Level ($\alpha$)
- Standard Normal Distribution
- Central Limit Theorem
- Confidence Intervals

---

# Statistical Tests

Different statistical tests are used for different types of problems.

| Test | Common Use |
|---|---|
| **Z-Test** | Population mean when $\sigma$ is known |
| **T-Test** | Population mean when $\sigma$ is unknown |
| **Chi-Square Test** | Categorical data, variance-related tests, independence |
| **ANOVA** | Comparing means across multiple groups |
| **F-Test** | Comparing variances and related statistical procedures |

The appropriate test depends on the:

- Type of data
- Population assumptions
- Sample size
- Parameter being tested
- Information available about the population

---

# What is a Z-Test?

A **Z-Test** is a hypothesis test based on the **Standard Normal Distribution**.

For a one-sample test of a population mean, the classical Z-test is appropriate when:

1. The population standard deviation $\sigma$ is known.
2. The sampling distribution of the sample mean is Normal or approximately Normal.

A large sample size is commonly used to justify approximate normality through the **Central Limit Theorem**.

> A commonly taught rule of thumb is $n \geq 30$, but $n \geq 30$ alone does not automatically make every problem a Z-test.

---

# Z-Test and Hypothesis Testing

The general process is:

1. State the Null Hypothesis ($H_0$).
2. State the Alternate Hypothesis ($H_1$).
3. Choose the significance level ($\alpha$).
4. Determine whether the test is one-tailed or two-tailed.
5. Calculate the Z-statistic.
6. Calculate the P-value or determine the critical value.
7. Compare the result with the decision criterion.
8. Make a statistical conclusion.

---

# Z-Test for a Population Mean

The Z-test statistic is:

$$
Z =
\frac{\bar{x} - \mu_0}
{\frac{\sigma}{\sqrt{n}}}
$$

where:

- $\bar{x}$ = Sample mean
- $\mu_0$ = Population mean assumed under $H_0$
- $\sigma$ = Known population standard deviation
- $n$ = Sample size

The denominator is the **standard error of the sample mean**:

$$
SE_{\bar{x}} =
\frac{\sigma}{\sqrt{n}}
$$

---

# Why $\sigma / \sqrt{n}$?

According to the Central Limit Theorem, the sampling distribution of the sample mean has:

### Mean

$$
\mu_{\bar{x}} = \mu
$$

### Standard Deviation

$$
\sigma_{\bar{x}} =
\frac{\sigma}{\sqrt{n}}
$$

The standard deviation of the sampling distribution of the sample mean is called the **Standard Error of the Mean**.

Therefore, the Z-statistic measures how many standard errors the sample mean is away from the hypothesized population mean.

---

# Confidence Level and Significance Level

The relationship is:

$$
\text{Confidence Level} = 1 - \alpha
$$

Therefore:

### 95% Confidence Level

$$
\alpha = 1 - 0.95 = 0.05
$$

### 98% Confidence Level

$$
\alpha = 1 - 0.98 = 0.02
$$

---

# Two-Tailed Z-Test

A two-tailed test is used when the alternate hypothesis is:

$$
H_1: \mu \neq \mu_0
$$

The test checks whether the population mean could be either:

- Greater than $\mu_0$
- Less than $\mu_0$

---

## Example

Suppose:

$$
H_0: \mu = 168
$$

and:

$$
H_1: \mu \neq 168
$$

Because the alternate hypothesis uses $\neq$, this is a **two-tailed test**.

For a 95% confidence level:

$$
\alpha = 0.05
$$

The significance level is divided between the two tails:

$$
\frac{\alpha}{2} = 0.025
$$

The critical Z-values are approximately:

$$
Z_{critical} = \pm 1.96
$$

---

# Two-Tailed Decision Rule

Reject $H_0$ when:

$$
Z < -1.96
$$

or

$$
Z > 1.96
$$

Equivalently:

$$
|Z| > 1.96
$$

Otherwise:

$$
-1.96 \leq Z \leq 1.96
$$

→ **Fail to Reject $H_0$**

---

# One-Tailed Z-Test

A one-tailed test is used when the alternate hypothesis specifies a direction.

There are two types.

---

## Left-Tailed Test

Used when:

$$
H_1: \mu < \mu_0
$$

The rejection region is on the **left side** of the distribution.

Example:

> Is the average lifetime less than 5 years?

---

## Right-Tailed Test

Used when:

$$
H_1: \mu > \mu_0
$$

The rejection region is on the **right side** of the distribution.

Example:

> Is the average height greater than 168 cm?

---

# Example 1 — Average Height

Suppose:

- Population mean: $\mu_0 = 168$ cm
- Population standard deviation: $\sigma = 3.9$ cm
- Sample size: $n = 36$
- Sample mean: $\bar{x} = 169.5$ cm
- Confidence level: 95%

Therefore:

$$
\alpha = 0.05
$$

---

## Step 1: Hypotheses

$$
H_0: \mu = 168
$$

$$
H_1: \mu \neq 168
$$

This is a **two-tailed test**.

---

## Step 2: Critical Values

For a 95% two-tailed test:

$$
Z_{critical} = \pm 1.96
$$

---

## Step 3: Calculate the Z-Statistic

$$
Z =
\frac{\bar{x} - \mu_0}
{\frac{\sigma}{\sqrt{n}}}
$$

Substituting:

$$
Z =
\frac{169.5 - 168}
{\frac{3.9}{\sqrt{36}}}
$$

Since:

$$
\sqrt{36} = 6
$$

we get:

$$
Z =
\frac{1.5}{3.9/6}
$$

Therefore:

$$
Z \approx 2.31
$$

---

## Step 4: Compare with Critical Value

We have:

$$
Z = 2.31
$$

and:

$$
Z_{critical} = 1.96
$$

Since:

$$
2.31 > 1.96
$$

the test statistic falls in the rejection region.

### Decision

**Reject $H_0$.**

### Conclusion

There is sufficient evidence at the 5% significance level to conclude that the population mean is different from 168 cm.

The sample mean is higher than 168 cm, but because this is a two-tailed test, the formal conclusion is that the population mean is **different**, not specifically that it is increasing.

---

# P-Value for Example 1

The calculated Z-statistic is approximately:

$$
Z = 2.31
$$

The cumulative probability to the left of $Z=2.31$ is approximately:

$$
P(Z \leq 2.31) \approx 0.98956
$$

Therefore, the right-tail probability is:

$$
1 - 0.98956 = 0.01044
$$

Because this is a two-tailed test:

$$
p = 2(0.01044)
$$

Therefore:

$$
p \approx 0.02088
$$

Compare:

$$
p = 0.02088
$$

with:

$$
\alpha = 0.05
$$

Since:

$$
0.02088 < 0.05
$$

we:

**Reject $H_0$.**

The P-value and critical-value approaches lead to the same decision.

---

# Example 2 — Bulb Warranty

Suppose:

- Population mean: $\mu_0 = 5$ years
- Population standard deviation: $\sigma = 0.50$ years
- Sample size: $n = 40$
- Sample mean: $\bar{x} = 4.8$ years
- Confidence level: 98%

Therefore:

$$
\alpha = 1 - 0.98
$$

$$
\alpha = 0.02
$$

---

# Step 1: Hypotheses

Suppose we want to test whether the average bulb lifetime is **less than 5 years**.

Therefore:

$$
H_0: \mu = 5
$$

$$
H_1: \mu < 5
$$

Because the alternate hypothesis specifies a direction, this is a **left-tailed test**.

---

# Step 2: Significance Level

The significance level is:

$$
\alpha = 0.02
$$

Because this is a left-tailed test, the entire 2% rejection region is in the left tail.

---

# Step 3: Calculate the Z-Statistic

Using:

$$
Z =
\frac{\bar{x} - \mu_0}
{\frac{\sigma}{\sqrt{n}}}
$$

Substituting:

$$
Z =
\frac{4.8 - 5}
{\frac{0.50}{\sqrt{40}}}
$$

Therefore:

$$
Z \approx -2.53
$$

---

# Step 4: Calculate the P-Value

For a left-tailed test:

$$
p = P(Z \leq -2.53)
$$

Approximately:

$$
p \approx 0.0057
$$

Compare:

$$
p = 0.0057
$$

with:

$$
\alpha = 0.02
$$

Since:

$$
0.0057 < 0.02
$$

we:

**Reject $H_0$.**

### Conclusion

There is sufficient evidence at the 2% significance level to support the claim that the average bulb lifetime is less than 5 years.

---

# One-Tailed vs Two-Tailed Tests

| Test | Alternate Hypothesis | Direction |
|---|---|---|
| **Two-Tailed** | $H_1: \mu \neq \mu_0$ | Both directions |
| **Left-Tailed** | $H_1: \mu < \mu_0$ | Lower values |
| **Right-Tailed** | $H_1: \mu > \mu_0$ | Higher values |

---

# Critical-Value Approach vs P-Value Approach

There are two common ways to make the decision.

## Critical-Value Approach

Calculate the Z-statistic and compare it with the critical Z-value.

For a two-tailed 95% test:

$$
|Z| > 1.96
$$

→ Reject $H_0$

Otherwise:

→ Fail to Reject $H_0$

---

## P-Value Approach

Calculate the P-value and compare it with $\alpha$.

$$
p < \alpha
$$

→ Reject $H_0$

$$
p \geq \alpha
$$

→ Fail to Reject $H_0$

Both approaches should lead to the same statistical decision when applied correctly.

---

# Important Conditions

For the classical one-sample Z-test for a population mean:

- The population standard deviation $\sigma$ is known.
- The observations should be independent.
- The population should be Normal, or the sample size should be sufficiently large for the sampling distribution of the mean to be approximately Normal.

A commonly taught rule of thumb is:

$$
n \geq 30
$$

However, **$n \geq 30$ is not a universal requirement for every Z-test**.

---

# Important Takeaways

- **Z-Test** is commonly used for hypothesis tests involving population means when $\sigma$ is known.
- The Z-statistic is:

$$
Z =
\frac{\bar{x} - \mu_0}
{\frac{\sigma}{\sqrt{n}}}
$$

- The standard error is:

$$
SE =
\frac{\sigma}{\sqrt{n}}
$$

- 95% confidence level corresponds to:

$$
\alpha = 0.05
$$

- 98% confidence level corresponds to:

$$
\alpha = 0.02
$$

- $H_1: \mu \neq \mu_0$ → Two-tailed test.
- $H_1: \mu < \mu_0$ → Left-tailed test.
- $H_1: \mu > \mu_0$ → Right-tailed test.
- For a 95% two-tailed test:

$$
Z_{critical} = \pm 1.96
$$

- If:

$$
p < \alpha
$$

  → Reject $H_0$.

- If:

$$
p \geq \alpha
$$

  → Fail to Reject $H_0$.
- **Fail to Reject $H_0$** does not prove that $H_0$ is true.

---

# Applications

Z-tests can be used in areas such as:

- Quality Control
- Manufacturing
- Business Analytics
- A/B Testing
- Medical Research
- Education
- Data Analysis
- Scientific Research

---

# Interview Questions

1. What is a Z-Test?
2. When is a Z-Test used?
3. What is the Z-test formula for a population mean?
4. Why do we divide $\sigma$ by $\sqrt{n}$?
5. What is the Standard Error of the Mean?
6. What is the role of the Central Limit Theorem in a Z-Test?
7. What is the difference between a one-tailed and two-tailed Z-Test?
8. What are the critical values for a 95% two-tailed Z-Test?
9. What happens when the P-value is less than $\alpha$?
10. What is the difference between the critical-value and P-value approaches?
11. Why is the population standard deviation important in a classical Z-Test?
12. What is the difference between a Z-Test and a T-Test?

---

# Quick Revision

**Z-Test**

→ Hypothesis test based on the Standard Normal Distribution.

**Classical one-sample mean Z-Test**

→ Population standard deviation $\sigma$ is known.

**Z-statistic**

$$
Z =
\frac{\bar{x} - \mu_0}
{\frac{\sigma}{\sqrt{n}}}
$$

**Standard Error**

$$
SE =
\frac{\sigma}{\sqrt{n}}
$$

**95% Confidence**

$$
\alpha = 0.05
$$

**Two-tailed 95% critical values**

$$
Z = \pm 1.96
$$

**P-value < α**

→ Reject $H_0$

**P-value ≥ α**

→ Fail to Reject $H_0$

**Two-tailed**

$$
H_1: \mu \neq \mu_0
$$

**Left-tailed**

$$
H_1: \mu < \mu_0
$$

**Right-tailed**

$$
H_1: \mu > \mu_0
$$

---

## Core Idea

```text
Sample Data
     │
     ▼
State H₀ and H₁
     │
     ▼
Choose α
     │
     ▼
Determine Test Type
     │
     ▼
Calculate Z
     │
     ├───────────────┐
     ▼               ▼
Critical Value     P-Value
     │               │
     └───────┬───────┘
             ▼
       Compare with α
             │
       ┌─────┴─────┐
       ▼           ▼
   Reject H₀   Fail to Reject H₀