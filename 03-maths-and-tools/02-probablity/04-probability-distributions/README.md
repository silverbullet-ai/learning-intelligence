# Probability Distributions

## Overview

A **probability distribution** describes how the probabilities of a random variable are distributed across its possible values.

In simple terms, a probability distribution tells us:

> **How likely are the possible values of a random variable?**

Probability distributions are fundamental to statistics and machine learning because they provide a mathematical way to model uncertainty in data.

---

## Random Variables

A **random variable** is a variable whose value is determined by the outcome of a random experiment.

Random variables are broadly divided into two types:

1. Discrete Random Variables
2. Continuous Random Variables

---

## 1. Discrete Random Variable

A **discrete random variable** takes values that can be counted.

Examples:

* Number obtained when rolling a die
* Number of students in a classroom
* Number of rooms in a house
* Number of emails received
* Number of defective products

### Example

For a six-sided die:

[
X \in {1,2,3,4,5,6}
]

The possible values can be explicitly listed and counted.

---

## 2. Continuous Random Variable

A **continuous random variable** can take any value within an interval.

Its possible values are theoretically uncountably infinite.

Examples:

* Height
* Weight
* Temperature
* Time
* Age
* House size

For example, height could be:

[
170.1,\ 170.15,\ 170.153,\ldots
]

There can theoretically be infinitely many possible values within an interval.

---

# PMF, PDF, and CDF

Three important functions used to describe probability distributions are:

1. **Probability Mass Function (PMF)**
2. **Probability Density Function (PDF)**
3. **Cumulative Distribution Function (CDF)**

PMF is primarily used with discrete random variables, while PDF is used with continuous random variables.

CDF can be used for **both discrete and continuous random variables**.

---

# 1. Probability Mass Function (PMF)

## Definition

The **Probability Mass Function (PMF)** gives the probability that a discrete random variable takes a particular value.

For a discrete random variable (X):

[
p(x)=P(X=x)
]

### Example: Rolling a Fair Die

Let:

[
X=\text{result of a die roll}
]

The possible values are:

[
X\in{1,2,3,4,5,6}
]

For a fair die:

[
P(X=x)=\frac{1}{6}
]

for every:

[
x\in{1,2,3,4,5,6}
]

Therefore:

[
P(X=1)=P(X=2)=\cdots=P(X=6)=\frac{1}{6}
]

---

## Properties of a PMF

A valid PMF must satisfy:

### 1. Non-negativity

[
P(X=x)\geq0
]

### 2. Total probability equals one

[
\sum_x P(X=x)=1
]

For a fair die:

[
\sum_{x=1}^{6}\frac{1}{6}=1
]

---

## PMF Visualization

A PMF is commonly visualized using separate bars or spikes because the possible values are discrete.

For example:

```text
Probability
   |
1/6|  ●   ●   ●   ●   ●   ●
   |  |   |   |   |   |   |
   +--------------------------> X
      1   2   3   4   5   6
```

The separation represents the discrete nature of the possible values.

---

# 2. Probability Density Function (PDF)

## Definition

The **Probability Density Function (PDF)** is used to describe the distribution of a continuous random variable.

A PDF is written as:

[
f(x)
]

Unlike a PMF, a PDF does **not** directly give the probability of an exact value.

Instead, probability is represented by the **area under the PDF curve**.

For an interval ([a,b]):

[
\boxed{
P(a\leq X\leq b)
================

\int_a^b f(x),dx
}
]

---

## Important Property

For a continuous random variable:

[
\boxed{
P(X=x)=0
}
]

for any individual exact point (x).

This does not mean that continuous random variables cannot take that value.

It means that a single point has zero width and therefore contributes zero area under the continuous density.

Instead, we calculate probabilities over intervals.

For example:

[
P(30\leq X\leq40)
]

is represented by the area under the PDF between (30) and (40).

---

## Properties of a PDF

### 1. Non-negativity

A PDF cannot be negative:

[
f(x)\geq0
]

### 2. Total area equals one

