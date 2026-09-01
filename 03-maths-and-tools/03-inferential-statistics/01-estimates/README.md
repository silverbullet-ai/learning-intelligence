# Estimates

## Overview

**Estimation** is one of the fundamental concepts of **Inferential Statistics**.

In inferential statistics, we use **sample data** to make conclusions or estimates about an unknown **population parameter**.

Since studying an entire population is often impractical, we collect a sample and use statistics calculated from that sample to estimate the corresponding population parameters.

---

## Definition

An **estimate** is a numerical value calculated from sample data and used to estimate an unknown population parameter.

In simple terms:

```text
Population
    │
    ▼
Unknown Population Parameter
    │
    │  Take a Sample
    ▼
Sample Data
    │
    ▼
Calculate Sample Statistic
    │
    ▼
Estimate Population Parameter
```

### Example

Suppose we want to know the average height of all students in a university.

Studying every student may be impractical.

Instead:

1. Select a sample of students.
2. Calculate their average height.
3. Use the sample average to estimate the population average.

---

# Types of Estimates

There are two major types of estimates:

1. **Point Estimate**
2. **Interval Estimate**

```text
Estimation
│
├── Point Estimate
│
└── Interval Estimate
```

---

# 1. Point Estimate

## Definition

A **Point Estimate** is a **single numerical value** used to estimate an unknown population parameter.

### Example

Suppose:

- Population mean = `μ`
- Sample mean = `x̄`

The sample mean is used to estimate the population mean.

Therefore:

```text
x̄ → Point Estimate of μ
```

### Example

Suppose a sample produces:

```text
Sample Mean = 60
```

The value `60` can be used as the point estimate of the population mean.

So:

```text
Point Estimate = 60
```

---

## Common Point Estimators

Different sample statistics can estimate different population parameters.

| Population Parameter | Point Estimate |
|---|---|
| Population Mean `μ` | Sample Mean `x̄` |
| Population Proportion `p` | Sample Proportion `p̂` |
| Population Variance `σ²` | Sample Variance `s²` |
| Population Standard Deviation `σ` | Sample Standard Deviation `s` |

The important idea is:

> A sample statistic can be used as an estimate of the corresponding population parameter.

---

# Limitation of Point Estimates

A point estimate provides only **one value**.

For example:

```text
Estimated Population Mean = 60
```

The actual population mean could be:

```text
58
61
63
...
```

The point estimate does not communicate how uncertain the estimate is.

Therefore, a single value may not provide enough information about the population parameter.

This leads to **Interval Estimation**.

---

# 2. Interval Estimate

## Definition

An **Interval Estimate** provides a **range of values** used to estimate an unknown population parameter.

Instead of giving only one value:

```text
60
```

we provide a range:

```text
55 ---------------------- 65
```

This gives more information about the possible location of the population parameter.

### Example

Instead of saying:

> Estimated population mean = 60

we could say:

> The population mean is estimated to lie between 55 and 65.

---

# Confidence Interval

A **confidence interval** is a statistical interval constructed from sample data to estimate a population parameter with a specified level of confidence.

For example:

```text
55 ---------------------- 65
```

where:

```text
Lower Limit = 55
Upper Limit = 65
```

The detailed calculation and interpretation of confidence intervals will be covered separately.

---

# Margin of Error

An interval estimate can commonly be represented as:

```text
Point Estimate ± Margin of Error
```

### Example

Suppose:

```text
Point Estimate = 60
Margin of Error = 5
```

Then:

```text
60 ± 5
```

which gives:

```text
Lower Limit = 60 - 5 = 55
Upper Limit = 60 + 5 = 65
```

Therefore:

```text
Interval = [55, 65]
```

---

# Point Estimate vs Interval Estimate

| Point Estimate | Interval Estimate |
|---|---|
| Single numerical value | Range of values |
| Estimates a population parameter | Estimates a population parameter using a range |
| Simple representation | Provides more information |
| Does not directly show uncertainty | Reflects uncertainty through an interval |
| Example: `60` | Example: `55–65` |

