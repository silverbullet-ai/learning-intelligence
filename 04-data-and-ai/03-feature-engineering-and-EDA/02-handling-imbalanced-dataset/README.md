# Handling Imbalanced Dataset

This lecture continues the **Feature Engineering** series and focuses on how to handle **imbalanced datasets** in Machine Learning and Deep Learning.

---

# 1. What is an Imbalanced Dataset?

An **imbalanced dataset** occurs when the classes in a classification problem are not represented equally.

For example:

```text
Total data points = 1000

Class Yes = 900
Class No  = 100
```

So the class distribution is:

```
900 : 100 = 9 : 1
```

This is an **imbalanced dataset** because one class has significantly more observations than the other.

### Majority and Minority Classes

```
Class Yes → 900 → Majority Class
Class No  → 100 → Minority Class
```

- **Majority class** → Class containing the larger number of observations.
- **Minority class** → Class containing the smaller number of observations.

---

# 2. Why is an Imbalanced Dataset a Problem?

When training a Machine Learning model on imbalanced data, the model can become **biased toward the majority class**.

For example:

```
Class Yes → 900
Class No  → 100
```

Since the model sees far more examples from the Yes class, it can become heavily influenced by the majority class.

This can negatively affect the model's ability to correctly predict the minority class.

Therefore, we may need to **balance the dataset** before training the model.

---

# 3. Techniques to Handle Imbalanced Data

The lecture discusses two basic techniques:

1. **Upsampling**
2. **Downsampling**

The basic idea is:

```
                  Imbalanced Dataset
                         │
              ┌──────────┴──────────┐
              │                     │
          Upsampling            Downsampling
              │                     │
       Increase minority      Reduce majority
            class                  class
```

---

# 4. Upsampling

## Definition

**Upsampling** means increasing the number of observations in the **minority class**.

Suppose:

```
Majority → 900
Minority → 100
```

We increase the minority class:

```
100 → 900
```

Final dataset:

```
Majority → 900
Minority → 900
```

Total:

```
900 + 900 = 1800
```

### Key Idea

> **Upsampling increases the minority class.**

---

# 5. Creating an Imbalanced Dataset

The lecture uses NumPy and Pandas to create an example dataset.

```Python
import numpy as np
import pandas as pd
```

A random seed is used so that randomly generated values remain reproducible:

```Python
np.random.seed(42)
```

Suppose:

```Python
n_samples = 1000
class_zero_ratio = 0.9
```

Then:

```
1000 × 0.9 = 900
```

Therefore:

```
Class 0 → 900
Class 1 → 100
```

This gives us an imbalanced dataset.

The class distribution can be checked using:

```Python
df["target"].value_counts()
```

Expected distribution:

```
0    900
1    100
```

---

# 6. Separating Majority and Minority Classes

Before performing upsampling or downsampling, we separate the two classes.

### Minority Class

```Python
df_minority = df[df["target"] == 1]
```

Here, class `1` is the minority class.

### Majority Class

```Python
df_majority = df[df["target"] == 0]
```

Here, class `0` is the majority class.

So:

```
df_minority → target = 1
df_majority → target = 0
```

---

# 7. Upsampling Using `resample`

The lecture uses:

```Python
from sklearn.utils import resample
```

We use `resample()` to increase the number of minority observations.

### Code

```Python
df_minority_upsampled = resample(
    df_minority,
    replace=True,
    n_samples=len(df_majority),
    random_state=42
)
```

### Important Parameters

#### `df_minority`

The dataset we want to upsample.

```Python
df_minority
```

#### `replace=True`

Sampling is performed **with replacement**.

This allows existing minority observations to be selected again.

Therefore, additional observations can be generated from the minority class by repeatedly sampling existing observations.

#### `n_samples`

Specifies how many samples we want after upsampling.

```Python
n_samples=len(df_majority)
```

Since the majority class contains 900 observations:

```
n_samples = 900
```

Therefore, the minority class is increased to 900 observations.

#### `random_state`

Used to make the random sampling reproducible.

---

# 8. Combining the Upsampled Dataset

After upsampling, we combine:

- Original majority dataset
- Upsampled minority dataset

```Python
df_upsampled = pd.concat([
    df_majority,
    df_minority_upsampled
])
```

Now check:

```Python
df_upsampled["target"].value_counts()
```

Result:

```
0    900
1    900
```

Therefore:

```
Upsampled Dataset = 900 : 900
```

The classes are now balanced.

---

# 9. Downsampling

## Definition

**Downsampling** means reducing the number of observations in the **majority class**.

Suppose:

```
Majority → 900
Minority → 100
```

We reduce the majority class:

```
900 → 100
```

