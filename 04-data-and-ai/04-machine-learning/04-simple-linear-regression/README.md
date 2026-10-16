# Simple Linear Regression

*First Machine Learning Algorithm · Supervised Learning · Regression*

**Core idea:** Simple Linear Regression learns a best-fit line from training data so that a new input value can be used to predict a continuous output.

## 1. Introduction

Simple Linear Regression is a foundational machine learning algorithm. Understanding its basic intuition helps prepare for more advanced machine learning concepts and mathematical ideas used in neural networks and deep learning.

## 2. What Problem Does It Solve?

Simple Linear Regression is used for a **regression problem** in **supervised machine learning**.

**Supervised Learning + Regression Problem → Simple Linear Regression**

- **Supervised learning:** Training examples include the output values.
- **Regression:** The model predicts a numerical output.

## 3. Example: Predicting Height from Weight

| Weight (kg) | Height (cm) |
| ----------: | ----------: |
|          74 |         170 |
|          80 |         180 |
|          75 |       175.5 |

The objective is to train a model on existing data. After training, a new weight can be supplied to predict a corresponding height.

| Variable | Role                        | Example                       |
| -------- | --------------------------- | ----------------------------- |
| Weight   | Independent feature / input | New weight given to the model |
| Height   | Dependent feature / output  | Height predicted by the model |

**Input:** Weight · **Output:** Height

## 4. Why Is It Called “Simple”?

“Simple” refers to the use of **one input feature**.

| Type                       | Input features | Output |
| -------------------------- | -------------- | ------ |
| Simple Linear Regression   | One            | One    |
| Multiple Linear Regression | Multiple       | One    |

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

## 8. Understanding the Mathematical Notation

### 8.1 Three Equivalent Straight-Line Notations

A straight line can be represented using different mathematical notations.

| Notation                      | Equation                  | Symbols                                    |
| ----------------------------- | ------------------------- | ------------------------------------------ |
| School algebra                | `y = mx + c`            | `m`: slope, `c`: intercept             |
| Regression notation           | `ŷ = β₀ + β₁x`     | `β₀`: intercept, `β₁`: coefficient |
| Notation used in this lecture | `hθ(x) = θ₀ + θ₁x` | `θ₀`: intercept, `θ₁`: coefficient |

Throughout this section, we use the lecture's notation:

$$
h_\theta(x) = \theta_0 + \theta_1x
$$

Here, `x` is the independent feature (Weight), and `hθ(x)` is the predicted output (Height).

### 8.2 Intercept: θ₀

The intercept is the predicted output when the input feature is zero.

Starting with the model equation:

$$
h_\theta(x) = \theta_0 + \theta_1x
$$

Substituting `x = 0`:

$$
h_\theta(0) = \theta_0 + \theta_1(0) = \theta_0
$$

Geometrically, the intercept determines where the line crosses the y-axis.

In the Weight–Height example, this represents the line's predicted height at zero weight. Although mathematically defined, this prediction may not be physically meaningful.

### 8.3 Slope / Coefficient: θ₁

The slope describes how much the predicted output changes when the input feature changes.

For a change in input of `Δx`:

$$
\Delta \hat{y} = \theta_1 \Delta x
$$

When `Δx = 1`:

$$
\Delta \hat{y} = \theta_1
$$

- **Positive slope:** The line rises from left to right.
- **Negative slope:** The line falls from left to right.
- **Zero slope:** The line is horizontal.

Changing `θ₁` changes the line's tilt, while changing `θ₀` shifts the line vertically.

### 8.4 Multiple Input Features

Simple Linear Regression uses one input feature. The same linear model can be extended to multiple features:

$$
h_\theta(\mathbf{x}) =
\theta_0 + \theta_1x_1 + \theta_2x_2 + \cdots + \theta_nx_n
$$

Each feature `xᵢ` has a corresponding coefficient `θᵢ`. This extension is commonly called **Multiple Linear Regression**.

Our current focus remains on the one-feature model.

### 8.5 Predicted Output: hθ(x) and ŷ

After fitting the line, a new input value can be substituted into the equation to calculate its predicted output.

$$
\hat{y} = h_\theta(x) = \theta_0 + \theta_1x
$$

| Symbol     | Meaning                              |
| ---------- | ------------------------------------ |
| `x`      | Input / independent feature (Weight) |
| `y`      | Actual output (Height)               |
| `ŷ`     | Predicted output                     |
| `hθ(x)` | Prediction made by the model         |
| `θ₀`   | Intercept                            |
| `θ₁`   | Slope / coefficient                  |

The symbols `ŷ` and `hθ(x)` both represent the predicted output.

## 9. Actual Values, Predictions, and Residuals

### 9.1 Understanding Prediction Error

For each training observation, compare the actual output with the predicted output. Their difference is called the **error** or **residual**.

$$
e_i = y_i - \hat{y}_i
$$

