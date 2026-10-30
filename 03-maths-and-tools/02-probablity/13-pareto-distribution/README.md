# Pareto Distribution

## 1. Definition

The **Pareto Distribution** is a **continuous probability distribution** used to model situations in which a relatively small number of observations account for a disproportionately large share of the total.

It is closely related to **power-law distributions** and is commonly associated with the **Pareto Principle (80/20 Rule)**.

> A small number of causes can account for a large proportion of the effects.

The famous 80/20 relationship is one example of Pareto-like behavior. However, an exact 80/20 split is **not** a mathematical requirement of the Pareto Distribution.

## 2. Type and Characteristics

- Continuous probability distribution
- Non-Gaussian distribution
- Heavy-tailed distribution
- Right-skewed distribution
- Described using a probability density function (PDF)

### Shape

A Pareto Distribution typically has:

- A high density near its minimum value.
- A long right tail.
- Strong positive (right) skewness.
- More probability in the extreme upper tail than a Normal Distribution.

```text
Density
  ^
  |************
  |********
  |*****
  |***
  |**
  |*
  |*
  +------------------------------------>
                    Long right tail
```

Unlike a symmetric, bell-shaped Normal Distribution, the Pareto Distribution is strongly right-skewed.

## 3. Pareto Principle (80/20 Rule)

The **Pareto Principle**, commonly called the **80/20 Rule**, states that approximately 80% of effects may come from approximately 20% of causes.

Examples:

- A small percentage of customers may generate most of a business's revenue.
- A small percentage of software defects may cause most software failures.
- A small percentage of products may account for most sales.

The percentages do not have to be exactly 80% and 20%. The central idea is **unequal contribution**.

## 4. Parameter: α (Alpha)

A standard Pareto Distribution is characterized by two parameters:

- **$x_m$**: minimum possible value (scale parameter)
- **$\alpha$**: shape parameter

The shape parameter $\alpha$ controls how quickly the tail decreases.

- **Larger $\alpha$:** the tail decays faster, so extremely large observations are less likely.
- **Smaller $\alpha$:** the tail decays more slowly, so extremely large observations are more likely.

For the standard Pareto Type I distribution:

$$
x_m > 0,\qquad \alpha > 0,\qquad x \geq x_m
$$

## 5. Mathematical Representation

A random variable following a standard Pareto Type I distribution is written as:

$$
X \sim \mathrm{Pareto}(x_m,\alpha)
$$

where:

- $X$ = random variable
- $x_m$ = minimum possible value (scale parameter)
- $\alpha$ = shape parameter

The distribution has support on $x \geq x_m$.

## 6. Probability Density Function (PDF)

The PDF is:

$$
f(x)=
\begin{cases}
\dfrac{\alpha x_m^\alpha}{x^{\alpha+1}}, & x\geq x_m\\[6pt]
0, & x<x_m
\end{cases}
$$

The PDF describes the relative density of probability at each value of $x$. Probabilities over intervals are found by integrating the PDF.

For interviews, understand what the parameters represent rather than only memorizing the formula.

## 7. Cumulative Distribution Function (CDF)

The CDF is:

$$
F(x)=
\begin{cases}
0, & x<x_m\\[4pt]
1-\left(\dfrac{x_m}{x}\right)^\alpha, & x\geq x_m
\end{cases}
$$

It represents the probability that the random variable is less than or equal to $x$:

$$
F(x)=P(X\leq x)
$$

## 8. Survival Function

The survival function gives the probability that a value exceeds $x$:

$$
P(X>x)=1-F(x)=\left(\frac{x_m}{x}\right)^\alpha,\qquad x\geq x_m
$$

This is useful for understanding the long tail. Extremely large values are uncommon, but the probability of observing them decreases more slowly than it does in a Normal Distribution.

## 9. Mean

The theoretical mean exists only when:

$$
\alpha>1
$$

When $\alpha>1$:

$$
\mu=E[X]=\frac{\alpha x_m}{\alpha-1}
$$

When $0<\alpha\leq1$, the theoretical mean is infinite (and therefore is not finite).

## 10. Variance

The theoretical variance exists only when:

$$
\alpha>2
$$

When $\alpha>2$:

$$
\sigma^2=\mathrm{Var}(X)
=\frac{\alpha x_m^2}{(\alpha-1)^2(\alpha-2)}
$$

When $0<\alpha\leq2$, the theoretical variance is infinite (and therefore is not finite).

## 11. Why Is It Heavy-Tailed?

The defining characteristic of the Pareto Distribution is its **heavy right tail**.

