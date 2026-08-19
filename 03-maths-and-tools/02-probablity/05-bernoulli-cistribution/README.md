
# Bernoulli Distribution

## Overview

The **Bernoulli Distribution** is one of the simplest discrete probability distributions.

It models a random experiment with exactly **two possible outcomes**.

These outcomes are commonly represented as:

- Success → \(1\)
- Failure → \(0\)

Examples include:

- Head / Tail
- Pass / Fail
- Yes / No
- Buy / Not Buy
- Defective / Non-defective

The Bernoulli Distribution is important because it forms the foundation of the **Binomial Distribution**.

---

## Definition

A random variable \(X\) follows a Bernoulli Distribution if it has exactly two possible outcomes:

\[
X\in\{0,1\}
\]

where:

- \(X=1\) represents success
- \(X=0\) represents failure

Let:

\[
P(X=1)=p
\]

Then:

\[
P(X=0)=1-p
\]

The probability parameter must satisfy:

\[
\boxed{0\leq p\leq1}
\]

---

## Parameters

The Bernoulli Distribution has one primary parameter:

\[
\boxed{p}
\]

where:

\[
p=P(X=1)
\]

The failure probability is derived from \(p\):

\[
q=1-p
\]

Therefore:

| Quantity        | Meaning                   |
| --------------- | ------------------------- |
| \(p\)           | Probability of success    |
| \(1-p\)         | Probability of failure    |
| \(X\)           | Bernoulli random variable |
| \(X\in\{0,1\}\) | Possible outcomes         |

> **Note:** \(q=1-p\) is derived from \(p\), so it is not an independent parameter.

---

## Characteristics

A Bernoulli Distribution:

- Is a **discrete probability distribution**
- Has exactly **two possible outcomes**
- Uses a **Probability Mass Function (PMF)**
- Has one primary parameter \(p\)
- Represents outcomes using \(0\) and \(1\)

### Outcome Representation

| Outcome | Random Variable |
| ------- | --------------: |
| Failure |           \(0\) |
| Success |           \(1\) |

---

# Probability Mass Function (PMF)

The PMF of a Bernoulli Distribution is:

\[
\boxed{
P(X=k)=p^k(1-p)^{1-k}
}
\]

where:

\[
k\in\{0,1\}
\]

---

## When \(k=1\)

For success:

\[
P(X=1)
======

p^1(1-p)^0
\]

Therefore:

\[
\boxed{
P(X=1)=p
}
\]

---

## When \(k=0\)

For failure:

\[
P(X=0)
======

p^0(1-p)^1
\]

Therefore:

\[
\boxed{
P(X=0)=1-p
}
\]

---

## Example

Suppose the probability of a customer purchasing a product is:

\[
p=0.6
\]

Then:

\[
P(X=1)=0.6
\]

and:

\[
P(X=0)=1-0.6=0.4
\]

The complete distribution is:

| \(X\) | Outcome | Probability |
| ----: | ------- | ----------: |
|     0 | Failure |         0.4 |
|     1 | Success |         0.6 |

The probabilities sum to:

\[
0.4+0.6=1
\]

---

# Examples of Bernoulli Trials

## Example 1: Coin Toss

Consider a fair coin.

Let:

- Head = Success
- Tail = Failure

Then:

\[
P(X=1)=0.5
\]

and:

\[
P(X=0)=0.5
\]

Therefore:

\[
X\sim\operatorname{Bernoulli}(0.5)
\]

---

## Example 2: Pass / Fail

Suppose the probability that a student passes an exam is:

\[
P(\text{Pass})=0.4
\]

Then:

\[
P(\text{Fail})=1-0.4=0.6
\]

Therefore:

\[
X\sim\operatorname{Bernoulli}(0.4)
\]

---

## Example 3: Smartphone Purchase

Suppose a company launches a new smartphone and estimates that a randomly selected user has a \(60\%\) probability of purchasing it.

Let:

- Buy = Success = \(1\)
- Don't Buy = Failure = \(0\)

Then:

\[
p=0.6
\]

and:

\[
1-p=0.4
\]

Therefore:

\[
X\sim\operatorname{Bernoulli}(0.6)
\]

This is a Bernoulli experiment because there are exactly two possible outcomes.

---

# Mean of Bernoulli Distribution

The expected value of a discrete random variable is:

\[
E[X]=\sum_x xP(X=x)
\]

For a Bernoulli random variable:

\[
X\in\{0,1\}
\]

Therefore:

\[
E[X]
====

0P(X=0)+1P(X=1)
\]

Substituting:

\[
E[X]
====

0(1-p)+1(p)
\]

Thus:

\[
\boxed{
E[X]=p
}
\]

Therefore, the mean of a Bernoulli Distribution is:

\[
\boxed{\mu=p}
\]

---

# Variance of Bernoulli Distribution

The variance of a random variable is:

\[
\operatorname(X)
================

E[X^2]-(E[X])^2
\]

For a Bernoulli random variable:

\[
X^2=X
\]

because:

\[
0^2=0
\]

and:

\[
1^2=1
\]

Therefore:

\[
E[X^2]=E[X]=p
\]

Since:

\[
E[X]=p
\]

we get:

\[
\operatorname(X)
================

p-p^2
\]

\[
=p(1-p)
\]

Therefore:

\[
\boxed{
\operatorname{Var}(X)=p(1-p)
}
\]

---

# Standard Deviation

Standard deviation is the square root of variance:

\[
\sigma=\sqrt{\operatorname{Var}(X)}
\]

Therefore:

\[
\boxed{
\sigma=\sqrt{p(1-p)}
}
\]

---

# Median

The median depends on the value of \(p\).

\[
\operatorname{Median}(X)=
\begin{cases}
0, & p<0.5\\[4pt]
\text{any value in }[0,1], & p=0.5\\[4pt]
1, & p>0.5
\end{cases}
\]

### Intuition

- If failure is more likely, the median is \(0\).
- If success is more likely, the median is \(1\).
- If both outcomes are equally likely, every value between \(0\) and \(1\) satisfies the definition of a median.

---

# Mode

The mode is the value with the highest probability.

### If:

\[
p>0.5
\]

then:

\[
\boxed{\text{Mode}=1}
\]

### If:

\[
p<0.5
\]

then:

\[
\boxed{\text{Mode}=0}
\]

### If:

\[
p=0.5
\]

then both \(0\) and \(1\) are modes.

---

# Important Properties

For:

\[
X\sim\operatorname{Bernoulli}(p)
\]

we have:

### Support

\[
X\in\{0,1\}
\]

### Mean

\[
\boxed{\mu=p}
\]

### Variance

\[
\boxed{\sigma^2=p(1-p)}
\]

### Standard Deviation

\[
\boxed{\sigma=\sqrt{p(1-p)}}
\]

### PMF

\[
\boxed{
P(X=k)=p^k(1-p)^{1-k}
}
\]

where:

\[
k\in\{0,1\}
\]

---

# Bernoulli Distribution vs Binomial Distribution

The Bernoulli Distribution describes **one trial** with two possible outcomes.

The Binomial Distribution describes the **number of successes across multiple independent Bernoulli trials**.

| Bernoulli                       | Binomial                        |
| ------------------------------- | ------------------------------- |
| One trial                       | \(n\) trials                    |
| Two possible outcomes per trial | Two possible outcomes per trial |
| Counts success in one trial     | Counts total successes          |
| Parameter:\(p\)                 | Parameters:\(n,p\)              |
| Example: One coin toss          | Example: 10 coin tosses         |

This relationship is important:

\[
\boxed
======

\text{Number of successes in repeated Bernoulli trials}
}
\]

The Binomial Distribution will be studied separately in the next topic.

---

# Bernoulli Distribution in Data Science

Bernoulli variables appear frequently in data science because many real-world outcomes are binary.

Examples include:

- Customer buys / does not buy
- Email spam / not spam
- Loan default / no default
- Disease present / absent
- Model prediction correct / incorrect
- Click / no click

Binary target variables can therefore often be represented using:

\[
X\in\{0,1\}
\]

Bernoulli probability models are also closely related to **binary classification** and **logistic regression**.

---

# Quick Revision

| Property            | Formula / Value           |
| ------------------- | ------------------------- |
| Type                | Discrete Distribution     |
| Outcomes            | \(0,1\)                   |
| Parameter           | \(p\)                     |
| Success Probability | \(p\)                     |
| Failure Probability | \(1-p\)                   |
| PMF                 | \(P(X=k)=p^k(1-p)^{1-k}\) |
| Mean                | \(p\)                     |
| Variance            | \(p(1-p)\)                |
| Standard Deviation  | \(\sqrt{p(1-p)}\)         |
| Support             | \(k\in\{0,1\}\)           |

---

# Key Takeaways

- The Bernoulli Distribution is the simplest discrete probability distribution.
- It models exactly **two possible outcomes**.
- The outcomes are commonly represented as \(0\) and \(1\).
- Its primary parameter is \(p\), the probability of success.
- The probability of failure is \(1-p\).
- Its PMF is:

\[
P(X=k)=p^k(1-p)^{1-k}
\]

- Its mean is:

\[
E[X]=p
\]

- Its variance is:

\[
\operatorname{Var}(X)=p(1-p)
\]

- Its standard deviation is:

\[
\sigma=\sqrt{p(1-p)}
\]

- A Binomial Distribution is based on repeated Bernoulli trials.

---

# Interview Questions

1. What is a Bernoulli Distribution?
2. Is Bernoulli Distribution discrete or continuous?
3. What are the possible outcomes of a Bernoulli random variable?
4. What is the parameter of a Bernoulli Distribution?
5. What is the PMF of a Bernoulli Distribution?
6. Derive the mean of a Bernoulli Distribution.
7. What is the variance of a Bernoulli Distribution?
8. What is the standard deviation of a Bernoulli Distribution?
9. What is the difference between Bernoulli and Binomial Distribution?
10. Give three real-world examples of Bernoulli trials.
