# Python Data Structures – Sets

---

## Overview

Sets are one of the most powerful data structures in Python when dealing with:

- Uniqueness
- Fast lookup
- Removing duplicates
- Mathematical operations

They are heavily used in:
- AI preprocessing
- Databases
- Recommendation systems
- NLP pipelines
- Graph algorithms

---

## What is a Set?

A set is an unordered collection of unique elements.

---

## Key Properties of Sets

| Property | Description |
|----------|-------------|
| Unordered | No fixed indexing |
| Unique Elements | No duplicates allowed |
| Mutable | Can add/remove elements |
| No Indexing | Cannot access using indexes |

---

## Creating Sets

### Using Curly Braces

```python
my_set = {1, 2, 3, 4, 5}
```

---

### Empty Set

⚠️ Important:

```python
empty_set = set()
```

NOT:

```python
empty_set = {}
```

Because `{}` creates a dictionary.

---

## Duplicate Elements Automatically Removed

```python
nums = {1, 2, 2, 3, 4, 4, 5}

print(nums)
```

### Output

```python
{1, 2, 3, 4, 5}
```

---

## Type Conversion

### List → Set

```python
numbers = [1, 2, 2, 3, 4]

unique_numbers = set(numbers)
```

---

### Tuple → Set

```python
nums = (1, 2, 3)

s = set(nums)
```

---

## Adding Elements

### Using `.add()`

```python
my_set = {1, 2, 3}

my_set.add(4)
```

---

### Duplicate Add Ignored

```python
my_set.add(4)
```

No error.  
No duplicate added.

---

## Removing Elements

### `remove()`

```python
my_set.remove(2)
```

⚠️ Raises error if element does not exist.

---

### `discard()`

```python
my_set.discard(10)
```

No error even if element is absent.

---

## `pop()`

Removes a random element.

```python
removed = my_set.pop()
```

⚠️ Since sets are unordered, removal is unpredictable.

---

## `clear()`

```python
my_set.clear()
```

Removes all elements.

---

## Membership Test

Very important and extremely fast.

```python
3 in my_set
```

### Output

```python
True
```

---

## Mathematical Set Operations

This is where sets become extremely powerful.

---

## Union

Combines all unique elements.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.union(set2)
```

### Output

```python
{1, 2, 3, 4, 5}
```

---

## Intersection

Common elements only.

```python
set1.intersection(set2)
```

### Output

```python
{3}
```

---

## Difference

Elements present in first set but not second.

```python
set1.difference(set2)
```

### Output

```python
{1, 2}
```

---

## Symmetric Difference

Removes common elements.

```python
set1.symmetric_difference(set2)
```

### Output

```python
{1, 2, 4, 5}
```

---

## Update Methods

These modify the original set.

---

### `intersection_update()`

```python
set1.intersection_update(set2)
```

Updates set1 with common elements only.

---

### `difference_update()`

```python
set1.difference_update(set2)
```

Updates set1 after removing common elements.

---

## Subset and Superset

### `issubset()`

```python
a = {1, 2}
b = {1, 2, 3}

a.issubset(b)
```

### Output

```python
True
```

---

### `issuperset()`

```python
b.issuperset(a)
```

### Output

```python
True
```

---

## Practical Use Case – Remove Duplicates

```python
nums = [1, 2, 2, 3, 4, 4, 5]

unique = list(set(nums))
```

---

## Practical Example – Unique Words

```python
text = "python is powerful and python is easy"

words = text.split()

unique_words = set(words)

print(unique_words)
```

---

## Iterating Through Sets

```python
for item in my_set:
    print(item)
```

⚠️ Order is not guaranteed.

---

## Important Limitation

Sets do not support indexing.

Invalid:

```python
my_set[0]
```

### Error

```python
TypeError: 'set' object is not subscriptable
```

---

## Why Sets are Fast?

Sets internally use:

- Hashing
- Hash tables

This makes:

- Lookup → extremely fast
- Membership test → O(1)

---

## Real-World Applications

Sets are heavily used in:

- Search systems
- Recommendation engines
- Caching
- AI preprocessing
- Analytics pipelines

---

## ⚔️ List vs Tuple vs Set

| Feature              | List | Tuple | Set |
| -------------------- | ---- | ----- | --- |
| Ordered              | ✅    | ✅     | ❌   |
| Mutable              | ✅    | ❌     | ✅   |
| Duplicates Allowed   | ✅    | ✅     | ❌   |
| Indexing             | ✅    | ✅     | ❌   |
| Fast Membership Test | ❌    | ❌     | ✅   |

---

## ⚠️ Common Errors

### Using `{}` for Empty Set

```python
x = {}
```

Creates dictionary.

Correct:

```python
x = set()
```

---

### Indexing Sets

```python
my_set[0]
```

Not allowed.

---

## Common Interview Questions

1. Remove duplicates from a list
2. Find common elements between lists
3. Find unique words in a paragraph
4. Check subset/superset
5. Difference between `remove()` and `discard()`

---

## Best Practices

- Use sets for uniqueness
- Use membership tests for fast lookup
- Prefer sets for duplicate removal
- Avoid relying on order
