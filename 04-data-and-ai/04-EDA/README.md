# Exploratory Data Analysis (EDA)

**Understanding, Cleaning, Analyzing, and Visualizing Data Before Modeling**

Exploratory Data Analysis (EDA) is the process of understanding a dataset before moving toward Machine Learning modeling.

The main goal of EDA is to understand:

- Dataset structure
- Features / columns
- Data types
- Missing values
- Duplicate records
- Descriptive statistics
- Unique values
- Relationships / correlation between features
- Distribution of features
- Outliers
- Target / class distribution
- Patterns and unusual observations
- Data through visualizations

> **Core idea:** Before building a Machine Learning model, understand the data first.

---

# 1. What is EDA?

EDA is the systematic process of exploring a dataset to understand what the data contains and how its different variables behave.

A basic EDA process can be thought of as:

```text
Understand
    ↓
Inspect
    ↓
Clean
    ↓
Analyze
    ↓
Visualize
    ↓
Prepare for Modeling
```

EDA helps answer questions such as:

```text
What data do I have?
        ↓
How is the dataset structured?
        ↓
Are there missing or duplicate records?
        ↓
What do the features look like?
        ↓
How are the features related?
        ↓
Is the target balanced?
        ↓
Are there outliers or unusual patterns?
```

---

# 2. Dataset Structure

The first step is to understand the basic structure of the dataset.

## `head()`

Displays the first few rows:

```python
df.head()
```

You can also inspect the last few rows:

```python
df.tail()
```

---

# 3. Dataset Information — `info()`

```python
df.info()
```

`df.info()` provides a concise summary of the DataFrame.

It tells us:

- Number of entries
- Column names
- Number of non-null values
- Data types
- Memory information

It helps determine:

- Whether missing values exist
- Whether features are numerical or categorical
- Whether the dataset has the expected number of records
- Whether data types are appropriate

---

# 4. Dataset Shape

To find the number of rows and columns:

```python
df.shape
```

The result has the form:

```text
(rows, columns)
```

For example:

```text
(1000, 10)
```

means:

- 1000 rows
- 10 columns

---

# 5. Column Names

To list all columns:

```python
df.columns
```

This helps identify the available:

- Features
- Target variable
- Categorical columns
- Numerical columns

---

# 6. Data Types

To inspect data types:

```python
df.dtypes
```

Common Pandas data types include:

```text
int64
float64
object
bool
```

Understanding data types is important because different types of data require different analysis and preprocessing techniques.

---

# 7. Descriptive Statistics

Use:

```python
df.describe()
```

This generates descriptive statistics for numerical columns.

| Statistic | Meaning |
|---|---|
| `count` | Number of non-null observations |
| `mean` | Average |
| `std` | Standard deviation |
| `min` | Minimum |
| `25%` | First quartile / Q1 |
| `50%` | Median / Q2 |
| `75%` | Third quartile / Q3 |
| `max` | Maximum |

These statistics help us understand:

- Central tendency
- Spread
- Range
- Potentially unusual values

---

# 8. Unique Values

To find unique values:

```python
df["column"].unique()
```

To count the number of unique values:

```python
df["column"].nunique()
```

This is especially useful for categorical features.

---

# 9. Value Counts

To count how frequently each value occurs:

```python
df["column"].value_counts()
```

This is particularly useful for:

- Categorical variables
- Target variables
- Class distributions

---

# 10. Checking Missing Values

To check missing values:

```python
df.isnull().sum()
```

Another equivalent approach:

```python
df.isna().sum()
```

The result shows how many missing values exist in each column.

Missing values can affect:

- Statistical analysis
- Visualizations
- Machine Learning models

Possible handling techniques include:

- Mean imputation
- Median imputation
- Mode imputation
- Other feature-specific strategies

---

# 11. Checking Duplicate Records

To identify duplicate rows:

```python
df.duplicated()
```

This returns:

- `True` → duplicate record
- `False` → non-duplicate record

To count duplicates:

```python
df.duplicated().sum()
```

To view duplicate records:

```python
df[df.duplicated()]
```

---

# 12. Removing Duplicate Records

Duplicates can be removed using:

```python
df.drop_duplicates()
```

To modify the existing DataFrame:

```python
df.drop_duplicates(inplace=True)
```

`inplace=True` modifies the existing DataFrame instead of returning a separate modified DataFrame.

---

# 13. Numerical vs Categorical Features

During EDA, identify the type of each feature.

## Numerical Features

Contain numerical measurements or values.

Examples:

```text
Age
Salary
Height
Weight
Temperature
```

## Categorical Features

Contain categories or labels.

Examples:

```text
Gender
City
Color
Department
Education Level
```

This distinction is important because numerical and categorical features are analyzed differently.

---

# 14. Correlation

Correlation helps us understand the relationship between numerical features.

```python
df.corr()
```

A correlation value generally ranges from:

```text
-1 to +1
```

Conceptually:

```text
+1 → Strong positive relationship
 0 → Little / no linear relationship
-1 → Strong negative relationship
```

Correlation can help identify relationships between numerical variables.

---

# 15. Correlation Heatmap

A correlation matrix can be visualized using Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True)
plt.show()
```

`annot=True` displays the numerical correlation values inside the heatmap.

---

# 16. Distribution of Features

Understanding the distribution of a feature is an important part of EDA.

A histogram can be used:

```python
sns.histplot(df["column"])
plt.show()
```

To add a Kernel Density Estimate:

```python
sns.histplot(df["column"], kde=True)
plt.show()
```

`kde=True` adds a KDE curve that helps visualize the approximate probability density of the feature.

Distribution analysis can reveal:

- Shape
- Spread
- Concentration
- Skewness
- Possible unusual values

---

# 17. Distribution of Multiple Features

We can inspect multiple columns using a loop:

```python
for column in df.columns:
    sns.histplot(df[column], kde=True)
    plt.show()
```

This provides a quick visual overview of feature distributions.

---

# 18. Class Distribution

For a categorical target or class variable:

```python
df["target"].value_counts()
```

This shows how many observations belong to each class.

If some classes contain significantly more observations than others, the dataset may be **imbalanced**.

Example:

```text
Class A → 900
Class B → 100
```

Class imbalance can become important when building Machine Learning models.

---

# 19. Bar Plot

A bar plot can visualize categorical or class distributions:

```python
df["target"].value_counts().plot(kind="bar")

plt.xlabel("Target")
plt.ylabel("Count")
plt.show()
```

This makes differences in category frequency easier to see.

---

# 20. Pair Plot

Seaborn provides:

```python
sns.pairplot(df)
```

A pair plot compares multiple features against each other.

It can help with:

### Univariate Analysis

Understanding one feature.

### Bivariate Analysis

Understanding the relationship between two features.

### Multivariate Analysis

Looking at relationships involving multiple features.

---

# 21. Box Plot

A box plot can be used to understand the distribution of a numerical feature and identify potential outliers.

```python
sns.boxplot(x=df["column"])
plt.show()
```

A box plot helps visualize:

- Median
- Quartiles
- IQR
- Whiskers
- Potential outliers

The detailed mathematics behind box plots and IQR-based outlier detection is covered separately under Feature Engineering.

---

# 22. Categorical Box Plot

A numerical feature can also be compared across categories:

```python
sns.catplot(
    x="category",
    y="numerical_feature",
    data=df,
    kind="box"
)
```

This helps compare the distribution of a numerical variable across different categories.

---

# 23. Scatter Plot

For relationships between two numerical features:

```python
sns.scatterplot(
    x="feature_1",
    y="feature_2",
    data=df
)
plt.show()
```

A third variable can be represented using `hue`:

```python
sns.scatterplot(
    x="feature_1",
    y="feature_2",
    hue="target",
    data=df
)
```

This allows us to visually examine relationships while considering another variable.

---

# 24. Univariate, Bivariate, and Multivariate Analysis

## Univariate Analysis

Analysis of one variable.

Examples:

```python
df["age"].describe()
sns.histplot(df["age"])
```

Goal:

```text
Understand one feature
```

## Bivariate Analysis

Analysis of two variables.

Example:

```python
sns.scatterplot(
    x="age",
    y="salary",
    data=df
)
```

Goal:

```text
Understand the relationship between two variables
```

## Multivariate Analysis

Analysis involving multiple variables.

Examples:

```python
sns.pairplot(df)
```

or:

```python
sns.scatterplot(
    x="age",
    y="salary",
    hue="department",
    data=df
)
```

Goal:

```text
Understand relationships involving multiple variables
```

---

# 25. EDA and Outliers

EDA can help identify unusual observations.

Useful tools include:

- `describe()`
- Box plots
- Histograms
- Scatter plots

Potential outliers should be investigated rather than automatically removed.

---

# 26. General EDA Workflow

```text
                         EDA
                          │
             ┌────────────┴────────────┐
             │                         │
      Understand Data            Visualize Data
             │                         │
             ├── head()                ├── Heatmap
             ├── info()                ├── Histogram
             ├── describe()            ├── Pair Plot
             ├── shape                 ├── Bar Plot
             ├── columns               ├── Box Plot
             ├── dtypes                └── Scatter Plot
             └── unique()
             │
             ├── Missing Values
             ├── Duplicate Values
             ├── Correlation
             ├── Feature Distribution
             └── Class Distribution
