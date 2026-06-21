# Pandas

## Overview

Pandas is one of the most important Python libraries for Data Analysis.

It provides powerful data structures and tools for:

* Data Analysis
* Data Cleaning
* Data Manipulation
* Data Exploration
* Data Preparation for Machine Learning

Pandas is built on top of NumPy and is the standard library used by data analysts, data scientists, and machine learning engineers.

---

## Installation

```bash
pip install pandas(bash/terminal)
!pip install pandas(jupyter notebook)
```

```python
import pandas as pd
```

---

## Topics Covered

### Series

A Series is a one-dimensional labeled array.

Covered:

* Creating Series from Lists
* Creating Series from Dictionaries
* Custom Indexing
* Series Structure

### DataFrames

A DataFrame is a two-dimensional tabular data structure.

Covered:

* Creating DataFrames
* DataFrame Structure
* Reading CSV Files
* Accessing Columns
* Accessing Rows

### Indexing & Selection

Covered:

* loc[]
* iloc[]
* at[]
* iat[]

### DataFrame Operations

Covered:

* Adding Columns
* Updating Columns
* Removing Columns
* Removing Rows

### DataFrame Inspection

Covered:

* head()
* tail()
* shape
* columns
* dtypes
* describe()

---

## Key Concepts

| Concept    | Description                              |
| ---------- | ---------------------------------------- |
| Series     | One-dimensional labeled data             |
| DataFrame  | Two-dimensional tabular data             |
| loc        | Label-based indexing                     |
| iloc       | Position-based indexing                  |
| at         | Fast single-value access using labels    |
| iat        | Fast single-value access using positions |
| describe() | Statistical summary                      |
| shape      | Rows and columns                         |
| dtypes     | Data types of columns                    |

---

## DataFrame vs Series

| Feature    | Series        | DataFrame        |
| ---------- | ------------- | ---------------- |
| Dimensions | 1D            | 2D               |
| Structure  | Single Column | Multiple Columns |
| Creation   | pd.Series()   | pd.DataFrame()   |
| Similar To | NumPy Array   | Excel Sheet      |

---

## Why Pandas Matters

Most real-world data comes in tabular form:

* CSV Files
* Excel Files
* SQL Tables
* API Responses
* Business Reports

Pandas provides a consistent way to load, clean, transform, and analyze this data.

`refer example.ipynb`
---

## Practice Assignment

Create a DataFrame containing:

| Name    | Age | City     |
| ------- | --- | -------- |
| Alice   | 25  | New York |
| Bob     | 30  | Chicago  |
| Charlie | 28  | Dallas   |

Perform the following tasks:

1. Display the first two rows.
2. Display only the Age column.
3. Add a Salary column.
4. Increase all ages by 1.
5. Remove the City column.
6. Display shape and column names.
7. Generate a statistical summary using describe().

Expected Concepts:

* pd.DataFrame()
* head()
* column selection
* adding columns
* updating columns
* drop()
* shape
* columns
* describe()

---

## Real-World Connection

Pandas is used extensively in:

* Data Analysis
* Business Intelligence
* Data Cleaning
* Machine Learning Pipelines
* Financial Analysis
* Reporting Systems

Almost every machine learning workflow begins with data preparation using Pandas.

---

## References

Previous Module:

* NumPy

Next Module:

* Pandas Data Cleaning & Missing Values