Equivalently:

$$
e_i = y_i - h_\theta(x_i)
$$

Where:

- `yᵢ` is the actual output for observation `i`.
- `ŷᵢ` is the predicted output for observation `i`.
- `eᵢ` is the residual.

The sign of the residual indicates the position of the actual point relative to the predicted line:

- **Positive residual:** The actual point lies above the predicted line.
- **Negative residual:** The actual point lies below the predicted line.
- **Zero residual:** The prediction matches the actual value.

The absolute vertical difference is:

$$
|e_i| = |y_i - \hat{y}_i|
$$

### 9.2 Selecting the Best-Fit Line

Many lines can be drawn through or near the observed points. The goal is to choose a line that fits the training data well by evaluating its prediction errors.

The training process adjusts the parameters `θ₀` and `θ₁` to reduce an overall error measure.

Simply adding signed residuals is not a reliable error measure because positive and negative residuals can cancel each other out.

A common approach in linear regression is to minimize the **Sum of Squared Errors (SSE)**:

$$
SSE = \sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

Another commonly used measure is the **Mean Squared Error (MSE)**:

* [ ] 
  ```math
  MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
  ```

These measures square the residuals, preventing positive and negative errors from canceling and penalizing larger errors more heavily.

For ordinary least-squares linear regression, the parameters are selected to minimize the sum of squared residuals.

### 9.3 Preview: Parameter Optimization

Instead of drawing many unrelated lines, we can systematically adjust the model parameters and evaluate how the error changes.

**Basic workflow:**

```text
Initial Line
     ↓
Adjust θ₀ and θ₁
     ↓
Calculate Predictions
     ↓
Evaluate Prediction Error
     ↓
Seek a Better-Fitting Line
```

The precise optimization algorithm used to find suitable parameter values will be covered in a later lesson.

## 10. Important Terminology

| Term                        | Meaning                                                     |
| --------------------------- | ----------------------------------------------------------- |
| Supervised machine learning | Learns from examples that include known outputs             |
| Regression                  | Predicts a numerical output                                 |
| Independent feature         | Input used to make a prediction                             |
| Dependent feature           | Output the model predicts                                   |
| Simple Linear Regression    | Regression with one input feature                           |
| Multiple Linear Regression  | Regression with multiple input features                     |
| Intercept                   | Predicted output when the input is zero                     |
| Slope / coefficient         | Change in predicted output for a one-unit increase in input |
| Best-fit line               | Learned line representing the input-output relationship     |
| Actual output               | Observed value in the dataset                               |
| Predicted output            | Estimated value from the model                              |
| Error / residual            | Difference between actual and predicted output              |
| SSE                         | Sum of squared residuals                                    |
| MSE                         | Mean of squared residuals                                   |

## 11. Key Takeaways

- Simple Linear Regression is a supervised learning algorithm for regression problems.
- It uses one input feature to predict a numerical output.
- In this example, Weight is the input and Height is the output.
- The model learns a best-fit line from training data.
- The equation used in this lecture is `hθ(x) = θ₀ + θ₁x`.
- `θ₀` represents the intercept, while `θ₁` represents the slope.
- `hθ(x)` and `ŷ` represent the predicted output.
- The residual is the actual output minus the predicted output.
- Training adjusts the intercept and slope to reduce an overall error measure.
- SSE and MSE are common measures used to evaluate prediction errors.

## 12. Exam / Interview Summary

**Simple Linear Regression** is a supervised learning algorithm used to predict a numerical output from one input feature. It learns a best-fit line represented by:

$$
\hat{y} = \theta_0 + \theta_1x
$$

The intercept `θ₀` determines where the line meets the y-axis, while the coefficient `θ₁` determines its slope. For each observation, the residual is the difference between the actual and predicted outputs. Model fitting adjusts these parameters to minimize an error measure, commonly the sum of squared residuals.

| Question                       | Answer                                 |
| ------------------------------ | -------------------------------------- |
| Type of learning?              | Supervised learning                    |
| Type of problem?               | Regression                             |
| Number of input features?      | One                                    |
| Example input?                 | Weight                                 |
| Example output?                | Height                                 |
| What does the model learn?     | A best-fit line                        |
| What does `θ₀` represent?  | Intercept                              |
| What does `θ₁` represent?  | Slope / coefficient                    |
| What is a residual?            | Actual output minus predicted output   |
| What is SSE?                   | Sum of squared residuals               |
| How is the best line selected? | By minimizing the chosen error measure |

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

- Model equation: `hθ(x) = θ₀ + θ₁x`
- Intercept: `θ₀`
- Slope: `θ₁`
- Predicted output: `ŷ = hθ(x)`
- Actual output: `y`
- Residual: `e = y − ŷ`
- Common squared-error measures: SSE and MSE

**Next concept:** The mathematical equation of the best-fit line and a deeper explanation of error and optimization.
