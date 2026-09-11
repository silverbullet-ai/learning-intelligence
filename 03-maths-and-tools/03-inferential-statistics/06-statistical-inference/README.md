# Statistical Inference

Statistical inference is the process of using sample data to reason about
unknown population characteristics and make decisions under uncertainty.

This section covers several important concepts that extend hypothesis testing
and provide a foundation for statistical reasoning in Data Science and
Machine Learning.

---

## Topics Covered

- Type I and Type II Errors
- Bayesian Statistics
- Independent Events
- Dependent Events
- Conditional Probability
- Bayes' Theorem
- Bayes' Theorem in Machine Learning
- Point Estimates
- Confidence Intervals
- Margin of Error
- Z-Test Confidence Intervals
- t-Test Confidence Intervals
- 95% Confidence Intervals

---

# 1. Type I and Type II Errors

## Concept of Errors in Hypothesis Testing

In hypothesis testing, there are two different perspectives:

### Reality

The null hypothesis ($H_0$) can actually be:

- True
- False

### Statistical Decision

Based on the hypothesis test, we can:

- Reject $H_0$
- Fail to reject $H_0$

Because our statistical decision may or may not match reality, there are
four possible outcomes.

---

## Four Possible Outcomes

| Reality | Our Decision | Outcome |
|---|---|---|
| $H_0$ is true | Reject $H_0$ | ❌ Type I Error |
| $H_0$ is true | Fail to reject $H_0$ | ✅ Correct |
| $H_0$ is false | Reject $H_0$ | ✅ Correct |
| $H_0$ is false | Fail to reject $H_0$ | ❌ Type II Error |

---

## Type I Error

A **Type I Error** occurs when we reject the null hypothesis when it is
actually true.

In short:

$$
\boxed{\text{True } H_0 \rightarrow \text{Reject } H_0}
$$

A Type I Error is associated with the significance level $\alpha$.

---

## Type II Error

A **Type II Error** occurs when we fail to reject the null hypothesis when
it is actually false.

In short:

$$
\boxed{\text{False } H_0 \rightarrow \text{Fail to Reject } H_0}
$$

---

## Complete Error Framework

| Decision \ Reality | $H_0$ True | $H_0$ False |
|---|---|---|
| **Reject $H_0$** | ❌ Type I Error | ✅ Correct |
| **Fail to reject $H_0$** | ✅ Correct | ❌ Type II Error |

### Easy Way to Remember

**Type I Error**

> Reject a true $H_0$.

**Type II Error**

> Fail to reject a false $H_0$.

---

# 2. Bayesian Statistics

**Bayesian statistics** is an approach to data analysis and parameter
estimation based on **Bayes' theorem**.

Bayes' theorem is particularly important in Machine Learning because it
forms the mathematical foundation of the **Naive Bayes algorithm**.

---

# 3. Independent Events

Two events are **independent** when the occurrence of one event does not
affect the probability of the other event.

### Example: Rolling a Die

A die has six possible outcomes:

$$
1,2,3,4,5,6
$$

For a fair die:

$$
P(1)=P(2)=\cdots=P(6)=\frac{1}{6}
$$

The outcome of one roll does not affect the next roll.

Therefore, consecutive die rolls are independent events.

### Example: Tossing a Coin

For a fair coin:

$$
P(\text{Head})=0.5
$$

$$
P(\text{Tail})=0.5
$$

The outcome of one toss does not affect the next toss.

Therefore, consecutive coin tosses are independent events.

---

# 4. Dependent Events

Two events are **dependent** when the occurrence of one event affects the
probability of another event.

### Example: Bag of Marbles

Suppose a bag contains:

- 3 yellow marbles
- 2 red marbles

Total:

$$
5
$$

The probability of selecting a red marble is:

$$
P(\text{Red})=\frac{2}{5}
$$

Suppose a red marble is selected and **not returned** to the bag.

The bag now contains:

- 3 yellow marbles
- 1 red marble

Total:

$$
4
$$

The probability of selecting a yellow marble is now:

$$
P(\text{Yellow}\mid\text{Red})=\frac{3}{4}
$$

The first event changed the situation for the second event.

Therefore, these events are dependent.

---

# 5. Conditional Probability

Conditional probability represents the probability of an event occurring
given that another event has already occurred.

It is written as:

$$
P(B\mid A)
$$

and means:

> Probability of $B$ given that $A$ has occurred.

For dependent events:

$$
P(A\cap B)=P(A)\times P(B\mid A)
$$

Where:

