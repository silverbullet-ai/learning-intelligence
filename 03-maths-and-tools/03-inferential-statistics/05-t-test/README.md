# Student's t-Distribution and t-Test

## Overview

The **Student's t-distribution** and **t-test** are used for statistical inference when the **population standard deviation ($\sigma$) is unknown** and must be estimated using the sample standard deviation ($s$).

The t-test is especially useful for smaller samples when the population is approximately Normally distributed.

---

# 1. Why Do We Need Student's t-Distribution?

In the previous topic, we studied the **Z-test**.

A classical one-sample Z-test uses the population standard deviation:

$$
Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}}
$$

Where:

- $\bar{x}$ = sample mean
- $\mu_0$ = hypothesized population mean
- $\sigma$ = population standard deviation
- $n$ = sample size

However, in real-world problems, the population standard deviation $\sigma$ is often **unknown**.

### The Question

How can we perform statistical inference when the population standard deviation is unknown?

The answer is:

> **Use the Student's t-distribution and t-test.**

Instead of using the unknown population standard deviation $\sigma$, we estimate it using the sample standard deviation $s$.

---

# 2. Student's t-Distribution

The **Student's t-distribution** is a probability distribution used when estimating a population mean from a sample while the population standard deviation is unknown.

The corresponding t-statistic is:

$$
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
$$

Where:

- $\bar{x}$ = sample mean
- $\mu_0$ = hypothesized population mean
- $s$ = sample standard deviation
- $n$ = sample size

The t-statistic measures how many estimated standard errors the sample mean is away from the hypothesized population mean.

---

# 3. Why Does the t-Distribution Look Different from the Z-Distribution?

The major difference is that the Z-test assumes that $\sigma$ is known.

In a t-test, $\sigma$ is unknown and is replaced by the estimate $s$.

Because $s$ is itself estimated from the sample, there is additional uncertainty.

The t-distribution therefore has **heavier tails** than the Standard Normal distribution.

This means that, especially for small samples, the t-distribution gives more probability to extreme values.

As the sample size increases, the estimate $s$ becomes more reliable and the t-distribution approaches the Standard Normal distribution.

---

# 4. Z-Test vs t-Test

| Z-Test | t-Test |
|---|---|
| Population standard deviation $\sigma$ is known | Population standard deviation $\sigma$ is unknown |
| Uses $\sigma$ | Uses $s$ |
| Uses the Standard Normal (Z) distribution | Uses the Student's t-distribution |
| Uses Z critical values | Uses t critical values |
| Does not use sample-based degrees of freedom in the same way | Uses degrees of freedom |

### Core Idea

$$
\sigma\ \text{known} \rightarrow \text{Z-test}
$$

$$
\sigma\ \text{unknown} \rightarrow \text{t-test}
$$

> **Note:** The distinction between known and unknown population standard deviation is the key idea here. A rule such as $n \geq 30$ is only a common rule of thumb and is not a universal requirement for choosing between a Z-test and t-test.

---

# 5. t-Distribution and t-Table

Similar to the Z-table used with the Standard Normal distribution, a **t-table** can be used to obtain critical values from the Student's t-distribution.

The appropriate critical t-value depends on:

- Degrees of freedom
- One-tailed or two-tailed test
- Significance level $\alpha$
- Corresponding confidence level

Modern statistical software can calculate critical values and p-values directly.

For example, in Python, `scipy.stats.t` can be used to work with the t-distribution.

---

# 6. Degrees of Freedom

An important parameter in a t-test is the **degrees of freedom (df)**.

For a one-sample t-test:

$$
df = n - 1
$$

Where:

- $df$ = degrees of freedom
- $n$ = sample size

### Example

If:

$$
n = 10
$$

Then:

$$
df = 10 - 1 = 9
$$

Therefore, the t-distribution with **9 degrees of freedom** is used.

---

# 7. Intuition Behind Degrees of Freedom

Consider three observations:

$$
x_1,\ x_2,\ x_3
$$

Suppose their sample mean is fixed.

If we know the first two observations and the sample mean, the third observation is no longer completely free to vary.

For example, if:

$$
x_1 + x_2 + x_3 = 30
$$

