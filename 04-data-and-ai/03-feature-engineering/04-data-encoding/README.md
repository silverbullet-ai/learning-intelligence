# Data Encoding

**Feature Engineering — Converting Categorical Features into Numerical Values**

Data Encoding is a Feature Engineering technique used to convert categorical features into numerical values so that Machine Learning models can process them.

---

# 1. Why Do We Need Data Encoding?

Machine Learning models primarily work with numerical values.

Consider a dataset containing:

| Experience | Degree | Salary |
|---:|---|---:|
| 2 | B | 40K |
| 5 | Masters | 70K |
| 8 | PhD | 100K |

Here:

- **Experience** → numerical feature
- **Degree** → categorical feature
- **Salary** → target

The `Degree` feature contains categories such as `B`, `Masters`, and `PhD`.

A Machine Learning model cannot directly work with these categorical labels in their original form. Therefore, we need to convert:

**Categorical Data → Numerical Data**

This process is called **Data Encoding**.

---

# 2. Definition of Data Encoding

Data encoding is the process of converting categorical features into meaningful numerical values so that Machine Learning models can understand and process them.

## Basic Idea

```text
Categorical Feature
        ↓
     Encoding
        ↓
Numerical Feature
        ↓
Machine Learning Model
```

---

# 3. Types of Encoding

The lecture introduces three encoding techniques:

## 1. Nominal / One-Hot Encoding

Used for categorical variables where categories do not have a meaningful order.

## 2. Label / Ordinal Encoding

Used to represent categories using numerical values, particularly when an order exists.

## 3. Target-Guided Ordinal Encoding

Uses information from the target variable to determine the encoding.

> This topic focuses primarily on **Nominal / One-Hot Encoding**.

---

# 4. One-Hot Encoding

One-Hot Encoding is also called **Nominal Encoding**.

It converts a categorical feature into multiple binary numerical features.

Each category gets its own column.

---

# 5. Example — Color

Suppose we have a categorical feature:

```text
Color
-----
Red
Green
Blue
Red
Blue
Green
```

There are three unique categories:

```text
Red
Green
Blue
```

One-Hot Encoding creates three new features:

```text
Color_Red
Color_Green
Color_Blue
```

---

# 6. How One-Hot Encoding Works

For every observation:

- The column corresponding to its category gets `1`
- All other category columns get `0`

Example:

| Color | Blue | Green | Red |
|---|---:|---:|---:|
| Red | 0 | 0 | 1 |
| Blue | 1 | 0 | 0 |
| Green | 0 | 1 | 0 |
| Green | 0 | 1 | 0 |
| Red | 0 | 0 | 1 |
| Blue | 1 | 0 | 0 |

Therefore:

```text
Red   → (0, 0, 1)
Blue  → (1, 0, 0)
Green → (0, 1, 0)
```

---

# 7. Why Is It Called One-Hot?

Each observation has exactly one active category.

For example:

```text
Red = (0, 0, 1)
```

Only one position contains `1`.

Hence:

**One category = one "hot" / active position**

---

# 8. One-Hot Encoding Using Scikit-Learn

Scikit-Learn provides the `OneHotEncoder` class for performing One-Hot Encoding.

```python
from sklearn.preprocessing import OneHotEncoder
```

---

# 9. Create the Dataset

```python
import pandas as pd

df = pd.DataFrame({
    "color": [
        "red",
        "blue",
        "blue",
        "green",
        "green",
        "red",
        "blue"
    ]
})

print(df)
```

---

# 10. Create the Encoder

```python
encoder = OneHotEncoder()
```

This creates an instance of `OneHotEncoder`.

---

# 11. Fit and Transform

```python
encoded = encoder.fit_transform(df[["color"]])
```

## `fit_transform()`

This combines two operations:

### `fit()`

Learns the unique categories.

For example:

```text
blue
green
red
```

### `transform()`

Converts the categories into their One-Hot numerical representation.

Therefore:

```text
fit + transform = fit_transform()
```

---

# 12. Why `df[["color"]]`?

The encoder expects the input in two-dimensional form.

Therefore:

```python
df[["color"]]
```

is used instead of:

```python
df["color"]
```

## Difference

```text
df["color"]    → Series → 1D
df[["color"]]  → DataFrame → 2D
```

Scikit-Learn transformers generally expect data in the form:

```text
(number of samples, number of features)
```

---

# 13. Sparse Matrix

After running `fit_transform()`, the result is a **sparse matrix**.

A sparse matrix is useful when there are many zeros compared with the number of ones.

For example:

```text
0 0 1
1 0 0
0 1 0
0 1 0
0 0 1
1 0 0
```

There are many `0`s compared with `1`s.

