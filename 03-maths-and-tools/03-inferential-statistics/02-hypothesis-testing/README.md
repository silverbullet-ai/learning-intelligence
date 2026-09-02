# Hypothesis Testing

## Overview

**Hypothesis Testing** is one of the most important concepts in **Inferential Statistics**.

It is a statistical method used to make conclusions about an **unknown population parameter** using **sample data**.

Since it is often difficult or impossible to collect data from an entire population, we use a sample and perform statistical analysis to determine whether the evidence supports or rejects an assumption about the population.

---

## What is Hypothesis Testing?

**Hypothesis Testing** is a statistical method used to:

> Make conclusions or inferences about an unknown population parameter using sample data.

### General Flow

```text
Population
    │
    ▼
Unknown Population Parameter
    │
    ▲
    │
Sample Data
    │
    ▼
Hypothesis Testing
    │
    ▼
Conclusion / Decision
```

The goal is to determine whether the evidence from the sample provides enough support to reject the initial assumption.

---

## Why Do We Use Hypothesis Testing?

Studying an entire population is often:

- Expensive
- Time-consuming
- Impractical
- Sometimes impossible

Therefore, we:

1. Collect a sample.
2. Perform statistical analysis.
3. Draw conclusions about the population.

Population parameters may include:

- Population Mean ($\mu$)
- Population Variance ($\sigma^2$)
- Population Standard Deviation ($\sigma$)

---

# Steps in Hypothesis Testing

There are four fundamental steps:

1. **Define the Null Hypothesis**
2. **Define the Alternate Hypothesis**
3. **Perform Statistical Analysis**
4. **Make a Decision**

---

## Step 1: Define the Null Hypothesis ($H_0$)

The **Null Hypothesis ($H_0$)** is the default assumption that we begin with.

It generally represents:

> There is no significant difference, effect, or change.

### Example

Suppose a person is accused of a crime.

Initially, the court assumes:

> The person is not guilty.

Therefore:

$$
H_0: \text{Person is not guilty}
$$

The null hypothesis represents the assumption that is tested using evidence.

---

## Step 2: Define the Alternate Hypothesis ($H_1$)

The **Alternate Hypothesis ($H_1$)** represents the alternative to the null hypothesis.

It is generally what we want to investigate.

For the court example:

$$
H_1: \text{Person is guilty}
$$

Therefore:

```text
Null Hypothesis
      │
      ▼
Default Assumption
      │
      │
      ▼
Alternate Hypothesis
      │
      ▼
Alternative to the Default Assumption
```

---

# Step 3: Perform Statistical Analysis

After defining the hypotheses, we perform an appropriate statistical test using the sample data.

Common statistical tests include:

- **Z-Test**
- **T-Test**
- **Chi-Square Test**
- **ANOVA**
- **F-Test**

These tests help determine whether the sample provides sufficient evidence against the null hypothesis.

---

## Real-World Analogy

For the court example, evidence may include:

- DNA tests
- Fingerprint tests
- Forensic evidence
- Witness evidence

Similarly, in statistics, sample data acts as evidence that helps us evaluate the hypotheses.

---

# Step 4: Make the Decision

After performing the statistical test, we make a decision regarding the null hypothesis.

Traditionally, the decision is described as:

- **Reject $H_0$**
- **Fail to reject $H_0$**

> **Important:** In statistical terminology, "fail to reject $H_0$" is preferred over "accept $H_0$" because the test does not prove that the null hypothesis is true.

The decision is based on the statistical evidence obtained from the sample.

---

# Example: College Pass Percentage

Suppose a college claims:

> The average pass percentage of students is **85%**.

A new college in the same district has:

- Sample Size = 100 students
- Sample Mean Pass Percentage = 90%
- Standard Deviation = 4%

Question:

> Does this college have a different average pass percentage?

---

## Step 1: Null Hypothesis

The original claim is taken as the default assumption.

$$
H_0: \mu = 85
$$

where:

- $\mu$ = Population mean pass percentage
- $85$ = Claimed population mean

Meaning:

> The average pass percentage is 85%.

---

## Step 2: Alternate Hypothesis

The question asks whether the pass percentage is **different** from 85%.

Therefore:

$$
H_1: \mu \neq 85
$$

This is a **two-tailed hypothesis** because the average could be either:

- Greater than 85%
- Less than 85%

---

# Types of Alternate Hypotheses

The form of the alternate hypothesis depends on the question.

## Two-Tailed Test

If the question asks:

> Is the population mean different from the claimed value?

Then:

$$
H_1: \mu \neq \mu_0
$$

Example:

$$
H_1: \mu \neq 85
$$

Both directions are possible.

```text
Less than       Different       Greater than
     ◄──────────────┬──────────────►
                    μ₀
```

