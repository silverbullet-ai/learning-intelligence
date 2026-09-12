```
```

````
# Chi-Square Test

The **Chi-Square Test ($\chi^2$)** is a statistical test used for
categorical data.

This section focuses on the **Chi-Square Goodness-of-Fit Test**, which is
used to determine whether an observed categorical distribution fits a
theoretical or expected distribution.

---

## Topics Covered

- Chi-Square Test
- Categorical Data
- Nominal and Ordinal Data
- Chi-Square Goodness-of-Fit Test
- Observed Distribution
- Expected Distribution
- Expected Values
- Hypothesis Testing
- Significance Level
- Confidence Level
- Degrees of Freedom
- Chi-Square Test Statistic
- Critical Value
- Decision Rule
- Complete Chi-Square Workflow
- Python Implementation

---

# 1. What Is a Chi-Square Test?

The **Chi-Square Test ($\chi^2$)** is a statistical test used for
categorical data.

The test discussed in this section is the:

> **Chi-Square Goodness-of-Fit Test**

It is used to determine whether observed categorical data fits a
theoretical or expected categorical distribution.

---

# 2. Key Characteristics

The Chi-Square Goodness-of-Fit Test discussed here is:

- A non-parametric test
- Performed on categorical data
- Used to make conclusions about population proportions
- Used to compare an observed categorical distribution with a theoretical
  categorical distribution

---

# 3. Categorical Data

Categorical data represents observations divided into categories.

Categorical data can broadly be:

- **Nominal**
- **Ordinal**

Examples include:

- Bike color
- Handedness
- Weight categories
- Other categorical groups

---

# 4. Goodness of Fit

The central question in a goodness-of-fit test is:

> **Does the observed sample data support the theory about the population?**

We compare:

$$
\boxed{
\text{Observed Distribution}
\quad\text{vs}\quad
\text{Theoretical/Expected Distribution}
}
$$

If the observed distribution is sufficiently close to what the theory
predicts, the data can be considered a good fit for the theory.

---

# 5. Observed vs Expected Distribution

This distinction is fundamental to the Chi-Square Goodness-of-Fit Test.

## Theoretical / Expected Distribution

The distribution predicted by a theory or population proportion.

For example:

$$
\frac{1}{3},\frac{1}{3},\frac{1}{3}
$$

## Observed Distribution

The distribution actually obtained from sample data.

For example:

$$
22,\;17,\;59
$$

The goodness-of-fit test compares the observed values with the expected
values.

---

# 6. Example — Bike Color Preference

Suppose a theory states that:

- $\frac{1}{3}$ of males like yellow bikes
- $\frac{1}{3}$ of males like red bikes
- $\frac{1}{3}$ of males like orange bikes

This represents the theoretical categorical distribution.

A sample produces:

| Bike Color | Observed |
|---|---:|
| Yellow | 22 |
| Red | 17 |
| Orange | 59 |
| **Total** | **98** |

The Chi-Square Goodness-of-Fit Test can be used to determine whether this
observed sample supports the theoretical distribution.

---

# 7. Example — Left-Handed Students

Consider a science class containing:

$$
75
$$

students.

Suppose:

$$
11
$$

students are left-handed.

The question is:

> **Does this class fit the theory that 12% of people are left-handed?**

### Step 1: Identify the Categories

There are two categories:

- Left-handed
- Right-handed

### Step 2: Identify Observed Values

Left-handed students:

$$
11
$$

Right-handed students:

$$
75-11=64
$$

Therefore:

| Category | Observed |
|---|---:|
| Left-handed | 11 |
| Right-handed | 64 |
| **Total** | **75** |

---

# 8. Calculate Expected Values

The theory states that:

$$
12\%
$$

of people are left-handed.

Therefore:

$$
E_{\text{left}}=0.12\times75
$$

$$
E_{\text{left}}=9
$$

The remaining students are expected to be right-handed:

$$
75-9=66
$$

Therefore:

| Category | Observed | Expected |
|---|---:|---:|
| Left-handed | 11 | 9 |
| Right-handed | 64 | 66 |
| **Total** | **75** | **75** |

The observed distribution is:

$$
(11,64)
$$