and we know:

$$
x_1 = 8,\quad x_2 = 12
$$

then:

$$
x_3 = 10
$$

The third observation is determined by the constraint.

Therefore, only two observations are free to vary.

Hence:

$$
df = n - 1
$$

The "chairs and people" analogy can be useful for intuition, but mathematically, degrees of freedom arise from the number of independent pieces of information remaining after estimating a parameter.

---

# 8. Why Does Degree of Freedom Matter?

The shape of the Student's t-distribution depends on the degrees of freedom.

For a one-sample t-test:

$$
df = n - 1
$$

Therefore:

- Small sample → smaller df → heavier tails
- Large sample → larger df → t-distribution closer to Normal

Conceptually:

$$
df \uparrow \quad \Rightarrow \quad t\text{-distribution} \rightarrow \text{Normal distribution}
$$

This is why the sample size affects the critical t-value.

---

# 9. One-Tailed and Two-Tailed t-Tests

The type of hypothesis determines whether the test is one-tailed or two-tailed.

## One-Tailed Test

A one-tailed test is used when the alternative hypothesis specifies a direction.

### Left-Tailed Test

$$
H_0: \mu = \mu_0
$$

$$
H_1: \mu < \mu_0
$$

The rejection region is in the **left tail**.

### Right-Tailed Test

$$
H_0: \mu = \mu_0
$$

$$
H_1: \mu > \mu_0
$$

The rejection region is in the **right tail**.

---

## Two-Tailed Test

A two-tailed test is used when we want to determine whether the population mean is different from the hypothesized value in either direction.

$$
H_0: \mu = \mu_0
$$

$$
H_1: \mu \neq \mu_0
$$

The rejection regions are present in **both tails**.

---

# 10. Significance Level and Critical t-Value

The significance level is represented by:

$$
\alpha
$$

Common significance levels include:

- $\alpha = 0.10$
- $\alpha = 0.05$
- $\alpha = 0.01$

For a two-tailed test with:

$$
\alpha = 0.05
$$

the total rejection probability is 0.05, with:

$$
\frac{\alpha}{2} = 0.025
$$

in each tail.

The critical t-value is determined using:

- Degrees of freedom
- Significance level
- Tail type

---

# 11. t-Test Decision Rule

There are two common approaches.

## Critical-Value Approach

For a two-tailed test:

$$
|t| > t_{\text{critical}}
$$

→ Reject $H_0$

Otherwise:

→ Fail to reject $H_0$

The exact decision rule depends on whether the test is one-tailed or two-tailed.

---

## P-Value Approach

Compare the p-value with the significance level:

$$
p < \alpha
$$

→ Reject $H_0$

$$
p \geq \alpha
$$

→ Fail to reject $H_0$

As with hypothesis testing generally, we say **"fail to reject $H_0$"** rather than "accept $H_0$."

---

# 12. Assumptions of a One-Sample t-Test

The classical one-sample t-test generally assumes:

1. The observations are independent.
2. The data come from a population that is approximately Normally distributed, especially for small samples.
3. The population standard deviation is unknown.
4. The sample standard deviation $s$ is used to estimate $\sigma$.

For large samples, the test can be more robust to moderate departures from Normality, depending on the data and circumstances.

---

# 13. Basic One-Sample t-Test Example

Suppose we want to test whether the average weight of a population is 70 kg.

We collect a sample of:

$$
n = 10
$$

Suppose:

$$
\bar{x} = 72
$$

and:

$$
s = 3
$$

We test:

$$
H_0: \mu = 70
$$

against:

$$
H_1: \mu \neq 70
$$

The t-statistic is:

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

Substituting the values:

$$
t = \frac{72 - 70}{3/\sqrt{10}}
$$

$$
t \approx 2.108
$$

The degrees of freedom are:

$$
df = n - 1 = 9
$$

We can then use the t-distribution with 9 degrees of freedom to calculate the p-value or determine the critical t-value.

---

# 14. One-Sample t-Test — Medication and IQ Example

## Problem

Suppose the population average IQ is:

$$
\mu_0 = 100
$$

Researchers give a new medication to a sample of participants to determine whether the medication has:

- A positive effect
- A negative effect
- No effect

The sample contains:

$$
n = 30
$$

participants.

The sample has:

$$
\bar{x} = 140
$$

and:

$$
s = 20
$$

The confidence level is:

$$
95\%
$$

Therefore:

$$
\alpha = 1 - 0.95
$$

$$
\alpha = 0.05
$$

Since the population standard deviation is not given, we use a **one-sample t-test**.

---

# 15. Identify the Parameters

| Parameter | Value |
|---|---:|
| Hypothesized population mean $\mu_0$ | 100 |
| Sample size $n$ | 30 |
| Sample mean $\bar{x}$ | 140 |
| Sample standard deviation $s$ | 20 |
| Confidence level | 95% |
| Significance level $\alpha$ | 0.05 |

---

# 16. State the Hypotheses

The researchers want to determine whether the medication has either a positive or negative effect.

Therefore, this is a **two-tailed test**.

### Null Hypothesis

The null hypothesis states that the population mean remains equal to 100:

$$
H_0: \mu = 100
$$

### Alternative Hypothesis

The alternative hypothesis states that the population mean is different from 100:

$$
H_1: \mu \neq 100
$$

We are therefore checking both directions:

$$
\mu > 100
$$

and:

$$
\mu < 100
$$

---

# 17. Calculate Degrees of Freedom

For a one-sample t-test:

$$
df = n - 1
$$

Substituting:

$$
df = 30 - 1
$$

Therefore:

$$
\boxed{df = 29}
$$

---

# 18. Determine the Critical t-Value

We have:

- Confidence level = 95%
- $\alpha = 0.05$
- Two-tailed test
- $df = 29$

For a two-tailed test:

$$
\frac{\alpha}{2} = \frac{0.05}{2} = 0.025
$$

Using the t-table with:

$$
df = 29
$$

and:

$$
\alpha = 0.05
$$

for a two-tailed test, the critical value is approximately:

$$
t_{\text{critical}} = \pm 2.045
$$

Therefore, the decision boundaries are:

$$
-2.045
$$

and:

$$
+2.045
$$

---

# 19. Decision Rule

For this two-tailed test:

If:

$$
t < -2.045
$$

or:

$$
t > 2.045
$$

then:

$$
\boxed{\text{Reject }H_0}
$$

If:

$$
-2.045 \leq t \leq 2.045
$$

then:

$$
\boxed{\text{Fail to reject }H_0}
$$

The regions outside the critical values are the **rejection regions**.

---

# 20. Calculate the t-Statistic

The formula is:

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

Substitute the values:

$$
t = \frac{140 - 100}{20/\sqrt{30}}
$$

Therefore:

$$
t \approx 10.954
$$

So:

$$
\boxed{t \approx 10.95}
$$

---

# 21. Compare the t-Statistic with the Critical Value

We have:

$$
t \approx 10.95
$$

and:

$$
t_{\text{critical}} \approx \pm 2.045
$$

Since:

$$
10.95 > 2.045
$$

the calculated t-statistic lies in the rejection region.

Therefore:

$$
\boxed{\text{Reject }H_0}
$$

---

# 22. P-Value Approach

We can also make the decision using the p-value.

For a two-tailed test:

$$
p = P(|T| \geq |t_{\text{observed}}| \mid H_0)
$$

For this example, the p-value is extremely small:

$$
p < 0.0001
$$

Since:

$$
p < \alpha
$$

we reject $H_0$.

Therefore, both the **critical-value approach** and the **p-value approach** lead to the same decision.

---

# 23. Final Conclusion

The null hypothesis was:

$$
H_0: \mu = 100
$$

We rejected $H_0$.

Therefore, there is sufficient statistical evidence to conclude that the population mean IQ differs from 100 under the assumptions of the test.

Since the sample mean is:

$$
\bar{x} = 140 > 100
$$

the observed effect in this sample is in the **positive direction**.

### Important Interpretation

The statistical test provides evidence that the population mean differs from 100.

However, the statistical test alone does **not prove that the medication causes an increase in intelligence**.

A causal conclusion would require an appropriate experimental design and consideration of other factors.

