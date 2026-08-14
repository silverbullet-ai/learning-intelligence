# Probability

Probability is one of the most fundamental concepts in statistics, machine learning, and data science.

It measures the likelihood or chance that an event will occur.

Probability is widely used in:

- Statistics
- Data Analysis
- Machine Learning
- Deep Learning
- Classification
- Risk Analysis
- Decision Making

Many machine learning classification algorithms output probabilities, which can then be converted into class predictions using a threshold such as `0.5`.

---

## What is Probability?

Probability is the measure of the likelihood or chance of an event occurring.

In simple terms:

> Probability tells us how likely an event is to happen.

The probability of an event lies between:

$$
0 \leq P(E) \leq 1
$$

where:

- `0` → Impossible event
- `1` → Certain event
- Values between `0` and `1` → Different levels of likelihood

---

## Basic Probability Formula

$$
P(E) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}}
$$

Where:

- `P(E)` = Probability of event `E`
- Favorable Outcomes = Outcomes we are interested in
- Total Outcomes = All possible outcomes

This formula applies when all outcomes are equally likely.

---

## Example 1: Tossing a Coin

Possible outcomes:

$$
\{Head, Tail\}
$$

Total outcomes:

$$
2
$$

Probability of getting Head:

$$
P(Head) = \frac{1}{2} = 0.5 = 50\%
$$

Probability of getting Tail:

$$
P(Tail) = \frac{1}{2} = 0.5 = 50\%
$$

Therefore:

$$
P(Head) + P(Tail) = 1
$$

The probability of getting either Head or Tail is `100%`.

---

## Example 2: Rolling a Die

A standard die has six possible outcomes:

$$
\{1,2,3,4,5,6\}
$$

Therefore:

$$
P(1) = \frac{1}{6}
$$

Similarly:

$$
P(2) = P(3) = P(4) = P(5) = P(6) = \frac{1}{6}
$$

Each outcome has an equal probability of:

$$
\frac{1}{6} \approx 0.1667
$$

---

# Types of Events

Two important types of events are:

1. Mutually Exclusive Events
2. Non-Mutually Exclusive Events

---

## 1. Mutually Exclusive Events

Two events are **mutually exclusive** if they cannot occur at the same time.

In other words:

> If one event occurs, the other cannot occur simultaneously.

### Example: Tossing a Coin

Possible outcomes:

- Head
- Tail

A single coin toss cannot produce both Head and Tail.

Therefore:

```text
Head and Tail → Mutually Exclusive
```

There is no overlap between the two events.

---

### Example: Rolling a Die

Consider the events:

- Event A → Getting `1`
- Event B → Getting `5`

A single die roll cannot produce both `1` and `5`.

Therefore, these events are mutually exclusive.

---

### Addition Rule for Mutually Exclusive Events

For mutually exclusive events:

$$
P(A \cup B) = P(A) + P(B)
$$

Since the events cannot overlap, there is no intersection to subtract.

---

### Example: Head OR Tail

$$
P(Head \cup Tail) = P(Head) + P(Tail)
$$

$$
= \frac{1}{2} + \frac{1}{2}
$$

$$
= 1
$$

Therefore:

$$
P(Head \cup Tail) = 1
$$

This means we are certain that a coin toss produces either Head or Tail.

---

### Example: Rolling a Die — 1 OR 5

$$
P(1 \cup 5) = P(1) + P(5)
$$

$$
= \frac{1}{6} + \frac{1}{6}
$$

$$
= \frac{2}{6}
$$

$$
= \frac{1}{3}
$$

---

## 2. Non-Mutually Exclusive Events

Two events are **non-mutually exclusive** if they can occur at the same time.

This means the events have an overlapping region.

---

### Example: King OR Heart

Consider drawing one card from a standard deck of `52` cards.

Event A:

> Drawing a King

There are `4` Kings.

Event B:

> Drawing a Heart

There are `13` Hearts.

These events overlap because of:

> King of Hearts

The King of Hearts is both:

- A King
- A Heart

