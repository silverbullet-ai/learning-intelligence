# Data Ingestion & I/O with Pandas

## Overview

Pandas provides powerful tools for reading and writing data from various sources.

This module covers:

- CSV Files
- JSON Files
- Excel Files
- HTML Tables
- Pickle Files
- Data Export Operations

These capabilities make Pandas the central library for data ingestion and preprocessing in Data Analysis, Machine Learning, and AI workflows.

---

## Topics Covered

### CSV Operations

- `pd.read_csv()`
- `df.to_csv()`

### JSON Operations

- `pd.read_json()`
- `df.to_json()`
- JSON Orientations
  - `index`
  - `records`

### Excel Operations

- `pd.read_excel()`
- Reading specific worksheets

### HTML Tables

- `pd.read_html()`
- Extracting tables from web pages

### Pickle Operations

- `df.to_pickle()`
- `pd.read_pickle()`

### Other Data Sources

- `pd.read_sql()`
- `pd.read_sql_query()`
- `pd.read_xml()`
- `pd.read_table()`

---

## Key Concepts

| Concept       | Purpose                   |
| ------------- | ------------------------- |
| read_csv()    | Read CSV files            |
| read_json()   | Read JSON data            |
| read_excel()  | Read Excel files          |
| read_html()   | Extract HTML tables       |
| to_csv()      | Export DataFrame to CSV   |
| to_json()     | Export DataFrame to JSON  |
| to_pickle()   | Serialize DataFrame       |
| read_pickle() | Load serialized DataFrame |

---

## Common Dependencies

### Excel Support

```bash
pip install openpyxl
```

### HTML Parsing

```bash
pip install lxml
pip install html5lib
pip install beautifulsoup4
```

---

## Common Errors

### Missing openpyxl

```text
ImportError: Missing optional dependency 'openpyxl'
```

Install:

```bash
pip install openpyxl
```

### Missing lxml

```text
ImportError: lxml not found
```

Install:

```bash
pip install lxml
```

---

## Typical Workflow

```python
import pandas as pd

df = pd.read_csv("data.csv")

print(df.head())

df.to_csv("output.csv", index=False)
```

---

## Real-World Applications

These operations are heavily used in:

- Data Analysis
- ETL Pipelines
- Machine Learning
- Deep Learning
- Business Intelligence
- Data Engineering

Almost every data project begins with reading data from one of these sources.

---

## Practice Assignment (Solved)

### Problem

Create a DataFrame containing employee information, save it as a CSV file, and then load it back into Pandas.

### Solution

```python
import pandas as pd

employees = {
    "Name": ["Aahish", "Manav", "Raj"],
    "Salary": [50000, 60000, 55000]
}

df = pd.DataFrame(employees)

df.to_csv("employees.csv", index=False)

loaded_df = pd.read_csv("employees.csv")

print(loaded_df)
```

### Expected Output

```text
     Name  Salary
0  Aahish   50000
1   Manav   60000
2     Raj   55000
```

---

## Key Takeaways

- Pandas can read data from multiple sources.
- CSV is the most commonly used format.
- JSON is widely used in APIs.
- Excel is common in business environments.
- HTML tables can be extracted directly from websites.
- Pickle is frequently used for storing Python objects and ML artifacts.
- Data ingestion is the first step of every data analysis workflow.