- $P(A)$ = probability of event $A$
- $P(B\mid A)$ = probability of $B$ given $A$
- $P(A\cap B)$ = probability that both $A$ and $B$ occur

### Marble Example

$$
P(\text{Red}\cap\text{Yellow})
=
P(\text{Red})P(\text{Yellow}\mid\text{Red})
$$

$$
=
\frac{2}{5}\times\frac{3}{4}
$$

$$
=
\frac{6}{20}
=
0.3
$$

---

# 6. Bayes' Theorem

The probability of $A$ and $B$ can be expressed in two ways:

$$
P(A\cap B)=P(A)P(B\mid A)
$$

and:

$$
P(A\cap B)=P(B)P(A\mid B)
$$

Since both expressions represent the same probability:

$$
P(A)P(B\mid A)
=
P(B)P(A\mid B)
$$

Rearranging gives Bayes' theorem:

$$
\boxed{
P(B\mid A)=
\frac{P(B)P(A\mid B)}{P(A)}
}
$$

An equivalent form is:

$$
\boxed{
P(A\mid B)=
\frac{P(A)P(B\mid A)}{P(B)}
}
$$

Both forms represent Bayes' theorem. The notation depends on which
conditional probability we want to calculate.

---

# 7. Understanding the Terms

For:

$$
P(B\mid A)=
\frac{P(B)P(A\mid B)}{P(A)}
$$

### $P(A)$

Probability of event $A$.

### $P(B)$

Probability of event $B$.

### $P(A\mid B)$

Probability of $A$ given that $B$ has already occurred.

### $P(B\mid A)$

Probability of $B$ given that $A$ has already occurred.

---

# 8. Bayes' Theorem in Machine Learning

Bayes' theorem becomes particularly useful in Machine Learning.

Consider a dataset containing:

| Feature | Meaning |
|---|---|
| $X_1$ | Size of house |
| $X_2$ | Number of rooms |
| $X_3$ | Location |
| $Y$ | Price |

The input features are:

$$
X_1,X_2,X_3
$$

The output is:

$$
Y
$$

We can express the probability of the output given the input features as:

$$
P(Y\mid X_1,X_2,X_3)
$$

Using Bayes' theorem:

$$
P(Y\mid X_1,X_2,X_3)
=
\frac{
P(Y)P(X_1,X_2,X_3\mid Y)
}{
P(X_1,X_2,X_3)
}
$$

This forms part of the mathematical foundation used by the
**Naive Bayes algorithm**.

---

# 9. Why Bayes' Theorem Matters for AI/ML

Bayesian reasoning allows us to reason about the probability of an outcome
given observed information.

In Machine Learning:

$$
\text{Observed Features}
\rightarrow
\text{Probability of Possible Output}
$$

For example:

$$
X_1,X_2,X_3
\rightarrow
P(Y\mid X_1,X_2,X_3)
$$

This idea becomes particularly important when studying **Naive Bayes**.

---

# 10. Point Estimate

A **point estimate** is a single value used to estimate an unknown
population parameter.

For the population mean:

$$
\boxed{\bar{x}=\text{Point Estimate}}
$$

For example, if:

$$
\bar{x}=2.5
$$

then $2.5$ is the point estimate of the population mean.

Although a point estimate is useful, different samples can produce
different sample means.

Therefore, it can be useful to provide a range of plausible values instead
of a single number.

---

# 11. Confidence Interval

A **confidence interval** provides a range around a point estimate.

A general confidence interval can be written as:

$$
\boxed{
\text{Confidence Interval}
=
\text{Point Estimate}
\pm
\text{Margin of Error}
}
$$

For the population mean:

$$
\boxed{
CI=\bar{x}\pm\text{Margin of Error}
}
$$

The interval contains:

- Lower confidence limit
- Upper confidence limit

---

# 12. Margin of Error

The **margin of error** determines how far we move from the point estimate
to construct the confidence interval.

For a Z-based confidence interval:

$$
\boxed{
ME=
Z_{\alpha/2}
\frac{\sigma}{\sqrt{n}}
}
$$

Therefore:

$$
\boxed{
CI=
\bar{x}
\pm
Z_{\alpha/2}
\frac{\sigma}{\sqrt{n}}
}
$$

Where:

- $\bar{x}$ = sample mean / point estimate
- $Z_{\alpha/2}$ = critical Z-value
- $\sigma$ = population standard deviation
- $n$ = sample size

---

# 13. Z-Test vs t-Test Confidence Interval

## Z-Based Confidence Interval

