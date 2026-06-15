# Seaborn

## Overview

Seaborn is a high-level Python data visualization library built on top of Matplotlib.

It provides:

- Attractive default themes
- Statistical visualizations
- Simpler syntax than Matplotlib
- Better integration with Pandas DataFrames

Seaborn is widely used in:

- Data Analysis
- Exploratory Data Analysis (EDA)
- Machine Learning
- Statistical Visualization

The standard import convention is:

```python
import seaborn as sns
```

---

## Installation

```bash
pip install seaborn
```

---

## Topics Covered

### Dataset Loading

- `sns.load_dataset()`

### Relationship Plots

- Scatter Plot
- Line Plot

### Categorical Plots

- Bar Plot
- Box Plot
- Violin Plot

### Distribution Plots

- Histogram
- KDE Plot

### Exploratory Data Analysis

- Pair Plot
- Correlation Matrix
- Heatmap

---

## Built-in Dataset

This module uses Seaborn's popular `tips` dataset.

Example:

```python
import seaborn as sns

tips = sns.load_dataset("tips")

print(tips.head())
```

Common Columns:

| Column     | Description           |
| ---------- | --------------------- |
| total_bill | Total restaurant bill |
| tip        | Tip amount            |
| sex        | Customer gender       |
| smoker     | Smoker or non-smoker  |
| day        | Day of visit          |
| time       | Lunch or dinner       |
| size       | Number of people      |

---

## Key Visualizations

### Scatter Plot

Used to visualize relationships between numerical variables.

```python
sns.scatterplot(
    x="total_bill",
    y="tip",
    data=tips
)
```

---

### Line Plot

Used to identify trends.

```python
sns.lineplot(
    x="size",
    y="total_bill",
    data=tips
)
```

---

### Bar Plot

Used for category comparison.

```python
sns.barplot(
    x="day",
    y="total_bill",
    data=tips
)
```

---

### Box Plot

Useful for:

- Outlier Detection
- Distribution Analysis
- Quartile Visualization

```python
sns.boxplot(
    x="day",
    y="total_bill",
    data=tips
)
```

---

### Violin Plot

Combines:

- Box Plot
- Distribution Plot

```python
sns.violinplot(
    x="day",
    y="total_bill",
    data=tips
)
```

---

### Histogram

Visualizes data distribution.

```python
sns.histplot(
    tips["total_bill"],
    bins=10
)
```

---

### KDE Plot

Displays a smooth probability density curve.

```python
sns.kdeplot(
    tips["total_bill"],
    fill=True
)
```

---

### Pair Plot

One of Seaborn's most powerful EDA tools.

```python
sns.pairplot(tips)
```

Used to quickly explore relationships between numerical features.

---

### Heatmap

Used to visualize correlation matrices.

```python
corr = tips[
    ["total_bill", "tip", "size"]
].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)
```

---

## Seaborn vs Matplotlib

| Feature                    | Matplotlib | Seaborn    |
| -------------------------- | ---------- | ---------- |
| Ease of Use                | Moderate   | Easy       |
| Default Styling            | Basic      | Attractive |
| Statistical Visualizations | Limited    | Excellent  |
| Pandas Integration         | Good       | Excellent  |
| Code Length                | More       | Less       |

---

## Common Functions

| Function          | Purpose             |
| ----------------- | ------------------- |
| sns.scatterplot() | Scatter Plot        |
| sns.lineplot()    | Line Plot           |
| sns.barplot()     | Bar Plot            |
| sns.boxplot()     | Box Plot            |
| sns.violinplot()  | Violin Plot         |
| sns.histplot()    | Histogram           |
| sns.kdeplot()     | KDE Plot            |
| sns.pairplot()    | Pair Plot           |
| sns.heatmap()     | Correlation Heatmap |

---

## Real-World Applications

Seaborn is heavily used for:

- Exploratory Data Analysis (EDA)
- Machine Learning Projects
- Statistical Analysis
- Business Intelligence
- Feature Relationship Analysis
- Correlation Analysis

It is often one of the first libraries used when exploring a new dataset.

---

## Practice Assignment (Solved)

### Problem

Using Seaborn's tips dataset, create a heatmap showing the correlation between:

- total_bill
- tip
- size

### Solution

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")

corr = tips[
    ["total_bill", "tip", "size"]
].corr()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Tips Dataset Correlation Matrix")

plt.show()
```

### Expected Outcome

A heatmap showing:

- Strong positive correlation between total_bill and tip
- Correlation values displayed inside cells
- Color intensity representing correlation strength

---

## Key Takeaways

- Seaborn is built on top of Matplotlib.
- It provides cleaner syntax and better default styling.
- It integrates naturally with Pandas DataFrames.
- Pair Plots and Heatmaps are essential EDA tools.
- Seaborn is one of the most widely used visualization libraries in Data Science and Machine Learning.
