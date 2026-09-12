# Analysis of Variance (ANOVA)

**ANOVA** stands for **Analysis of Variance**.

It is a statistical method used to compare the means of **two or more
groups**.

ANOVA is particularly useful when we want to determine whether there are
statistically significant differences among several group means.

---

## Topics Covered

- What is ANOVA?
- Why ANOVA is Used
- Factors and Levels
- Factor vs Level
- ANOVA Assumptions
- Normality
- Absence of Outliers
- Homogeneity of Variance
- Independent and Random Samples
- Types of ANOVA
  - One-Way ANOVA
  - Repeated Measures ANOVA
  - Factorial ANOVA
- Hypothesis Testing in ANOVA
- F-Test Statistic
- Between-Group Variance
- Within-Group Variance
- Sum of Squares
- Degrees of Freedom
- Mean Squares
- F-Statistic
- Critical F-Value
- Decision Rule
- Complete ANOVA Workflow
- Python Implementation

---

# 1. What Is ANOVA?

ANOVA stands for:

> **Analysis of Variance**

It is a statistical method used to:

> **Compare the means of two or more groups.**

For example, if we want to compare the means of:

- 2 groups
- 3 groups
- 4 groups
- or more groups

we can use ANOVA.

The important idea is:

$$
\boxed{\text{ANOVA} \rightarrow \text{Compare means of 2 or more groups}}
$$

---

# 2. Why Do We Use ANOVA?

Statistical tests such as the Z-test and t-test can be used to compare
means under their respective conditions.

ANOVA becomes particularly useful when we have **two or more groups**
whose means we want to compare.

For example:

```text
Group 1 ──┐
Group 2 ──┤
Group 3 ──┼──→ ANOVA → Compare Means
Group 4 ──┘
````

---

# 3. Important Components of ANOVA

Two important terms are:

1. **Factor**
2. **Level**

Understanding these terms is essential when working with ANOVA problems.

---

# 4. Factor

A **factor** is the variable or characteristic that we are studying.

### Example — Medicine

Suppose we are studying the effect of a medicine.

Here:

```math
\boxed{\text{Medicine}=\text{Factor}}
```

The factor represents the main variable being investigated.

---

# 5. Levels

A factor can have different possible values or categories.

These are called **levels**.

### Medicine Example

Suppose a medicine is administered at different dosages:

- 5 mg
- 10 mg
- 15 mg

Here:

```math
\text{Medicine}=\text{Factor}
```

and:

```math
5\text{ mg},10\text{ mg},15\text{ mg}
=
\text{Levels}
```

Therefore:

```

```

```
Medicine
├── 5 mg  → Level 1
├── 10 mg → Level 2
└── 15 mg → Level 3
```

---

# 6. Another Example — Mode of Payment

Consider **mode of payment**.

This is the factor:

```math
\boxed{\text{Mode of Payment}=\text{Factor}}
```

Possible levels include:

- Google Pay
- PhonePe
- IMPS
- NEFT
- Demand Draft

Therefore:

```