Therefore, the events are non-mutually exclusive.

---

### Addition Rule for Non-Mutually Exclusive Events

For non-mutually exclusive events:

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

Where:

- `P(A)` = Probability of event A
- `P(B)` = Probability of event B
- `P(A ∩ B)` = Probability that both A and B occur

---

### Why Do We Subtract the Intersection?

Suppose we simply add:

$$
P(A) + P(B)
$$

The overlapping outcome gets counted twice.

For the King and Heart example, the King of Hearts is included:

- Once among the Kings
- Once among the Hearts

Therefore, we subtract the intersection once.

---

### Solved Example: King OR Heart

#### Step 1: Probability of King

There are `4` Kings in a deck of `52` cards.

$$
P(K) = \frac{4}{52}
$$

---

#### Step 2: Probability of Heart

There are `13` Hearts.

$$
P(H) = \frac{13}{52}
$$

---

#### Step 3: Probability of King AND Heart

Only one card is both a King and a Heart:

> King of Hearts

Therefore:

$$
P(K \cap H) = \frac{1}{52}
$$

---

#### Step 4: Apply the Addition Rule

$$
P(K \cup H) = P(K) + P(H) - P(K \cap H)
$$

$$
= \frac{4}{52} + \frac{13}{52} - \frac{1}{52}
$$

$$
= \frac{16}{52}
$$

$$
= \frac{4}{13}
$$

Therefore:

$$
P(K \cup H) = \frac{4}{13} \approx 0.3077
$$

So the probability of drawing either a King or a Heart is approximately:

**30.77%**

---

## Mutually Exclusive vs Non-Mutually Exclusive

| Feature | Mutually Exclusive | Non-Mutually Exclusive |
|---|---|---|
| Can occur together? | No | Yes |
| Overlap | No | Yes |
| Addition Rule | `P(A ∪ B) = P(A) + P(B)` | `P(A ∪ B) = P(A) + P(B) - P(A ∩ B)` |
| Example | Head or Tail | King or Heart |

---

## Why Do We Study Probability?

Probability provides the mathematical foundation for many areas of data science and machine learning.

It is used for:

- Classification
- Prediction
- Risk estimation
- Statistical inference
- Probability distributions
- Bayesian methods
- Machine learning algorithms
- Decision making

For example, a classification model might output:

```text
P(Class A) = 0.82
P(Class B) = 0.18
```

A threshold can then be used to convert the probability into a class prediction.

---

## Key Formulas

### Basic Probability

$$
P(E) = \frac{\text{Favorable Outcomes}}{\text{Total Outcomes}}
$$

### Mutually Exclusive Events

$$
P(A \cup B) = P(A) + P(B)
$$

### Non-Mutually Exclusive Events

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

---

# Interview Questions

### 1. What is probability?

Probability is the measure of the likelihood or chance that an event will occur.

### 2. What is the range of probability?

$$
0 \leq P(E) \leq 1
$$

### 3. What are mutually exclusive events?

Events that cannot occur simultaneously.

Example:

- Head and Tail in a single coin toss.

### 4. What is the addition rule for mutually exclusive events?

$$
P(A \cup B) = P(A) + P(B)
$$

### 5. What are non-mutually exclusive events?

Events that can occur simultaneously and therefore have an overlapping region.

Example:

- King and Heart when drawing a card.

### 6. What is the addition rule for non-mutually exclusive events?

$$
P(A \cup B) = P(A) + P(B) - P(A \cap B)
$$

### 7. Why do we subtract the intersection?

Because the overlapping outcomes are counted twice when the probabilities of the two events are added.

Subtracting the intersection once ensures that the overlap is counted only once.

---

# Key Takeaways

- **Probability** measures the likelihood of an event occurring.
- Probability ranges from **0 to 1**.
- **Mutually exclusive events** cannot occur together.
- **Non-mutually exclusive events** can occur together.
- Mutually exclusive events use simple addition.
- Non-mutually exclusive events require subtracting the intersection.
- Probability forms the foundation of **statistics, machine learning, and data science**.