When the population standard deviation is known:

$$
\boxed{
CI=
\bar{x}
\pm
Z_{\alpha/2}
\frac{\sigma}{\sqrt{n}}
}
$$

The critical value comes from the standard Normal distribution.

---

## t-Based Confidence Interval

When the population standard deviation is unknown and the sample standard
deviation is used:

$$
\boxed{
CI=
\bar{x}
\pm
t_{\alpha/2}
\frac{s}{\sqrt{n}}
}
$$

The critical value comes from the t-distribution.

Degrees of freedom:

$$
\boxed{df=n-1}
$$

---

# 14. 95% Confidence Interval

Suppose the confidence level is:

$$
95\%
$$

Then:

$$
\alpha=1-0.95
$$

$$
\alpha=0.05
$$

For a two-sided confidence interval:

$$
\frac{\alpha}{2}=0.025
$$

The corresponding critical Z-values are approximately:

$$
\boxed{-1.96,\,+1.96}
$$

Therefore, the central region contains 95% of the probability under the
standard Normal distribution.

---

# 15. Example — CAT Exam Scores

Suppose:

- Population standard deviation: $\sigma=100$
- Sample size: $n=25$
- Sample mean: $\bar{x}=520$
- Confidence level: $95\%$

Since the population standard deviation is known, a Z-based confidence
interval is used in this example.

### Step 1: Determine $\alpha$

$$
\alpha=1-0.95=0.05
$$

For a two-sided 95% confidence interval:

$$
Z_{\alpha/2}=1.96
$$

### Step 2: Calculate the Margin of Error

$$
ME=
1.96\frac{100}{\sqrt{25}}
$$

Since:

$$
\sqrt{25}=5
$$

we get:

$$
ME=
1.96\times20
$$

$$
\boxed{ME=39.2}
$$

### Step 3: Calculate the Confidence Interval

$$
CI=520\pm39.2
$$

Lower limit:

$$
520-39.2=480.8
$$

Upper limit:

$$
520+39.2=559.2
$$

Therefore:

$$
\boxed{480.8\leq\mu\leq559.2}
$$

The interval is:

$$
\boxed{[480.8,\;559.2]}
$$

---

# 16. Confidence Interval and Hypothesis Testing

Confidence intervals are closely connected to hypothesis testing.

For a 95% two-sided confidence interval:

- Central region = 95%
- Left tail = 2.5%
- Right tail = 2.5%

The corresponding standard Normal critical values are:

$$
-1.96,\;+1.96
$$

The confidence interval provides a range of plausible values for the
population parameter, while hypothesis testing provides a formal decision
about a specified null hypothesis.

---

# 17. Statistical Inference Workflow

The concepts in this section can be connected as:

$$
\text{Sample Data}
\rightarrow
\text{Point Estimate}
\rightarrow
\text{Uncertainty}
\rightarrow
\text{Confidence Interval}
$$

Hypothesis testing introduces another decision-making perspective:

$$
H_0
\rightarrow
\text{Test Statistic}
\rightarrow
\text{Decision}
\rightarrow
\text{Possible Error}
$$

Bayesian reasoning provides another way to reason about uncertainty:

$$
\text{Observed Evidence}
\rightarrow
\text{Updated Probability}
$$

Together, these concepts form important foundations for statistical
reasoning in Data Science and Machine Learning.

---

# Key Takeaways

- **Type I Error:** Reject $H_0$ when $H_0$ is actually true.
- **Type II Error:** Fail to reject $H_0$ when $H_0$ is actually false.
- Independent events do not affect each other's probabilities.
- Dependent events affect the probability of subsequent events.
- Conditional probability represents the probability of an event given
  another event.
- Bayes' theorem allows us to calculate conditional probabilities using
  related probabilities.
- Bayes' theorem forms an important mathematical foundation for
  **Naive Bayes**.
- A **point estimate** is a single value used to estimate a population
  parameter.
- A **confidence interval** provides a range around a point estimate.
- The **margin of error** determines the distance from the point estimate
  to the confidence limits.
- Z-based confidence intervals use the population standard deviation
  $\sigma$.
- t-based confidence intervals use the sample standard deviation $s$.
- For a t-based interval, degrees of freedom are $df=n-1$.
- A 95% confidence interval corresponds to $\alpha=0.05$ and critical
  Z-values of approximately $\pm1.96$ for a two-sided interval.

---

## Core Idea

> **Statistical inference allows us to reason about populations, uncertainty,
> probability, and decisions using sample data.**