```

```
Mode of Payment
├── Google Pay
├── PhonePe
├── IMPS
├── NEFT
└── Demand Draft
```

These individual options are the levels of the factor.

---

# 7. Factor vs Level

| TermMeaningExample |                                            |                    |
| ------------------ | ------------------------------------------ | ------------------ |
| Factor             | Variable being studied                     | Medicine           |
| Level              | Different value/category within the factor | 5 mg, 10 mg, 15 mg |

Another example:

| FactorLevels    |                                 |
| --------------- | ------------------------------- |
| Mode of Payment | Google Pay, PhonePe, IMPS, NEFT |
| Medicine        | 5 mg, 10 mg, 15 mg              |

### Easy Way to Remember

> **Factor = What are we studying?**

> **Level = What are the different values/categories of that factor?**

---

# 8. ANOVA Assumptions

Before applying ANOVA, the problem should satisfy certain assumptions.

The four assumptions discussed in the lectures are:

1. Normality of the sampling distribution of the mean
2. Absence of problematic outliers
3. Homogeneity of variance
4. Independent and randomly selected samples

These assumptions are also important from an interview perspective.

---

## 8.1 Normality

The first assumption is:

> **Normality of Sampling Distribution of Mean**

The distribution of sample means should be approximately normally

distributed.

This connects to the **Central Limit Theorem (CLT)**.

Conceptually:

```math
\boxed{
\text{Sampling Distribution of Mean}
\rightarrow
\text{Approximately Normal}
}
```

---

## 8.2 Absence of Outliers

The dataset should not contain problematic outliers.

Outliers can affect statistical analysis and should be investigated before

performing ANOVA.

The lectures mention techniques such as:

- Box Plot
- Interquartile Range (IQR)

for identifying outliers.

---

## 8.3 Homogeneity of Variance

The population variances across the different levels of the factor should

be approximately equal.

For three groups:

```math
\boxed{
\sigma_1^2\approx\sigma_2^2\approx\sigma_3^2
}
```

This is called **homogeneity of variance**.

---

## 8.4 Independent and Random Samples

The samples should be:

- Independent
- Randomly selected

### Independent

One observation/sample should not influence another.

### Random

Samples should be selected randomly rather than deliberately in a

biased manner.

---

## ANOVA Assumption Memory Trick

Remember:

```math
\boxed{\text{N-O-H-I}}
```

- **N** → Normality
- **O** → Outliers absent
- **H** → Homogeneity of variance
- **I** → Independent & random samples

---

# 9. Types of ANOVA

The three main types discussed are:

1. **One-Way ANOVA**
2. **Repeated Measures ANOVA**
3. **Factorial ANOVA**

The type depends mainly on:

- Number of factors
- Relationship between levels

---

# 10. One-Way ANOVA

In **One-Way ANOVA**, there is:

- One factor
- At least two levels
- Independent levels

Therefore:

```math
\boxed{
\text{One factor + 2 or more independent levels}
}
```

### Example — Medication and Headache

Suppose a doctor wants to study a medication for reducing headaches.

Participants are divided into three dosage groups:

- 10 mg
- 20 mg
- 30 mg

The participants rate their headache.

Here:

**Factor:**

```math
\text{Medication}
```

**Levels:**

```math
10\text{ mg},20\text{ mg},30\text{ mg}
```

The groups are independent because a participant belongs to one dosage

group.

Therefore:

```math
\boxed{\text{One-Way ANOVA}}
```

---

# 11. Repeated Measures ANOVA

In **Repeated Measures ANOVA**, there is:

- One factor
- At least two levels
- Dependent levels

Therefore:

```math
\boxed{
\text{One factor + 2 or more dependent levels}
}
```

The key difference from One-Way ANOVA is that the **same participants are**
**
measured repeatedly**.

### Example — Running

Suppose the same people are measured on:

- Day 1
- Day 2
- Day 3

For example:

| PersonDay 1Day 2Day 3 |      |      |      |
| --------------------- | ---- | ---- | ---- |
| Person 1              | 8 km | 5 km | 4 km |
| Person 2              | 7 km | 4 km | 9 km |
| Person 3              | ...  | ...  | ...  |

The same participants are measured across all three days.

Therefore, the measurements are dependent.

Hence:

```math
\boxed{\text{Repeated Measures ANOVA}}
```

---

# 12. Factorial ANOVA

In **Factorial ANOVA**, there are:

- Two or more factors
- Each factor has at least two levels
- Levels can be independent or dependent

Therefore:

```math
\boxed{
\text{2+ factors + each factor has 2+ levels}
}
```

### Example — Running + Gender

Suppose we have:

### Factor 1

**Running**

Levels:

- Day 1
- Day 2
- Day 3

### Factor 2

**Gender**

Levels:

- Male
- Female

Therefore:

| FactorLevels |                     |
| ------------ | ------------------- |
| Running      | Day 1, Day 2, Day 3 |
| Gender       | Male, Female        |

This represents:

```math
\boxed{\text{Factorial ANOVA}}
```

---

# 13. Comparing the Three Types

| TypeNumber of FactorsLevelsRelationship |    |                    |                          |
| --------------------------------------- | -- | ------------------ | ------------------------ |
| One-Way ANOVA                           | 1  | 2+                 | Independent              |
| Repeated Measures ANOVA                 | 1  | 2+                 | Dependent                |
| Factorial ANOVA                         | 2+ | Each factor has 2+ | Independent or dependent |

---

# 14. How to Identify the Type of ANOVA

When given an ANOVA problem, ask:

### Question 1

> How many factors are there?

If:

```math
\text{One factor}
```

→ Go to Question 2.

If:

```math
\text{Two or more factors}
```

→ **Factorial ANOVA**

### Question 2

> Are the levels independent or dependent?

If:

```math
\text{Independent}
```

→ **One-Way ANOVA**

If:

```math
\text{Dependent}
```

→ **Repeated Measures ANOVA**

### Decision Tree

```