Final dataset:

```
Majority → 100
Minority → 100
```

Total:

```
100 + 100 = 200
```

### Key Idea

> **Downsampling reduces the majority class.**

---

# 10. Downsampling Using `resample`

We again use:

```Python
from sklearn.utils import resample
```

But this time we resample the majority class.

```Python
df_majority_downsampled = resample(
    df_majority,
    replace=False,
    n_samples=len(df_minority),
    random_state=42
)
```

### Important Difference

For downsampling:

```Python
replace=False
```

because we want to select fewer observations from the majority class.

We also set:

```Python
n_samples=len(df_minority)
```

Since the minority class contains 100 observations:

```Python
n_samples = 100
```

Therefore:

```
Majority class:
900 → 100
```

---

# 11. Combining the Downsampled Dataset

We combine:

```Python
df_downsampled = pd.concat([
    df_minority,
    df_majority_downsampled
])
```

Then check:

```Python
df_downsampled["target"].value_counts()
```

Result:

```
0    100
1    100
```

Therefore:

```
Downsampled Dataset = 100 : 100
```

The classes are now balanced.

---

# 12. Upsampling vs Downsampling

| FeatureUpsamplingDownsampling |                                   |                     |
| ----------------------------- | --------------------------------- | ------------------- |
| What changes?                 | Minority class                    | Majority class      |
| Direction                     | Increases data                    | Decreases data      |
| Example                       | 100 → 900                        | 900 → 100          |
| Final classes                 | 900 : 900                         | 100 : 100           |
| Main concern                  | Creates additional sampled points | Loses existing data |

---

# 13. Why Downsampling Can Be Bad

The lecture specifically points out that **downsampling can result in loss of data**.

Original dataset:

```
900 + 100 = 1000
```

After downsampling:

```
100 + 100 = 200
```

Therefore:

```
1000 - 200 = 800
```

We lose **800 data points**.

Therefore, potentially useful information from the majority class is discarded.

---

# 14. Why Upsampling Can Be Preferred

With upsampling:

```
900 + 100 = 1000
```

becomes:

```
900 + 900 = 1800
```

The original majority observations are retained while the minority class is increased.

Therefore, the lecture suggests that **upsampling can be used to address class imbalance while avoiding the direct loss of majority-class observations**.

---

# 15. SMOTE

## Synthetic Minority Oversampling Technique

**SMOTE** stands for:

> **Synthetic Minority Oversampling Technique**

SMOTE is an advanced technique for handling **imbalanced datasets**.

It is particularly useful when the minority class has significantly fewer observations than the majority class.

---

# 16. Why Do We Need SMOTE?

Suppose:

```
Majority class → 900
Minority class → 100
```

With basic upsampling, we repeatedly sample existing minority observations.

Conceptually:

```
Original minority:

●    ●
```

After upsampling:

```
```

The problem is that the new observations are essentially **duplicates or repetitions of existing observations**.

The number of observations increases, but the variation in the minority data does not increase significantly.

---

# 17. SMOTE's Main Idea

SMOTE solves this problem by creating **synthetic data points**.

Suppose we have two nearby minority observations:

```
●----------------●
A                B
```

SMOTE identifies nearby minority points and generates new points between them:

```
●----●----●----●----●
A                  B
     ↑    ↑    ↑
     Synthetic Points
```

Instead of simply copying:

```
A → A → A → A
```

SMOTE creates new observations around existing minority observations.

### Key Concept

> **SMOTE increases the number of minority observations while introducing variation through interpolation.**

---

# 18. How SMOTE Works

The basic process is:

1. Identify the minority class.
2. Find nearby minority-class observations.
3. Select neighboring minority points.
4. Interpolate between those points.
5. Generate synthetic minority observations.
6. Continue until the desired class balance is achieved.

Conceptually:

```
Minority Point A
       ●
        \
         ● Synthetic Point
          \
           ● Synthetic Point
            \
             ●
        Minority Point B
```

The important point is that the generated points are **synthetic**, rather than exact copies of existing observations.

---

# 19. SMOTE vs Basic Upsampling

| FeatureBasic UpsamplingSMOTE    |              |                                  |
| ------------------------------- | ------------ | -------------------------------- |
| Minority class increased?       | Yes          | Yes                              |
| Creates synthetic observations? | No           | Yes                              |
| Uses existing observations?     | Repeats them | Uses them to generate new points |
| Increases variation?            | Limited      | Yes                              |
| Main technique                  | Resampling   | Interpolation                    |

### Memory Trick

```
Upsampling
→ Copy/repeat existing minority observations

SMOTE
→ Create new minority observations between existing ones
```

---

# 20. Creating a Dataset for SMOTE