---

## Right-Tailed Test

If the question asks:

> Is the population mean greater than the claimed value?

Then:

$$
H_1: \mu > \mu_0
$$

Example:

$$
H_1: \mu > 85
$$

This is a **right-tailed test**.

---

## Left-Tailed Test

If the question asks:

> Is the population mean less than the claimed value?

Then:

$$
H_1: \mu < \mu_0
$$

Example:

$$
H_1: \mu < 85
$$

This is a **left-tailed test**.

---

# Understanding the Hypotheses

| Type | Null Hypothesis | Alternate Hypothesis | Test |
|---|---|---|---|
| Two-Tailed | $H_0: \mu = \mu_0$ | $H_1: \mu \neq \mu_0$ | Two-tailed |
| Right-Tailed | $H_0: \mu = \mu_0$ | $H_1: \mu > \mu_0$ | Right-tailed |
| Left-Tailed | $H_0: \mu = \mu_0$ | $H_1: \mu < \mu_0$ | Left-tailed |

---

# Overall Flow

```text
Start
  │
  ▼
Define H₀
(Default Assumption)
  │
  ▼
Define H₁
(Alternative Assumption)
  │
  ▼
Collect / Analyze Sample Data
  │
  ▼
Perform Statistical Test
  │
  ▼
Evaluate Statistical Evidence
  │
  ▼
Make Decision
  │
  ├── Reject H₀
  │
  └── Fail to Reject H₀
```

---

# Key Concepts

| Concept | Meaning |
|---|---|
| Hypothesis Testing | Method for making conclusions about a population using sample data |
| $H_0$ | Null hypothesis; default assumption |
| $H_1$ | Alternate hypothesis; alternative to the null hypothesis |
| Statistical Test | Mathematical procedure used to analyze sample evidence |
| Two-Tailed Test | Tests whether a parameter is different from a specified value |
| Right-Tailed Test | Tests whether a parameter is greater than a specified value |
| Left-Tailed Test | Tests whether a parameter is less than a specified value |
| Decision | Reject or fail to reject the null hypothesis |

---

# Important Points

- Hypothesis Testing is part of **Inferential Statistics**.
- It uses **sample data** to make conclusions about an **unknown population parameter**.
- The **Null Hypothesis ($H_0$)** represents the default assumption.
- The **Alternate Hypothesis ($H_1$)** represents the alternative to the null hypothesis.
- Statistical tests are used to evaluate the evidence against $H_0$.
- The final decision is generally stated as **reject $H_0$** or **fail to reject $H_0$**.
- The form of $H_1$ determines whether the test is **two-tailed, right-tailed, or left-tailed**.
- Common tests include **Z-Test, T-Test, Chi-Square Test, ANOVA, and F-Test**.
- **P-value** and **Significance Level ($\alpha$)** are commonly used later to make the final statistical decision.

---

# Applications

Hypothesis Testing is widely used in:

- Data Analysis
- Machine Learning
- Medical Research
- Scientific Research
- A/B Testing
- Quality Control
- Business Analytics
- Experimental Research
- Population Studies

---

# Interview Questions

1. What is Hypothesis Testing?
2. Why is Hypothesis Testing part of Inferential Statistics?
3. What is a Null Hypothesis ($H_0$)?
4. What is an Alternate Hypothesis ($H_1$)?
5. What is the difference between $H_0$ and $H_1$?
6. What are the steps involved in Hypothesis Testing?
7. What are some common statistical tests?
8. What is a two-tailed test?
9. What is a right-tailed test?
10. What is a left-tailed test?
11. In the college pass-percentage example, write $H_0$ and $H_1$.
12. When do we use $H_1: \mu \neq \mu_0$?
13. When do we use $H_1: \mu > \mu_0$?
14. When do we use $H_1: \mu < \mu_0$?
15. What does "fail to reject the null hypothesis" mean?
16. What is the role of the p-value in hypothesis testing?
17. What is the significance level?
18. What is the difference between a one-tailed and two-tailed test?

---

# Quick Revision

- **Hypothesis Testing** → Statistical method for making conclusions about a population using sample data.
- **$H_0$** → Null Hypothesis / Default Assumption.
- **$H_1$** → Alternate Hypothesis / Alternative Assumption.
- **Two-Tailed** → $H_1: \mu \neq \mu_0$
- **Right-Tailed** → $H_1: \mu > \mu_0$
- **Left-Tailed** → $H_1: \mu < \mu_0$
- **Common Tests** → Z-Test, T-Test, Chi-Square, ANOVA, F-Test.
- **Decision** → Reject $H_0$ or Fail to Reject $H_0$.
- **Next Concepts** → P-value and Significance Level.
