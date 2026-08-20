
# Binomial Distribution

## Overview

The **Binomial Distribution** is a **discrete probability distribution** that models the number of successes obtained in a fixed number of independent Bernoulli trials.

Each trial has exactly two possible outcomes:

- Success
- Failure

The probability of success remains constant for every trial.

For example:

- Number of heads in 10 coin tosses
- Number of defective products in a sample
- Number of customers who purchase a product
- Number of students who pass an exam

The Binomial Distribution is built directly from the **Bernoulli Distribution**.

---

## Definition

A random variable \(X\) follows a Binomial Distribution if it represents the number of successes in \(n\) independent Bernoulli trials, where each trial has a constant probability \(p\) of success.

The distribution is written as:

\[
X \sim \operatorname{Binomial}(n,p)
\]

where:

- \(n\) = number of trials
- \(p\) = probability of success
- \(q = 1-p\) = probability of failure

The possible values of \(X\) are:

\[
X \in \{0,1,2,\ldots,n\}
\]

---

## Conditions for a Binomial Distribution

A problem follows a Binomial Distribution when all of the following conditions are satisfied.

### 1. Fixed Number of Trials

There must be a predetermined number of trials.

\[
n = \text{fixed}
\]

For example, tossing a coin exactly 10 times.

---

### 2. Two Possible Outcomes

Each trial must have exactly two possible outcomes.

Examples:

- Success / Failure
- Yes / No
- Pass / Fail
- Defective / Non-defective
- Head / Tail

---

### 3. Independent Trials

The outcome of one trial must not affect the outcome of another trial.

For example, repeated tosses of a fair coin are independent.

---

### 4. Constant Probability of Success

The probability of success must remain the same for every trial.

\[
P(\text{Success}) = p
\]

and

\[
P(\text{Failure}) = 1-p
\]

---

### 5. Count the Number of Successes

The random variable must represent the number of successes obtained across the \(n\) trials.

---

## Parameters

The Binomial Distribution has two parameters:

### Number of Trials

\[
n \in \{0,1,2,\ldots\}
\]

where \(n\) is the number of trials.

### Probability of Success

\[
0 \leq p \leq 1
\]

where \(p\) is the probability of success in each trial.

The probability of failure is:

\[
q = 1-p
\]

---

## Random Variable

Let

\[
X = \text{number of successes in } n \text{ trials}
\]

Then:

\[
X \in \{0,1,2,\ldots,n\}
\]

For example, if a coin is tossed 5 times:

\[
X \in \{0,1,2,3,4,5\}
\]

where \(X\) represents the number of heads.

---

## Probability Mass Function (PMF)

The probability of obtaining exactly \(k\) successes in \(n\) trials is:

\[
\boxed{
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
}
\]

where:

- \(n\) = number of trials
- \(k\) = number of successes
- \(p\) = probability of success
- \(1-p\) = probability of failure
- \(\binom{n}{k}\) = binomial coefficient

The possible values of \(k\) are:

\[
k=0,1,2,\ldots,n
\]

---

## Binomial Coefficient

The binomial coefficient determines how many different arrangements can produce exactly \(k\) successes in \(n\) trials.

It is given by:

\[
\boxed
======

\frac{n!}{k!(n-k)!}
}
\]

For example:

\[
\binom
======

\frac
=====

10
\]

This means there are 10 different arrangements containing exactly 3 successes in 5 trials.

---

## Understanding the PMF

The Binomial PMF:

\[
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
\]

has three components.

### 1. Binomial Coefficient

\[
\binom{n}{k}
\]

Counts the number of ways to arrange the \(k\) successes among the \(n\) trials.

### 2. Probability of Successes

\[
p^k
\]

Represents the probability of obtaining \(k\) successes.

### 3. Probability of Failures

\[
(1-p)^{n-k}
\]

Represents the probability of obtaining the remaining \(n-k\) failures.

Therefore:

\[
\text{Number of arrangements}
\times
\text{Probability of successes}
\times
\text{Probability of failures}
\]

gives the probability of exactly \(k\) successes.

---

# Example 1: Coin Toss

Suppose a fair coin is tossed 5 times.

We want to find the probability of getting exactly 3 heads.

### Step 1: Identify the parameters

\[
n=5
\]

\[
p=0.5
\]

\[
k=3
\]

Since the probability of tails is:

\[
1-p=0.5
\]

### Step 2: Apply the Binomial PMF

\[
P(X=3)
======

\binom{5}{3}(0.5)^3(0.5)^2
\]

The binomial coefficient is:

\[
\binom{5}{3}=10
\]

Therefore:

\[
P(X=3)
======

10(0.5)^3(0.5)^2
\]

\[
=10(0.5)^5
\]

\[
=\frac{10}{32}
\]

\[
\boxed{P(X=3)=0.3125}
\]

Therefore, the probability of getting exactly 3 heads is:

\[
\boxed{31.25\%}
\]

---

# Example 2: Quality Control

Suppose a factory produces products where each product has a 10% probability of being defective.

A quality-control team randomly inspects 10 products.

Find the probability of getting exactly 2 defective products.

### Step 1: Identify the parameters

\[
n=10
\]

\[
p=0.1
\]

\[
k=2
\]

The probability of a non-defective product is:

\[
1-p=0.9
\]

### Step 2: Apply the PMF

