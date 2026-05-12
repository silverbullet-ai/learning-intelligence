# Functions in Python

---

## Overview

A function is a reusable block of code that performs a specific task.

Functions help in:
- code reuse
- modularity
- organization
- scalability

---

## Why Functions Exist

Without functions:
- repeated code
- messy files
- difficult debugging
- poor readability

With functions:
- reusable logic
- clean structure
- scalable systems

---

## Industry Insight

Large software systems are essentially:

> Thousands of functions working together.

---

## Basic Function Syntax

```python
def function_name(parameters):
    # function body
    return value
```

---

## Example

```python
def greet():
    print("Hello")
```

---

## Important Keywords

| Part | Meaning |
|------|----------|
| def | defines function |
| function name | identifier |
| parameters | inputs |
| function body | logic |
| return | sends output back |

---

## Calling a Function

Defining a function does NOT execute it.

```python
greet()
```

---

## Even/Odd Example

### Without Function

```python
num = 24

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

### With Function

```python
def even_or_odd(num):

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
```

### Calling

```python
even_or_odd(24)
```

---

## Parameter vs Argument

| Term | Meaning |
|------|----------|
| parameter | variable in function definition |
| argument | actual value passed |

### Example

```python
def greet(name):   # parameter
    print(name)

greet("Aahish")    # argument
```

---

## Docstrings

Used for documentation inside functions.

```python
def add(a, b):
    """Adds two numbers"""
```

---

## Why Docstrings Matter

In industry:

- multiple developers work together
- logic becomes complex
- documentation becomes essential

---

## Return Statement (VERY IMPORTANT)

### print()

Only displays output.

```python
def add(a, b):
    print(a + b)
```

---

### return

Actually sends value back.

```python
def add(a, b):
    return a + b
```

---

## Why return is Powerful

```python
result = add(2, 3)
```

Now the value can be reused later.

---

## Industry-Level Understanding

Functions usually RETURN data.

Printing is mostly used for:

- debugging
- testing

---

## Multiple Parameters

```python
def add(a, b):
    return a + b
```

### Calling

```python
add(2, 4)
```

---

## Default Parameters

### Problem

```python
def greet(name):
```

Calling:

```python
greet()
```

Causes error.

---

### Solution

```python
def greet(name="Guest"):
    print(name)
```

Now:

```python
greet()
```

works.

---

## Important Rule

Default values make parameters optional.

---

## Positional Arguments (*args)

Used when number of arguments is unknown.

### Example

```python
def print_numbers(*args):

    for num in args:
        print(num)
```

### Calling

```python
print_numbers(1, 2, 3, 4, 5)
```

---

## Internal Understanding

args becomes a tuple.

```python
args = (1, 2, 3, 4, 5)
```

---

## Important Note

args is convention.

This also works:

```python
def func(*aahish):
```

But conventions matter in industry.

---

## Keyword Arguments (**kwargs)

Used for key-value arguments.

### Example

```python
def details(**kwargs):

    for key, value in kwargs.items():
        print(key, value)
```

### Calling

```python
details(
    name="Aahish",
    age=23,
    country="India"
)
```

---

## 🧠 Internal Understanding

kwargs becomes a dictionary.

```python
kwargs = {
    "name": "Aahish",
    "age": 23,
    "country": "India"
}
```

---

## *args vs **kwargs

| Type | Structure |
|------|------------|
| *args | tuple |
| **kwargs | dictionary |

---

## Combining Both

```python
def func(*args, **kwargs):
```

---

## ⚠️ Important Rule

Positional arguments must come first.

Correct:

```python
func(1, 2, name="Aahish")
```

Wrong:

```python
func(name="Aahish", 1, 2)
```

---

## Multiple Return Values

Python supports multiple returns.

```python
def multiply(a, b):

    return a, b, a * b
```

### Calling

```python
x, y, result = multiply(2, 3)
```

---

## Internal Truth

Python actually returns a tuple.

```python
(2, 3, 6)
```

---

## Most Important Concepts

- Functions improve reuse and modularity
- return is more important than print
- *args handles unlimited positional arguments
- **kwargs handles unlimited keyword arguments
- Functions are fundamental for scalable systems

---

## Real Industry Examples

| Area | Functions Used For |
|------|--------------------|
| AI | preprocessing, training |
| Web Dev | API endpoints |
| Games | player movement |
| Banking | transactions |
| ML | model pipelines |

---

## Practice Assignments

- Calculator functions
- Student report generator
- Dynamic sum function using *args
- User profile using **kwargs
- Even/Odd checker returning values

---

## Best Practices

- Keep functions focused on one task
- Prefer return over unnecessary printing
- Use meaningful function names
- Add docstrings for important logic
- Avoid extremely large functions