To convert the sparse matrix into a normal NumPy array:

```python
encoded.toarray()
```

---

# 14. Why Does Red Become `001`?

The encoder orders the categories alphabetically.

The categories are:

```text
blue
green
red
```

Therefore, the columns become:

```text
blue
green
red
```

So:

```text
Blue  = (1, 0, 0)
Green = (0, 1, 0)
Red   = (0, 0, 1)
```

This explains why `red` appears as:

```text
001
```

---

# 15. Getting Feature Names

We can obtain the names of the newly created features using:

```python
encoder.get_feature_names_out()
```

The result will be similar to:

```text
color_blue
color_green
color_red
```

---

# 16. Creating a DataFrame from Encoded Data

The encoded values can be converted into a Pandas DataFrame:

```python
encoded_df = pd.DataFrame(
    encoded.toarray(),
    columns=encoder.get_feature_names_out()
)
```

Now the encoded data contains:

| color_blue | color_green | color_red |
|---:|---:|---:|
| 0 | 0 | 1 |
| 1 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |
| 1 | 0 | 0 |

---

# 17. Concatenating with the Original DataFrame

The encoded features can be combined with the original DataFrame:

```python
df_encoded = pd.concat(
    [df, encoded_df],
    axis=1
)
```

Here:

```text
axis=1
```

means column-wise concatenation.

Once the categorical feature has been successfully encoded, the original categorical column generally isn't required for model training.

---

# 18. Encoding New Data

After fitting the encoder, the same encoder can be used to transform new data.

For example:

```python
encoder.transform([["blue"]])
```

This produces the corresponding encoded representation:

```text
Blue → (1, 0, 0)
```

The important distinction is:

```text
Training data → encoder.fit_transform(...)

New data → encoder.transform(...)
```

We do **not** fit the encoder again on new data.

---

# 19. Disadvantages of One-Hot Encoding

One-Hot Encoding is useful, but it has some important disadvantages.

## Problem 1 — Too Many Categories

Suppose a categorical feature has `100` unique categories.

One-Hot Encoding will create:

```text
100 new features
```

If a feature contains a very large number of categories, One-Hot Encoding may not be the best choice.

---

## Problem 2 — Sparse Matrix

One-Hot Encoding produces a lot of `0`s.

For example, with many categories:

```text
1 0 0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0
...
```

Most values are zeros, creating a sparse representation.

The lecture notes that a large number of categorical features converted into many columns can contribute to overfitting.

---

# 20. When Should You Avoid One-Hot Encoding?

You should be cautious about using One-Hot Encoding when a categorical feature has:

**Very High Cardinality**

Cardinality means the number of unique categories.

For example, a `City` feature with thousands of unique cities could create thousands of columns.

---

# 21. Practical Example — Seaborn Tips Dataset

The Seaborn `tips` dataset contains categorical features such as:

- `sex`
- `smoker`
- `day`
- `time`

Example:

```python
import seaborn as sns

df = sns.load_dataset("tips")
```

The task is to practice One-Hot Encoding on these categorical columns using `OneHotEncoder` and `fit_transform()`.

---

# 22. Complete One-Hot Encoding Workflow

```text
Categorical Feature
        ↓
Identify unique categories
        ↓
Create OneHotEncoder
        ↓
fit_transform()
        ↓
Sparse Matrix
        ↓
toarray()
        ↓
Create DataFrame
        ↓
get_feature_names_out()
        ↓
Numerical Features
```

---

# Quick Revision

## What is Data Encoding?

**Categorical Features → Numerical Features**

## Why?

Because Machine Learning models primarily work with numerical representations.

## What is One-Hot Encoding?

A technique that represents each category as a separate binary feature.

## Example

```text
Red   → (0, 0, 1)
Green → (0, 1, 0)
Blue  → (1, 0, 0)
```

## Key Python Steps

```python
from sklearn.preprocessing import OneHotEncoder

encoder = OneHotEncoder()

encoded = encoder.fit_transform(df[["color"]])

encoded.toarray()

encoder.get_feature_names_out()

encoder.transform(new_data)
```

## Key Disadvantages

### High Cardinality

```text
Many Categories → Many New Features
```

### Sparse Representation

```text
Many 0s + Few 1s → Sparse Matrix
```

---

# Core Concept to Remember

> **One-Hot Encoding converts each categorical value into a binary vector by creating one feature per category.**

For:

```text
Color = {Red, Green, Blue}
```

we get:

```text
Red   → (0, 0, 1)
Green → (0, 1, 0)
Blue  → (1, 0, 0)
```

This allows categorical information to be represented numerically without assigning an artificial numerical ranking to the categories.

---

# 23. Label Encoding & Ordinal Encoding

