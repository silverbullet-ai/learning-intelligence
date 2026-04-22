# Python Basics – Operators

---

## Overview

Operators are symbols used to perform operations on variables and values.

Types covered:

- Arithmetic Operators
- Comparison Operators
- Logical Operators

---

## Arithmetic Operators

Used for mathematical operations.

```python
a = 10
b = 5
```

### Addition
```python
a + b  # 15
```

### Subtraction
```python
a - b  # 5
```

### Multiplication
```python
a * b  # 50
```

### Division
```python
a / b  # 2.0
```

👉 Always returns float

### Floor Division
```python
a // b  # 2
```

👉 Removes decimal part

### Modulus
```python
a % b  # 0
```

👉 Remainder

### Exponentiation
```python
a ** b  # 100000
```

---

## Key Difference

```python
21 / 5   # 4.2
21 // 5  # 4
```

---

## Comparison Operators

Always return boolean values.

```python
a = 10
b = 10

a == b   # True
a != b   # False
a > b    # False
a < b    # False
a >= b   # True
a <= b   # True
```

### Case Sensitivity

```python
"Aahish" == "aahish"  # False
```

---

## Logical Operators

Used with boolean values.

### AND
```python
True and True   # True
True and False  # False
```

### OR
```python
True or False   # True
False or False  # False
```

### NOT
```python
not True   # False
not False  # True
```

---

## Truth Table

| A | B | A and B | A or B |
|---|---|--------|--------|
| T | T | T      | T      |
| T | F | F      | T      |
| F | T | F      | T      |
| F | F | F      | F      |

---

## Quick Revision

- Arithmetic → math operations  
- Comparison → boolean results  
- Logical → combine conditions  
- / → float  
- // → integer result  
- % → remainder  
- ** → power  
