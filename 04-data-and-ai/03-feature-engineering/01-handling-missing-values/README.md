```
```

````
# Handling Missing Values

Handling missing values is one of the fundamental techniques in Feature Engineering.

Real-world datasets are often messy and may contain:

- Missing values
- Incorrect entries
- Incomplete information
- Other data-quality problems

A missing value occurs when some information for a variable is not stored in the dataset.

---

## 1. Why Missing Values Matter

In real-world Data Science, Machine Learning, and Deep Learning projects, the data received is often raw or messy.

For example, consider a survey given to a group of people.

If someone is uncomfortable answering a particular question, they may leave that field empty. When the dataset is created, that empty field becomes a missing value.

Missing values need to be handled before applying many machine learning algorithms.

---

# 2. Mechanisms of Missing Data

There are three main mechanisms through which missing values can occur:

1. **MCAR — Missing Completely At Random**
2. **MAR — Missing At Random**
3. **MNAR — Missing Data Not At Random**

---

## 3. MCAR — Missing Completely At Random

### Definition

**Missing Completely At Random (MCAR)** means that the probability of a value being missing is unrelated to both the observed data and the missing data.

In simple terms:

> There is no specific reason or pattern behind why the value is missing.

The missing values are randomly distributed throughout the dataset.

### Possible Causes

- Data-entry error
- Machine/system error
- Accidental omission

There is no systematic relationship explaining the missingness.

### Example

Suppose a survey collects information about the presence of a particular disease.

If some survey responses are missing simply because of an accidental data-entry problem, the missingness can be considered MCAR.

### Quick Memory

**MCAR → No systematic reason for missingness**

---

# 4. MAR — Missing At Random

### Definition

**Missing At Random (MAR)** means that the probability of a value being missing depends on observed data.

In other words, there is some relationship between the missing value and other information that is already observed in the dataset.

### Example

Suppose a survey collects:

- Gender
- Age
- Income

People may behave differently when answering certain questions.

For example:

- Some men may be less comfortable reporting their income.
- Some women may be less comfortable reporting their age.

Therefore, the missingness is related to another observed variable such as gender.

This represents a systematic relationship.

### Quick Memory

**MAR → Missingness depends on observed data**

---

# 5. MNAR — Missing Data Not At Random

### Definition

**Missing Data Not At Random (MNAR)** means that the probability of a value being missing depends on the value of the missing data itself or other associated factors.

### Example

Suppose we collect:

- Employee income
- Job satisfaction

Employees who are less satisfied with their jobs may be more likely to not report their income.

Therefore, the missingness is related to job satisfaction.

So the missing data is not random.

### Quick Memory

**MNAR → Missingness depends on the missing value or associated factors**

---

# 6. MCAR vs MAR vs MNAR

| Mechanism | Full Form | Main Idea |
|---|---|---|
| MCAR | Missing Completely At Random | No systematic reason for missingness |
| MAR | Missing At Random | Missingness depends on observed data |
| MNAR | Missing Data Not At Random | Missingness depends on the missing value itself or associated factors |

### Easy Memory Trick

```text
MCAR → Completely random
MAR  → Related to observed data
MNAR → Related to the missing information itself
````

---

# 7. Titanic Dataset Example

The lecture uses the **Titanic dataset from Seaborn** because it contains many missing values.

```
```

```
import seaborn as sns

