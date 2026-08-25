# Uniform Distribution

## Overview

A **Uniform Distribution** is a probability distribution in which outcomes are equally likely within a specified range or set of outcomes.

There are two main types:

1. **Continuous Uniform Distribution**
2. **Discrete Uniform Distribution**

The key idea is:

> **Uniform Distribution → Equal likelihood**

However, "equal likelihood" has a slightly different meaning for continuous and discrete variables.

---

# 1. Continuous Uniform Distribution

## Definition

A **Continuous Uniform Distribution** is a probability distribution for a continuous random variable where the **probability density is constant** over a specified interval.

It is also called the **Rectangular Distribution** because its PDF has a rectangular shape.

It is represented as:

$$
X \sim U(a,b)
$$

where:

- $a$ = Lower bound
- $b$ = Upper bound
- $a < b$

---

## Type

- Continuous Random Variable
- Continuous Probability Distribution
- Uses **Probability Density Function (PDF)**

---

## Important Idea

For a continuous uniform distribution, the **probability density is constant** between $a$ and $b$.

However, an individual point has zero probability:

$$
P(X=x)=0
$$

Probability is calculated over an **interval**.

For example:

$$
P(c \leq X \leq d)
$$

is the area under the PDF between $c$ and $d$.

---

# PDF

The Probability Density Function is:

$$
f(x)=
\begin{cases}
\frac{1}{b-a}, & a\leq x\leq b\\
0, & \text{otherwise}
\end{cases}
$$

Therefore, between $a$ and $b$:

$$
f(x)=\frac{1}{b-a}
$$

Outside the interval:

$$
f(x)=0
$$

---

## Why Is the PDF Constant?

The total area under a PDF must equal 1.

For the uniform distribution, the graph is a rectangle with:

- Width = $b-a$
- Height = $\frac{1}{b-a}$

Therefore:

$$
\text{Area}
=
(b-a)\times\frac{1}{b-a}
=1
$$

This satisfies the total probability requirement.

---

# CDF

The Cumulative Distribution Function is:

$$
F(x)=
\begin{cases}
0, & x<a\\
\frac{x-a}{b-a}, & a\leq x\leq b\\
1, & x>b
\end{cases}
$$

The CDF represents:

$$
F(x)=P(X\leq x)
$$

---

# Probability Between Two Values

For:

$$
a\leq c\leq d\leq b
$$

the probability is:

$$
P(c\leq X\leq d)
=
\frac{d-c}{b-a}
$$

In other words:

$$
\boxed{
\text{Probability}
=
\frac{\text{Length of desired interval}}
{\text{Length of total interval}}
}
$$

This is one of the easiest ways to understand the Continuous Uniform Distribution.

---

# Mean

The mean of a Continuous Uniform Distribution is:

$$
\boxed{
\mu=\frac{a+b}{2}
}
$$

It is simply the midpoint of the interval.

---

# Median

The median is also:

$$
\boxed{
\text{Median}=\frac{a+b}{2}
}
$$

Therefore:

$$
\text{Mean}=\text{Median}
$$

---

# Variance

The variance is:

$$
\boxed{
\sigma^2=\frac{(b-a)^2}{12}
}
$$

---

# Standard Deviation

The standard deviation is:

$$
\boxed{
\sigma=\frac{b-a}{\sqrt{12}}
}
$$

---

# Example 1: Daily Candy Sales

Suppose the number of candies sold per day is modeled as a Continuous Uniform Distribution between:

$$
a=10
$$

and:

$$
b=40
$$

Therefore:

$$
X\sim U(10,40)
$$

Find:

$$
P(15\leq X\leq30)
$$

## Step 1: Total Interval

$$
40-10=30
$$

## Step 2: Desired Interval

$$
30-15=15
$$

## Step 3: Calculate Probability

$$
P(15\leq X\leq30)
=
\frac{30-15}{40-10}
=
\frac{15}{30}
=0.5
$$

Therefore:

$$
\boxed{P(15\leq X\leq30)=0.5}
$$

or:

$$
\boxed{50\%}
$$

---

# Example 2: Probability of at Least 20

Using:

$$
X\sim U(10,40)
$$

find:

$$
P(X\geq20)
$$

The desired interval is:

$$
20\leq X\leq40
$$

Its length is:

$$
40-20=20
$$

Therefore:

$$
P(X\geq20)
=
\frac{20}{30}
=
\frac{2}{3}
\approx0.6667
$$

Therefore:

$$
\boxed{P(X\geq20)\approx66.67\%}
$$

---

# Key Characteristics of Continuous Uniform Distribution

- Continuous Random Variable
- Constant probability density between $a$ and $b$
- Rectangular PDF
- Defined over a finite interval
- Probability outside the interval is zero
- Individual points have probability zero
- Probability is calculated using area under the PDF

---

# 2. Discrete Uniform Distribution

## Definition

A **Discrete Uniform Distribution** is a probability distribution in which a finite set of discrete outcomes are **equally likely**.

Examples include:

- Rolling a fair die
- Tossing a fair coin
- Randomly selecting one equally likely option

It uses a **Probability Mass Function (PMF)**.

---

## Type

- Discrete Random Variable
- Discrete Probability Distribution
- Uses **Probability Mass Function (PMF)**

---

# PMF

If there are $n$ equally likely outcomes, then:

$$
\boxed{
P(X=x)=\frac{1}{n}
}
$$

for every possible outcome $x$.

For consecutive integer outcomes from $a$ to $b$:

$$
n=b-a+1
$$

Therefore:

$$
P(X=x)=\frac{1}{b-a+1}
$$

---

# Example: Rolling a Fair Die

A fair die has six possible outcomes:

$$
\{1,2,3,4,5,6\}
$$

