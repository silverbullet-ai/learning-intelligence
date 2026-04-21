# Python Basics – Data Types

---

## Overview

Data types define:

- What kind of data a variable holds
- What operations can be performed
- How memory is allocated

👉 They tell Python how to store and use data.

---

## Importance of Data Types

- Ensure efficient memory usage
- Enable correct operations
- Help prevent errors and bugs

---

## Basic Data Types

### Integer (`int`)

```python
age = 23
print(type(age))  # int
```

👉 Whole numbers (positive or negative)

---

### Float (`float`)

```python
height = 5.5
print(type(height))  # float
```

👉 Decimal numbers

---

### String (`str`)

```python
name = "Aahish"
print(type(name))  # str
```

👉 Text data

---

### Boolean (`bool`)

```python
is_student = True
print(type(is_student))  # bool
```

👉 Only two values:

- True
- False

---

## Boolean from Expressions

```python
a = 10
b = 10

print(a == b)         # True
print(type(a == b))   # bool
```

---

## Type Conversion (Casting)

### Error Example

```python
result = "Hello"
result = result + 5  # ERROR
```

👉 Cannot combine string and integer

---

### Fix Using Casting

```python
result = "Hello"
result = result + str(5)

print(result)  # Hello5
```

---

## Key Insight

Operations depend on data types:

```python
"Hello" + "World"   # CORRECT
"Hello" + 5 	    # WRONG
```

---

## Dynamic Typing

```python
x = 10       # int
x = "Hello"  # str
```

👉 Same variable, different types over time.

---

## Common Errors

### Type Error

```python
"Hello" + 5
```

👉 Fix:

```python
"Hello" + str(5)
```

---

### Wrong Operations

- Mixing incompatible types
- Not converting input properly

---

## Built-in Methods (Intro)

```python
text = "hello"
print(text.upper())  # HELLO
```

👉 Strings have many methods:

- .upper()
- .lower()
- .count()

(More later)

---

## Quick Revision

- Data types define kind of data
- Basic types: int, float, str, bool
- Use type() to check
- Use casting (int(), str())
- Python is dynamically typed
