# Random Variables

## Overview

Random Variables are one of the fundamental concepts in **Probability, Statistics, Machine Learning, and Deep Learning**.

They provide a mathematical way to represent the outcomes of random experiments using numerical values.

Almost every probability distribution, statistical model, and machine learning algorithm is built upon the concept of random variables.

---

# What is a Random Variable?

A **Random Variable** is a function that assigns a numerical value to each outcome of a random experiment.

It is usually represented using capital letters such as:

- X
- Y
- Z

Unlike a normal mathematical variable, the value of a random variable depends on the outcome of a random experiment.

---

# Mathematical Intuition

Consider the equation:

```text
y = 5x + 2
```

Here, **x** is a normal mathematical variable.

| x | y = 5x + 2 |
|---|-----------:|
| 1 | 7 |
| 2 | 12 |
| 3 | 17 |

The value of **x** is chosen directly.

A random variable, however, receives its value only after a random experiment is performed.

---

# Random Variable vs Normal Variable

A normal variable can be assigned any value directly.

A random variable obtains its value from the outcome of a random experiment.

Example:

```text
Experiment

↓

Toss a Coin

↓

Outcome

Head
Tail

↓

Random Variable X

Head → 0

Tail → 1
```

The numbers assigned are completely arbitrary.

For example:

```text
Head → 1

Tail → 0
```

or

```text
Head → 10

Tail → 20
```

The important idea is that the random variable maps outcomes to numbers.

---

# Definition

```text
Random Experiment

↓

Possible Outcomes

↓

Random Variable (X)

↓

Numerical Values
```

---

# Example 1: Tossing a Coin

Experiment:

```text
Toss a Coin
```

Possible outcomes:

```text
Head

Tail
```

Define the random variable:

```text
X =

{

0, if Head occurs

1, if Tail occurs

}
```

| Experiment | Outcome | X |
|------------|---------|---|
| Toss Coin | Head | 0 |
| Toss Coin | Tail | 1 |

---

# Example 2: Rolling a Fair Die

Experiment:

```text
Roll a Fair Die
```

Possible outcomes:

```text
1

2

3

4

5

6
```

Define:

```text
X = Outcome of the Die
```

Possible values:

```text
1, 2, 3, 4, 5, 6
```

---

# Types of Random Variables

```text
Random Variables

│

├── Discrete Random Variable

│

└── Continuous Random Variable
```

---

# 1. Discrete Random Variable

A **Discrete Random Variable** takes countable numerical values.

The possible values are finite or countably infinite.

---

## Examples

### Tossing a Coin

```text
0

1
```

---

### Rolling a Die

```text
1

2

3

4

5

6
```

---

### Number of Students Present

```text
0

1

2

...

100
```

---

### Number of Cars Passing

```text
0

1

2

3

...
```

---

## Characteristics

- Countable values
- Usually whole numbers
- Finite or countably infinite outcomes

---

# 2. Continuous Random Variable

A **Continuous Random Variable** can take any value within an interval.

These values are measurable and may contain decimal values.

---

## Rainfall

```text
0 inches

1.2 inches

4.56 inches

8.734 inches
```

---

## Height

```text
150 cm

165.3 cm

170.82 cm

182.14 cm
```

---

## Temperature

```text
25°C

25.45°C

26.781°C
```

---

## Characteristics

- Infinite values within a range
- Decimal values allowed
- Measured rather than counted

---

# Discrete vs Continuous Random Variables

| Discrete Random Variable | Continuous Random Variable |
|---------------------------|----------------------------|
| Countable values | Infinite measurable values |
| Usually whole numbers | Decimal values allowed |
| Example: Die Roll | Example: Height |
| Example: Number of Children | Example: Rainfall |

---

# Experiment vs Random Variable

These are different concepts.

### Example 1

Experiment:

```text
Roll a Die
```

Outcome:

```text
1

2

3

4

5

6
```

Random Variable:

```text
X = Outcome of the Die
```

---

### Example 2

Experiment:

```text
Toss a Coin
```

Outcome:

```text
Head

Tail
```

Random Variable:

```text
Head → 0

Tail → 1
```

---

# Why Do We Use Random Variables?

Instead of working with labels such as:

```text
Head

Tail
```

we convert them into numbers:

```text
0

1
```

This enables us to:

- Calculate probabilities
- Compute expected values
- Compute variance
- Build probability distributions
- Develop Machine Learning algorithms
- Perform statistical analysis

Most statistical formulas require numerical values, making random variables essential.

---

# Probability Distribution

Once a random variable is defined, we can describe how likely each value is using a probability distribution.

Examples:

- Discrete Random Variables → Probability Mass Function (PMF)
- Continuous Random Variables → Probability Density Function (PDF)

These topics are covered in the next lessons.

---

# Summary

```text
Random Experiment

↓

Possible Outcomes

↓

Random Variable

↓

Numerical Values

↓

Probability Distribution
```

---

# Examples at a Glance

| Experiment | Random Variable | Type |
|------------|-----------------|------|
| Toss a Coin | Head → 0, Tail → 1 | Discrete |
| Roll a Die | 1–6 | Discrete |
| Number of Customers | 0,1,2,… | Discrete |
| Height | 150.5, 175.2,… | Continuous |
| Weight | 65.3, 80.6,… | Continuous |
| Rainfall | 0.2, 3.75,… | Continuous |

---

# Interview Questions

### What is a Random Variable?

A random variable is a function that assigns numerical values to the outcomes of a random experiment.

---

### Why is it called a Random Variable?

Because its value depends on the outcome of a random experiment.

---

### What are the two types of Random Variables?

- Discrete Random Variable
- Continuous Random Variable

---

### Give examples of Discrete Random Variables.

- Tossing a Coin
- Rolling a Die
- Number of Students
- Number of Customers

---

### Give examples of Continuous Random Variables.

- Height
- Weight
- Temperature
- Rainfall

---

### What is the difference between Discrete and Continuous Random Variables?

| Discrete | Continuous |
|-----------|------------|
| Countable values | Infinite measurable values |
| Usually whole numbers | Decimal values allowed |
| Example: Die Roll | Example: Height |

---

# Key Takeaways

- A Random Variable converts the outcomes of a random experiment into numerical values.
- Random Variables are represented using capital letters such as X, Y, and Z.
- Random Variables are classified as Discrete or Continuous.
- Random Variables form the foundation of Probability Distributions, Statistics, Machine Learning, and Deep Learning.