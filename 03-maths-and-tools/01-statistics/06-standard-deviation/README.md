# Standard Deviation

## Overview

Standard Deviation is a statistical measure that describes how far observations are spread from the mean of a dataset.

While **Variance** measures the average squared distance from the mean, **Standard Deviation** is the square root of Variance, making it easier to interpret because it is expressed in the same unit as the original data.

This chapter also revises the important formulas for both Population and Sample statistics.

---

# Population

## Population Size

Population size is represented by:

```text
N
```

Where:

- **N** = Total number of observations in the population.

---

## Population Mean

Population Mean is represented by:

```text
μ (Mu)
```

Formula

```text
        ΣXi
μ =  ----------
          N
```

Where:

- **μ** = Population Mean
- **Xi** = Individual observation
- **N** = Population Size

The population mean represents the average of all observations in the population.

---

## Population Variance

Population Variance is represented by:

```text
σ²
```

Formula

```text
           Σ(Xi − μ)²
σ² = -----------------------
               N
```

Where:

- **σ²** = Population Variance
- **μ** = Population Mean
- **N** = Population Size

Variance measures how spread out the entire population is around its mean.

---

## Population Standard Deviation

Population Standard Deviation is represented by:

```text
σ
```

Formula

```text
σ = √σ²
```

or

```text
Population Standard Deviation

=

√(Population Variance)
```

Unlike Variance, Standard Deviation is measured in the same unit as the original observations.

---

# Understanding Standard Deviation

Consider the dataset:

```text
1   2   3   4   5
```

Suppose

```text
Mean = 3

Standard Deviation = 1
```

Then

```text
2 → 1 Standard Deviation Left

4 → 1 Standard Deviation Right

1 → 2 Standard Deviations Left

5 → 2 Standard Deviations Right
```

Standard Deviation tells us how far observations lie from the mean.

---

# Sample

## Sample Size

Sample size is represented by:

```text
n
```

Where

- **n** = Number of observations in the sample.

---

## Sample Mean

Sample Mean is represented by:

```text
X̄
```

Formula

```text
        ΣXi
X̄ = ----------
         n
```

Where

- **X̄** = Sample Mean
- **n** = Sample Size

---

## Sample Variance

Sample Variance is represented by:

```text
s²
```

Formula

```text
            Σ(Xi − X̄)²
s² = --------------------------
             n − 1
```

Where

- **s²** = Sample Variance
- **X̄** = Sample Mean
- **n** = Sample Size

Notice the denominator:

```text
n − 1
```

This is known as **Bessel's Correction**, which helps provide a better estimate of the population variance.

---

## Sample Standard Deviation

Sample Standard Deviation is represented by:

```text
s
```

Formula

```text
s = √s²
```

or

```text
Sample Standard Deviation

=

√(Sample Variance)
```

Like Population Standard Deviation, it measures the spread of observations around the sample mean.

---

# Population vs Sample

| Quantity | Population | Sample |
|----------|------------|--------|
| Size | N | n |
| Mean | μ | X̄ |
| Variance | σ² | s² |
| Standard Deviation | σ | s |
| Variance Denominator | N | n − 1 |

---

# Variance vs Standard Deviation

| Variance | Standard Deviation |
|----------|--------------------|
| Measures spread | Measures distance from the mean |
| Squared units | Same unit as original data |
| Harder to interpret | Easier to interpret |

---

# Important Symbols

| Symbol | Meaning |
|---------|---------|
| N | Population Size |
| n | Sample Size |
| μ | Population Mean |
| X̄ | Sample Mean |
| σ² | Population Variance |
| s² | Sample Variance |
| σ | Population Standard Deviation |
| s | Sample Standard Deviation |

---

# Interview Questions

### What are the Measures of Central Tendency?

- Mean
- Median
- Mode

---

### What are the Measures of Dispersion?

- Variance
- Standard Deviation

---

### What does Variance measure?

Variance measures how spread out observations are around the mean.

---

### What does Standard Deviation measure?

Standard Deviation measures the average distance of observations from the mean and is expressed in the same unit as the original data.

---

### Why is Standard Deviation easier to interpret than Variance?

Because Standard Deviation uses the same units as the original observations, whereas Variance uses squared units.

---

### Why does Sample Variance divide by (n − 1)?

Because of **Bessel's Correction**, which compensates for the tendency of sample variance to underestimate the population variance.

---

# Key Takeaways

- Standard Deviation is the square root of Variance.
- It measures how far observations lie from the mean.
- It is expressed in the same unit as the original data.
- Population Standard Deviation is represented by **σ**.
- Sample Standard Deviation is represented by **s**.
- Population statistics use **N**.
- Sample statistics use **n**, with **n − 1** for Sample Variance.

---

# What's Next?

The next topic introduces **Probability**, where we'll begin studying uncertainty, random events, and probability distributions that build upon these statistical foundations.