The lecture uses Scikit-learn's `make_classification()` to create a sample classification dataset.

```Python
from sklearn.datasets import make_classification
```

`make_classification()` can generate:

- Binary classification datasets
- Multi-class classification datasets
- Different numbers of samples
- Different numbers of features
- Different class distributions
- Different numbers of clusters

---

# 21. Creating the Dataset

The lecture creates:

- 1000 samples
- 2 features
- 1 cluster per class
- 90% : 10% class distribution

Conceptually:

```
Total samples = 1000

Class 0 → 900
Class 1 → 100
```

A representative setup is:

```Python
X, y = make_classification(
    n_samples=1000,
    n_features=2,
    n_clusters_per_class=1,
    weights=[0.90, 0.10],
    random_state=12,
    n_redundant=0
)
```

### Important Parameters

#### `n_samples`

Number of observations:

```Python
n_samples=1000
```

#### `n_features`

Number of input features:

```Python
n_features=2
```

Two features make it easier to visualize the dataset in a 2D scatter plot.

#### `n_clusters_per_class`

Number of clusters for each class:

```
n_clusters_per_class=1
```

#### `weights`

Controls class distribution:

```
weights=[0.90, 0.10]
```

Approximately:

```
90% → Class 0
10% → Class 1
```

#### `random_state`

Controls reproducibility:

```Python
random_state=12
```

#### `n_redundant`

The lecture sets:

```Python
n_redundant=0
```

because redundant features are not required for this example.

---

# 22. Creating a DataFrame

The lecture separates the input and target variables.

```Python
df1 = pd.DataFrame(
    X,
    columns=["f1", "f2"]
)
```

```Python
df2 = pd.DataFrame(
    y,
    columns=["target"]
)
```

Then combines them:

```Python
final_df = pd.concat(
    [df1, df2],
    axis=1
)
```

The resulting structure is:

| f1f2target |     |   |
| ---------- | --- | - |
| ...        | ... | 0 |
| ...        | ... | 0 |
| ...        | ... | 1 |

Here:

```
f1, f2 → independent/input features
target → dependent/output feature
```

---

# 23. Checking Class Imbalance

We can check the number of observations in each class using:

```Python
final_df["target"].value_counts()
```

The lecture obtains approximately:

```
0    900
1    100
```

Therefore:

```
900 : 100
```

The dataset is clearly imbalanced.

---

# 24. Visualizing the Imbalanced Dataset

The lecture uses Matplotlib:

```Python
import matplotlib.pyplot as plt
```

A scatter plot can be created using the two features:

```Python
plt.scatter(
    final_df["f1"],
    final_df["f2"],
    c=final_df["target"]
)
```

This allows us to visually identify:

- Majority-class observations
- Minority-class observations
- Their distribution in feature space

The minority class contains only around 100 observations, while the majority class contains around 900.

---

# 25. Installing imbalanced-learn

SMOTE is provided through the **imbalanced-learn** library.

If it is not installed:

```
pip install imblearn
```

---

# 26. Importing SMOTE

Import the `SMOTE` class:

```Python
from imblearn.over_sampling import SMOTE
```

The class name is written in uppercase because `SMOTE` is a class.

---

# 27. Applying SMOTE

First create the SMOTE object:

```Python
oversample = SMOTE()
```

Then resample the data:

```Python
X_resampled, y_resampled = oversample.fit_resample(
    X,
    y
)
```

### What does `fit_resample()` do?

It takes:

```
X → independent features
y → target
```

and generates synthetic minority observations.

The output is:

```
X_resampled
y_resampled
```

---

# 28. Before and After SMOTE

### Before SMOTE

```
Class 0 → 900
Class 1 → 100

Total → 1000
```

### After SMOTE

```
Class 0 → 900
Class 1 → 900

Total → 1800
```

Therefore, SMOTE increases the minority class:

```
100 → 900
```

while keeping the original majority observations.

---

# 29. Checking the New Distribution

We can verify the result:

```Python
y_resampled[y_resampled == 0]
```

Count:

```Python
len(y_resampled[y_resampled == 0])
```

Similarly:

```Python
y_resampled[y_resampled == 1]
```

Count:

```Python
len(y_resampled[y_resampled == 1])
```

Expected result:

```
Class 0 → 900
Class 1 → 900
```

So the classes are now balanced.

---

# 30. Visualizing the SMOTE Dataset

After SMOTE, the new observations can be plotted again.

The important visual difference is that the minority observations are no longer simply repeated in exactly the same locations.

Instead, new points appear **between nearby minority observations**.

Conceptually:

### Before

```
×       ×
  ×
```

### After SMOTE