Each outcome has equal probability:

$$
P(X=1)=P(X=2)=\cdots=P(X=6)=\frac{1}{6}
$$

Therefore:

$$
P(X=x)=\frac{1}{6}
$$

for:

$$
x\in\{1,2,3,4,5,6\}
$$

---

# Mean of Discrete Uniform Distribution

For consecutive integer outcomes from $a$ to $b$:

$$
\boxed{
\mu=\frac{a+b}{2}
}
$$

For a fair die:

$$
\mu=\frac{1+6}{2}=3.5
$$

Notice that 3.5 is not itself an outcome.

The mean does not have to be one of the possible values of the random variable.

---

# Median

For consecutive equally spaced outcomes:

$$
\boxed{
\text{Median}=\frac{a+b}{2}
}
$$

For a fair die:

$$
\text{Median}=3.5
$$

---

# Variance of Discrete Uniform Distribution

For consecutive integer outcomes from $a$ to $b$, where:

$$
n=b-a+1
$$

the variance is:

$$
\boxed{
\sigma^2=\frac{n^2-1}{12}
}
$$

For a fair six-sided die:

$$
n=6
$$

Therefore:

$$
\sigma^2
=
\frac{6^2-1}{12}
=
\frac{35}{12}
$$

---

# Example: Fair Coin

A fair coin has two equally likely outcomes:

```text
Heads
Tails
```

Therefore:

$$
P(\text{Heads})=\frac{1}{2}
$$

and:

$$
P(\text{Tails})=\frac{1}{2}
$$

This is a Discrete Uniform Distribution over two outcomes.

---

# Continuous vs Discrete Uniform Distribution

| Feature | Continuous Uniform | Discrete Uniform |
|---|---|---|
| Variable | Continuous | Discrete |
| Function | PDF | PMF |
| Outcomes | Infinitely many values in an interval | Finite set of outcomes |
| Equal property | Constant probability density | Equal probability for each outcome |
| Individual value probability | $P(X=x)=0$ | $P(X=x)=1/n$ |
| Example | Random value between 0 and 1 | Fair die |
| Shape | Rectangular PDF | Equal-height PMF bars |

---

# Applications

## Continuous Uniform Distribution

Examples include:

- Random values generated within fixed limits
- Simulations with bounded random variables
- Modeling an unknown value assumed equally likely within a fixed interval
- Some bounded waiting-time models

> A real-world process should not automatically be modeled as Uniform merely because it has a minimum and maximum. The assumption of equal density across the interval must be reasonable.

## Discrete Uniform Distribution

Examples include:

- Rolling a fair die
- Tossing a fair coin
- Randomly selecting one equally likely option
- Random integer generation when every allowed integer has equal probability

---

# Uniform Distribution vs Normal Distribution

| Feature | Uniform | Normal |
|---|---|---|
| Shape | Rectangular | Bell-shaped |
| Equal density | Yes, within its interval | No |
| Symmetric | Yes | Yes |
| Continuous version | Yes | Yes |
| Mean | $(a+b)/2$ | $\mu$ |
| Main spread parameter | Interval width | $\sigma$ |

The key distinction is:

> **Uniform Distribution → Constant density across its range**

> **Normal Distribution → Density is highest near the mean and decreases toward the tails**

---

# Key Takeaways

- Uniform Distribution represents equal likelihood within a defined set or range.
- It has both **continuous** and **discrete** forms.
- Continuous Uniform Distribution uses a **PDF**.
- Discrete Uniform Distribution uses a **PMF**.
- Continuous Uniform PDF:

$$
f(x)=\frac{1}{b-a}
$$

for:

$$
a\leq x\leq b
$$

- Continuous Uniform Mean:

$$
\mu=\frac{a+b}{2}
$$

- Continuous Uniform Variance:

$$
\sigma^2=\frac{(b-a)^2}{12}
$$

- Continuous Uniform Standard Deviation:

$$
\sigma=\frac{b-a}{\sqrt{12}}
$$

- Discrete Uniform PMF:

$$
P(X=x)=\frac{1}{n}
$$

- For consecutive integer outcomes:

$$
n=b-a+1
$$

---

# Interview Questions

1. What is a Uniform Distribution?
2. What are the two types of Uniform Distribution?
3. What is a Continuous Uniform Distribution?
4. What is a Discrete Uniform Distribution?
5. Why is the Continuous Uniform Distribution called the Rectangular Distribution?
6. What is the PDF of a Continuous Uniform Distribution?
7. What is the CDF of a Continuous Uniform Distribution?
8. What is the PMF of a Discrete Uniform Distribution?
9. What are the parameters of a Continuous Uniform Distribution?
10. What is the mean of a Continuous Uniform Distribution?
11. What is the variance of a Continuous Uniform Distribution?
12. Why does a fair die follow a Discrete Uniform Distribution?
13. What is the difference between PDF and PMF?
14. What is the probability of an exact point in a Continuous Uniform Distribution?
15. What is the difference between Uniform and Normal Distribution?

---

# Quick Revision

## Continuous Uniform

$$
X\sim U(a,b)
$$

PDF:

$$
f(x)=\frac{1}{b-a}
$$

for:

$$
a\leq x\leq b
$$

Mean:

$$
\mu=\frac{a+b}{2}
$$

Variance:

$$
\sigma^2=\frac{(b-a)^2}{12}
$$

Standard Deviation:

$$
\sigma=\frac{b-a}{\sqrt{12}}
$$

---

## Discrete Uniform

For $n$ equally likely outcomes:

$$
P(X=x)=\frac{1}{n}
$$

For consecutive integers from $a$ to $b$:

$$
n=b-a+1
$$

Mean:

$$
\mu=\frac{a+b}{2}
$$