The expected distribution is:

$$
(9,66)
$$

---

# 9. What Are We Testing?

The Chi-Square Goodness-of-Fit Test determines whether the difference
between the observed and expected values is statistically significant.

In other words:

> **Does the observed distribution provide a good fit for the theoretical
> distribution?**

---

# 10. Chi-Square Hypothesis Testing

Consider the following example.

A city's **2010 census** reported this weight distribution:

| Weight Category | 2010 Population |
|---|---:|
| Less than 50 kg | 20% |
| 50–75 kg | 30% |
| Greater than 75 kg | 50% |

In 2020, a sample of 500 individuals was collected:

| Weight Category | 2020 Observed |
|---|---:|
| Less than 50 kg | 140 |
| 50–75 kg | 160 |
| Greater than 75 kg | 200 |
| **Total** | **500** |

At:

$$
\alpha=0.05
$$

we want to determine whether the population weight distribution has
changed between 2010 and 2020.

---

# 11. Why Chi-Square Test?

There are three categorical groups:

- Less than 50 kg
- 50–75 kg
- Greater than 75 kg

Therefore, we use a:

$$
\boxed{\text{Chi-Square Goodness-of-Fit Test}}
$$

The goal is to compare:

$$
\boxed{\text{Observed Values vs Expected Values}}
$$

---

# 12. Observed Data

The 2020 sample provides the observed values:

| Weight Category | Observed ($O$) |
|---|---:|
| Less than 50 kg | 140 |
| 50–75 kg | 160 |
| Greater than 75 kg | 200 |
| **Total** | **500** |

---

# 13. Expected Data

The 2010 population percentages are treated as the expected distribution
for 2020 if there has been no change.

### Less than 50 kg

$$
E=0.20\times500
$$

$$
E=100
$$

### 50–75 kg

$$
E=0.30\times500
$$

$$
E=150
$$

### Greater than 75 kg

$$
E=0.50\times500
$$

$$
E=250
$$

Therefore:

| Weight Category | Observed ($O$) | Expected ($E$) |
|---|---:|---:|
| Less than 50 kg | 140 | 100 |
| 50–75 kg | 160 | 150 |
| Greater than 75 kg | 200 | 250 |
| **Total** | **500** | **500** |

---

# 14. Hypotheses

## Null Hypothesis ($H_0$)

The observed data meets the expected distribution.

In this problem:

> The 2020 population has the same weight distribution as the 2010
> population.

---

## Alternative Hypothesis ($H_1$)

The observed data does not meet the expected distribution.

In this problem:

> The weight distribution has changed.

Therefore:

$$
H_0:\text{The distribution has not changed}
$$

$$
H_1:\text{The distribution has changed}
$$

---

# 15. Significance Level and Confidence Level

Given:

$$
\alpha=0.05
$$

The corresponding confidence level is:

$$
1-\alpha
$$

$$
1-0.05=0.95
$$

Therefore:

$$
\boxed{95\%}
$$

---

# 16. Degrees of Freedom

For the Chi-Square Goodness-of-Fit Test:

$$
\boxed{df=k-1}
$$

where:

- $df$ = degrees of freedom
- $k$ = number of categories

There are three categories:

$$
k=3
$$

Therefore:

$$
df=3-1
$$

$$
\boxed{df=2}
$$

---

# 17. Chi-Square Distribution and Critical Value

Unlike the Z-distribution and t-distribution, the Chi-Square distribution
is not symmetrical.

Therefore, the goodness-of-fit test uses a right-side critical boundary.

For:

$$
\alpha=0.05
$$

and:

$$
df=2
$$

the critical value is:

$$
\boxed{\chi^2_{\text{critical}}=5.991}
$$

---

# 18. Decision Rule

If:

$$
\chi^2_{\text{calculated}}>5.991
$$

then:

$$
\boxed{\text{Reject }H_0}
$$

Otherwise, if:

$$
\chi^2_{\text{calculated}}\leq5.991
$$

then:

$$
\boxed{\text{Fail to reject }H_0}
$$

---

# 19. Chi-Square Test Statistic

The Chi-Square test statistic is:

$$
\boxed{
\chi^2=
\sum
\frac{(O-E)^2}{E}
}
$$

