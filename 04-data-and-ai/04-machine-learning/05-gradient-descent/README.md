## Gradient Descent and Convergence

### 1 Why Do We Need Convergence?

In the previous lecture, we manually changed the slope `θ₁` and calculated the corresponding cost. This helped us visualize the cost curve, but trying arbitrary parameter values is inefficient.

**Gradient descent** provides a repeatable method for updating model parameters using the derivative of the cost function.

The objective is to minimize:

$$
J(\theta_0,\theta_1)
$$

In our simplified example, `θ₀ = 0`, so only the slope `θ₁` is updated.

### 2 The Gradient Descent Update Rule

The general update rule is:

$$
\theta_j \leftarrow
\theta_j-\alpha\frac{\partial J(\theta)}{\partial\theta_j}
$$

Repeat the update until a suitable stopping condition is reached.

| Symbol | Meaning |
|---|---|
| `θⱼ` | Model parameter being updated |
| `J(θ)` | Cost function |
| `∂J(θ)/∂θⱼ` | Partial derivative of cost with respect to parameter `θⱼ` |
| `α` | Learning rate |
| `←` | Assign the newly calculated value to the parameter |

The derivative indicates how the cost changes with the parameter. The learning rate scales the size of the update.

When a model has multiple parameters, each parameter is updated using its own partial derivative.

### 3 How the Derivative Determines the Direction

Consider a U-shaped cost curve with `θ₁` on the horizontal axis and `J(θ₁)` on the vertical axis.

| Position relative to the minimum | Derivative | Effect of the update |
|---|---|---|
| Left side | Negative | Subtracting a negative value increases `θ₁` |
| Right side | Positive | Subtracting a positive value decreases `θ₁` |
| At the minimum | Zero | No change from the gradient step |

The update rule is:

$$
\theta_1 \leftarrow
\theta_1-\alpha\frac{dJ}{d\theta_1}
$$

Therefore:

- **Negative derivative:** Increase the parameter.
- **Positive derivative:** Decrease the parameter.
- **Zero derivative:** The gradient update leaves the parameter unchanged.

For the convex quadratic cost curve in our simplified example, these updates move toward the global minimum when the learning rate is appropriate.

### 4 Understanding the Learning Rate

The learning rate `α` controls the size of each parameter update.

| Learning rate | Possible behavior |
|---|---|
| Too small | Very small updates; convergence may take many iterations |
| Too large | Updates may overshoot the minimum, oscillate, or fail to converge |
| Suitable for the problem | Progress toward the minimum at a useful rate |

The lecture uses `α = 0.001` as an illustrative value. It is not a universally optimal learning rate.

The appropriate learning rate depends on the cost function, parameter scale, and problem.

### 5 Step-by-Step Algorithm

1. Initialize the model parameters.
2. Calculate the current predictions and cost.
3. Calculate the derivative of the cost with respect to each parameter.
4. Update the parameters using the gradient descent rule.
5. Recalculate the gradient at the updated parameters.
6. Repeat until the chosen stopping condition is reached.

**Workflow:**

```text
Initialize Parameters
        ↓
Calculate Predictions
        ↓
Calculate Cost and Gradients
        ↓
Update Parameters
        ↓
Check Stopping Condition
        ↓
Repeat if Necessary
        ↓
Fitted Model
```

### 6 What Is Convergence?

**Convergence** describes the process of approaching a stable solution or satisfying a stopping condition during optimization.

In gradient descent, progress may be monitored using:

- The change in cost between iterations.
- The size of parameter updates.
- A predefined maximum number of iterations.

A small gradient or a stable cost can indicate convergence, but the appropriate stopping condition depends on the algorithm and problem. Convergence does not automatically guarantee the best possible solution for every optimization problem.

For the simplified convex quadratic cost curve, the global minimum occurs at `θ₁ = 1`.

## Connection to the Best-Fit Line

The prediction equation remains:

$$
h_\theta(x)=\theta_0+\theta_1x
$$

- Changing `θ₀` changes the intercept.
- Changing `θ₁` changes the slope.
- Gradient descent updates these parameters to reduce the cost.

In the simplified example, the intercept stays fixed at zero. The slope is updated until it approaches the value that minimizes the cost.

**Parameter initialization → Gradient calculation → Parameter update → Repeat → Lower cost → Fitted line**

## Important Distinctions

- **Cost curve:** Shows how cost varies with a parameter.
- **Gradient descent:** An iterative algorithm that updates parameters using derivatives.
- **Derivative:** Indicates the local rate and direction of cost change.
- **Learning rate:** Controls the size of each update.
- **Convergence:** Indicates that the algorithm has reached its stopping condition or stabilized sufficiently.
- **Global minimum:** The lowest cost over the parameter values being considered.

For the simplified convex cost curve, gradient descent can approach the global minimum when the learning rate is appropriate.

## Interview / Exam Revision

| Question | Short answer |
|---|---|
| Why use gradient descent? | To iteratively update parameters and reduce the cost |
| What is the update rule? | `θⱼ ← θⱼ − α × ∂J/∂θⱼ` |
| What does a negative derivative do? | Increases the parameter after the update |
| What does a positive derivative do? | Decreases the parameter after the update |
| What is the learning rate? | A factor that controls the update step size |
| What happens if the learning rate is too small? | Progress can be very slow |
| What happens if the learning rate is too large? | Updates may overshoot or fail to converge |
| What is convergence? | Reaching a stopping condition or sufficiently stable solution |
| Does convergence always guarantee a global minimum? | No; that depends on the optimization problem and its properties |

## Quick Revision

**INITIALIZE → CALCULATE GRADIENT → UPDATE PARAMETERS → CHECK CONVERGENCE → REPEAT**

$$
\theta_j \leftarrow
\theta_j-\alpha\frac{\partial J(\theta)}{\partial\theta_j}
$$

- `θⱼ`: Parameter being updated
- `J(θ)`: Cost function
- `∂J/∂θⱼ`: Derivative with respect to the parameter
- `α`: Learning rate
- Convergence: Reaching the stopping condition