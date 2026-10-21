# Multiple Linear Regression

**Core idea:** Simple Linear Regression uses one independent feature. Multiple Linear Regression uses two or more independent features to predict one output.

## 1. Recap: Simple Linear Regression

In Simple Linear Regression, the model predicts an output using one independent feature.

The hypothesis is:

$$
h_\theta(x)=\theta_0+\theta_1x
$$

Where:

- \(x\): Independent input feature.
- \(\theta_0\): Intercept.
- \(\theta_1\): Coefficient of the input feature.
- \(h_\theta(x)\): Predicted output.

During training, the model adjusts its parameters to reduce the cost function. The observed input values are provided by the dataset; they are not model parameters.

## 2. What Changes in Multiple Linear Regression?

Multiple Linear Regression extends the same linear-model idea to datasets with two or more independent features.

| Aspect | Simple Linear Regression | Multiple Linear Regression |
|---|---|---|
| Number of input features | One | Two or more |
| Output | One target | One target |
| Intercept | One, \(\theta_0\) | One, \(\theta_0\) |
| Feature coefficients | One | One per feature |
| Example | Predicting price from house size | Predicting price from size, rooms, and location |

The key difference is the number of input features. Both models use an intercept and coefficients to produce a prediction.

## 3. Example: House Price Prediction

Suppose we want to predict house prices using three input features.

| Feature | Symbol | Role |
|---|---|---|
| Number of rooms | \(x_1\) | Independent input |
| House size | \(x_2\) | Independent input |
| Location | \(x_3\) | Independent input |
| House price | \(y\) | Dependent output |

The hypothesis becomes:

$$
h_\theta(x)=\theta_0+\theta_1x_1+\theta_2x_2+\theta_3x_3
$$

Here:

- \(\theta_0\): The single intercept.
- \(\theta_1\): Coefficient for the number of rooms.
- \(\theta_2\): Coefficient for house size.
- \(\theta_3\): Coefficient for location.

The location feature may require numerical encoding before it can be used in a numerical model. The appropriate encoding depends on how location is represented in the dataset.

Each additional independent feature contributes another coefficient, while the model retains one intercept.

## 4. General Equation

For \(n\) independent features, the hypothesis is:

$$
h_\theta(x)=\theta_0+\sum_{j=1}^{n}\theta_jx_j
$$

Equivalently:

$$
h_\theta(x)=\theta_0+\theta_1x_1+\theta_2x_2+\cdots+\theta_nx_n
$$

Where:

- \(n\): Number of independent features.
- \(x_j\): Value of the \(j\)-th feature.
- \(\theta_j\): Coefficient associated with that feature.
- \(\theta_0\): Intercept.
- \(h_\theta(x)\): Predicted output.

The model has \(n+1\) parameters: one intercept and \(n\) feature coefficients.

## 5. Cost Function

The objective remains the same as in Simple Linear Regression: minimize the prediction error over the training examples.

For \(m\) training examples, the half mean squared-error cost is:

$$
J(\theta)=\frac{1}{2m}\sum_{i=1}^{m}
\left(h_\theta(x^{(i)})-y^{(i)}\right)^2
$$

Here, \(h_\theta(x^{(i)})\) is the prediction for the \(i\)-th training example, and \(y^{(i)}\) is its actual output.

The cost function measures the aggregate squared prediction error. A lower cost indicates a better fit to the observed training data under this objective.

## 6. Gradient Descent with Multiple Features

Gradient descent adjusts the intercept and each feature coefficient to reduce the cost.

The general update rule is:

$$
\theta_j\leftarrow\theta_j-\alpha
\frac{\partial J(\theta)}{\partial\theta_j}
$$

For multiple linear regression, the partial derivative for the intercept is:

$$
\frac{\partial J}{\partial\theta_0}
=\frac{1}{m}\sum_{i=1}^{m}
\left(h_\theta(x^{(i)})-y^{(i)}\right)
$$

For feature coefficient \(\theta_j\):

$$
\frac{\partial J}{\partial\theta_j}
=\frac{1}{m}\sum_{i=1}^{m}
\left(h_\theta(x^{(i)})-y^{(i)}\right)x_j^{(i)}
$$

The intercept derivative has no additional feature multiplier. Each coefficient derivative includes its corresponding feature value.

### Training sequence

1. Initialize the intercept and feature coefficients.
2. Calculate predictions using all input features.
3. Calculate the cost and all gradients.
4. Update the parameters simultaneously using their old values.
5. Repeat until the chosen stopping condition is reached.

The training inputs remain unchanged; gradient descent updates the model parameters.

## 7. Understanding the Cost Surface

When only one parameter varies, cost can be plotted as a two-dimensional curve. When two parameters vary, the cost can be represented as a three-dimensional surface.

With multiple feature coefficients and an intercept, the cost function depends on several parameters. It therefore cannot be fully represented in an ordinary three-dimensional graph when there are more than two parameters.

For the squared-error objective of linear regression, the cost is convex with respect to the model parameters. Gradient descent with a suitable learning rate can approach a global minimum. Feature scaling can help make optimization more stable and efficient.

## 8. Important Distinctions

- **Independent features:** Inputs used to make predictions.
- **Dependent variable:** The output the model predicts.
- **Intercept:** The single constant term in the hypothesis.
- **Feature coefficient:** The parameter multiplying a particular input feature.
- **Cost function:** Measures aggregate prediction error.
- **Gradient descent:** Iteratively updates parameters to reduce the cost.
- **Feature scaling:** Transforms feature magnitudes to help optimization behave more effectively.
- **Training inputs:** Observed values from the dataset, not parameters learned by gradient descent.

More input features do not automatically guarantee better predictions. The usefulness of a feature depends on the data and the problem.

## 9. Interview-Ready Revision

| Question | Answer |
|---|---|
| What distinguishes simple and multiple linear regression? | Simple uses one independent feature; multiple uses two or more. |
| How many intercepts are there? | One in both models. |
| How many feature coefficients are needed? | One per independent feature. |
| What does the model learn? | The intercept and feature coefficients. |
| What is the purpose of the cost function? | To quantify prediction error. |
| How does gradient descent work? | It updates parameters using their cost derivatives. |
| Do the input values change during training? | No, not during ordinary model fitting. |
| Can all cost dimensions be visualized in 3D? | No, not when the cost depends on more than two parameters. |

## 10. Quick Revision

**ONE FEATURE → SIMPLE LINEAR REGRESSION**

**MULTIPLE FEATURES → MULTIPLE LINEAR REGRESSION**

**ONE INTERCEPT + ONE COEFFICIENT PER FEATURE**

**PREDICT → CALCULATE COST → COMPUTE GRADIENTS → UPDATE PARAMETERS → REPEAT**

The next topic in the lecture series is the **assumptions of linear regression**.
