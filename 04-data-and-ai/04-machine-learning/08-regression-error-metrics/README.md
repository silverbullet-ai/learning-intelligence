# Regression Error Metrics

Mean Squared Error (MSE), Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE).

## Learning Objectives

- Understand residuals and prediction errors.
- Calculate Mean Squared Error (MSE).
- Understand why squaring errors matters.
- Calculate Mean Absolute Error (MAE).
- Calculate Root Mean Squared Error (RMSE).
- Compare the advantages and disadvantages of different error metrics.
- Understand how error metrics complement R² and adjusted R².

## 1. Why Do We Need Error Metrics?

After fitting a regression model, we need to evaluate how close its predictions are to the actual target values.

The difference between an observed value and its prediction is called a residual or prediction error.

$$
e_i = y_i-\hat{y}_i
$$

Where:

- $y_i$ = observed target value.
- $\hat{y}_i$ = predicted target value.
- $e_i$ = residual or prediction error.

Two categories of regression evaluation metrics:

| Category | Metrics | Purpose |
|---|---|---|
| Overall model performance | R², Adjusted R² | Describe explained target variation |
| Prediction error | MSE, MAE, RMSE | Measure the magnitude of prediction errors |

## 2. Mean Squared Error (MSE)

Mean Squared Error calculates the average of squared differences between observed and predicted values.

### Formula

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

### Main Goal

A lower MSE indicates a smaller aggregated squared prediction error.

MSE is also the squared-error objective commonly used when optimizing linear regression with gradient descent.

### Why Squaring the Error Matters

Squaring residuals produces a quadratic error function.

- **Differentiable:** Gradients can be calculated for optimization.
- **Smooth:** The quadratic objective supports gradient-based optimization.
- **Convex:** For ordinary linear regression with squared-error loss, the objective is convex.
- **Outlier-sensitive:** Large residuals contribute disproportionately because they are squared.

### Advantages of MSE

| Advantage | Explanation |
|---|---|
| Differentiable | Gradients can be calculated for optimization |
| Smooth objective | Supports gradient-descent optimization |
| Convex objective | Squared-error linear regression has no non-global local minima |

### Disadvantages of MSE

- Sensitive to outliers because large errors are squared.
- Large residuals can dominate the metric and influence the fitted model.
- The result is expressed in squared units of the target variable.

**Example:** If salary is measured in lakhs, MSE is expressed in lakhs².

## 3. Mean Absolute Error (MAE)

Mean Absolute Error calculates the average absolute difference between observed and predicted values.

### Formula

$$
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
$$

### Advantages of MAE

- More robust to large errors than MSE because residuals are not squared.
- Remains in the same unit as the target variable.
- Provides an intuitive measure of average absolute prediction error.

### Disadvantages of MAE

- The absolute-value function is not differentiable at zero.
- Sub-gradients can be used to handle optimization at the non-differentiable point.
- Optimization is less straightforward around zero than with squared-error loss.

## 4. Root Mean Squared Error (RMSE)

Root Mean Squared Error takes the square root of MSE.

### Formula

$$
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
$$

Or:

$$
RMSE = \sqrt{MSE}
$$

### Advantages

- Expressed in the same unit as the target variable.
- Retains the squared-error structure.
- Penalizes larger prediction errors more heavily than smaller ones.

### Disadvantages

- Sensitive to outliers because residuals are squared.
- A few large errors can substantially increase the metric.

## 5. MSE vs MAE vs RMSE

| Property | MSE | MAE | RMSE |
|---|---|---|---|
| Formula | Mean squared residuals | Mean absolute residuals | Square root of MSE |
| Outlier sensitivity | High | Lower | High |
| Same unit as target? | No | Yes | Yes |
| Differentiability | Yes | Not at zero | Yes |
| Optimization | Smooth squared-error objective | Sub-gradient at zero | Smooth squared-error structure |
| Error emphasis | Strongly penalizes large errors | Linear penalty | Strongly penalizes large errors |

## 6. How These Metrics Work Together

A useful regression evaluation workflow combines error metrics with overall model-performance measures.

1. Train the regression model.
2. Generate predictions.
3. Calculate residuals.
4. Calculate MSE, MAE, and RMSE.
5. Calculate R² and adjusted R² where applicable.
6. Compare the metrics and interpret them in the context of the target variable and possible outliers.
7. Evaluate performance on held-out data to assess generalization.

No single metric provides a complete picture of model performance.

## 7. Interview and Exam Revision

**Q1. Why use MSE?**

It provides a smooth, differentiable squared-error objective suitable for gradient-based optimization.

**Q2. Why use MAE?**

It is less sensitive to large errors than MSE and remains in the original target unit.

**Q3. What is a disadvantage of MAE?**

It is not differentiable at zero, although sub-gradients can be used for optimization.

**Q4. Why use RMSE?**

It brings MSE back to the original target unit while retaining the squared-error structure.

**Q5. What is the main weakness of MSE and RMSE?**

Both are sensitive to outliers because residuals are squared.

**Q6. Which metrics should be examined when evaluating a regression model?**

MSE, MAE, RMSE, R², and adjusted R² provide complementary information.

## 8. Quick Revision

| Metric | One-line explanation |
|---|---|
| MSE | Smooth squared-error objective, but sensitive to outliers and expressed in squared units |
| MAE | More robust to large errors and expressed in the original target unit |
| RMSE | Square root of MSE, expressed in the original target unit while retaining squared-error behavior |

### One-Line Memory Trick

- **MSE:** Smooth but outlier-sensitive.
- **MAE:** More robust but less straightforward to optimize at zero.
- **RMSE:** MSE brought back to the original unit.

## 9. Next Step

Apply MSE, MAE, RMSE, R², and adjusted R² to an actual linear regression model and compare the resulting values.