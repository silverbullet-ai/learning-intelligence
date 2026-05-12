# Lambda Functions in Python

---

## Overview

Lambda functions are:
- small anonymous functions
- one-line functions
- used for short operations

They are commonly used in:
- mapping
- filtering
- sorting
- functional programming

---

## What is a Lambda Function?

A lambda function:
- uses the `lambda` keyword
- can take multiple arguments
- contains only ONE expression

---

## Basic Syntax

```python
lambda arguments: expression
```

---

## Example

```python
lambda x: x * 2
```

Meaning:

- argument → x
- expression → x * 2

---

## Normal Function vs Lambda

### Normal Function

```python
def square(x):
    return x * x
```

### Lambda Equivalent

```python
lambda x: x * x
```

---

## Why Use Lambda Functions?

Lambda functions are useful when:

- logic is small
- full function definition feels unnecessary
- temporary operations are needed

---

## Converting Normal Function → Lambda

### Normal Function

```python
def add(a, b):
    return a + b
```

### Lambda Version

```python
addition = lambda a, b: a + b
```

### Calling

```python
addition(5, 6)
```

### Output

```python
11
```

---

## Important Understanding

The variable:

```python
addition
```

stores the lambda function.

---

## Lambda Example — Even Number

### Normal Function

```python
def even(num):
    return num % 2 == 0
```

### Lambda Version

```python
even_check = lambda num: num % 2 == 0
```

### Example

```python
even_check(12)
```

### Output

```python
True
```

---

## Important Concept

Lambda expressions directly return values.

No need for:

- return
- def

---

## Lambda with Multiple Arguments

```python
addition = lambda x, y, z: x + y + z
```

### Calling

```python
addition(12, 13, 14)
```

### Output

```python
39
```

---

## ⚠️ Important Rule

Lambda supports:

- multiple arguments

BUT:

- only ONE expression

---

## Lambda + map() Function

One of the most important use cases.

---

## Important Concepts to Remember

- Lambda = anonymous one-line function
- Lambda supports multiple arguments
- Lambda only allows ONE expression

---

## Common Functions Used with Lambda

- map()
- filter()
- sorted()
- reduce()

---

## Common Errors

### Multiple Statements Inside Lambda

```python
lambda x:
    y = x + 1
```

Not allowed.

---

## 🧪 Practice Assignments

- Cube numbers using lambda
- Convert strings to uppercase
- Find length of each word
- Even/Odd checker using lambda

---

## 🧭 Best Practices

- Use lambda for short operations only
- Prefer normal functions for complex logic
- Keep expressions readable
- Combine lambda with functional tools carefully

---

## Real-World Insight

Lambda functions are heavily used in:

- preprocessing pipelines
- transformations
- sorting systems
- data manipulation

Especially in:

- Pandas
- NumPy
- machine learning workflows

