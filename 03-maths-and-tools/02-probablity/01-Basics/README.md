# Probability Basics

## Overview

Probability is the mathematical study of **uncertainty and random events**.

It helps us quantify how likely an event is to occur.

Probability is fundamental to statistics, data science, and machine learning because many real-world problems involve uncertainty.

Examples include:

* The probability of getting heads when tossing a coin.
* The probability of rolling a particular number on a die.
* The probability that a customer will purchase a product.
* The probability that a machine-learning model makes a correct prediction.

---

## What Is Probability?

The probability of an event describes how likely that event is to occur.

For an event $A$, probability is represented as:

$$
P(A)
$$

For equally likely outcomes, the probability of an event can be calculated as:

$$
P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of possible outcomes}}
$$

### Example

Consider a fair six-sided die.

The probability of rolling a $4$ is:

$$
P(4) = \frac{1}{6}
$$

because there is one favorable outcome and six possible outcomes.

---

## Sample Space

The **sample space** is the set of all possible outcomes of a random experiment.

It is commonly represented by:

$$
S
$$

### Example

For a coin toss:

$$
S = \{\text{Heads}, \text{Tails}\}
$$

For a six-sided die:

$$
S = \{1, 2, 3, 4, 5, 6\}
$$

---

## Event

An **event** is a collection of one or more outcomes from the sample space.

An event is commonly represented by a capital letter such as $A$, $B$, or $C$.

### Example

When rolling a die, the event of getting an even number is:

$$
A = \{2, 4, 6\}
$$

Therefore:

$$
P(A) = \frac{3}{6} = \frac{1}{2}
$$

---

## Range of Probability

Probability always lies between $0$ and $1$:

$$
0 \leq P(A) \leq 1
$$

where:

* $P(A) = 0$ means the event is **impossible**.
* $P(A) = 1$ means the event is **certain**.
* $0 < P(A) < 1$ means the event has some degree of uncertainty.

Probability can also be expressed as a percentage.

For example:

$$
P(A) = 0.75 = 75\%
$$

---

## Complement of an Event

The **complement** of an event $A$ represents the event that $A$ does not occur.

It is written as:

$$
A^c
$$

The probability of the complement is:

$$
P(A^c) = 1 - P(A)
$$

### Example

If the probability of rain tomorrow is:

$$
P(\text{Rain}) = 0.3
$$

then the probability that it does not rain is:

$$
P(\text{No Rain}) = 1 - 0.3 = 0.7
$$

Therefore:

$$
P(A) + P(A^c) = 1
$$

---

## Key Terminology

| Term | Meaning |
| --- | --- |
| **Experiment** | A process that produces an outcome |
| **Outcome** | A single possible result |
| **Sample Space** | Set of all possible outcomes |
| **Event** | One or more outcomes of interest |
| **Probability** | Numerical measure of how likely an event is |
| **Complement** | The event that the original event does not occur |

---

## Why Probability Matters in Data Science

Probability provides the mathematical foundation for handling uncertainty in data.

It is used in:

* Statistical inference
* Machine learning
* Bayesian statistics
* Classification
* Risk analysis
* Forecasting
* Natural language processing
* Generative AI
* A/B testing

Many machine-learning models ultimately estimate probabilities.

For example, a classification model might produce:

$$
P(\text{Spam} \mid \text{Email}) = 0.92
$$

meaning the model estimates a $92\%$ probability that the email is spam.

---

## Summary

The fundamental ideas covered in this section are:

* Probability measures uncertainty.
* A sample space contains all possible outcomes.
* An event is one or more outcomes of interest.
* Probability ranges from $0$ to $1$.
* $0$ represents an impossible event.
* $1$ represents a certain event.
* The complement of an event represents its non-occurrence.
* The complement rule is:

$$
P(A^c) = 1 - P(A)
$$

These concepts form the foundation for more advanced probability rules, including the **Addition Rule** and **Multiplication Rule**.