### Normal Distribution

```text
Density
  ^
  |          ***
  |        *******
  |      ***********
  |        *******
  |          ***
  +---------------------------->
```

The probability of extremely large values in a Normal Distribution decreases very quickly.

### Pareto Distribution

```text
Density
  ^
  |************
  |*******
  |****
  |**
  |*
  |*
  |*
  +---------------------------->
                 Long right tail
```

A Pareto Distribution assigns relatively more probability to extreme large values than a Normal Distribution does.

## 12. Relationship with Power Laws

A **power law** is a broad mathematical relationship in which one quantity varies as a power of another.

The **Pareto Distribution** is a specific probability distribution whose tail follows a power law.

```text
Power-law relationship
          |
          v
  Pareto Distribution
          |
          v
   Heavy right tail
```

In short:

- **Power law:** a broad mathematical concept.
- **Pareto Distribution:** a specific probability distribution with a power-law tail.

Not every power-law phenomenon is necessarily a Pareto Type I distribution.

## 13. Pareto vs. Power Law

| Property | Power Law | Pareto Distribution |
|---|---|---|
| Meaning | General mathematical relationship | Specific probability distribution |
| Scope | Broad | Specific |
| Tail | Often associated with heavy tails | Has a power-law right tail |
| Distribution | Can describe many kinds of phenomena | Has a defined probability model |
| 80/20 Rule | Sometimes associated with it | Commonly associated with it |
| Parameters | Depend on the model | $x_m$, $\alpha$ for Pareto Type I |

## 14. Relationship with the Log-Normal Distribution

Both Pareto and Log-Normal distributions can model positive, right-skewed data, but their tails behave differently.

### Log-Normal Distribution

A random variable $X$ is Log-Normal if its natural logarithm is Normally distributed:

$$
X\sim\mathrm{LogNormal}(\mu,\sigma^2)
\quad\Longleftrightarrow\quad
\ln(X)\sim N(\mu,\sigma^2)
$$

### Pareto Distribution

A Pareto Distribution has a power-law tail. Its tail decreases more slowly than the tail of a Log-Normal Distribution, making it especially useful for modeling some forms of extreme-value behavior.

The two distributions can look similar over a limited range of data, so selecting between them requires appropriate model fitting and diagnostics.

## 15. Box-Cox Transformation

The **Box-Cox Transformation** is a family of power transformations used with positive-valued data.

It can help to:

- Reduce skewness.
- Stabilize variance.
- Make data more suitable for certain statistical models.

After transformation, a **Q-Q Plot** can help assess whether the transformed data is approximately Normally distributed.

```text
Positive, right-skewed data
           |
           v
   Box-Cox transformation
           |
           v
      Reduced skewness
           |
           v
         Q-Q plot
           |
           v
 Assess approximate normality
```

> Box-Cox can improve distributional properties, but it does not guarantee that Pareto-distributed data becomes Normally distributed.

## 16. How to Investigate a Pareto-Like Distribution

A combination of visual and statistical analysis can help assess whether data has a Pareto-like tail.

Useful tools include:

- **Histogram:** shows the overall shape of the data.
- **Q-Q Plot:** compares sample quantiles with those expected under a selected theoretical distribution.
- **Log-log plot:** can help reveal power-law behavior in the tail.
- **Tail analysis:** examines the behavior of unusually large observations.

A roughly straight-line pattern on an appropriate log-log plot can be evidence of power-law behavior, but it is not definitive proof on its own. Model fitting and statistical validation are also important.

## 17. Real-World Examples

### 1. Wealth Distribution

Wealth is often highly concentrated:

- Many people have relatively low or moderate wealth.
- A small number of individuals possess extremely large amounts of wealth.

This can produce a long right tail.

### 2. Software Defects

In software systems:

- A small number of defects may cause a large proportion of failures.
- Fixing high-impact defects can therefore produce a large improvement.

This pattern is commonly described using the Pareto Principle. It does not mean every defect dataset follows a Pareto Distribution.

### 3. Business Revenue

A small percentage of customers may contribute a large percentage of total revenue.

```text
Small share of customers
           |
           v
Large share of revenue
```

The exact proportions vary from business to business.

### 4. Sales and Products

A small number of products may generate a large proportion of total sales.

This analysis can help businesses identify:

- High-performing products
- Important customers
- Revenue concentration

### 5. City and Population Size

Population distributions can exhibit substantial inequality:

- Many cities have relatively small populations.
- A small number of cities have extremely large populations.

Such patterns are often studied using heavy-tailed or power-law models.

## 18. Applications

