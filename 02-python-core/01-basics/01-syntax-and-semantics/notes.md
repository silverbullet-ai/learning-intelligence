# Python Basics – Syntax & Semantics

---

## Overview

This lecture introduces two fundamental concepts:

- **Syntax** → How code is written
- **Semantics** → What the code means / does

👉 Both are essential for writing correct and meaningful programs.

---

## Syntax

### Definition

Syntax refers to the rules that define the structure of Python code.

- Arrangement of keywords, variables, symbols
- Violations lead to **SyntaxError**

---

## Semantics

### Definition

Semantics refers to the meaning or behavior of the code.

👉 Even if syntax is correct, semantics can still be wrong.

---

## Comments in Python

### Single-line Comment

```python
# This is a comment
```

### Multi-line Comment

```python
"""
This is a
multi-line comment
"""
```

### Purpose

- Explain code
- Improve readability
- Add documentation

---

## Basic Syntax Rules

### 1. Case Sensitivity

```python
name = "Aahish"
Name = "Aayan"
```

👉 These are different variables.

---

### 2. Indentation (VERY IMPORTANT)

Python uses indentation instead of `{}`

```python
age = 23

if age > 20:
    print(age)
```

Incorrect:

```python
if age > 20:
print(age)
```

👉 Causes: **IndentationError**

---

### 3. Line Continuation

```python
total = 1 + 2 + 3 + \
        4 + 5 + 6
```

---

### 4. Multiple Statements in One Line

```python
x = 5; y = 10; z = x + y
```

👉 Works, but not recommended.

---

## Semantics in Python

### Variable Assignment

```python
age = 23
name = "Aahish"
```

---

### Type Checking

```python
type(age)   # int
type(name)  # str
```

---

### Dynamic Typing

```python
var = 10
print(type(var))   # int

var = "Aahish"
print(type(var))   # str
```

👉 Same variable → different types.

---

## Common Errors

### 1. Indentation Error

```python
if age > 20:
print(age)
```

---

### 2. Name Error

```python
a = b
```

👉 Error:

```
NameError: name 'b' is not defined
```

---

## Example – Indentation Flow

```python
if True:
    print("Correct indentation")

    if False:
        print("Won’t print")

    print("This will print")

print("Outside block")
```

### Output:

```
Correct indentation
This will print
Outside block
```

---

## Quick Revision

- Syntax → structure of code
- Semantics → meaning of code
- Python is case-sensitive
- Indentation defines code blocks
- Supports comments, line continuation, dynamic typing

---

## Real-World Insight

Syntax errors are easy to fix.

Semantic errors are dangerous because:

- Code runs
- But produces wrong results

👉 This is where real debugging begins.

---

## Final Thought

This is not basic.

This is:

The grammar of Python

Strong grammar → clean code → faster debugging → better systems
