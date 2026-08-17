# Multiplication Rule

## Overview

In the previous topic, we learned the **Addition Rule of Probability**, which is used for situations involving **OR**.

In this topic, we study the **Multiplication Rule**, which is used for situations involving **AND**.

The Multiplication Rule helps calculate the probability that **two or more events occur together**.

It is especially important for understanding:

* Independent Events
* Dependent Events
* Conditional Probability
* Bayes' Theorem
* Probabilistic Machine Learning

---

## Multiplication Rule

For two events (A) and (B), the general Multiplication Rule is:

[
\boxed{
P(A\cap B)=P(A)P(B\mid A)
}
]

where:

* (P(A\cap B)) is the probability that both (A) and (B) occur.
* (P(A)) is the probability of event (A).
* (P(B\mid A)) is the probability of (B) occurring **given that (A) has already occurred**.

The notation (A\cap B) represents the logical **AND** operation.

Therefore:

[
A\cap B
]

means:

> A and B both occur.

---

## Addition Rule vs. Multiplication Rule

The two rules answer different types of probability questions.

| Rule                    | Used For | Mathematical Idea |
| ----------------------- | -------- | ----------------- |
| **Addition Rule**       | OR       | (P(A\cup B))      |
| **Multiplication Rule** | AND      | (P(A\cap B))      |

The Addition Rule determines the probability that **at least one** of the events occurs.

The Multiplication Rule determines the probability that **both** events occur.

---

# Independent Events

## Definition

Two events are **independent** if the occurrence of one event does not affect the probability of the other event.

In other words, knowing that event (A) occurred does not change the probability of event (B).

Mathematically:

[
P(B\mid A)=P(B)
]

Therefore, the general Multiplication Rule:

[
P(A\cap B)=P(A)P(B\mid A)
]

becomes:

[
\boxed{
P(A\cap B)=P(A)P(B)
}
]

This is the **Multiplication Rule for Independent Events**.

---

## Example 1: Tossing a Coin Twice

Suppose we toss a fair coin twice.

We want to find the probability of getting:

* Head on the first toss
* Tail on the second toss

The probability of getting Head on the first toss is:

[
P(H)=\frac{1}{2}
]

The probability of getting Tail on the second toss is also:

[
P(T)=\frac{1}{2}
]

The first toss does not affect the second toss.

Therefore, the events are independent.

Using the Multiplication Rule:

[
P(H\cap T)
==========

P(H)P(T)
]

# [

\frac{1}{2}\times\frac{1}{2}
]

[
=\frac{1}{4}
]

Therefore:

[
\boxed{P(H\cap T)=\frac{1}{4}}
]

or:

[
\boxed{P(H\cap T)=25%}
]

---

## Example 2: Rolling a Die Twice

Suppose a fair six-sided die is rolled twice.

Find the probability of getting:

[
1\text{ on the first roll}
]

and:

[
2\text{ on the second roll}
]

The probability of rolling (1) is:

[
P(1)=\frac{1}{6}
]

The probability of rolling (2) is:

[
P(2)=\frac{1}{6}
]

The result of the first roll does not affect the second roll.

Therefore:

[
P(1\cap2)
=========

\frac{1}{6}\times\frac{1}{6}
]

[
=\frac{1}{36}
]

Therefore:

[
\boxed{P(1\cap2)=\frac{1}{36}}
]

---

# Dependent Events

## Definition

Two events are **dependent** if the occurrence of one event affects the probability of the other event.

In other words, the probability of the second event changes depending on what happened during the first event.

For dependent events:

[
P(B\mid A)\neq P(B)
]

Therefore, we must use the general Multiplication Rule:

[
\boxed{
P(A\cap B)=P(A)P(B\mid A)
}
]

---

## Example: Drawing Cards Without Replacement

Consider a standard deck of:

[
52
]

playing cards.

Suppose we:

1. Draw one card.
2. Do not replace it.
3. Draw another card.

Find the probability of drawing:

* A King first
* A Queen second

---

### Step 1: Probability of Drawing a King

There are (4) Kings in a deck of (52) cards.

Therefore:

[
P(K)=\frac{4}{52}
]

---

### Step 2: Probability of Drawing a Queen Given a King Was Drawn

After drawing a King and not replacing it:

[
52-1=51
]

cards remain.

There are still (4) Queens.

Therefore:

[
P(Q\mid K)=\frac{4}{51}
]

Notice that the probability has changed because the first card was removed.

---

### Step 3: Apply the Multiplication Rule

[
P(K\cap Q)
==========

P(K)P(Q\mid K)
]

Substituting:

[
P(K\cap Q)
==========

\frac{4}{52}\times\frac{4}{51}
]

# [

\frac{16}{2652}
]

Simplifying:

[
\boxed{
P(K\cap Q)=\frac{4}{663}
}
]

Approximately:

[
\boxed{
P(K\cap Q)\approx0.603%
}
]

Therefore, the probability of drawing a King followed by a Queen without replacement is approximately (0.603%).

---

# Conditional Probability

The notation:

[
P(B\mid A)
]

is called **conditional probability**.

It is read as:

> The probability of (B) given that (A) has already occurred.

The conditional probability formula is:

[
\boxed{
P(B\mid A)=\frac{P(A\cap B)}{P(A)}
}
]

provided that:

[
P(A)>0
]

Rearranging this equation gives:

[
P(A\cap B)=P(A)P(B\mid A)
]

which is exactly the general Multiplication Rule.

### Important Connection

The concepts are therefore connected:

[
\boxed{
\text{Conditional Probability}
\rightarrow
\text{Multiplication Rule}
\rightarrow
\text{Dependent Events}
}
]

We will use conditional probability more extensively when studying later probability concepts.

---

# Independent vs. Dependent Events

| Feature                 | Independent Events         | Dependent Events                  |
| ----------------------- | -------------------------- | --------------------------------- |
| Effect of first event   | Does not affect the second | Affects the second                |
| Conditional probability | (P(B\mid A)=P(B))          | (P(B\mid A)\neq P(B))             |
| Multiplication Rule     | (P(A\cap B)=P(A)P(B))      | (P(A\cap B)=P(A)P(B\mid A))       |
| Example                 | Tossing a coin twice       | Drawing cards without replacement |

---

# With Replacement vs. Without Replacement

A useful way to identify dependence in probability problems is to look at whether objects are **replaced** after being selected.

### With Replacement

If an item is replaced before the next selection, the probability usually remains unchanged.

For example:

* Draw a card.
* Replace it.
* Draw another card.

The deck returns to (52) cards.

This can produce independent events.

### Without Replacement

If an item is not replaced, the sample space changes.

For example:

* Draw a card.
* Do not replace it.
* Draw another card.

The deck changes from (52) cards to (51) cards.

This generally produces dependent events.

---

# Key Takeaways

* The Multiplication Rule is associated with **AND** situations.
* The general Multiplication Rule is:

[
\boxed{
P(A\cap B)=P(A)P(B\mid A)
}
]

* For independent events:

[
\boxed{
P(A\cap B)=P(A)P(B)
}
]

* For dependent events:

[
\boxed{
P(A\cap B)=P(A)P(B\mid A)
}
]

* Independent events do not affect one another's probabilities.
* Dependent events affect the probability of subsequent events.
* (P(B\mid A)) represents the probability of (B) given that (A) has occurred.
* Drawing cards without replacement is a common example of dependent events.
* Tossing a coin multiple times is a common example of independent events.
* Conditional probability is an important foundation for more advanced probability concepts and probabilistic machine learning.

---

# Addition Rule vs. Multiplication Rule

| Rule                | Question                                | Formula      |
| ------------------- | --------------------------------------- | ------------ |
| Addition Rule       | What is the probability of A **or** B?  | (P(A\cup B)) |
| Multiplication Rule | What is the probability of A **and** B? | (P(A\cap B)) |

---

# Interview Questions

## 1. What are independent events?

Independent events are events where the occurrence of one event does not affect the probability of the other event.

Mathematically:

[
P(B\mid A)=P(B)
]

---

## 2. What are dependent events?

Dependent events are events where the occurrence of one event changes the probability of another event.

Mathematically:

[
P(B\mid A)\neq P(B)
]

---

## 3. What is the Multiplication Rule for independent events?

For independent events:

[
\boxed{
P(A\cap B)=P(A)P(B)
}
]

---

## 4. What is the Multiplication Rule for dependent events?

For dependent events:

[
\boxed{
P(A\cap B)=P(A)P(B\mid A)
}
]

---

## 5. What is conditional probability?

Conditional probability is the probability of an event occurring given that another event has already occurred.

It is represented as:

[
\boxed{
P(B\mid A)
}
]

---

## 6. Why are card-drawing problems usually dependent?

When cards are drawn **without replacement**, the total number of cards changes after each draw.

Therefore, the probability of subsequent events can change.

---

## 7. Why is conditional probability important in Machine Learning?

Conditional probability allows us to reason about the probability of an event under specific conditions.

It forms an important foundation for **Bayes' Theorem** and probabilistic machine-learning methods such as **Naive Bayes**.