```

---

# 27. Important EDA Checklist

When receiving a new dataset:

## Step 1 — Understand the Dataset

```python
df.head()
df.shape
df.columns
df.dtypes
df.info()
```

## Step 2 — Understand the Statistics

```python
df.describe()
```

## Step 3 — Check Data Quality

```python
df.isnull().sum()
df.duplicated().sum()
```

## Step 4 — Understand Categories

```python
df["column"].unique()
df["column"].nunique()
df["column"].value_counts()
```

## Step 5 — Analyze Relationships

```python
df.corr()
```

## Step 6 — Visualize

Use:

- Histogram
- Bar plot
- Box plot
- Scatter plot
- Pair plot
- Correlation heatmap
- Categorical plots

## Step 7 — Identify Important Patterns

Look for:

- Missing values
- Duplicates
- Outliers
- Skewed distributions
- Strong correlations
- Class imbalance
- Unusual observations

---

# 28. Most Important Commands

```python
# First look
df.head()

# Dataset information
df.info()

# Statistical summary
df.describe()

# Shape
df.shape

# Column names
df.columns

# Data types
df.dtypes

# Unique values
df["column"].unique()

# Number of unique values
df["column"].nunique()

# Value distribution
df["column"].value_counts()

# Missing values
df.isnull().sum()

# Duplicate records
df.duplicated()

# Number of duplicates
df.duplicated().sum()

# View duplicates
df[df.duplicated()]

# Remove duplicates
df.drop_duplicates(inplace=True)

# Correlation
df.corr()
```

---

# 29. Common Visualization Commands

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Histogram
sns.histplot(df["column"], kde=True)
plt.show()

# Bar plot
df["column"].value_counts().plot(kind="bar")
plt.show()

# Box plot
sns.boxplot(x=df["column"])
plt.show()

# Pair plot
sns.pairplot(df)

# Correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True)
plt.show()

# Scatter plot
sns.scatterplot(
    x="feature_1",
    y="feature_2",
    data=df
)
plt.show()

# Scatter plot with category
sns.scatterplot(
    x="feature_1",
    y="feature_2",
    hue="target",
    data=df
)
plt.show()
```

---

# 30. EDA vs Feature Engineering

EDA and Feature Engineering are related, but they have different purposes.

## EDA

Focuses on:

```text
Understanding the Data
```

Examples:

- Find missing values
- Find duplicates
- Understand distributions
- Analyze correlations
- Identify outliers
- Understand class distribution
- Visualize relationships

## Feature Engineering

Focuses on:

```text
Transforming / Creating Features
```

Examples:

- Handling missing values
- Encoding categorical features
- Handling imbalanced datasets
- Creating new features
- Transforming existing features

EDA often helps us decide **which Feature Engineering techniques may be necessary**.

---

# Core Takeaway

> **EDA = Understand → Clean → Analyze → Visualize**

Before building a Machine Learning model, understand:

```text
What data do I have?
        ↓
How is it structured?
        ↓
Is the data clean?
        ↓
What do the features look like?
        ↓
How are the variables related?
        ↓
Is the target balanced?
        ↓
Are there outliers or unusual patterns?
        ↓
What transformations may be required?
```

**EDA is not just about making plots.**

It is about developing an understanding of the dataset before making modeling decisions.