```

```
                    ANOVA
                      │
              How many factors?
                 /           \
               One          2 or more
                │               │
         Are levels?      Factorial ANOVA
          /       \
 Independent     Dependent
     │               │
One-Way ANOVA   Repeated Measures
                    ANOVA
```

---

# 15. Hypothesis Testing in ANOVA

ANOVA compares group means using variance.

The hypothesis test begins by defining:

- Null Hypothesis ($H\_0$)
- Alternative Hypothesis ($H\_1$)

---

## Null Hypothesis

The null hypothesis states that all group means are equal:

```math
\boxed{
H_0:\mu_1=\mu_2=\mu_3=\cdots=\mu_k
}
```

where $k$ is the number of groups.

---

## Alternative Hypothesis

The alternative hypothesis states:

> **At least one group mean is different.**

```math
\boxed{
H_1:\text{At least one mean is different}
}
```

We should **not** write:

```math
\mu_1\ne\mu_2\ne\mu_3
```

because that would imply that every mean differs from every other mean.

ANOVA only requires that **at least one mean differs**.

---

# 16. F-Test Statistic

ANOVA hypothesis testing uses the **F-test statistic**.

The core relationship is:

```math
\boxed{
F=
\frac{\text{Variance Between Groups}}
{\text{Variance Within Groups}}
}
```

The F-statistic compares variation between groups with variation within

groups.

---

## Between-Group Variance

This measures differences between the different groups.

It reflects how far apart the group means are.

---

## Within-Group Variance

This measures how much observations inside each group differ from that

group's own mean.

---

# 17. ANOVA Partitioning of Variance

The total variation in the data can be partitioned into:

```math
\boxed{
SS_{Total}=SS_{Between}+SS_{Within}
}
```

Where:

- $SS\_{Between}$ = variation between groups
- $SS\_{Within}$ = variation within groups
- $SS\_{Total}$ = total variation

This is the central idea behind **partitioning of variance** in ANOVA.

---

# 18. One-Way ANOVA Example

Consider a medication study.

A doctor wants to test a medication that reduces headaches.

There are three dosage groups:

- 15 mg
- 30 mg
- 45 mg

Patients rate their headache from 1 to 10.

The data are:

| Person15 mg30 mg45 mg |   |   |   |
| --------------------- | - | - | - |
| 1                     | 9 | 7 | 4 |
| 2                     | 8 | 6 | 3 |
| 3                     | 7 | 5 | 2 |
| 4                     | 8 | 7 | 3 |
| 5                     | 8 | 8 | 4 |
| 6                     | 9 | 8 | 3 |
| 7                     | 8 | 6 | 2 |

There are:

```math
7
```

observations per group and:

```math
3
```

groups.

Total observations:

```math
N=7\times3=21
```

---

# 19. Define the Hypotheses

### Null Hypothesis

```math
\boxed{
H_0:
\mu_{15mg}=
\mu_{30mg}=
\mu_{45mg}
}
```

### Alternative Hypothesis

```math
\boxed{
H_1:
\text{Not all means are equal}
}
```

That means at least one dosage group has a different mean.

---

# 20. Significance Level

Given:

```math
\alpha=0.05
```

The corresponding confidence level is:

```math
1-\alpha
```

```math
1-0.05=0.95
```

Therefore:

```math
\boxed{95\%}
```

---

# 21. Degrees of Freedom

ANOVA uses multiple degrees of freedom.

Let:

- $a$ = number of groups
- $N$ = total number of observations

For this example:

```math
a=3
```

```math
N=21
```

---

## Between-Group Degrees of Freedom

```math
\boxed{
df_{Between}=a-1
}
```

Therefore:

```math
df_{Between}=3-1=2
```

---

## Within-Group Degrees of Freedom

```math
\boxed{
df_{Within}=N-a
}
```

Therefore:

```math
df_{Within}=21-3=18
```

---

## Total Degrees of Freedom

```math
\boxed{
df_{Total}=N-1
}
```

Therefore:

```math
df_{Total}=21-1=20
```

Check:

```math
df_{Between}+df_{Within}
=
2+18
=
20
```

Therefore:

```math
\boxed{
df_{Between}+df_{Within}=df_{Total}
}
```

---

# 22. F-Distribution

The F-distribution is **right-skewed**.

Unlike the Z-distribution and t-distribution, it is not symmetrical.

Therefore, the ANOVA rejection region is located in the **right tail**.

For:

```math
df_1=2
```

```math
df_2=18
```

and:

```math
\alpha=0.05
```

the critical value is approximately:

```math
\boxed{
F_{critical}=3.5546
}
```

---

# 23. Decision Rule

If:

```math
F_{calculated}>F_{critical}
```

then:

```math
\boxed{\text{Reject }H_0}
```

Otherwise:

```math
F_{calculated}\leq F_{critical}
```

then:

```math
\boxed{\text{Fail to reject }H_0}
```

For this example:

```math
F_{critical}=3.5546
```

---

# 24. Sum of Squares Between

The lecture uses:

```math
\boxed{
SS_{Between}
=
\sum
\frac{(\sum A_i)^2}{n}
-
\frac{T^2}{N}
}
```

where:

- $A\_i$ = observations in each group
- $n$ = observations per group
- $T$ = grand total
- $N$ = total observations

The group totals are:

```math
15mg=57
```

```math
30mg=47
```

```math
45mg=21
```

Grand total:

```math
T=57+47+21=125
```

Therefore:

```math
SS_{Between}
=
\frac{57^2+47^2+21^2}{7}
-
\frac{125^2}{21}
```

```math
\boxed{
SS_{Between}\approx98.67
}
```

---

# 25. Sum of Squares Within

The lecture uses:

```math
\boxed{
SS_{Within}
=
\sum Y^2
-
\sum
\frac{(\sum A_i)^2}{n}
}
```

For this dataset:

```math
\sum Y^2=853
```

Therefore:

```math
SS_{Within}
=
853
-
\frac{57^2+47^2+21^2}{7}
```

```math
\boxed{
SS_{Within}\approx10.29
}
```

---

# 26. Sum of Squares Total

The total sum of squares is:

```math
\boxed{
SS_{Total}
=
SS_{Between}+SS_{Within}
}
```

Therefore:

```math
SS_{Total}
=
98.67+10.29
```

```math
\boxed{
SS_{Total}\approx108.96
}
```

---

# 27. ANOVA Sum of Squares Table

| SourceSSdf |        |    |
| ---------- | ------ | -- |
| Between    | 98.67  | 2  |
| Within     | 10.29  | 18 |
| Total      | 108.96 | 20 |

---

# 28. Mean Squares

Mean Square is calculated as:

```math
\boxed{
MS=\frac{SS}{df}
}
```

---

## Mean Square Between

```math
MS_{Between}
=
\frac{SS_{Between}}{df_{Between}}
```

```math
=
\frac{98.67}{2}
```

```math
\boxed{
MS_{Between}\approx49.34
}
```

---

## Mean Square Within

```math
MS_{Within}
=
\frac{SS_{Within}}{df_{Within}}
```

```math
=
\frac{10.29}{18}
```

```math
\boxed{
MS_{Within}\approx0.57
}
```

---

# 29. Calculate the F-Statistic

The F-statistic is:

```math
\boxed{
F=
\frac{MS_{Between}}{MS_{Within}}
}
```

Therefore:

```math
F=
\frac{49.34}{0.57}
```

```math
\boxed{
F\approx86.56
}
```

A large F-statistic indicates that between-group variation is large

relative to within-group variation.

---

# 30. Compare F With the Critical Value

We have:

```math
F_{calculated}=86.56
```

and:

```math
F_{critical}=3.5546
```

Since:

```math
86.56>3.5546
```

the calculated F-value falls in the rejection region.

Therefore:

```math
\boxed{\text{Reject }H_0}
```

---

# 31. Final Conclusion

We reject the null hypothesis that all three dosage-group means are equal.

Therefore:

> **There is a significant difference between the three dosage**
> **
> conditions.**

In other words, **not all group means are equal** — at least one dosage

group differs significantly from the others in headache rating.

ANOVA by itself tells us that at least one group differs; it does not by

itself identify exactly which specific groups differ.

---

# 32. Complete ANOVA Hypothesis-Testing Workflow

```

