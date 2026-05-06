# Python Data Structures – Tuples

---

## Overview

A tuple is an ordered and immutable collection of items.

### Key Properties

- Ordered
- Indexed
- Supports mixed data types
- Immutable (cannot be modified after creation)

---

## Creating Tuples

### Empty Tuple

```python
empty_tuple = ()

empty_tuple = tuple()
```

---

### Tuple with Elements

```python
numbers = (1, 2, 3, 4, 5)
mixed = (1, "Aahish", 3.14, True)
```

---

### Using `tuple()` Function

```python
numbers = tuple([1, 2, 3, 4])
```

👉 Converts list into tuple.

---

## Type Conversion

### List → Tuple

```python
my_list = [1, 2, 3]

my_tuple = tuple(my_list)
```

---

### Tuple → List

```python
my_tuple = (1, 2, 3)

my_list = list(my_tuple)
```

---

## Accessing Tuple Elements

### Indexing

```python
numbers[0]
numbers[2]
```

---

### Negative Indexing

```python
numbers[-1]
```

---

## Slicing

```python
numbers[0:4]
numbers[::2]
numbers[::-1]
```

👉 Same slicing behavior as lists.

---

## Tuple Operations

### Concatenation

```python
t1 = (1, 2)
t2 = (3, 4)

result = t1 + t2
```
### Output

```python
(1, 2, 3, 4)
```

---

### Repetition

```python
nums = (1, 2)

print(nums * 3)
```

### Output

```python
(1, 2, 1, 2, 1, 2)
```

---

## Immutable Nature of Tuples

### Lists are Mutable

```python
my_list = [1, 2, 3]

my_list[0] = 100
```

---

### Tuples are Immutable

```python
my_tuple = (1, 2, 3)

my_tuple[0] = 100
```

### Error

```python
TypeError: 'tuple' object does not support item assignment
```

---

## Why Immutability Matters

Tuples:

- Prevent accidental modification
- Are memory efficient
- Are faster than lists
- Can be used as dictionary keys

---

## Important Tuple Methods

### count()

```python
nums = (1, 2, 2, 3)

nums.count(2)
```

---

### index()

```python
nums.index(3)
```

---

## Packing and Unpacking

### Tuple Packing

```python
packed = (1, "hello", 3.14)
```

Or:

```python
packed = 1, "hello", 3.14
```

Python automatically packs values into a tuple.

---

### Tuple Unpacking

```python
a, b, c = packed
```

Result:

```python
a = 1
b = "hello"
c = 3.14
```

---

## Unpacking with `*`

```python
nums = (1, 2, 3, 4, 5, 6)

first, *middle, last = nums
```

### Result

```python
first = 1
middle = [2, 3, 4, 5]
last = 6
```

---

## Nested Tuples

```python
nested = (
    (1, 2, 3),
    ("A", "B", "C"),
    (True, False)
)
```

---

### Access Nested Elements

```python
nested[1][2]
```

### Output

```python
'C'
```

---

## Iterating Nested Tuples

```python
for sub_tuple in nested:
    for item in sub_tuple:
        print(item)
```

---

## Real-World Usage

### Function Returns

```python
def get_user():
    return ("Aahish", 23)
```

---

### Multiple Function Returns

```python
def calculate(a, b):
    return a + b, a - b

sum_result, diff_result = calculate(10, 5)
```

---

### Coordinates

```python
point = (10, 20)
```

---

### Dictionary Keys

```python
locations = {
    (10, 20): "Home"
}
```

👉 Lists cannot be dictionary keys because they are mutable.

---

## Tuple vs List

| Feature        | List | Tuple |
| -------------- | ---- | ----- |
| Mutable        | ✅    | ❌     |
| Syntax         | `[]` | `()`  |
| Faster         | ❌    | ✅     |
| Dictionary Key | ❌    | ✅     |
| Methods        | Many | Few   |

---

## Performance Insight

Tuples are generally faster and consume less memory than lists because they are immutable.

Useful for:

- Fixed datasets
- Model outputs
- Configuration values

---

## Common Errors

### Modifying Tuple

```python
t[0] = 5
```

---

### Wrong Unpacking Count

```python
a, b = (1, 2, 3)
```

👉 Error because:

- Variables = 2
- Values = 3

---

## Best Practices

- Use tuples for fixed data
- Use lists for frequently changing data
- Prefer tuples for coordinates and constant values
- Use unpacking for cleaner code

---

## Real-World Insight

Tuples are widely used in:

- APIs
- Databases
- AI model outputs
- Distributed systems

👉 Stability and immutability improve reliability.