Pareto and Pareto-like models are useful in areas such as:

- Economics and wealth analysis
- Business analytics
- Revenue and customer analysis
- Risk analysis
- Reliability engineering
- Software defect analysis
- Network analysis
- Population studies
- Data Science

## 19. Pareto Distribution in Data Science

Many real-world datasets are not Normally distributed. Pareto-like behavior may appear in data such as:

- Income and wealth
- Transaction sizes
- Website traffic
- Insurance claims
- File sizes
- Network activity

Understanding heavy-tailed distributions can help analysts investigate:

- Extreme values
- Outliers
- Risk concentration
- Unequal distributions

It is important to distinguish a dataset that is merely right-skewed from one that genuinely follows a Pareto model.

## 20. Pareto vs. Normal vs. Log-Normal

| Property | Normal | Log-Normal | Pareto |
|---|---|---|---|
| Type | Continuous | Continuous | Continuous |
| Shape | Bell-shaped | Right-skewed | Right-skewed |
| Symmetric | Yes | No | No |
| Support | All real numbers | Positive values | $x\geq x_m$ |
| Tail behavior | Light (exponential-type) | Heavier than Normal, but not power-law | Power-law; very heavy |
| Negative values possible? | Yes | No | No |
| Mean | Always finite | Always finite | Finite only if $\alpha>1$ |
| Variance | Always finite | Always finite | Finite only if $\alpha>2$ |
| Main characteristic | Symmetry | Logarithm is Normally distributed | Power-law tail |

## 21. Key Points

- The Pareto Distribution is a **continuous probability distribution**.
- It is **right-skewed** and has a **long, heavy right tail**.
- It is closely related to **power-law behavior**.
- It is commonly associated with the **Pareto Principle (80/20 Rule)**, but an exact 80/20 split is not required.
- Its standard Type I parameters are:
  - $x_m$: minimum possible value (scale parameter)
  - $\alpha$: shape parameter
- A smaller $\alpha$ produces a heavier tail.
- A larger $\alpha$ produces a faster-decaying tail.
- The mean is finite only when $\alpha>1$.
- The variance is finite only when $\alpha>2$.
- Histograms, Q-Q plots, log-log plots, and tail analysis can help investigate Pareto-like behavior.
- Box-Cox can reduce skewness in positive data, but it does not guarantee normality.

## 22. Interview Questions

1. What is a Pareto Distribution?
2. Is the Pareto Distribution continuous or discrete?
3. Why is the Pareto Distribution called heavy-tailed?
4. What is the Pareto Principle?
5. What is the 80/20 Rule?
6. What does $\alpha$ (alpha) represent?
7. What happens to the tail when $\alpha$ decreases?
8. What happens to the tail when $\alpha$ increases?
9. What is the difference between a power law and the Pareto Distribution?
10. What are the parameters of a standard Pareto Distribution?
11. Under what condition does its mean exist as a finite value?
12. Under what condition does its variance exist as a finite value?
13. What are some real-world examples of Pareto-like data?
14. How is the Pareto Distribution different from the Normal Distribution?
15. How is it different from the Log-Normal Distribution?
16. How can you investigate whether data has a Pareto-like tail?
17. What is the role of a Q-Q Plot?
18. What is the Box-Cox Transformation?
19. Does Box-Cox always convert Pareto data into a Normal Distribution?
20. Why are heavy-tailed distributions important in Data Science?

## 23. Quick Revision

| Property | Description |
|---|---|
| Type | Continuous probability distribution |
| Shape | Right-skewed |
| Tail | Long, heavy right tail |
| Parameters | $x_m$, $\alpha$ |
| $x_m$ | Minimum possible value (scale parameter) |
| $\alpha$ | Shape parameter |
| Distribution family | Power-law related |
| Associated principle | Pareto Principle / 80/20 Rule |
| Mean | $\frac{\alpha x_m}{\alpha-1}$, if $\alpha>1$ |
| Variance | $\frac{\alpha x_m^2}{(\alpha-1)^2(\alpha-2)}$, if $\alpha>2$ |
| Applications | Wealth, revenue, risk, defects, population |
| Analysis | Histogram, Q-Q Plot, log-log analysis, tail analysis |

## 💡 Remember

- **Normal** → Symmetric bell curve.
- **Log-Normal** → Right-skewed distribution whose logarithm is Normally distributed.
- **Power Law** → General mathematical relationship involving powers.
- **Pareto** → Specific heavy-tailed probability distribution related to power laws.
- **80/20 Rule** → A small proportion of causes may account for a large proportion of effects.