df = sns.load_dataset("titanic")
```

To view the first few rows:

```
```

```
df.head()
```

---

# 8. Checking Missing Values

To check where missing values exist:

```
```

```
df.isnull()
```

This returns:

- `True` → value is missing 
- `False` → value is present 

To count missing values in each column:

```
```

```
df.isnull().sum()
```

This gives the number of null values in each column.

---

# 9. Method 1 — Delete Rows

One simple way of handling missing values is to delete rows containing missing values.

```
```

```
df.dropna()
```

By default, this removes rows containing missing values.

## Problem

Row deletion can cause a huge loss of data.

In the lecture example:

```
```

```
Original data points → 891
After dropping rows → 182
```

Therefore:

```
```

```
891 → 182
```

This represents a massive loss of information.

### Conclusion

Row-wise deletion should not be used blindly, especially when a large amount of data would be lost.

---

# 10. Method 2 — Delete Columns

Sometimes a particular column contains a very large number of missing values.

In that situation, it may be reasonable to remove the entire column.

For example, the `deck` column contains a large number of missing values.

```
```

```
df.dropna(axis=1)
```

### `axis`

```
```

```
axis = 0 → rows
axis = 1 → columns
```

To make the operation permanent:

```
```

```
df.dropna(axis=1, inplace=True)
```

### Important

Column deletion can be appropriate when a column contains too many missing values and is not useful enough to retain.

---

# 11. Imputation Techniques

Instead of deleting data, we can replace missing values.

This process is called **Imputation**.

The lecture covers:

1.  Mean imputation 
2.  Median imputation 
3.  Mode imputation 
4.  Random sample imputation 

---

# 12. Mean Value Imputation

## Definition

Mean imputation replaces missing values with the mean of that column.

```
```

```
Missing Value → Column Mean
```

For example, suppose there are missing values in the `age` column.

First, calculate the mean:

```
```

```
df["age"].mean()
```

Then replace missing values:

```
```

```
df["age"].fillna(df["age"].mean())
```

The lecture obtains approximately:

```
```

```
Mean age ≈ 29.699
```

Therefore, a missing age can be replaced with approximately `29.699`.

### Creating a New Column

```
```

```
df["age_mean"] = df["age"].fillna(df["age"].mean())
```

Now the missing values in `age_mean` are replaced by the mean.

## When to Use Mean Imputation?

Mean imputation works well when numerical data is normally distributed.

```
```

```
Normally Distributed Data → Mean Imputation
```

---

# 13. Median Value Imputation

If the data is skewed or contains outliers, median imputation can be preferred.

## Definition

Median imputation replaces missing values with the median of the column.

```
```

```
Missing Value → Column Median
```

Example:

```
```

```
df["age"].fillna(df["age"].median())
```

Or save the result in a new column:

```
```

```
df["age_median"] = df["age"].fillna(df["age"].median())
```

In the lecture example:

```
```

```
Median age ≈ 28
```

So missing values are replaced with approximately `28`.

### When to Use?

```
```

```
Outliers / Skewed Data → Median Imputation
```

The median is less affected by extreme values than the mean.

---

# 14. Mean vs Median Imputation

| Data ConditionPreferred Method |        |
| ------------------------------ | ------ |
| Normally distributed data      | Mean   |
| Skewed data                    | Median |
| Outliers present               | Median |

### Easy Rule

```
```

```
Normal → Mean
Outliers / Skew → Median
```

---

# 15. Mode Imputation

Mode imputation is generally used for categorical variables.

```
```

```
Categorical Variable → Mode Imputation
```

## Example — `embarked`

First, check its unique values:

```
```

```
df["embarked"].unique()
```

Possible values include:

```
```

```
S
C
Q
NaN
```

Since `embarked` is categorical, we can use the mode.

Find the mode:

```
```

```
df["embarked"].mode()
```

In the lecture example, the mode is:

```
```

```
S
```

Then replace missing values:

```
```

```
df["embarked"].fillna(df["embarked"].mode()[0])
```

Or save it into a new column:

```
```

```
df["embarked_mode"] = df["embarked"].fillna(
    df["embarked"].mode()[0]
)
```

Now the missing values are replaced by the most frequently occurring category.

---

# 16. Checking Whether Missing Values Remain

After imputation, check the number of missing values:

```
```

```
df["embarked_mode"].isnull().sum()
```

Expected output:

```
```

```
0
```

This means there are no remaining null values in that column.

In the lecture example, the original `embarked` column contained two missing values.

---

# 17. Random Sample Imputation

Another technique discussed is **Random Sample Imputation**.

## Idea

Instead of replacing all missing values with the same mean, median, or mode:

1.  Select a random value from the existing values in the column. 
2.  Replace the missing value with that randomly selected value. 

Conceptually:

```
```

```
Existing Values
       ↓
Select a Random Value
       ↓
Replace Missing Value
```

Because the value is randomly selected, the replacement can change each time.

---

# 18. Missing Value Handling Overview

```
```

```
                    Missing Values
                          │
             ┌────────────┴────────────┐
             │                         │
        Delete Data               Imputation
             │                         │
       ┌─────┴─────┐          ┌────────┼────────┐
       │           │          │        │        │
      Rows       Columns     Mean    Median    Mode
                                                │
                                           Categorical
                                              Data
```

---

# 19. Important Techniques

| TechniqueWhat It DoesWhen to Use |                                                                |                                           |
| -------------------------------- | -------------------------------------------------------------- | ----------------------------------------- |
| Row deletion                     | Removes rows containing missing values                         | When data loss is acceptable              |
| Column deletion                  | Removes columns with excessive missing values                  | When a column has too many missing values |
| Mean imputation                  | Replaces missing values with mean                              | Normally distributed numerical data       |
| Median imputation                | Replaces missing values with median                            | Skewed data / outliers                    |
| Mode imputation                  | Replaces missing values with most frequent category            | Categorical variables                     |
| Random sample imputation         | Replaces missing values with randomly selected existing values | Alternative imputation approach           |

---

# 20. Interview Revision

### What are the three missing-data mechanisms?

**MCAR, MAR, MNAR**

### What is MCAR?

Missingness has no systematic relationship with observed or missing data.

### What is MAR?

Missingness depends on observed data.

### What is MNAR?

Missingness depends on the missing value itself or associated factors.

### What is imputation?

Replacing missing values with suitable estimated or substitute values.

### Mean vs Median?

```
```

```
Mean → Normally distributed data
Median → Skewed data / Outliers
```

### What is used for categorical data?

**Mode imputation**

### Why shouldn't we blindly drop rows?

Because a large amount of useful data can be lost.

---

# Quick Revision

```
```

```
Missing Values
│
├── Understand Missingness
│   ├── MCAR → Completely random
│   ├── MAR  → Depends on observed data
│   └── MNAR → Depends on missing information
│
├── Delete Data
│   ├── Rows
│   └── Columns
│
└── Imputation
    ├── Mean → Normal numerical data
    ├── Median → Skew / Outliers
    ├── Mode → Categorical data
    └── Random Sample → Existing random value
```