Where:

- $O$ = Observed value
- $E$ = Expected value

The calculation is performed for every category and the individual
contributions are added together.

---

# 20. Calculate the Test Statistic

### Category 1 — Less than 50 kg

$$
\frac{(140-100)^2}{100}
$$

$$
=
\frac{40^2}{100}
$$

$$
=16
$$

### Category 2 — 50–75 kg

$$
\frac{(160-150)^2}{150}
$$

$$
=
\frac{10^2}{150}
$$

$$
\approx0.67
$$

### Category 3 — Greater than 75 kg

$$
\frac{(200-250)^2}{250}
$$

$$
=
\frac{(-50)^2}{250}
$$

$$
=10
$$

Therefore:

$$
\chi^2=16+0.67+10
$$

$$
\boxed{\chi^2\approx26.67}
$$

---

# 21. Compare With Critical Value

We have:

$$
\chi^2_{\text{calculated}}=26.67
$$

and:

$$
\chi^2_{\text{critical}}=5.991
$$

Since:

$$
26.67>5.991
$$

the test statistic falls in the rejection region.

Therefore:

$$
\boxed{\text{Reject }H_0}
$$

---

# 22. Final Conclusion

We reject the null hypothesis that the 2020 data follows the 2010 expected
distribution.

Therefore:

> **The weight distribution of the 2020 population is different from the
> 2010 population.**

At the 5% significance level, the sample provides sufficient evidence that
the population weight distribution has changed over the ten-year period.

---

# 23. Complete Chi-Square Workflow

The complete process is:

```text
Given categorical data
        ↓
Identify Observed values
        ↓
Determine Expected values
        ↓
State H₀ and H₁
        ↓
Choose significance α
        ↓
Calculate df = k − 1
        ↓
Find χ² critical value
        ↓
Calculate χ² statistic
        ↓
Compare χ² calculated
with χ² critical
       /       \
  Greater     Smaller
     ↓           ↓
Reject H₀    Fail to reject H₀
        ↓
Statistical Conclusion
````

---

# 24. Important Formula Sheet

### Expected Value

```math
\boxed{
E=\text{Expected Proportion}\times n
}
```

### Chi-Square Statistic

```math
\boxed{
\chi^2=
\sum
\frac{(O-E)^2}{E}
}
```

### Degrees of Freedom

```math
\boxed{
df=k-1
}
```

### Decision Rule

```math
\boxed{
\chi^2_{\text{calculated}}
>
\chi^2_{\text{critical}}
\Rightarrow
\text{Reject }H_0
}
```

---

# 25. Easy Memory Trick

For a Chi-Square Goodness-of-Fit problem:

```math
\boxed{
O\rightarrow E\rightarrow H\rightarrow df
\rightarrow\text{Critical Value}
\rightarrow\chi^2
\rightarrow\text{Compare}
\rightarrow\text{Conclusion}
}
```

Where:

- **O** → Observed 
- **E** → Expected 
- **H** → Hypothesis 
- **df** → Degrees of Freedom 
- **Critical Value** → Chi-Square critical value 
- **$\chi^2$** → Chi-Square test statistic 
- **Compare** → Compare calculated and critical values 
- **Conclusion** → Reject or fail to reject $H\_0$ 

---

# Key Takeaways

-  Chi-Square Goodness-of-Fit is used for **categorical data**. 
-  It compares an **observed categorical distribution** with a
   **theoretical/expected distribution**. 
-  Expected values are calculated from theoretical proportions. 
-  Observed values come directly from the sample. 
-  The test is a **non-parametric test**. 
-  The test statistic is: 

```math
\chi^2=
\sum
\frac{(O-E)^2}{E}
```

-  Degrees of freedom are: 

```math
df=k-1
```

-  The Chi-Square distribution is not symmetrical. 
-  The goodness-of-fit test uses a right-side critical boundary. 
-  If the calculated Chi-Square statistic exceeds the critical value,
   reject $H\_0$. 
-  Otherwise, fail to reject $H\_0$. 

---

## Core Idea

> **Chi-Square Goodness of Fit = Observed Distribution vs Expected**
> **
> Distribution**