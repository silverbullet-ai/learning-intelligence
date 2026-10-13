# Distance of a Point from a Plane

*Mathematical Foundations for Logistic Regression and Support Vector Machines (SVM)*

The distance of a point from a plane helps describe how far a point is from a decision boundary and which side of that boundary it lies on. This concept is useful when studying classification algorithms such as Logistic Regression and Support Vector Machines (SVM).

## 1. Equation of a Plane

A plane that passes through the origin can be written as:

$$
\mathbf{W}^{T}\mathbf{X}=0
$$

Where:

- $\mathbf{W}$ is the weight vector and the normal vector to the plane.
- $\mathbf{X}$ is a point/vector.
- $\mathbf{W}^{T}\mathbf{X}$ represents the dot product.

The normal vector $\mathbf{W}$ is perpendicular to the plane.

For a general plane that does not necessarily pass through the origin, include a bias/intercept term:

$$
\mathbf{W}^{T}\mathbf{X}+b=0
$$

## 2. A Point in n-Dimensional Space

Let the point whose distance we want to calculate be:

$$
\mathbf{S}=(X_1,X_2,\ldots,X_n)
$$

The shortest path from a point to a plane is perpendicular to the plane. Therefore, the normal vector $\mathbf{W}$ gives the direction used to measure the distance.

## 3. Signed Distance Formula

For a plane through the origin, the signed distance of $\mathbf{S}$ from the plane is:

$$
d_{\text{signed}}=\frac{\mathbf{W}^{T}\mathbf{S}}{\|\mathbf{W}\|}
$$

For a general plane $\mathbf{W}^{T}\mathbf{X}+b=0$, the formula becomes:

$$
d_{\text{signed}}=\frac{\mathbf{W}^{T}\mathbf{S}+b}{\|\mathbf{W}\|}
$$

Here, $\|\mathbf{W}\|$ is the Euclidean norm (magnitude) of the normal vector:

$$
\|\mathbf{W}\|=\sqrt{w_1^2+w_2^2+\cdots+w_n^2}
$$

> **Important:** The sign tells us which side of the plane the point lies on, relative to the orientation of $\mathbf{W}$. The absolute value gives the ordinary, non-negative geometric distance.

## 4. Why Does the Formula Use a Dot Product?

The dot product can be expressed as:

$$
\mathbf{W}^{T}\mathbf{S}=\|\mathbf{W}\|\,\|\mathbf{S}\|\cos\theta
$$

Where $\theta$ is the angle between $\mathbf{W}$ and $\mathbf{S}$.

Dividing by $\|\mathbf{W}\|$ gives:

$$
\frac{\mathbf{W}^{T}\mathbf{S}}{\|\mathbf{W}\|}=\|\mathbf{S}\|\cos\theta
$$

This is the signed component of $\mathbf{S}$ along the unit normal direction. For a plane not passing through the origin, the bias term $b$ must also be included.

## 5. Interpreting the Sign

For a plane through the origin:

- $d_{\text{signed}}>0$: The point is on the side toward which $\mathbf{W}$ points.
- $d_{\text{signed}}<0$: The point is on the opposite side.
- $d_{\text{signed}}=0$: The point lies on the plane.

A negative signed distance does **not** mean that physical distance is negative. It records direction/side relative to the plane.

## 6. Signed Distance vs. Actual Distance

**Signed distance:**

$$
d_{\text{signed}}=\frac{\mathbf{W}^{T}\mathbf{S}+b}{\|\mathbf{W}\|}
$$

**Actual geometric distance:**

$$
d_{\text{actual}}=\left|\frac{\mathbf{W}^{T}\mathbf{S}+b}{\|\mathbf{W}\|}\right|
$$

The absolute value removes the sign, leaving only how far the point is from the plane.

## 7. Connection to Classification

A classifier can use a decision boundary to separate regions associated with different classes. The sign of the decision function

$$
f(\mathbf{S})=\mathbf{W}^{T}\mathbf{S}+b
$$

indicates the side of the boundary on which the point lies.

Dividing by $\|\mathbf{W}\|$ converts this value into signed geometric distance:

$$
d_{\text{signed}}=\frac{f(\mathbf{S})}{\|\mathbf{W}\|}
$$

This geometric view is especially useful for understanding the margin and support vectors in SVM. Logistic Regression also uses a linear decision boundary, although its prediction is based on a probability obtained from the decision score.

## 8. Quick Revision

| Concept | Formula / Meaning |
|---|---|
| Plane through origin | $\mathbf{W}^{T}\mathbf{X}=0$ |
| General plane | $\mathbf{W}^{T}\mathbf{X}+b=0$ |
| Normal vector | $\mathbf{W}$, perpendicular to the plane |
| Dot product | $\mathbf{W}^{T}\mathbf{S}$ |
| Normal vector magnitude | $\sqrt{w_1^2+w_2^2+\cdots+w_n^2}$ |
| Signed distance, origin plane | $\frac{\mathbf{W}^{T}\mathbf{S}}{\|\mathbf{W}\|}$ |
| Signed distance, general plane | $\frac{\mathbf{W}^{T}\mathbf{S}+b}{\|\mathbf{W}\|}$ |
| Actual distance | Absolute value of the signed distance |
| Positive signed distance | Side toward which $\mathbf{W}$ points |
| Negative signed distance | Opposite side |
| Zero signed distance | Point lies on the plane |

## 9. Exam and Interview Questions

**Q1. What is the signed distance of a point $\mathbf{S}$ from a plane through the origin?**

$$
d_{\text{signed}}=\frac{\mathbf{W}^{T}\mathbf{S}}{\|\mathbf{W}\|}
$$

**Q2. What does $\mathbf{W}$ represent?**

It is the normal vector to the plane and is perpendicular to it.

**Q3. What does a positive signed distance mean?**

The point is on the side toward which the oriented normal vector points.

**Q4. What does a negative signed distance mean?**

The point is on the opposite side of the plane.

**Q5. What does zero signed distance mean?**

The point lies on the plane.

**Q6. How do we calculate ordinary geometric distance?**

Take the absolute value of the signed distance:

$$
d_{\text{actual}}=|d_{\text{signed}}|
$$

**Q7. What changes when the plane does not pass through the origin?**

Include the bias term $b$:

$$
d_{\text{signed}}=\frac{\mathbf{W}^{T}\mathbf{S}+b}{\|\mathbf{W}\|}
$$

## Mental Model

**Plane → Normal vector $\mathbf{W}$ → Dot product plus bias → Divide by $\|\mathbf{W}\|$ → Signed distance**

The normal vector gives the perpendicular direction. The signed distance tells us how far a point lies from the plane and on which side it is located.