
# Addition Rule

## Overview

The **Addition Rule** is used to calculate the probability that **at least one of multiple events occurs**.

It is associated with the logical operation **OR**.

For two events $A$ and $B$, the general Addition Rule is:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

where:

* $A \cup B$ means **A or B or both**.
* $A \cap B$ means **A and B occurring together**.

The rule depends on whether the events are **mutually exclusive** or **non-mutually exclusive**.

---

## Union of Events

The **union** of two events contains all outcomes that belong to $A$, $B$, or both.

It is represented as:

$$
A \cup B
$$

The union corresponds to the logical **OR**.

### Example

Suppose we roll a die.

Let:

$$
A = \{2, 4, 6\}
$$

represent rolling an even number.

Let:

$$
B = \{4, 5, 6\}
$$

represent rolling a number greater than $3$.

Then:

$$
A \cup B = \{2, 4, 5, 6\}
$$

The outcomes $4$ and $6$ belong to both events.

---

## Intersection of Events

The **intersection** contains outcomes that belong to both events.

It is represented as:

$$
A \cap B
$$

The intersection corresponds to the logical **AND**.

Using the previous example:

$$
A = \{2, 4, 6\}
$$

and:

$$
B = \{4, 5, 6\}
$$

Therefore:

$$
A \cap B = \{4, 6\}
$$

---

## General Addition Rule

For any two events $A$ and $B$:

$$
\boxed{P(A \cup B) = P(A) + P(B) - P(A \cap B)}
$$

The intersection term is subtracted because outcomes belonging to both events would otherwise be counted twice.

### Example

Suppose:

$$
P(A) = 0.5
$$

$$
P(B) = 0.5
$$

and:

$$
P(A \cap B) = 0.3333
$$

Then:

$$
P(A \cup B) = 0.5 + 0.5 - 0.3333
$$

$$
P(A \cup B) \approx 0.6667
$$

---

## Mutually Exclusive Events

Two events are **mutually exclusive** when they cannot occur at the same time.

Therefore:

$$
A \cap B = \varnothing
$$

and:

$$
P(A \cap B) = 0
$$

The Addition Rule simplifies to:

$$
\boxed{P(A \cup B) = P(A) + P(B)}
$$

### Example

When rolling a single die:

* $A$: rolling a $2$
* $B$: rolling a $5$

A single roll cannot be both $2$ and $5$.

Therefore, the events are mutually exclusive.

$$
P(A \cup B) = \frac{1}{6} + \frac{1}{6} = \frac{2}{6} = \frac{1}{3}
$$

---

## Non-Mutually Exclusive Events

Two events are **non-mutually exclusive** when they can occur at the same time.

Therefore:

$$
P(A \cap B) > 0
$$

The general Addition Rule must be used:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### Example

For a six-sided die:

* $A$: rolling an even number
* $B$: rolling a number greater than $3$

We have:

$$
A = \{2, 4, 6\}
$$

$$
B = \{4, 5, 6\}
$$

Their intersection is:

$$
A \cap B = \{4, 6\}
$$

Therefore:

$$
P(A) = \frac{3}{6}
$$

$$
P(B) = \frac{3}{6}
$$

$$
P(A \cap B) = \frac{2}{6}
$$

Using the Addition Rule:

$$
P(A \cup B) = \frac{3}{6} + \frac{3}{6} - \frac{2}{6}
$$

$$
P(A \cup B) = \frac{4}{6}
$$

$$
P(A \cup B) = \frac{2}{3}
$$

---

## Why Do We Subtract the Intersection?

Consider:

$$
P(A) + P(B)
$$

If $A$ and $B$ overlap, the outcomes in:

$$
A \cap B
$$

are counted twice.

Therefore, we subtract the intersection once:

$$
P(A) + P(B) - P(A \cap B)
$$

This ensures that every outcome is counted exactly once.

---

## Addition Rule vs. Multiplication Rule

The two rules answer different types of questions.

| Rule                          | Main Idea              | Logical Operation |
| ----------------------------- | ---------------------- | ----------------- |
| **Addition Rule**       | Probability of A or B  | OR                |
| **Multiplication Rule** | Probability of A and B | AND               |

The Addition Rule focuses on:

$$
P(A \cup B)
$$

while the Multiplication Rule focuses on:

$$
P(A \cap B)
$$

The concepts are related, but they should not be confused.

---

## Connection to Conditional Probability

The intersection term can also be expressed using conditional probability:

$$
P(A \cap B) = P(A) \, P(B \mid A)
$$

Therefore, the Addition Rule can eventually be connected to conditional probability.

This connection will become more important when studying the **Multiplication Rule and Conditional Probability**.

---

## Summary

The key ideas are:

* The Addition Rule is used for **OR** situations.
* The union $A \cup B$ represents A or B or both.
* The intersection $A \cap B$ represents A and B.
* For general events:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

* For mutually exclusive events:

$$
P(A \cup B) = P(A) + P(B)
$$

* The intersection must be subtracted when events overlap to avoid double counting.
