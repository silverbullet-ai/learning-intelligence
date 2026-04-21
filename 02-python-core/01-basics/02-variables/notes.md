# Python Basics – Variables

---

## Overview

A variable is a container used to store data that can be:

- Referenced
- Modified
- Used in computations

👉 In Python, variables are created automatically when a value is assigned.

---

## Declaring & Assigning Variables

```python
a = 100
age = 23
height = 5.5
name = "Aahish"
is_student = True
```

👉 No need to declare types explicitly.

---

## Printing Variables

```python
print("Age:", age)
print("Height:", height)
print("Name:", name)
```

---

## Naming Conventions

### Rules

- Must start with a letter or underscore  
- Can contain letters, numbers, underscores  
- Case-sensitive  

### Valid Names

```python
first_name = "Aahish"
_lastname = "Aayan"
age1 = 23
```

### Invalid Names

```python
1age = 23        # starts with number
first-name = ""  # dash not allowed
@name = "abc"    # special character
```

---

## Case Sensitivity

```python
name = "Aahish"
Name = "Aayan"
```

👉 Different variables.

---

## Variable Types (Dynamic Typing)

Python decides type at runtime.

### Common Types

```python
age = 23           # int
height = 5.5       # float
name = "Aahish"    # str
is_student = True  # bool
```

---

## Type Checking

```python
print(type(age))    # int
print(type(name))   # str
```

---

## Type Conversion (Casting)

### Convert int → string

```python
age = 23
age_str = str(age)
```

### Convert string → int

```python
age = "23"
age_int = int(age)
```

### Invalid Conversion

```python
int("Aahish")  # Error
```

### Float → int

```python
height = 5.11
int(height)  # 5
```

### int → float

```python
float(5)  # 5.0
```

---

## Dynamic Typing

```python
var = 10
print(type(var))

var = "Hello"
print(type(var))

var = 3.14
print(type(var))
```

👉 Same variable, different types.

---

## Input Function

### Taking Input

```python
age = input("Enter your age: ")
```

### Important

```python
type(age)  # always str
```

### Convert Input

```python
age = int(input("Enter your age: "))
```
