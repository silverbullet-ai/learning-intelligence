# R² and Adjusted R²

**AI-2 • Linear Regression • Lecture 7**

Performance metrics for simple and multiple linear regression.

## Learning Objectives

- Understand residual variation and total variation.
- Calculate and interpret the coefficient of determination (R²).
- Understand why R² can be misleading when adding features.
- Calculate adjusted R² and understand its feature-count penalty.
- Compare regression models using both metrics.

## 1. Why Evaluate a Regression Model?

After fitting a regression line or hyperplane, we need to measure how well its predictions explain variation in the target.

Two useful evaluation metrics are:

- **R²:** Coefficient of determination.
- **Adjusted R²:** A variation of R² that accounts for the number of predictors and observations.

## 2. R²: Coefficient of Determination

The coefficient of determination measures how well the model explains target variation relative to predicting the observed target mean.

### Formula

$$
R^2 = 1 - \frac{SS_{res}}{SS_{tot}}
$$

Where:

| Term | Definition |
|---|---|
| $y_i$ | Observed target for observation $i$ |
| $\hat{y}_i$ | Model prediction for observation $i$ |
| $\bar{y}$ | Mean of observed target values |
| $SS_{res}$ | Sum of squared residuals |
| $SS_{tot}$ | Total sum of squares |

$$
SS_{res} = \sum_{i=1}^{n}(y_i-\hat{y}_i)^2
$$

$$
SS_{tot} = \sum_{i=1}^{n}(y_i-\bar{y})^2
$$

A residual is the difference between an observed value and its prediction:

$$
e_i = y_i-\hat{y}_i
$$

### Interpretation

| R² value | Meaning |
|---|---|
| $1$ | Perfect predictions on the evaluated data |
| $0$ | Same squared-error performance as predicting the target mean |
| Below $0$ | Worse squared-error performance than the mean baseline |

For example, $R^2=0.70$ means the model explains 70% of target variation relative to the mean-prediction baseline on the evaluated data.

**Important:** R² is not classification-style prediction accuracy. A high training R² does not guarantee good performance on unseen data.

## 3. Why R² Alone Can Mislead

Consider a house-price prediction model that starts with house size and then adds bedrooms and location.

Illustrative R² values might increase from $0.75$ to $0.80$, then $0.85$. Even adding an irrelevant feature could produce an illustrative increase to $0.87$.

These figures are hypothetical examples, not measured results.

For ordinary least squares with an intercept, adding predictors cannot decrease training R² on the same dataset. The expanded model can assign a coefficient of zero to a new predictor.

Therefore, a higher training R² alone does not establish that the new feature is useful.

## 4. Adjusted R²

Adjusted R² accounts for the number of predictors and the number of observations.

### Formula

$$
R^2_{adj}
=
1-(1-R^2)\frac{n-1}{n-p-1}
$$

Where:

| Symbol | Meaning |
|---|---|
| $n$ | Number of observations |
| $p$ | Number of independent features, excluding the intercept |
| $n-p-1$ | Residual degrees of freedom; must be greater than zero |

### How It Works

Adjusted R² introduces a penalty for the number of predictors.

- It increases when the improvement in fit sufficiently offsets the feature-count penalty.
- It decreases when the improvement is insufficient.
- It can increase or decrease when predictors are added.

Adjusted R² does not directly test whether a feature is correlated with the target.

## 5. R² vs Adjusted R²

| Aspect | R² | Adjusted R² |
|---|---|---|
| Purpose | Describe explained variation | Account for model complexity |
| Feature-count penalty | No | Yes |
| Adding predictors to training OLS with an intercept | Cannot decrease | May increase or decrease |
| Common use | Describe model fit | Compare models with different predictor counts on the same data |

Neither metric replaces evaluation on unseen data.

## 6. Practical Evaluation Workflow

1. Fit the regression model.
2. Generate predictions.
3. Calculate residuals.
4. Calculate $SS_{res}$ and $SS_{tot}$.
5. Calculate R².
6. Calculate adjusted R² using the number of observations and predictors.
7. Compare models on the same evaluation dataset.
8. Evaluate generalization using held-out validation or test data.

Also inspect residuals and other error metrics when evaluating regression performance.

## 7. Interview Revision

**Q1. What does R² measure?**

It measures explained target variation relative to predicting the observed target mean.

**Q2. Can R² be negative?**

Yes. A model can perform worse than the mean-prediction baseline on the evaluated data.

**Q3. Why can training R² be misleading?**

It cannot decrease when predictors are added to ordinary least squares with an intercept, even if the new predictors provide little practical value.

**Q4. Why use adjusted R²?**

It accounts for the number of predictors and sample size, allowing a feature-count penalty when comparing models.

**Q5. Can adjusted R² decrease after adding a feature?**

Yes. It may decrease when the improvement in fit is insufficient to offset the penalty.

**Q6. Does a high R² guarantee good predictions on unseen data?**

No. Held-out evaluation is needed to assess generalization.

## 8. Quick Recap

- Residual: observed value minus predicted value.
- $SS_{res}$: sum of squared residuals.
- $SS_{tot}$: sum of squared deviations from the observed mean.
- R² measures fit relative to a mean-prediction baseline.
- Adjusted R² accounts for predictor count and sample size.
- Use held-out evaluation to assess generalization.

**Next:** Practical implementation and further evaluation of linear regression.