---

# Population Parameter vs Sample Statistic

It is important to distinguish between a **parameter** and a **statistic**.

### Population Parameter

A numerical value describing the entire population.

Examples:

```text
μ  → Population Mean
p  → Population Proportion
σ² → Population Variance
σ  → Population Standard Deviation
```

### Sample Statistic

A numerical value calculated from sample data.

Examples:

```text
x̄ → Sample Mean
p̂ → Sample Proportion
s² → Sample Variance
s  → Sample Standard Deviation
```

The sample statistic is often used to estimate the corresponding population parameter.

---

# Flow of Estimation

```text
Population
    │
    ▼
Unknown Parameter
    │
    │
    ▼
Take a Sample
    │
    ▼
Calculate Sample Statistic
    │
    ├───────────────┐
    ▼               ▼
Point Estimate   Interval Estimate
    │               │
    │               ▼
    │        Confidence Interval
    │
    ▼
Single Value
```

---

# Example

Suppose we want to estimate the average salary of employees in a company.

The actual population mean is unknown.

We randomly select employees and calculate:

```text
Sample Mean = ₹60,000
```

### Point Estimate

```text
Estimated Population Mean = ₹60,000
```

### Interval Estimate

Suppose the estimated interval is:

```text
₹55,000 to ₹65,000
```

Then:

```text
Point Estimate = ₹60,000
Interval Estimate = ₹55,000 – ₹65,000
```

The interval provides more information than the point estimate alone.

---

# Important Concepts

### Estimate

A numerical value obtained from sample data and used to estimate an unknown population parameter.

### Point Estimate

A single value used to estimate a population parameter.

### Interval Estimate

A range of values used to estimate a population parameter.

### Confidence Interval

A statistically constructed interval used to estimate a population parameter at a specified confidence level.

### Margin of Error

The amount added to and subtracted from the point estimate to form an interval.

```text
Interval Estimate
=
Point Estimate ± Margin of Error
```

---

# Key Points

- **Estimation** is a fundamental concept of Inferential Statistics.
- Sample data is used to estimate unknown population parameters.
- There are two major types of estimates:
  - **Point Estimate**
  - **Interval Estimate**
- A point estimate provides a **single value**.
- An interval estimate provides a **range**.
- The sample mean `x̄` is a point estimator of the population mean `μ`.
- A confidence interval is a type of statistical interval used for estimation.
- Margin of error represents the amount of uncertainty around a point estimate.
- Interval estimates generally provide more information about uncertainty than point estimates.

---

# Quick Revision

| Property | Description |
|---|---|
| Topic | Estimation |
| Branch | Inferential Statistics |
| Purpose | Estimate unknown population parameters |
| Point Estimate | Single numerical value |
| Interval Estimate | Range of values |
| Mean Estimator | Sample Mean `x̄` |
| Population Mean | `μ` |
| Margin of Error | Amount added/subtracted from point estimate |
| Common Form | Point Estimate ± Margin of Error |

---

# Interview Questions

1. What is estimation in inferential statistics?
2. What is an estimate?
3. What are the two types of estimates?
4. What is a point estimate?
5. What is an interval estimate?
6. What is the point estimate of the population mean?
7. What is the difference between a parameter and a statistic?
8. Why can a point estimate be insufficient?
9. What is a confidence interval?
10. What is margin of error?
11. How is an interval estimate constructed conceptually?
12. What is the difference between a point estimate and an interval estimate?

---

# 💡 Remember

```text
Population Parameter
        ↑
        │
    Estimation
        ↑
        │
Sample Statistic
```

### The simplest way to remember:

```text
Point Estimate
→ One value

Interval Estimate
→ Range of values

Sample Mean (x̄)
→ Estimates Population Mean (μ)
```

> **Sample → Statistic → Estimate → Population Parameter**