The total area under the PDF must equal (1):

[
\boxed{
\int_{-\infty}^{\infty}f(x),dx=1
}
]

### Important Note

A PDF value can be greater than (1).

What must equal (1) is the **total area under the curve**, not the height of the curve.

---

# 3. Cumulative Distribution Function (CDF)

## Definition

The **Cumulative Distribution Function (CDF)** gives the probability that a random variable is less than or equal to a particular value.

For a random variable (X):

[
\boxed{
F(x)=P(X\leq x)
}
]

CDFs can be used for **both discrete and continuous random variables**.

---

## Example: Fair Die

Suppose:

[
X\in{1,2,3,4,5,6}
]

For:

[
P(X\leq2)
]

we add the probabilities of (1) and (2):

[
P(X\leq2)
=========

P(X=1)+P(X=2)
]

# [

\frac16+\frac16
]

[
=\frac13
]

Therefore:

[
\boxed{
F(2)=\frac13
}
]

Similarly:

[
F(6)=P(X\leq6)=1
]

because all possible outcomes are included.

---

## CDF Properties

A CDF satisfies:

[
0\leq F(x)\leq1
]

It is also **non-decreasing**, meaning that it never decreases as (x) increases.

The limiting behavior is:

[
\lim_{x\to-\infty}F(x)=0
]

and:

[
\lim_{x\to\infty}F(x)=1
]

For a discrete random variable, the CDF has a **step-like shape**.

For a continuous random variable, the CDF is generally **smooth** when the PDF is continuous.

---

# Relationship Between PDF and CDF

For a continuous random variable, the CDF is related to the PDF through integration:

[
\boxed{
F(x)=\int_{-\infty}^{x}f(t),dt
}
]

If the CDF is differentiable, the PDF is its derivative:

[
\boxed{
f(x)=\frac{d}{dx}F(x)
}
]

Therefore:

[
\text{PDF} \xrightarrow{\text{integration}} \text{CDF}
]

and:

[
\text{CDF} \xrightarrow{\text{differentiation}} \text{PDF}
]

### Intuition

* **PDF** → describes probability density.
* **CDF** → describes accumulated probability.

---

# Common Probability Distributions

Probability distributions can take many different forms.

Some important distributions are:

---

## 1. Bernoulli Distribution

The **Bernoulli distribution** is a discrete distribution with exactly two possible outcomes.

Usually represented as:

[
X\in{0,1}
]

Examples:

* Success / Failure
* Yes / No
* Head / Tail
* Defective / Non-defective

It is described using a PMF.

---

## 2. Binomial Distribution

The **Binomial distribution** models the number of successes in a fixed number of independent Bernoulli trials.

For example:

> Number of Heads obtained in 10 coin tosses.

It is a discrete distribution and uses a PMF.

---

## 3. Normal Distribution

The **Normal distribution**, also called the **Gaussian distribution**, is a continuous probability distribution.

It has a characteristic bell-shaped curve.

Important characteristics include:

* Symmetry around the mean
* Bell-shaped curve
* Mean, median, and mode coincide for a standard normal distribution
* Described by parameters such as mean and standard deviation

The Normal distribution is one of the most important and widely used distributions in statistics and machine learning.

It uses a PDF.

---

## 4. Poisson Distribution

The **Poisson distribution** is a discrete distribution used to model the number of events occurring within a fixed interval of time or space when certain assumptions are appropriate.

Examples:

* Number of emails received per hour
* Number of calls received per minute
* Number of arrivals at a service desk
* Number of defects produced in a fixed length of material

It uses a PMF.

---

## 5. Log-Normal Distribution

A random variable follows a **log-normal distribution** if its logarithm follows a normal distribution.

It is a continuous distribution.

It can be useful for modeling positive, right-skewed quantities in appropriate contexts, such as:

* Some income distributions
* Certain biological measurements
* Some financial variables
* Some types of prices or sizes

It uses a PDF.

---

## 6. Uniform Distribution

In a uniform distribution, outcomes are equally likely within the specified support.

