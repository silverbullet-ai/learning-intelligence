# Python Data Structures – Dictionaries

---

## Overview

A dictionary is a mutable collection of items stored as key-value pairs.

Dictionaries are one of the most important data structures in Python because they provide:

- Fast lookup
- Structured storage
- Dynamic data handling

They are heavily used in:
- APIs
- JSON
- Machine Learning
- Backend systems
- Databases

---

## Key Features

- Stores data as `key : value`
- Keys must be:
  - unique
  - immutable
- Values can be any datatype
- Dictionaries are mutable

---

## Creating Dictionaries

### Empty Dictionary

```python
empty_dict = {}

print(type(empty_dict))
```

### Using dict()

```python
empty_dict = dict()
```

---

## Creating Dictionary with Values

```python
student = {
    "name": "Aahish",
    "age": 23,
    "grade": "A"
}

print(student)
```

---

## Important Rule About Keys

Keys must be unique.

```python
student = {
    "name": "Manav",
    "name": "Aahish"
}

print(student)
```

### Output

```python
{'name': 'Aahish'}
```

👉 Latest value replaces previous value.

---

## Accessing Dictionary Elements

### Using Keys

```python
print(student["grade"])
```

### Using get()

```python
print(student.get("age"))
```

### Default Value with get()

```python
print(student.get("last_name", "Not Available"))
```

---

## Modifying Dictionary Elements

### Updating Values

```python
student["age"] = 24
```

### Adding New Key-Value Pair

```python
student["address"] = "India"
```

### Deleting Key-Value Pair

```python
del student["grade"]
```

---

## Common Dictionary Methods

### keys()

Returns all keys.

```python
print(student.keys())
```

### values()

Returns all values.

```python
print(student.values())
```

### items()

Returns all key-value pairs.

```python
print(student.items())
```

---

## Shallow Copy

### Wrong Way

```python
student_copy = student
```

Changes affect both variables.

### Correct Way

```python
student_copy = student.copy()
```

Creates separate memory reference.

---

## Iterating Over Dictionaries

### Iterating Over Keys

```python
for key in student.keys():
    print(key)
```

### Iterating Over Values

```python
for value in student.values():
    print(value)
```

### Iterating Over Key-Value Pairs

```python
for key, value in student.items():
    print(f"{key} : {value}")
```

---

## Nested Dictionaries

Dictionary inside another dictionary.

```python
students = {
    "student1": {
        "name": "Aahish",
        "age": 23
    },

    "student2": {
        "name": "Manav",
        "age": 22
    }
}
```

---

## Accessing Nested Dictionary

```python
print(students["student2"]["name"])
```

---

## Iterating Nested Dictionary

```python
for student_id, info in students.items():
    print(student_id)

    for key, value in info.items():
        print(f"{key} : {value}")
```

---

## Dictionary Comprehension

### Syntax

```python
{
    key_expression: value_expression
    for item in iterable
}
```

---

## Basic Dictionary Comprehension

```python
squares = {x: x**2 for x in range(5)}

print(squares)
```

---

## Conditional Dictionary Comprehension

```python
even_squares = {
    x: x**2
    for x in range(10)
    if x % 2 == 0
}
```

---

## Frequency Counter Example

```python
numbers = [1,2,2,3,3,3,4,4,4,4]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
```

---

## Merging Dictionaries

```python
dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "b": 3,
    "c": 4
}

merged = {
    **dict1,
    **dict2
}

print(merged)
```

---

## Important Concepts

Dictionaries are:

- Mutable
- Dynamic
- Fast for lookup
- Key-value based

---

## Real-World Usage

Dictionaries are heavily used in:

- APIs
- JSON data
- Backend development
- Machine Learning
- Databases
- Configuration files

---

## Important Interview Topics

You should clearly understand:

- get()
- items()
- Iteration
- Nested dictionaries
- Shallow copy
- Dictionary comprehension
- Frequency counter problems

---

## Data Structure Comparison

| Data Structure | Ordered | Mutable | Duplicates | Key Feature |
|----------------|---------|----------|-------------|-------------|
| List | ✅ | ✅ | ✅ | General-purpose collection |
| Tuple | ✅ | ❌ | ✅ | Fixed/immutable data |
| Set | ❌ | ✅ | ❌ | Unique elements |
| Dictionary | ✅ | ✅ | Keys unique | Key-value storage |

Modern Python preserves insertion order in dictionaries.

---

## Dictionary Summary

| Feature | Dictionary |
|----------|------------|
| Ordered | ✅ |
| Mutable | ✅ |
| Duplicate Keys | ❌ |
| Key-Value Pair | ✅ |
| Fast Lookup | ✅ |

---

## Best Practices

- Use meaningful keys
- Prefer get() when unsure about keys
- Keep nested dictionaries readable
- Use comprehension for cleaner transformations

