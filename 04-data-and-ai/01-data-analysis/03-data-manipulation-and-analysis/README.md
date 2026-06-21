# Data Manipulation & Analysis

## Overview

Data Manipulation and Analysis are core Pandas skills used for:

- Data Cleaning
- Data Transformation
- Feature Engineering
- Aggregation
- Exploratory Data Analysis (EDA)

---

## Topics Covered

### Data Inspection

- head()
- tail()
- describe()
- dtypes()

### Missing Values

- isnull()
- isnull().sum()
- fillna()

### Data Transformation

- rename()
- astype()
- apply()

### Aggregation

- groupby()
- mean()
- sum()
- count()
- agg()

### Data Merging

- inner join
- outer join
- left join
- right join

`refer example.ipynb`

---

## Key Concepts

| Concept   | Purpose                      |
| --------- | ---------------------------- |
| isnull()  | Detect missing values        |
| fillna()  | Handle missing data          |
| apply()   | Apply custom transformations |
| groupby() | Aggregate grouped data       |
| agg()     | Multiple aggregations        |
| merge()   | Combine DataFrames           |

---

## Practice Assignment

Using a sales dataset:

1. Load the CSV file.
2. Check for missing values.
3. Fill missing sales values using the mean.
4. Calculate average sales per product.
5. Calculate total sales per region.
6. Rename the Date column to Sales_Date.
7. Merge product information from another DataFrame.

Expected Concepts:

- read_csv()
- fillna()
- groupby()
- agg()
- rename()
- merge()

---

## Real-World Connection

These operations form the foundation of:

- Exploratory Data Analysis (EDA)
- Business Intelligence
- Data Engineering
- Machine Learning Data Preparation

Almost every real-world data project uses these techniques before building models.
