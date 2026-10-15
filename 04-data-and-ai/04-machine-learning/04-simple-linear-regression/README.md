# Simple Linear Regression

*First Machine Learning Algorithm · Supervised Learning · Regression*

**Core idea:** Simple Linear Regression learns a best-fit line from training data so that a new input value can be used to predict a continuous output.

## 1. Introduction

Simple Linear Regression is a foundational machine learning algorithm. Understanding its basic intuition helps prepare for more advanced machine learning concepts and mathematical ideas used in neural networks and deep learning.

## 2. What Problem Does It Solve?

Simple Linear Regression is used for a **regression problem** in **supervised machine learning**.

**Supervised Learning + Regression Problem → Simple Linear Regression**

- **Supervised learning:** training examples include the output values.
- **Regression:** the model predicts a numerical output.

## 3. Example: Predicting Height from Weight

| Weight (kg) | Height (cm) |
|---:|---:|
| 74 | 170 |
| 80 | 180 |
| 75 | 175.5 |

The objective is to train a model on existing data. After training, a new weight can be supplied to predict a corresponding height.

| Variable | Role | Example |
|---|---|---|
| Weight | Independent feature / input | New weight given to the model |
| Height | Dependent feature / output | Height predicted by the model |

**Input:** Weight · **Output:** Height

## 4. Why Is It Called “Simple”?

“Simple” refers to the use of **one input feature**.

| Type | Input features | Output |
|---|---|---|
| Simple Linear Regression | One | One |
| Multiple Linear Regression | Multiple | One |

## 5. Overall Objective

```text
Training Data
     ↓
Learn from the data
     ↓
Trained Simple Linear Regression Model
     ↓
New Weight
     ↓
Predicted Height
```

## 6. Geometric Intuition: The Best-Fit Line

Place the independent feature on the x-axis and the dependent feature on the y-axis:

- **X-axis:** Weight
- **Y-axis:** Height

Simple Linear Regression learns a **best-fit line** that represents the relationship between the input and output. For a new input, the line provides the predicted output.

## 7. How Prediction Happens

1. Give the model a new weight.
2. Locate that weight on the x-axis.
3. Move to the best-fit line.
4. Read the corresponding y-value.
5. Use that y-value as the predicted height.

## 8. Actual Values, Predicted Values, and Error

| Concept | Meaning |
|---|---|
| True / actual point | Observed output value in the dataset |
| Predicted point | Output estimated by the best-fit line |
| Error / residual | Difference between actual and predicted output |

A residual is commonly written as:

$$
e_i = y_i - \hat{y}_i
$$

where \(y_i\) is the actual output and \(\hat{y}_i\) is the predicted output.

The lecture introduces error as the difference between actual and predicted outputs. The exact mathematical objective and treatment of errors are covered in the next material.

## 9. How Is the Best-Fit Line Selected?

Many lines could be drawn through or near the observed points. The goal is to choose a line that fits the data well by comparing actual values with predicted values and minimizing an overall error measure.

```text
Candidate line
      ↓
Compare actual and predicted values
      ↓
Calculate errors
      ↓
Evaluate overall error
      ↓
Choose a line with a low overall error
```

The phrase “minimize total distance” is an introductory intuition. The exact objective used in ordinary least-squares linear regression is more specific and will be covered with the line equation and error calculation.

## 10. Important Terminology

| Term | Meaning |
|---|---|
| Supervised machine learning | Learns from examples that include known outputs |
| Regression | Predicts a numerical output |
| Independent feature | Input used to make the prediction |
| Dependent feature | Output the model predicts |
| Simple Linear Regression | Regression with one input feature |
| Multiple Linear Regression | Regression with multiple input features |
| Best-fit line | Learned line representing the input-output relationship |
| Actual output | Observed value in the dataset |
| Predicted output | Estimated value from the model |
| Error / residual | Difference between actual and predicted output |

## 11. Key Takeaways

- Simple Linear Regression is a supervised learning algorithm for regression problems.
- It uses one input feature to predict a numerical output.
- In this example, Weight is the input and Height is the output.
- The model learns a best-fit line from training data.
- A new input is mapped to a predicted output using that line.
- Error describes the difference between actual and predicted values.
- The best-fit line is chosen by optimizing an overall error measure.

## 12. Exam / Interview Summary

**Simple Linear Regression** is a supervised learning algorithm used for regression with one independent/input feature. It learns a best-fit line from training data and uses that line to predict the dependent/output value for a new input.

| Question | Answer |
|---|---|
| Type of learning? | Supervised learning |
| Type of problem? | Regression |
| Number of input features? | One |
| Example input? | Weight |
| Example output? | Height |
| What does the model learn? | A best-fit line representing the relationship |
| How is prediction made? | Use the line for a new input |
| What is error? | Difference between actual and predicted output |
| How is the best line selected? | By minimizing an overall error measure |

## Quick Revision

**REGRESSION → ONE INPUT → BEST-FIT LINE → LOW OVERALL ERROR → PREDICTION**

```text
Weight (X) → Independent / Input Feature
Height (Y) → Dependent / Output Feature
                 ↓
       Simple Linear Regression
                 ↓
            Best-Fit Line
                 ↓
   New Weight → Predicted Height
```

**Next concept:** The mathematical equation of the best-fit line and a more detailed explanation of error.
