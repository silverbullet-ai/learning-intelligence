# filter() Function in Python

---

## Overview

The `filter()` function is used to:

- select only elements that satisfy a condition
- filter data from iterables
- avoid manual conditional loops

It works with:
- lists
- tuples
- sets
- dictionaries
- other iterables

---

## What is filter()?

`filter()`:
- constructs an iterator
- keeps only elements where the function returns `True`

---

## Syntax

```python
filter(function, iterable)
```

---

## Parameters

| Parameter | Meaning |
|------------|----------|
| function | condition function |
| iterable | collection to filter |

---

## Return Type

Returns:

```python
<filter object>
```

which is:

- an iterator
- lazily evaluated

Usually converted using:

```python
list(filter(...))
```

---

## Basic Example — Filter Even Numbers

### Step 1: Create Function

```python
def even(num):

    if num % 2 == 0:
        return True
```

### Step 2: Create List

```python
numbers = [1,2,3,4,5,6,7,8,9,10]
```

### Step 3: Apply Filter

```python
list(filter(even, numbers))
```

### Output

```python
[2,4,6,8,10]
```

---

## Internal Working

Internally:

```python
even(1) → False
even(2) → True
even(3) → False
```

Only True values survive.

---

## Important Mental Model

Think of filter() as:

> “Keep only matching elements.”

---

## Why Use filter()?

### Without filter()

```python
result = []

for x in numbers:

    if x % 2 == 0:
        result.append(x)
```

### With filter()

```python
list(filter(even, numbers))
```

Cleaner and more concise.

---

## filter() with Lambda

MOST COMMON USE CASE.

### Example — Numbers Greater Than 5

```python
numbers = [1,2,3,4,5,6,7,8,9]
```

### Code

```python
list(
    filter(
        lambda x: x > 5,
        numbers
    )
)
```

### Output

```python
[6,7,8,9]
```

---

## Breakdown

```python
lambda x: x > 5
```

means:

- input → x
- keep only if x > 5

---

## Multiple Conditions with filter()

VERY IMPORTANT.

### Goal

Keep numbers:

- greater than 5
- AND even

### Code

```python
list(
    filter(
        lambda x: x > 5 and x % 2 == 0,
        numbers
    )
)
```

### Output

```python
[6,8]
```

---

## Important Concept

You can combine:

- and
- or
- not

inside filter conditions.

---

## filter() with Dictionary Data

Very practical use case.

### Data

```python
people = [
    {"name": "Aahish", "age": 23},
    {"name": "Manav", "age": 22},
    {"name": "Raj", "age": 20}
]
```

### Function

```python
def age_greater_than_20(person):
    return person["age"] > 20
```

### Applying Filter

```python
list(filter(age_greater_than_20, people))
```

### Output

```python
[
    {"name":"Aahish","age":23},
    {"name":"Manav","age":22}
]
```

---

## Real Industry Usage

Used heavily in:

- APIs
- backend filtering
- database processing
- JSON processing
- data cleaning
- ML preprocessing

---

## Important Understanding — Boolean Logic

filter() depends completely on:

- True
- False

If function returns:

- True → keep item
- False → discard item

---

## ⚔️ Difference Between map() and filter()

| map() | filter() |
|--------|-----------|
| transforms data | filters data |
| changes values | keeps/removes values |
| applies operation | applies condition |
| output size usually same | output size may shrink |

---

## Example Comparison

### map()

```python
list(map(lambda x: x*x, [1,2,3]))
```

### Output

```python
[1,4,9]
```

---

### filter()

```python
list(filter(lambda x: x%2==0, [1,2,3]))
```

### Output

```python
[2]
```

---

## Hidden Advanced Concepts

This lecture quietly introduces:

- functional programming
- iterators
- lazy evaluation
- predicate functions
- boolean filtering
- higher-order functions

---

## Real-World Use Cases

| Use Case | Example |
|-----------|----------|
| Data Cleaning | remove invalid records |
| AI/ML | filter datasets |
| APIs | remove unwanted responses |
| Backend | active users only |
| Ecommerce | filter products |
| Security | request validation |

---

## Important Concepts to Remember

- filter() keeps matching elements
- function must return True or False
- returns iterator
- usually wrapped using list()
- works extremely well with lambda
- supports complex conditions

---

## Golden Rule

```python
map()    → transforms data
filter() → selects data
```

---

## Practice Assignments

- Filter odd numbers
- Filter names starting with "A"
- Filter numbers divisible by 3
- Filter positive numbers
- Filter students with marks > 80

---

## Best Practices

- Use filter() for condition-based selection
- Prefer readability over complex lambda chains
- Use named functions for complex filtering
- Combine with map() carefully

---

## Real-World Insight

Modern data pipelines often follow:

```python
raw_data
→ filter()
→ map()
→ transformation
→ output
```

This is extremely common in:

- AI pipelines
- backend systems
- analytics workflows