\[
P(X=2)
======

\binom{10}{2}(0.1)^2(0.9)^8
\]

Since:

\[
\binom{10}{2}=45
\]

we get:

\[
P(X=2)
======

45(0.1)^2(0.9)^8
\]

\[
\boxed{P(X=2)\approx0.1937}
\]

Therefore, there is approximately a:

\[
\boxed{19.37\%}
\]

probability of finding exactly 2 defective products.

---

# Mean

The mean or expected value of a Binomial Distribution is:

\[
\boxed{\mu=np}
\]

### Intuition

If each of \(n\) trials has a probability \(p\) of success, the expected number of successes is:

\[
n\times p
\]

For example, if:

\[
n=100,\qquad p=0.2
\]

then:

\[
\mu=np=100(0.2)=20
\]

So we expect approximately 20 successes.

---

# Variance

The variance of a Binomial Distribution is:

\[
\boxed{\sigma^2=np(1-p)}
\]

Using:

\[
q=1-p
\]

this can also be written as:

\[
\boxed{\sigma^2=npq}
\]

---

# Standard Deviation

The standard deviation is the square root of the variance:

\[
\boxed{
\sigma=\sqrt{np(1-p)}
}
\]

or:

\[
\boxed{
\sigma=\sqrt{npq}
}
\]

---

# Bernoulli vs Binomial Distribution

The Binomial Distribution is closely related to the Bernoulli Distribution.

| Feature            | Bernoulli            | Binomial                       |
| ------------------ | -------------------- | ------------------------------ |
| Number of trials   | One                  | \(n\) trials                   |
| Outcomes per trial | Two                  | Two                            |
| Random variable    | Outcome of one trial | Number of successes            |
| Support            | \(\{0,1\}\)          | \(\{0,1,\ldots,n\}\)           |
| Mean               | \(p\)                | \(np\)                         |
| Variance           | \(p(1-p)\)           | \(np(1-p)\)                    |
| PMF                | \(p^k(1-p)^{1-k}\)   | \(\binom{n}{k}p^k(1-p)^{n-k}\) |

### Important Relationship

A Binomial Distribution can be viewed as the sum of \(n\) independent Bernoulli random variables.

If:

\[
X_1,X_2,\ldots,X_n
\]

are independent Bernoulli random variables, then:

\[
X=X_1+X_2+\cdots+X_n
\]

follows a Binomial Distribution:

\[
X\sim\operatorname{Binomial}(n,p)
\]

---

# Real-World Applications

The Binomial Distribution can be used in situations such as:

- Number of heads in repeated coin tosses
- Number of defective products in a fixed sample
- Number of customers who purchase a product
- Number of students who pass an examination
- Number of successful predictions in repeated trials
- Number of users who click an advertisement

However, these examples must satisfy the Binomial assumptions, particularly independence and constant probability of success.

---

# When Not to Use a Binomial Distribution

A Binomial Distribution is not appropriate when the assumptions are violated.

For example:

### Probability Changes Between Trials

If the probability of success changes from one trial to another, the standard Binomial model does not apply.

### Trials Are Dependent

If one trial changes the probability of another trial, independence is violated.

For example, drawing cards **without replacement** usually produces dependent trials.

### More Than Two Outcomes

If a single trial has more than two possible outcomes, a standard Binomial Distribution is not appropriate.

---

# Important Formulas

| Property               | Formula                               |
| ---------------------- | ------------------------------------- |
| Distribution           | \(X\sim\operatorname{Binomial}(n,p)\) |
| Probability of failure | \(q=1-p\)                             |
| Support                | \(k\in\{0,1,\ldots,n\}\)              |
| PMF                    | \(P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}\) |
| Binomial coefficient   | \(\binom{n}{k}=\frac{n!}{k!(n-k)!}\)  |
| Mean                   | \(\mu=np\)                            |
| Variance               | \(\sigma^2=np(1-p)=npq\)              |
| Standard deviation     | \(\sigma=\sqrt{np(1-p)}\)             |

---

# Key Takeaways

- The **Binomial Distribution** is a **discrete probability distribution**.
- It models the number of successes in a fixed number of independent trials.
- Every trial must have exactly **two outcomes**.
- The probability of success must remain **constant**.
- The trials must be **independent**.
- The random variable counts the **number of successes**.
- The PMF is:

\[
P(X=k)=\binom{n}{k}p^k(1-p)^{n-k}
\]

- The mean is:

\[
\mu=np
\]

- The variance is:

\[
\sigma^2=np(1-p)
\]

- The standard deviation is:

\[
\sigma=\sqrt{np(1-p)}
\]

- Bernoulli models **one trial**.
- Binomial models the **number of successes across multiple Bernoulli trials**.

---

# Interview Questions

1. What is a Binomial Distribution?
2. What conditions must be satisfied for a Binomial Distribution?
3. What do \(n\), \(p\), and \(k\) represent?
4. What is the PMF of the Binomial Distribution?
5. What is the Binomial Coefficient?
6. Why is the Binomial Distribution discrete?
7. What is the mean of a Binomial Distribution?
8. What is the variance of a Binomial Distribution?
9. What is the standard deviation of a Binomial Distribution?
10. What is the difference between Bernoulli and Binomial Distribution?
11. Why must the trials be independent?
12. Why must the probability of success remain constant?
13. Give real-world examples of Binomial Distribution.
14. When should a Binomial Distribution not be used?