```
×   ×   ×   ×
  ×   ×   ×
×   ×   ×   ×
```

The minority class now occupies a broader region of the feature space.

---

# 31. Why SMOTE is Different From Simple Upsampling

### Simple Upsampling

Suppose we have:

```
A ●
B ●
```

Simple upsampling may produce:

```
A ●  A ●  A ●
B ●  B ●
```

We are mostly repeating the same observations.

### SMOTE

SMOTE instead creates observations between nearby points:

```
A ● -- ● -- ● -- ● B
       ↑    ↑
    synthetic
```

Thus, SMOTE introduces **new synthetic observations and variation**.

---

# 32. Complete Imbalanced Dataset Workflow

```
Original Dataset
       │
       ↓
Check Class Distribution
       │
       ↓
Identify Majority & Minority Classes
       │
       ├───────────────────┐
       │                   │
       ↓                   ↓
  Upsampling          Downsampling
       │                   │
       ↓                   ↓
Increase              Reduce
Minority              Majority
       │                   │
       └─────────┬─────────┘
                 │
                 ↓
          Balanced Dataset
```

For SMOTE:

```
Original Dataset
       │
       ↓
Check Class Distribution
       │
       ↓
Identify Minority Class
       │
       ↓
Apply SMOTE()
       │
       ↓
Find Nearby Minority Points
       │
       ↓
Interpolate Between Them
       │
       ↓
Generate Synthetic Observations
       │
       ↓
Balanced Dataset
       │
       ↓
Train ML Classification Model
```

---

# 33. Upsampling vs Downsampling vs SMOTE

| TechniqueWhat It DoesMain Effect |                                           |                                      |
| -------------------------------- | ----------------------------------------- | ------------------------------------ |
| Upsampling                       | Increases minority observations           | Adds sampled minority observations   |
| Downsampling                     | Reduces majority observations             | Removes majority observations        |
| SMOTE                            | Generates synthetic minority observations | Adds synthetic minority observations |

### Example

Starting distribution:

```
Class 0 → 900
Class 1 → 100
```

After basic upsampling:

```
Class 0 → 900
Class 1 → 900
```

After downsampling:

```
Class 0 → 100
Class 1 → 100
```

After SMOTE:

```
Class 0 → 900
Class 1 → 900
```

---

# 34. Important Takeaways

### 1. Imbalanced Dataset

A dataset where classes are not equally represented.

### 2. Majority Class

The class containing more observations.

### 3. Minority Class

The class containing fewer observations.

### 4. Upsampling

Increases the number of observations in the minority class.

### 5. Downsampling

Reduces the number of observations in the majority class.

### 6. SMOTE

**Synthetic Minority Oversampling Technique**

Generates synthetic minority observations through interpolation.

### 7. Main Difference

```
Upsampling
→ Repeatedly samples existing minority observations

SMOTE
→ Generates synthetic minority observations
```

### 8. Important Library

```Python
imbalanced-learn
```

### 9. Important Import

```Python
from imblearn.over_sampling import SMOTE
```

### 10. Important Method

```Python
fit_resample(X, y)
```

---

# 35. Interview Revision

### What is an imbalanced dataset?

A dataset where the classes in a classification problem are not equally represented.

### What is the majority class?

The class containing the larger number of observations.

### What is the minority class?

The class containing the smaller number of observations.

### What is upsampling?

Increasing the number of observations in the minority class.

### What is downsampling?

Reducing the number of observations in the majority class.

### Which technique uses `replace=True` in the lecture?

**Upsampling**

```Python
replace=True
```

### Which technique uses `replace=False`?

**Downsampling**

```Python
replace=False
```

### What library/function is used for basic resampling?

```Python
from sklearn.utils import resample
```

### Why can downsampling be problematic?

Because it throws away observations from the majority class, resulting in information loss.

### What is SMOTE?

SMOTE is an oversampling technique that handles imbalanced datasets by generating synthetic minority-class observations through interpolation between existing minority observations.

### Why is SMOTE different from simple upsampling?

Simple upsampling mainly repeats existing minority observations, whereas SMOTE generates synthetic observations and introduces variation.

### Does SMOTE increase the majority class?

**No.**

SMOTE generates additional observations for the **minority class**.

### What problem does SMOTE solve?

Class imbalance in classification problems.

### Which Python library provides SMOTE?

```
imblearn
```

### What does `fit_resample()` do?

It fits the resampling technique to the data and returns the resampled features and target.

---

# One-Line Memory Tricks

```
UP   → Increase the minority
DOWN → Decrease the majority
```

```
SMOTE
→ Find nearby minority points
→ Interpolate between them
→ Create synthetic minority points
→ Balance the dataset
```