Uniform distributions can be:

* Discrete
* Continuous

### Discrete Uniform Distribution

Example:

A fair six-sided die.

[
P(X=x)=\frac16
]

for:

[
x\in{1,2,3,4,5,6}
]

### Continuous Uniform Distribution

A continuous random variable can be uniformly distributed over an interval such as:

[
a\leq X\leq b
]

In this case, the PDF is constant over the interval.

---

# Choosing PMF or PDF

The choice primarily depends on whether the random variable is discrete or continuous.

| Example          | Variable Type               | Typical Function |
| ---------------- | --------------------------- | ---------------- |
| Number of rooms  | Discrete                    | PMF              |
| Floor number     | Discrete                    | PMF              |
| Number of emails | Discrete                    | PMF              |
| Height           | Continuous                  | PDF              |
| Weight           | Continuous                  | PDF              |
| Temperature      | Continuous                  | PDF              |
| House size       | Continuous                  | PDF              |
| Price            | Often modeled as continuous | PDF              |

The underlying statistical model matters more than how the value happens to be stored in a dataset.

---

# Categorical Variables

Categorical variables represent categories rather than numerical measurements.

Examples:

* Location
* Gender category
* Product category
* Sea-side indicator
* Color

When probabilities are assigned to categories, they can be represented using a discrete probability distribution.

For example:

[
P(\text{Urban})=0.6
]

[
P(\text{Rural})=0.4
]

If categories are encoded as numbers such as (0) and (1), that encoding does not automatically make the variable continuous.

---

# House Price Dataset Example

Consider a hypothetical house-price dataset:

| Feature            | Typical Variable Type       | Probability Representation |
| ------------------ | --------------------------- | -------------------------- |
| House Size         | Continuous                  | PDF                        |
| Number of Rooms    | Discrete                    | PMF                        |
| Floor Number       | Discrete                    | PMF                        |
| Location           | Categorical                 | Discrete probabilities     |
| Sea-side Indicator | Binary / Discrete           | PMF                        |
| Price              | Often modeled as continuous | PDF                        |

Understanding the type and distribution of variables is useful in:

* Exploratory Data Analysis (EDA)
* Statistical analysis
* Feature engineering
* Model selection
* Probabilistic modeling
* Machine learning

---

# PMF vs PDF vs CDF

| Feature               | PMF                                 | PDF                           | CDF                    |
| --------------------- | ----------------------------------- | ----------------------------- | ---------------------- |
| Mainly used with      | Discrete variables                  | Continuous variables          | Both                   |
| Represents            | Probability of exact discrete value | Probability density           | Cumulative probability |
| Exact value           | (P(X=x))                            | (P(X=x)=0) for continuous (X) | (P(X\leq x))           |
| Total                 | (\sum P(X=x)=1)                     | (\int f(x)dx=1)               | Approaches (1)         |
| Typical visualization | Bars / spikes                       | Continuous curve              | Increasing curve       |
| Main operation        | Sum probabilities                   | Calculate area                | Accumulate probability |

---

# Key Takeaways

* A **probability distribution** describes how probability is distributed across the values of a random variable.
* Random variables can be **discrete** or **continuous**.
* **PMF** is used primarily for discrete random variables.
* **PDF** is used for continuous random variables.
* A PDF represents **probability density**, not probability at an exact point.
* For continuous variables:

[
P(X=x)=0
]

* Probability over an interval is calculated using the area under the PDF:

[
P(a\leq X\leq b)
================

\int_a^b f(x),dx
]

* **CDF** gives cumulative probability:

[
F(x)=P(X\leq x)
]

* For a continuous distribution:

[
f(x)=\frac{d}{dx}F(x)
]

* The total probability represented by a PMF is:

[
\sum_xP(X=x)=1
]

* The total area represented by a PDF is:

[
\int_{-\infty}^{\infty}f(x),dx=1
]

* Important distributions include **Bernoulli, Binomial, Normal, Poisson, Log-Normal, and Uniform**.
