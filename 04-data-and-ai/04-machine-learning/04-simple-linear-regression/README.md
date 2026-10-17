# Simple Linear Regression

*First Machine Learning Algorithm · Supervised Learning · Regression*

**Core idea:** Simple Linear Regression learns a best-fit line from training data so that a new input value can be used to predict a continuous output. It does this by choosing suitable parameters and minimizing a cost function.

## 1. Introduction

Simple Linear Regression is a foundational machine learning algorithm. It helps us understand how a model represents a relationship between an input and an output, measures prediction errors, and finds parameters that fit the training data.

## 2. What Problem Does It Solve?

Simple Linear Regression is used for a **regression problem** in **supervised machine learning**.

**Supervised Learning + Regression Problem → Simple Linear Regression**

- **Supervised learning:** Training examples include the output values.
- **Regression:** The model predicts a numerical output.

## 3. Example: Predicting Height from Weight

| Weight (kg) | Height (cm) |
| ----------: | ----------: |
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
Learn suitable parameters
     ↓
Trained Simple Linear Regression Model
     ↓
New Input
     ↓
Predicted Output
```

The model learns a line by selecting an intercept and slope that produce predictions with a low overall error.

## 6. Geometric Intuition: The Best-Fit Line

Place the independent feature on the x-axis and the dependent feature on the y-axis.

- **X-axis:** Input feature
- **Y-axis:** Output feature

Simple Linear Regression learns a **best-fit line** representing the relationship between the input and output. For a new input, the line provides the predicted output.

## 7. How Prediction Happens

1. Give the model a new input value.
2. Substitute it into the model equation.
3. Calculate the corresponding output.
4. Use that result as the predicted value.

## 8. Understanding the Mathematical Notation

### 8.1 Three Equivalent Straight-Line Notations

A straight line can be represented using different mathematical notations.

| Notation | Equation | Symbols |
|---|---|---|
| School algebra | `y = mx + c` | `m`: slope, `c`: intercept |
| Regression notation | `ŷ = β₀ + β₁x` | `β₀`: intercept, `β₁`: coefficient |
| Notation used in this lecture | `hθ(x) = θ₀ + θ₁x` | `θ₀`: intercept, `θ₁`: coefficient |

Throughout these notes, we use the lecture's notation:

$$
h_\theta(x) = \theta_0 + \theta_1x
$$

Here, `x` is the input feature, and `hθ(x)` is the predicted output.

### 8.2 Intercept: θ₀

The intercept is the predicted output when the input feature is zero.

$$
h_\theta(0) = \theta_0 + \theta_1(0) = \theta_0
$$

Geometrically, the intercept determines where the line crosses the y-axis.

### 8.3 Slope / Coefficient: θ₁

The slope describes how much the predicted output changes when the input feature changes.

For an input change of `Δx`:

$$
\Delta \hat{y} = \theta_1 \Delta x
$$

- **Positive slope:** The line rises from left to right.
- **Negative slope:** The line falls from left to right.
- **Zero slope:** The line is horizontal.

Changing `θ₁` changes the line's tilt, while changing `θ₀` shifts it vertically.

### 8.4 Multiple Input Features

The linear model can be extended to multiple features:

$$
h_\theta(\mathbf{x}) =
\theta_0 + \theta_1x_1 + \theta_2x_2 + \cdots + \theta_nx_n
$$

Each feature has a corresponding coefficient. This extension is commonly called **Multiple Linear Regression**.

Our current focus remains on the one-feature model.

### 8.5 Predicted Output: hθ(x) and ŷ

$$
\hat{y} = h_\theta(x) = \theta_0 + \theta_1x
$$

| Symbol | Meaning |
|---|---|
| `x` | Input / independent feature |
| `y` | Actual output |
| `ŷ` | Predicted output |
| `hθ(x)` | Prediction made by the model |
| `θ₀` | Intercept |
| `θ₁` | Slope / coefficient |

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

- `yᵢ`: Actual output for observation `i`
- `ŷᵢ`: Predicted output for observation `i`
- `eᵢ`: Residual

The sign of the residual indicates the position of the actual point relative to the predicted line:

- **Positive residual:** The actual value is above the predicted value.
- **Negative residual:** The actual value is below the predicted value.
- **Zero residual:** The prediction matches the actual value.

The absolute residual is:

$$
|e_i| = |y_i - \hat{y}_i|
$$

### 9.2 Sum of Squared Errors (SSE)

A common way to measure a line's fit is to square each residual and add the results.

$$
SSE = \sum_{i=1}^{m}(y^{(i)}-\hat{y}^{(i)})^2
$$

Squaring prevents positive and negative residuals from canceling each other out and gives larger errors greater influence.

### 9.3 Mean Squared Error (MSE)

MSE is the average of the squared residuals.

$$
MSE = \frac{1}{m}\sum_{i=1}^{m}
\left(\hat{y}^{(i)}-y^{(i)}\right)^2
$$

Here, `m` represents the number of training examples.

SSE measures the total squared error, whereas MSE averages the squared error across all training examples.

## 10. The Cost Function

### 10.1 What Is a Cost Function?

A **cost function** assigns a numerical value to a candidate model's predictions. It helps us evaluate how well a particular choice of parameters fits the training data.

For simple linear regression, the parameters are:

- `θ₀`: Intercept
- `θ₁`: Slope

Changing these parameters changes the line, its predictions, and therefore its cost.

### 10.2 Squared-Error Cost Function

This lecture uses the following cost function:

$$
J(\theta_0,\theta_1)
=
\frac{1}{2m}
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)})-y^{(i)}\right)^2
$$

Where:

| Symbol | Meaning |
|---|---|
| `J(θ₀, θ₁)` | Cost for the selected parameters |
| `m` | Number of training examples |
| `x⁽ⁱ⁾` | Input of the i-th example |
| `y⁽ⁱ⁾` | Actual output of the i-th example |
| `hθ(x⁽ⁱ⁾)` | Predicted output of the i-th example |
| `(hθ(x⁽ⁱ⁾) − y⁽ⁱ⁾)²` | Squared prediction error |
| `1/(2m)` | Scaling factor applied to the sum |

The function is also called the **squared-error cost function**.

The standard MSE divides the sum of squared errors by `m`. This cost function divides by `2m`, making it half of MSE:

$$
J(\theta_0,\theta_1) = \frac{1}{2}MSE
$$

The factor of `1/2` is included to simplify differentiation when deriving the gradient descent update rule.

**Important distinction:** MSE and the half-MSE cost function are closely related, but they are not the same quantity.

### 10.3 Why Square the Errors?

Squaring the prediction errors provides two important properties:

1. Positive and negative errors cannot cancel each other out.
2. Larger errors contribute disproportionately more to the cost.

For example, an error of `4` contributes `16` to the squared-error sum, whereas an error of `2` contributes `4`.

Other error measures include **Mean Absolute Error (MAE)** and **Root Mean Squared Error (RMSE)**. They measure prediction errors differently and will be useful for comparison later.

## 11. Simplified Example: Fix the Intercept at Zero

To understand the relationship between the slope and cost, temporarily fix the intercept:

$$
\theta_0 = 0
$$

The model becomes:

$$
h_\theta(x) = \theta_1x
$$

Consider this training dataset:

| x | Actual y |
|---:|---:|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |

There are three training examples, so `m = 3`.

Because the intercept is fixed at zero, every candidate line passes through the origin. Only the slope `θ₁` changes.

This is a simplified demonstration, not a restriction imposed on every simple linear regression model.

## 12. Compare Three Candidate Slopes

### 12.1 Candidate 1: θ₁ = 1

The model is:

$$
\hat{y} = x
$$

Predictions are `1, 2, 3`, which match the actual values exactly.

$$
J(1) = \frac{(1-1)^2+(2-2)^2+(3-3)^2}{6}=0
$$

### 12.2 Candidate 2: θ₁ = 0.5

The model is:

$$
\hat{y} = 0.5x
$$

Predictions are `0.5, 1, 1.5`.

$$
J(0.5)
=
\frac{(0.5-1)^2+(1-2)^2+(1.5-3)^2}{6}
$$

$$
J(0.5) = \frac{3.5}{6} \approx 0.5833
$$

### 12.3 Candidate 3: θ₁ = 0

The model predicts zero for every input.

$$
J(0) = \frac{(0-1)^2+(0-2)^2+(0-3)^2}{6}
$$

$$
J(0) = \frac{14}{6} \approx 2.3333
$$

### 12.4 Comparison Table

| Slope `θ₁` | Predictions for `x = 1, 2, 3` | Cost `J(θ₁)` |
|---:|---|---:|
| 1 | 1, 2, 3 | 0 |
| 0.5 | 0.5, 1, 1.5 | 0.5833 |
| 0 | 0, 0, 0 | 2.3333 |

The slope `θ₁ = 1` gives the lowest cost among these candidates and fits all three points exactly.

## 13. Plot Slope Against Cost

With `θ₀ = 0`, the cost becomes a function of just one parameter:

$$
J(\theta_1)
=
\frac{1}{2m}
\sum_{i=1}^{m}(\theta_1x^{(i)}-y^{(i)})^2
$$

For the dataset `(1, 1), (2, 2), (3, 3)`:

$$
J(\theta_1)
=
\frac{1}{6}
\left[(\theta_1-1)^2+(2\theta_1-2)^2+(3\theta_1-3)^2\right]
$$

Simplifying:

$$
J(\theta_1) = \frac{7}{6}(\theta_1-1)^2
$$

This is a U-shaped quadratic curve.

- **Horizontal axis:** Candidate slope `θ₁`
- **Vertical axis:** Cost `J(θ₁)`
- **Minimum:** `θ₁ = 1`, where `J = 0`

The minimum is global because the cost is a nonnegative squared expression and reaches zero at `θ₁ = 1`. No other slope can produce a lower cost for this dataset under the fixed-intercept assumption.

## 14. Gradient Descent: The Optimization Idea

### 14.1 What Is Gradient Descent?

**Gradient descent** is an iterative optimization algorithm used to adjust model parameters to reduce a cost function.

Instead of manually trying every possible parameter value, the algorithm uses information about how the cost changes to decide how to update the parameters.

The cost curve represents the relationship between a parameter and its cost. Gradient descent is the procedure that moves the parameter toward a minimum.

### 14.2 Basic Intuition

The general process is:

1. Start with initial parameter values.
2. Calculate predictions using the current model.
3. Evaluate the cost.
4. Determine which parameter changes would reduce the cost.
5. Update the parameters.
6. Repeat until the algorithm converges or a stopping condition is reached.

In the simplified example, `θ₀` remains fixed at zero, so only `θ₁` changes. In the general model, both `θ₀` and `θ₁` can be updated.

### 14.3 Visual Intuition

Imagine starting somewhere on the U-shaped cost curve.

- If the current slope is away from the minimum, the cost is higher.
- Parameter updates move the current point toward lower cost.
- Near the minimum, the cost approaches its smallest value.

The next lecture will derive the gradient descent update rule, explain the learning rate, and show how the parameters are updated mathematically.

## 15. Important Terminology

| Term | Meaning |
|---|---|
| Supervised learning | Learning from examples with known outputs |
| Regression | Predicting a numerical output |
| Independent feature | Input used to make a prediction |
| Dependent feature | Output the model predicts |
| Simple Linear Regression | Regression with one input feature |
| Intercept | Predicted output when the input is zero |
| Slope / coefficient | Change in predicted output for a one-unit increase in input |
| Residual | Actual output minus predicted output |
| SSE | Sum of squared residuals |
| MSE | Mean of squared residuals |
| Cost function | Numerical measure used to evaluate a model's fit |
| Half-MSE cost | MSE multiplied by `1/2` |
| Gradient descent | Iterative algorithm for reducing a cost function |
| Global minimum | Lowest attainable cost over the parameter values being considered |
| Convergence | The algorithm's progress reaches a stopping condition or stabilizes sufficiently |

## 16. Key Takeaways

- Simple Linear Regression predicts a numerical output from one input feature.
- Its model equation is `hθ(x) = θ₀ + θ₁x`.
- `θ₀` is the intercept, and `θ₁` is the slope.
- Residuals measure the difference between actual and predicted outputs.
- SSE and MSE are common squared-error measures.
- The lecture's cost function is `J(θ₀, θ₁) = (1/(2m)) Σ(hθ(x⁽ⁱ⁾) − y⁽ⁱ⁾)²`.
- The half-MSE cost includes a factor of `1/2` to simplify differentiation.
- Different parameter values produce different predictions and costs.
- In the simplified dataset, `θ₀ = 0` and `θ₁ = 1` give zero cost.
- The cost curve illustrates how cost changes as the slope changes.
- Gradient descent iteratively updates parameters to reduce cost.

## 17. Exam / Interview Summary

**Simple Linear Regression** predicts a continuous output using one input feature and a straight-line model:

$$
\hat{y} = \theta_0 + \theta_1x
$$

The squared-error cost function evaluates the fit of the model:

$$
J(\theta_0,\theta_1)
=
\frac{1}{2m}
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)})-y^{(i)}\right)^2
$$

The objective is to find parameter values that minimize this cost. Gradient descent is an iterative method for updating parameters in a direction that reduces the cost.

| Question | Short answer |
|---|---|
| What does the cost function measure? | How well a candidate model fits the training data |
| Why square the errors? | To prevent cancellation and penalize larger errors more heavily |
| Why use `1/(2m)`? | To average the squared errors and simplify differentiation |
| Why fix `θ₀ = 0` in the example? | To visualize cost as a function of one changing parameter |
| Which slope minimizes cost for `(1,1), (2,2), (3,3)`? | `θ₁ = 1`, with cost `0` |
| What is a global minimum? | The lowest attainable cost over the parameter values considered |
| What is gradient descent? | An iterative method for updating parameters to reduce cost |
| What is the learning rate? | A parameter controlling the step size of gradient descent; covered next |

## Quick Revision

**CHOOSE PARAMETERS → PREDICT → CALCULATE COST → UPDATE PARAMETERS → APPROACH THE MINIMUM**

```text
Training Data
     ↓
Choose θ₀ and θ₁
     ↓
Calculate Predictions
     ↓
Calculate Cost J(θ₀, θ₁)
     ↓
Update Parameters
     ↓
Repeat to Reduce Cost
```

- Model equation: `hθ(x) = θ₀ + θ₁x`
- Residual: `e = y − ŷ`
- MSE: `(1/m) Σ(ŷ − y)²`
- Cost function: `(1/(2m)) Σ(ŷ − y)²`
- Simplified example: `J(θ₁) = (7/6)(θ₁ − 1)²`
- Minimum for the example: `θ₁ = 1`, `J = 0`