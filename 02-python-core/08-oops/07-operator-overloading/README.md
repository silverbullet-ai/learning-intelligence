# Python OOPs — Operator Overloading

---

# What is Operator Overloading?

Operator Overloading means:

> Changing the default behavior of operators for user-defined objects.

Python allows us to redefine how operators work for our classes using magic methods (dunder methods).

---

# Why Do We Need Operator Overloading?

Normally operators work on built-in data types.

Example:

```python
print(5 + 3)
```

Output:

```python
8
```

---

```python
print(10 - 4)
```

Output:

```python
6
```

---

But what if we create our own class?

```python
class Vector:
    pass
```

and write:

```python
v1 + v2
```

Python doesn't know how to add two vectors.

We must define that behavior ourselves.

This is called:

> Operator Overloading

---

# Magic Methods Behind Operators

Python internally maps operators to magic methods.

| Operator | Magic Method      |
| -------- | ----------------- |
| +        | `__add__()`     |
| -        | `__sub__()`     |
| *        | `__mul__()`     |
| /        | `__truediv__()` |
| ==       | `__eq__()`      |
| <        | `__lt__()`      |
| >        | `__gt__()`      |
| <=       | `__le__()`      |
| >=       | `__ge__()`      |

---

## Example

When you write:

```python
a + b
```

Python executes:

```python
a.__add__(b)
```

---

Similarly:

```python
a - b
```

becomes:

```python
a.__sub__(b)
```

---

```python
a == b
```

becomes:

```python
a.__eq__(b)
```

---

# Vector Example

## Step 1: Create Class

```python
class Vector:

    def __init__(self, x, y):

        self.x = x
        self.y = y
```

---

## Create Objects

```python
v1 = Vector(2, 3)

v2 = Vector(4, 5)
```

---

# Overloading + Operator

```python
def __add__(self, other):

    return Vector(
        self.x + other.x,
        self.y + other.y
    )
```

---

### Understanding

Suppose:

```python
v1 = (2,3)

v2 = (4,5)
```

When:

```python
v1 + v2
```

Python executes:

```python
v1.__add__(v2)
```

Internally:

```python
(2 + 4, 3 + 5)
```

Result:

```python
(6,8)
```

---

# Overloading - Operator

```python
def __sub__(self, other):

    return Vector(
        self.x - other.x,
        self.y - other.y
    )
```

---

Example:

```python
v1 - v2
```

Result:

```python
(-2, -2)
```

---

# Overloading * Operator

```python
def __mul__(self, scalar):

    return Vector(
        self.x * scalar,
        self.y * scalar
    )
```

---

Example:

```python
v1 * 3
```

Result:

```python
(6, 9)
```

---

# Overloading == Operator

```python
def __eq__(self, other):

    return (
        self.x == other.x
        and
        self.y == other.y
    )
```

---

Example:

```python
v1 == v2
```

Output:

```python
True
```

---

Without `__eq__()`:

Python compares memory addresses instead of values.

---

# String Representation

To display vectors nicely:

```python
def __repr__(self):

    return f"Vector({self.x}, {self.y})"
```

---

Example:

```python
print(v1)
```

Output:

```python
Vector(2, 3)
```

---

# Complete Vector Example

```python
class Vector:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def __add__(self, other):

        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):

        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, scalar):

        return Vector(
            self.x * scalar,
            self.y * scalar
        )

    def __eq__(self, other):

        return (
            self.x == other.x
            and
            self.y == other.y
        )

    def __repr__(self):

        return f"Vector({self.x}, {self.y})"
```

---

## Usage

```python
v1 = Vector(2, 3)

v2 = Vector(4, 5)

print(v1 + v2)

print(v1 - v2)

print(v1 * 3)

print(v1 == v2)
```

Output:

```python
Vector(6, 8)

Vector(-2, -2)

Vector(6, 9)

False
```

---

# How Python Actually Works

When you write:

```python
v1 + v2
```

Python converts it to:

```python
v1.__add__(v2)
```

---

When you write:

```python
v1 - v2
```

Python converts it to:

```python
v1.__sub__(v2)
```

---

When you write:

```python
v1 == v2
```

Python converts it to:

```python
v1.__eq__(v2)
```

---

# Real-World Example

Imagine a game or AI simulation.

```python
agent1 = Position(10, 20)

agent2 = Position(5, 7)
```

Instead of writing:

```python
Position(
    agent1.x + agent2.x,
    agent1.y + agent2.y
)
```

You can simply write:

```python
agent1 + agent2
```

Much cleaner and easier to read.

---

# Common Operator Overloading Methods

| Magic Method       | Operator |
| ------------------ | -------- |
| `__add__()`      | +        |
| `__sub__()`      | -        |
| `__mul__()`      | *        |
| `__truediv__()`  | /        |
| `__floordiv__()` | //       |
| `__mod__()`      | %        |
| `__pow__()`      | **       |
| `__eq__()`       | ==       |
| `__ne__()`       | !=       |
| `__lt__()`       | <        |
| `__gt__()`       | >        |
| `__le__()`       | <=       |
| `__ge__()`       | >=       |

---

# Advantages of Operator Overloading

- Cleaner code
- More readable code
- Better object behavior
- Easier mathematical modeling
- Supports domain-specific design

---

# Interview Questions

### What is Operator Overloading?

Operator overloading is the ability to redefine the behavior of operators for user-defined objects using magic methods.

---

### What method handles + ?

```python
__add__()
```

---

### What happens internally when we write?

```python
obj1 + obj2
```

Python executes:

```python
obj1.__add__(obj2)
```

---

### Why is Operator Overloading useful?

- Cleaner code
- Better readability
- Mathematical modeling
- Custom object behavior

---

# Practice Assignments

### 1. Point Class

Overload:

```python
+
```

Example:

```python
Point(2,3) + Point(4,5)
```

Output:

```python
Point(6,8)
```

---

### 2. BankAccount

Overload:

```python
+
```

Combine balances.

---

### 3. Book

Overload:

```python
==
```

Books are equal when:

- title matches
- author matches

---

### 4. Student

Overload:

```python
>
```

Compare marks.

---

### 5. Car

Overload:

```python
>
```

Compare horsepower.

Example:

```python
revuelto > huracan
```

returns:

```python
True
```

---

# Quick Revision

| Concept              | Meaning                |
| -------------------- | ---------------------- |
| Operator Overloading | Redefining operators   |
| `__add__()`        | +                      |
| `__sub__()`        | -                      |
| `__mul__()`        | *                      |
| `__eq__()`         | ==                     |
| `__gt__()`         | >                      |
| `__lt__()`         | <                      |
| Purpose              | Custom object behavior |

---

# One-Line Summary

> Operator overloading in Python allows us to redefine the behavior of operators such as `+`, `-`, `*`, `==`, `>`, and others for user-defined objects using magic methods (dunder methods).
>