*Feature Engineering — Encoding Categories With and Without Meaningful Order*

This section covers two categorical data encoding techniques: **Label Encoding** and **Ordinal Encoding**. The key distinction is whether categories have a meaningful order or ranking.

## 23.1. Label Encoding

Label Encoding assigns a unique numerical label to each category. These numbers are identifiers, not meaningful ranks.

| Color | Encoded label |
|---|---:|
| Blue | 0 |
| Green | 1 |
| Red | 2 |

### Label Encoding with Scikit-Learn

```python
import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({"color": ["red", "blue", "green", "red", "blue"]})

label_encoder = LabelEncoder()
df["color_encoded"] = label_encoder.fit_transform(df["color"])
print(df)
```

For this example, `LabelEncoder` assigns labels in alphabetically sorted order: blue → 0, green → 1, red → 2.

### Encoding New Values

Once the encoder is fitted, use the same encoder to transform new values:

```python
print(label_encoder.transform(["red"]))    # [2]
print(label_encoder.transform(["blue"]))   # [0]
print(label_encoder.transform(["green"]))  # [1]
```

**Training data:** `fit_transform(...)`  
**New data:** `transform(...)`

### The Problem with Label Encoding

With blue → 0, green → 1, and red → 2, some models may treat `2 > 1 > 0` as an actual ordering. But color is **nominal**: red, green, and blue have no inherent rank.

**Arbitrary label ≠ meaningful rank.**

For nominal input features such as color, **One-Hot Encoding** is generally more appropriate when arbitrary numerical ordering would mislead the model.

| Color | Blue | Green | Red |
|---|---:|---:|---:|
| Blue | 1 | 0 | 0 |
| Green | 0 | 1 | 0 |
| Red | 0 | 0 | 1 |

> `LabelEncoder` is designed primarily for encoding target labels (`y`). For nominal input features (`X`), consider `OneHotEncoder` instead.

## 23.2. When Does Ranking Make Sense?

Some categorical variables have a meaningful order. For example:

**High School < College < Graduate < Post Graduate**

In this case, an encoding that preserves order makes sense.

## 23.3. Ordinal Encoding

Ordinal Encoding represents categorical variables according to their intrinsic order.

| Size | Encoded value |
|---|---:|
| Small | 0 |
| Medium | 1 |
| Large | 2 |

The ordering **small < medium < large** is meaningful.

### Ordinal Encoding with Scikit-Learn

```python
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

df = pd.DataFrame({"size": ["small", "medium", "large", "medium", "small", "large"]})

encoder = OrdinalEncoder(categories=[["small", "medium", "large"]])
df["size_encoded"] = encoder.fit_transform(df[["size"]]).astype(int)
print(df)
```

### Why Specify the Categories Manually?

```python
categories=[["small", "medium", "large"]]
```

This explicitly tells the encoder the intended order. The output begins at zero, but the **relative order** is preserved: `0 < 1 < 2`.

### Transforming New Data

```python
print(encoder.transform([["small"]]))   # [[0.]]
print(encoder.transform([["medium"]]))  # [[1.]]
print(encoder.transform([["large"]]))   # [[2.]]
```

Fit on training data; transform new observations using the already-fitted encoder.

## 23.4. Label Encoding vs Ordinal Encoding

| Feature | Label Encoding | Ordinal Encoding |
|---|---|---|
| Purpose | Assign a unique label to each category | Represent meaningful category order |
| Example | Red, Green, Blue | Small, Medium, Large |
| Ranking meaningful? | No, not inherently | Yes |
| Example encoding | Blue → 0, Green → 1, Red → 2 | Small → 0, Medium → 1, Large → 2 |
| Main concern | Artificial ranking if used as an input feature | Must specify the correct order |

## 23.5. Decision Rule

```text
Categorical feature
        |
        v
Meaningful order?
    /       \
   No       Yes
   |         |
   v         v
Nominal   Ordinal
   |         |
   v         v
One-Hot   Ordinal
Encoding  Encoding
```

## 23.6. Interview Revision

**What is Label Encoding?** Assigning a unique numerical label to each category.

**What is its major problem with nominal input features?** The numerical labels may introduce an artificial order that does not exist.

**What is Ordinal Encoding?** Encoding categorical values according to their meaningful intrinsic order.

**Nominal example:** Color — red, green, blue.

**Ordinal example:** Size — small, medium, large.

**Which encoding suits nominal categories?** One-Hot Encoding is generally appropriate.

**Which encoding suits ordered categories?** Ordinal Encoding.

### Final Memory Trick

- **Nominal = No order → One-Hot Encoding**
- **Ordinal = Order exists → Ordinal Encoding**
- **Arbitrary label ≠ meaningful rank**

