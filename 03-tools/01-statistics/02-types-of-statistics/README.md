# Types of Statistics

## Overview

Statistics is broadly classified into two major branches:

1. Descriptive Statistics
2. Inferential Statistics

These two branches form the foundation of statistical analysis and are widely used in Data Science, Machine Learning, Artificial Intelligence, Business Analytics, Healthcare, Finance, and Scientific Research.

Understanding the difference between descriptive and inferential statistics is one of the most common interview topics for aspiring data professionals.

---

# What are the Types of Statistics?

Statistics is divided into two major categories:

- Descriptive Statistics
- Inferential Statistics

Each serves a different purpose.

- **Descriptive Statistics** focuses on summarizing and describing existing data.
- **Inferential Statistics** focuses on drawing conclusions or making predictions about a larger population using sample data.

---

# 1. Descriptive Statistics

## Definition

Descriptive Statistics is the branch of statistics that deals with:

- Organizing data
- Summarizing data
- Presenting data

Its purpose is to describe the important characteristics of a dataset without making predictions beyond the available data.

---

## Purpose

Descriptive Statistics helps answer questions such as:

- What does the dataset look like?
- What is the average value?
- How spread out is the data?
- Are there any unusual observations?

It provides a clear summary of the available data.

---

# Techniques Used in Descriptive Statistics

Descriptive Statistics mainly consists of two types of measures.

## A. Measures of Central Tendency

Measures of Central Tendency identify the central or typical value of a dataset.

### Mean

The arithmetic average of all observations.

**Formula**

```text
Mean = Sum of Observations / Number of Observations
```

---

### Median

The middle value after arranging the data in ascending or descending order.

---

### Mode

The value that appears most frequently in the dataset.

---

## B. Measures of Dispersion

Measures of Dispersion describe how spread out the data is around its center.

### Variance

Variance measures how far each observation is from the mean.

A larger variance indicates greater variability within the dataset.

---

### Standard Deviation

Standard Deviation is the square root of the variance.

It measures the average amount by which observations differ from the mean.

A smaller standard deviation indicates that data points are closer to the average value.

---

# Example

Consider the following student heights:

```text
180 cm
170 cm
162 cm
150 cm
160 cm
```

Using descriptive statistics, we can calculate:

- Mean Height
- Median Height
- Mode Height
- Variance
- Standard Deviation

These values summarize the characteristics of the dataset.

---

# 2. Inferential Statistics

## Definition

Inferential Statistics is the branch of statistics that uses a sample of data to draw conclusions or make predictions about an entire population.

Instead of analyzing every member of a population, we analyze a smaller representative sample.

---

## Purpose

Inferential Statistics is used to:

- Make predictions
- Draw conclusions
- Test hypotheses
- Generalize findings

It helps us make informed decisions about populations using sample data.

---

# Process of Inferential Statistics

```text
Population

      ↓

Take Sample

      ↓

Perform Statistical Analysis

      ↓

Draw Conclusions

      ↓

Make Decisions About Population
```

---

# Common Techniques in Inferential Statistics

## Hypothesis Testing

Hypothesis testing is used to determine whether assumptions about a population are statistically valid.

Common hypothesis tests include:

- Z-Test
- T-Test
- Chi-Square Test
- ANOVA

---

## Confidence Intervals

Confidence intervals estimate a population parameter using sample data.

They provide a range within which the true population value is likely to lie.

---

## Regression Analysis

Regression Analysis is used to predict future values based on relationships between variables.

It is widely used in Machine Learning and Data Analytics.

---

# Example

Suppose a college has:

```text
Total Students = 1000
```

Measuring the height of every student would require significant time and effort.

Instead, we randomly select five students.

```text
180 cm
170 cm
162 cm
150 cm
160 cm
```

---

## Descriptive Statistics Perspective

Here, we only summarize the selected sample.

For example, we calculate:

- Mean Height
- Median Height
- Variance
- Standard Deviation

We do **not** make conclusions about the remaining students.

---

## Inferential Statistics Perspective

Now we ask:

> Can this sample help estimate the average height of all 1000 students?

This is Inferential Statistics.

We use sample information to make conclusions about the entire population.

---

# Population vs Sample

## Population

A population is the complete group being studied.

### Example

All **1000 students** in a college.

Population Size is represented by:

```text
N
```

---

## Sample

A sample is a smaller subset selected from the population.

### Example

Five randomly selected students.

Sample Size is represented by:

```text
n
```

---

# Relationship Between Population and Sample

```text
Population

      ↓

Select Sample

      ↓

Analyze Sample

      ↓

Draw Conclusions

      ↓

Infer About Population
```

---

# Descriptive Statistics vs Inferential Statistics

| Feature | Descriptive Statistics | Inferential Statistics |
|----------|-----------------------|------------------------|
| Purpose | Summarize data | Draw conclusions |
| Data Used | Existing dataset | Sample dataset |
| Focus | Description | Prediction & Inference |
| Output | Mean, Median, Mode, Variance, Standard Deviation | Population estimates, Hypothesis Tests |
| Example | Average height of sampled students | Estimate average height of all students |

---

# Real-World Applications

## Descriptive Statistics

Used in:

- Data Analysis
- Business Reports
- Dashboards
- Sales Analysis
- Customer Analytics
- Survey Summaries

---

## Inferential Statistics

Used in:

- Clinical Trials
- Election Polls
- Machine Learning
- Scientific Research
- Market Research
- Financial Forecasting

---

# Why This Matters in Data Science

Both branches of statistics are essential in modern data-driven fields.

**Descriptive Statistics** helps us understand and summarize data before analysis.

**Inferential Statistics** helps us build predictive models and make decisions based on limited data.

Almost every Machine Learning workflow begins with descriptive statistics and later applies inferential statistical concepts during model evaluation and experimentation.

---

# Interview Questions

### What are the two major types of Statistics?

Statistics is divided into:

- Descriptive Statistics
- Inferential Statistics

---

### What is Descriptive Statistics?

Descriptive Statistics is used to organize, summarize, and present existing data.

---

### What is Inferential Statistics?

Inferential Statistics uses sample data to draw conclusions or make predictions about a larger population.

---

### What is the difference between Population and Sample?

A population is the complete group under study, whereas a sample is a smaller subset selected from that population.

---

### Name some measures of Central Tendency.

- Mean
- Median
- Mode

---

### Name some measures of Dispersion.

- Variance
- Standard Deviation

---

### Name some hypothesis tests.

- Z-Test
- T-Test
- Chi-Square Test
- ANOVA

---

# Key Takeaways

- Statistics is broadly divided into Descriptive Statistics and Inferential Statistics.
- Descriptive Statistics summarizes and describes existing data.
- Inferential Statistics draws conclusions about a population using sample data.
- Measures of Central Tendency identify the center of the data.
- Measures of Dispersion measure the spread of data.
- Population represents the complete dataset, while a sample is a subset of the population.
- Both branches of statistics are fundamental to Data Science, Machine Learning, Artificial Intelligence, and Business Analytics.

---

# What's Next?

In the next chapter, we'll explore the **Measures of Central Tendency** in detail, including:

- Mean
- Median
- Mode

We'll learn how to calculate them, interpret their meaning, and understand when to use each measure.