```

```
Define H₀ and H₁
        ↓
Choose significance level α
        ↓
Calculate degrees of freedom
(Between, Within, Total)
        ↓
Find F critical value
from F-table
        ↓
Calculate SS Between
SS Within
SS Total
        ↓
Calculate MS Between
MS Within
        ↓
Calculate F
        ↓
Compare F calculated
with F critical
       /       \
   Greater   Smaller/Equal
      ↓           ↓
 Reject H₀    Fail to reject H₀
      ↓
Statistical Conclusion
```

---

# 33. Important Formula Sheet

### Between-Group Degrees of Freedom

```math
\boxed{
df_{Between}=a-1
}
```

### Within-Group Degrees of Freedom

```math
\boxed{
df_{Within}=N-a
}
```

### Total Degrees of Freedom

```math
\boxed{
df_{Total}=N-1
}
```

### Sum of Squares

```math
\boxed{
SS_{Total}
=
SS_{Between}+SS_{Within}
}
```

### Mean Square

```math
\boxed{
MS=\frac{SS}{df}
}
```

### F-Statistic

```math
\boxed{
F=
\frac{MS_{Between}}{MS_{Within}}
}
```

### Decision Rule

```math
\boxed{
F_{calculated}>F_{critical}
\Rightarrow
\text{Reject }H_0
}
```

---

# 34. Interview-Ready Summary

### One-Way ANOVA

One factor with at least two independent levels.

**Example:**

Comparing headache scores across 10 mg, 20 mg, and 30 mg medication groups.

### Repeated Measures ANOVA

One factor with at least two dependent levels.

**Example:**

Measuring the same people's running performance on Day 1, Day 2, and

Day 3.

### Factorial ANOVA

Two or more factors, each having at least two levels.

**Example:**

Studying running performance across different days and genders.

---

# Key Takeaways

- ANOVA stands for **Analysis of Variance**.
- ANOVA is used to compare the means of two or more groups.
- A **factor** is the variable being studied.
- A **level** is a value or category within a factor.
- ANOVA has four important assumptions:
- Normality
- Absence of problematic outliers
- Homogeneity of variance
- Independent and randomly selected samples
- The three types discussed are:
- One-Way ANOVA
- Repeated Measures ANOVA
- Factorial ANOVA
- ANOVA hypothesis testing uses the **F-statistic**.
- The null hypothesis states that all group means are equal.
- The alternative hypothesis states that at least one mean is different.
- ANOVA partitions total variation into between-group and within-group
  variation.
- The F-statistic is:

```math
F=
\frac{MS_{Between}}{MS_{Within}}
```

- The F-distribution is right-skewed.
- If the calculated F-value exceeds the critical F-value, reject $H\_0$.
- A significant ANOVA result tells us that at least one group mean differs,
  but does not identify which specific groups differ.

---

## Core Idea

> **ANOVA compares group means by comparing the variation between groups with the variation within groups**

$$
F = \frac{\text{Between-Group Variation}}{\text{Within-Group Variation}}
$$

## ANOVA terminology:
$$
F = \frac{MS_{\text{Between}}}{MS_{\text{Within}}}
$$
