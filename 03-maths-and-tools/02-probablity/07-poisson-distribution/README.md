# Poisson Distribution

## Overview

The **Poisson Distribution** is a discrete probability distribution used to model the number of times an event occurs within a **fixed interval of time or space**, when events occur independently at a constant average rate.

It is especially useful for modeling **count data**, such as:

- Number of customers arriving at a bank per hour
- Number of calls received by a call center per minute
- Number of website visitors per minute
- Number of vehicles passing a checkpoint per hour
- Number of defects produced in a manufacturing process per day

---

## Learning Objectives

After studying this topic, you should be able to:

- Understand what the Poisson Distribution represents.
- Identify when a problem follows a Poisson Distribution.
- Understand the parameter `λ (lambda)`.
- Calculate probabilities using the Poisson PMF.
- Calculate the mean, variance, and standard deviation.
- Solve probability questions such as:
  - Exactly `k` events
  - At most `k` events
  - More than `k` events
  - A range of event counts
- Understand the relationship between Poisson and Binomial Distributions.
- Understand how increasing `λ` changes the shape of the distribution.

---

## Definition

A Poisson Distribution models the probability of observing exactly `k` events in a fixed interval, assuming:

1. Events occur independently.
2. The average rate of occurrence is constant.
3. Events are counted over a fixed interval of time or space.
4. Events occur individually rather than simultaneously.

The random variable represents a **count**:

```text
X = Number of events in a fixed interval
```

Possible values are:

```text
X = 0, 1, 2, 3, ...
```

Because the possible values are countable, Poisson Distribution is a **discrete probability distribution** and uses a **PMF**.

---

## Parameter: λ (Lambda)

The Poisson Distribution has one main parameter:

```text
λ = average number of events per interval
```

For example, if:

```text
λ = 3
```

then we expect an average of **3 events per interval**.

If the rate is `λ` events per unit time and we consider an interval of length `t`, the effective Poisson parameter becomes:

```text
λt
```

---

## Probability Mass Function (PMF)

The Poisson PMF is:

\[
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}
\]

where:

- `X` = random variable
- `k` = observed number of events
- `λ` = average number of events
- `e ≈ 2.71828`
- `k!` = factorial of `k`

---

## Mean, Variance and Standard Deviation

For:

\[
X \sim Poisson(\lambda)
\]

### Mean

\[
\boxed{\mu=\lambda}
\]

### Variance

\[
\boxed{\sigma^2=\lambda}
\]

### Standard Deviation

\[
\boxed{\sigma=\sqrt{\lambda}}
\]

An important property of the Poisson Distribution is:

\[
\boxed{\text{Mean}=\text{Variance}=\lambda}
\]

---

## Rate Over a Time Interval

If `λ` represents the average number of events per unit time and the interval is `t`, then:

\[
X \sim Poisson(\lambda t)
\]

Therefore:

\[
\boxed{\mu=\lambda t}
\]

\[
\boxed{\sigma^2=\lambda t}
\]

\[
\boxed{\sigma=\sqrt{\lambda t}}
\]

---

## Example

Suppose a bank receives an average of **3 customers per hour**.

Therefore:

```text
λ = 3
```

What is the probability that exactly **5 customers** arrive in one hour?

Using the Poisson PMF:

\[
P(X=5)=\frac{e^{-3}3^5}{5!}
\]

\[
P(X=5)\approx0.1008
\]

Therefore:

\[
\boxed{P(X=5)\approx10.08\%}
\]

---

## Common Probability Questions

### Exactly `k`

```text
P(X = k)
```

Use the PMF directly.

### At most `k`

```text
P(X ≤ k)
```

Calculate:

```text
P(X=0) + P(X=1) + ... + P(X=k)
```

### More than `k`

```text
P(X > k)
```

Using the complement:

```text
P(X > k) = 1 - P(X ≤ k)
```

### Between two values

For example:

```text
P(4 ≤ X ≤ 5)
```

Calculate:

```text
P(X=4) + P(X=5)
```

---

## Effect of λ

The value of `λ` controls the center and spread of the distribution.

- **Small λ** → events are concentrated near zero.
- **Moderate λ** → distribution becomes more spread out.
- **Large λ** → distribution becomes more symmetric and can resemble a Normal Distribution.

As `λ` increases:

```text
Mean increases
Variance increases
Standard deviation increases
```

---

## Poisson vs Binomial

| Feature | Binomial | Poisson |
|---|---|---|
| Type | Discrete | Discrete |
| Main idea | Number of successes | Number of events |
| Trials | Fixed `n` | No fixed number of trials |
| Parameters | `n, p` | `λ` |
| Outcomes | Success / Failure per trial | Event count |
| Interval | Usually `n` trials | Fixed time/space interval |
| PMF | Yes | Yes |
| Mean | `np` | `λ` |
| Variance | `np(1-p)` | `λ` |

### Simple distinction

> **Binomial → How many successes occur in `n` trials?**

> **Poisson → How many events occur in a fixed interval?**

---

## When to Use Poisson Distribution

A problem is a good candidate for the Poisson Distribution when:

- The outcome is a **count**.
- The interval is fixed.
- Events occur independently.
- The average occurrence rate is approximately constant.
- We want the probability of observing a particular number of events.

---

## Real-World Applications

### Healthcare

Number of patients arriving at a hospital per hour.

### Banking

Number of customers entering a bank per hour.

### Call Centers

Number of incoming calls per minute.

### Websites

Number of requests received by a server per second.

### Traffic

Number of vehicles passing a checkpoint per hour.

### Manufacturing

Number of defects produced per day.

---

## Relationship with Other Distributions

The progression is useful to remember:

```text
Bernoulli
    ↓
One trial
Success / Failure

Binomial
    ↓
n independent Bernoulli trials
Number of successes

Poisson
    ↓
Fixed interval
Number of events
```

A Poisson Distribution can also be viewed as an important limiting case of the Binomial Distribution when the number of trials becomes very large, the success probability becomes very small, and `np` approaches a finite value `λ`.

---

## Key Takeaways

- Poisson Distribution is **discrete**.
- It models the **number of events** in a fixed interval.
- Its main parameter is **λ (lambda)**.
- The PMF is:

\[
P(X=k)=\frac{e^{-\lambda}\lambda^k}{k!}
\]

- Mean:

\[
\mu=\lambda
\]

- Variance:

\[
\sigma^2=\lambda
\]

- Standard deviation:

\[
\sigma=\sqrt{\lambda}
\]

- For an interval of length `t`, use `λt`.
- Mean and variance are equal.
- It is closely related to the Binomial Distribution.

---

## Interview Questions

1. What is a Poisson Distribution?
2. Why is Poisson Distribution discrete?
3. What does `λ` represent?
4. State the Poisson PMF.
5. What assumptions are made by the Poisson Distribution?
6. What are the mean and variance of a Poisson Distribution?
7. Why are the mean and variance equal?
8. What is the difference between Binomial and Poisson Distribution?
9. When would you use Poisson instead of Binomial?
10. How does increasing `λ` affect the distribution?
11. What does "at most 3 events" mean?
12. What does "more than 3 events" mean?
13. How is Poisson Distribution related to Binomial Distribution?