---

# 24. Complete Flow of a One-Sample t-Test

```text
Population standard deviation unknown
                ↓
        One-Sample t-Test
                ↓
        State H₀ and H₁
                ↓
   Identify one/two-tailed test
                ↓
          Choose α
                ↓
       Calculate df = n − 1
                ↓
    Find critical t-value
                ↓
      Calculate t-statistic
                ↓
Compare t-statistic with critical value
                ↓
   Reject / Fail to reject H₀
                ↓
      Interpret the result
```

### P-Value Approach

```text
Calculate t-statistic
        ↓
   Calculate p-value
        ↓
 Compare p-value with α
        ↓
 p < α → Reject H₀
 p ≥ α → Fail to reject H₀
        ↓
 Interpret the result
```

---

# 25. Critical-Value vs P-Value Approach

| Critical-Value Approach | P-Value Approach |
|---|---|
| Calculate t-statistic | Calculate t-statistic |
| Find critical t-value | Calculate p-value |
| Compare t-statistic with critical boundary | Compare p-value with $\alpha$ |
| Determine rejection region | Determine statistical significance |
| Make decision about $H_0$ | Make decision about $H_0$ |

Both approaches should lead to the same statistical decision when applied correctly.

---

# 26. Student's t-Distribution and Sample Size

The t-distribution is especially important for small samples.

As the sample size increases:

$$
df = n - 1
$$

also increases.

As $df$ becomes large, the t-distribution approaches the Standard Normal distribution.

Therefore:

$$
t\text{-distribution}
\xrightarrow[df\to\infty]{}
\text{Standard Normal distribution}
$$

This explains why the difference between Z-tests and t-tests becomes smaller for large samples.

---

# 27. Using Python

The `scipy.stats` module provides tools for working with the Student's t-distribution and performing t-tests.

### Critical t-Value

```python
from scipy import stats

t_critical = stats.t.ppf(1 - alpha / 2, df)
```

### One-Sample t-Test

```python
result = stats.ttest_1samp(sample, popmean=100)

print(result.statistic)
print(result.pvalue)
```

The returned result contains the t-statistic and corresponding p-value.

---

# 28. Key Takeaways

- The **Student's t-distribution** is used when the population standard deviation is unknown and estimated from the sample.
- A **one-sample t-test** compares a sample mean with a hypothesized population mean.
- The t-statistic is:

$$
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
$$

- $s$ is the sample standard deviation.
- A one-sample t-test has:

$$
df = n - 1
$$

- For $n = 30$:

$$
df = 29
$$

- A $\neq$ alternative hypothesis produces a **two-tailed test**.
- A $<$ alternative hypothesis produces a **left-tailed test**.
- A $>$ alternative hypothesis produces a **right-tailed test**.
- Critical t-values depend on degrees of freedom and the significance level.
- The p-value approach uses:

$$
p < \alpha \Rightarrow \text{Reject }H_0
$$

$$
p \geq \alpha \Rightarrow \text{Fail to reject }H_0
$$

- We say **"fail to reject $H_0$"**, rather than "accept $H_0$".
- As degrees of freedom increase, the t-distribution approaches the Standard Normal distribution.
- In the medication/IQ example:

$$
df = 29
$$

$$
t \approx 10.95
$$

$$
t_{\text{critical}} \approx \pm 2.045
$$

Therefore:

$$
\boxed{\text{Reject }H_0}
$$

---

# Core Idea

$$
\boxed{
\sigma\ \text{known}
\rightarrow
\text{Z-test}
}
$$

$$
\boxed{
\sigma\ \text{unknown}
\rightarrow
\text{t-test}
}
$$

For a one-sample t-test:

$$
\boxed{
t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}}
}
$$

and:

$$
\boxed{
df = n - 1
}
$$

The t-test accounts for the additional uncertainty introduced by estimating the population standard deviation from the sample.

---

## Next Step

The next step is to practice the **one-sample t-test** using Python and work through:

1. Hypotheses
2. Sample mean
3. Sample standard deviation
4. Sample size
5. Degrees of freedom
6. t-statistic
7. Critical t-value
8. P-value
9. Final statistical conclusion
