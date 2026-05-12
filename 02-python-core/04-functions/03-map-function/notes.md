# map() Function in Python

---

## Overview

The `map()` function is used to:

- apply a function to every item in an iterable
- transform data efficiently
- avoid manual looping

It works with:
- lists
- tuples
- sets
- other iterables

---

## What is map()?

`map()`:
- takes a function
- applies it to every element
- returns a map object (iterator)

---

## Syntax

```python
map(function, iterable)
```

---

## Parameters

| Parameter | Meaning |
|------------|----------|
| function | operation to apply |
| iterable | list/tuple/set/etc |

---

## Return Type

map() returns:

```python
<map object>
```

which is:

- an iterator
- lazily evaluated

Usually converted using:

```python
list(map(...))
```

---

## Basic Example — Squaring Numbers

### Normal Function

```python
def square(x):
    return x * x
```

### List

```python
numbers = [1, 2, 3, 4, 5]
```

### Using map()

```python
list(map(square, numbers))
```

### Output

```python
[1, 4, 9, 16, 25]
```

---

## Important Understanding

Internally:

```python
square(1)
square(2)
square(3)
```

is happening automatically.

No need for:

- loops
- append
- temporary lists

---

## Why Use map()?

### Without map()

```python
result = []

for x in numbers:
    result.append(square(x))
```

### With map()

```python
list(map(square, numbers))
```

Cleaner and more readable.

---

## map() with Lambda

MOST COMMON USE CASE.

```python
numbers = [1, 2, 3, 4, 5]

list(map(lambda x: x * x, numbers))
```

### Output

```python
[1, 4, 9, 16, 25]
```

---

## Breakdown

### Lambda Function

```python
lambda x: x * x
```

means:

- input → x
- operation → x²

---

## Important Understanding

This combines:

- anonymous functions
- iteration
- transformation

into one line.

---

## Mapping Multiple Iterables

VERY IMPORTANT.

### Example

```python
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
```

### Goal

Add corresponding elements.

### Code

```python
list(
    map(
        lambda x, y: x + y,
        numbers1,
        numbers2
    )
)
```

### Output

```python
[5, 7, 9]
```

---

## Internal Working

```python
1 + 4
2 + 5
3 + 6
```

---

## Important Concept

map() can take:

- multiple iterables

IF:

- function accepts multiple arguments

---

## Type Conversion with map()

### Example

Convert string numbers → integers

```python
string_numbers = ["1", "2", "3"]
```

### Code

```python
list(map(int, string_numbers))
```

### Output

```python
[1, 2, 3]
```

---

## Important Understanding

Here:

```python
int
```

is passed as a function.

---

## Using Built-in Functions with map()

### Convert to Uppercase

```python
words = ["apple", "banana", "cherry"]
```

### Code

```python
list(map(str.upper, words))
```

### Output

```python
["APPLE", "BANANA", "CHERRY"]
```

---

## Important Concept

You can directly pass:

- functions
- methods

inside map().

---

## map() with Dictionary Data

Very practical example.

### Data

```python
people = [
    {"name": "Aahish", "age": 23},
    {"name": "Manav", "age": 22}
]
```

### Function

```python
def get_name(person):
    return person["name"]
```

### Using map()

```python
list(map(get_name, people))
```

### Output

```python
["Aahish", "Manav"]
```

---

## Real Industry Connection

Used heavily in:

- APIs
- JSON processing
- backend systems
- AI preprocessing
- databases

---

## Important Concept — Iterators

A map object is an iterator.

Meaning:

- values are generated one by one
- memory efficient
- lazy evaluation

---

## Why list(map(...)) is Common

Because:

```python
map(...)
```

alone returns iterator object.

To fully realize values:

```python
list(map(...))
```

---

## Real Use Cases

| Area | Usage |
|------|--------|
| Data Science | preprocessing |
| AI | transformations |
| APIs | response processing |
| Backend | formatting |
| NLP | token processing |
| Pandas | vectorized operations |

---

## Important Concepts to Remember

- map() applies function to every element
- map() returns iterator
- list(map(...)) converts iterator to list
- map() works extremely well with lambda
- map() supports multiple iterables

---

## Traditional Loop vs map()

| Traditional Loop | map() |
|------------------|--------|
| explicit iteration | automatic iteration |
| append required | no append |
| more lines | concise |
| manual transformation | built-in transformation |

---

## Hidden Intermediate Concepts

This lecture quietly introduces:

- iterators
- lazy evaluation
- functional programming
- transformation pipelines
- higher-order functions

---

## Practice Assignments

- Double every number
- Convert strings → float
- Get length of words
- Add two lists
- Extract ages from dictionary list

---

## Best Practices

- Use map() for transformation logic
- Prefer readability over over-optimization
- Combine with lambda carefully
- Convert iterator when needed
