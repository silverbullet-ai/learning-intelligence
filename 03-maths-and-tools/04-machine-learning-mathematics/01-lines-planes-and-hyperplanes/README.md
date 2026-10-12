# Equations of Lines, Planes, and Hyperplanes

## Why This Topic Matters

These mathematical concepts form the foundation for understanding Machine Learning algorithms such as Logistic Regression and Support Vector Machines (SVM).

## 1. Equation of a Straight Line

In two-dimensional (2D) space, a straight line can be represented using:

$$
y = mx + c
$$

Another common notation is:

$$
y = \beta_0 + \beta_1x
$$

The general form is:

$$
ax + by + c = 0
$$

These equations represent the same basic geometric object: a straight line.

## 2. Slope and Intercept

For the equation $y = mx + c$:

### Slope — $m$

The slope tells us how much $y$ changes for a unit change in $x$.

$$
m = \frac{\Delta y}{\Delta x}
$$

### Intercept — $c$

The y-intercept tells us where the line crosses the y-axis.

When $x = 0$:

$$
y = m(0) + c = c
$$

**Memory trick:** Slope describes how the line moves; the intercept tells where it crosses the y-axis.

## 3. Equation Using Weights

In Machine Learning, we commonly represent a line or decision boundary using weights and a bias.

For two features:

$$
W_1X_1 + W_2X_2 + b = 0
$$

Where:

- $W_1, W_2$: weights or coefficients
- $X_1, X_2$: input features
- $b$: bias/intercept

In vector notation:

$$
W^T X + b = 0
$$

## 4. Vector Representation and Dot Product

Let:

$$
W =
\begin{bmatrix}
W_1 \\
W_2
\end{bmatrix},
\qquad
X =
\begin{bmatrix}
X_1 \\
X_2
\end{bmatrix}
$$

Then:

$$
W^T X = W_1X_1 + W_2X_2
$$

This is the dot product of the two vectors.

Therefore, the equation becomes:

$$
W^T X + b = 0
$$

## 5. From a Line to a Plane

In three-dimensional (3D) space, the corresponding geometric object is a plane.

Its equation is:

$$
W_1X_1 + W_2X_2 + W_3X_3 + b = 0
$$

In vector notation:

$$
W^T X + b = 0
$$

Here, $W = (W_1,W_2,W_3)$ and $X = (X_1,X_2,X_3)$.

## 6. Hyperplane in n Dimensions

The same concept extends to $n$ dimensions.

$$
W_1X_1 + W_2X_2 + \cdots + W_nX_n + b = 0
$$

Compactly:

$$
W^T X + b = 0
$$

A **hyperplane** is the generalization of a line or plane to higher-dimensional spaces.

## 7. Passing Through the Origin

If a line, plane, or hyperplane passes through the origin, the bias/intercept is zero.

Starting with:

$$
W^T X + b = 0
$$

At the origin, $X = 0$:

$$
W^T(0) + b = 0
$$

Therefore:

$$
b = 0
$$

The equation simplifies to:

$$
W^T X = 0
$$

## 8. Dot Product and Perpendicularity

The dot product can be expressed as:

$$
W^T X = \|W\| \|X\| \cos\theta
$$

Where:

- $\|W\|$: magnitude of vector $W$
- $\|X\|$: magnitude of vector $X$
- $\theta$: angle between the vectors

When $W^T X = 0$, and both vectors are non-zero:

$$
\cos\theta = 0
$$

Therefore:

$$
\theta = 90^\circ
$$

The vectors are perpendicular.

### The Normal Vector

For the hyperplane:

$$
W^T X + b = 0
$$

the vector $W$ is called the **normal vector** because it is perpendicular to the hyperplane.

$$
W \perp \text{hyperplane}
$$

This is an important concept for understanding Logistic Regression and SVM later.

## 9. 2D, 3D, and nD Comparison

| Dimensions | Geometric Object | Equation |
|---|---|---|
| 2D | Straight line | $W_1X_1 + W_2X_2 + b = 0$ |
| 3D | Plane | $W_1X_1 + W_2X_2 + W_3X_3 + b = 0$ |
| nD | Hyperplane | $W^T X + b = 0$ |

## Key Takeaways

1. **Straight line:** $y = mx + c$
2. **ML-friendly form:** $W^T