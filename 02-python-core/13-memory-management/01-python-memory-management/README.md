# Python Memory Management

## Overview

Python automatically manages memory allocation and deallocation.

Memory management is handled through:

- Reference Counting
- Garbage Collection
- Memory Optimization Techniques

This allows developers to focus on application logic without manually managing memory.

---

## Topics Covered

- Reference Counting
- Garbage Collection
- Circular References
- Generators and Memory Efficiency
- Memory Profiling
- Memory Management Best Practices

---

## Reference Counting

Python tracks how many references point to an object.

When the reference count becomes zero, memory is released automatically.

### Example

```python
import sys

a = [1, 2, 3]

print(sys.getrefcount(a))
```

---

## Garbage Collection

Reference counting cannot handle circular references.

Python uses a Garbage Collector (GC) to detect and remove unreachable objects.

### GC Module

```python
import gc

gc.collect()
```

---

## Circular References

Example:

```text
obj1 ───► obj2
 ▲         │
 │         ▼
 └─────────┘
```

Even after deleting variables, objects may still reference each other.

Garbage collection resolves this issue.

---

## Generators and Memory Efficiency

Generators produce values lazily using `yield`.

Instead of storing all values:

```python
list(range(1000000))
```

use:

```python
(i for i in range(1000000))
```

This significantly reduces memory usage.

---

## Memory Profiling

Python provides:

```python
import tracemalloc
```

for tracking memory allocations.

Useful for:

- Finding memory leaks
- Measuring memory consumption
- Optimizing applications

---

## Best Practices

- Prefer local variables
- Avoid unnecessary circular references
- Use generators for large datasets
- Delete unused objects
- Profile memory usage when needed

---

## Reference Counting vs Garbage Collection

| Feature | Reference Counting | Garbage Collection |
|----------|-------------------|-------------------|
| Memory Release | Immediate | Periodic |
| Circular References | No | Yes |
| Automatic | Yes | Yes |
| Performance | Faster | Slightly Slower |

---

## Interview Questions

### What is Python's primary memory management technique?

Reference Counting.

### Why is Garbage Collection needed?

Because reference counting cannot handle circular references.

### What does `gc.collect()` do?

Manually triggers garbage collection.

### Why are generators memory efficient?

They generate values on demand instead of storing all values in memory.

### What is `tracemalloc`?

A module for tracking memory allocations.

---

## Key Takeaways

- Python manages memory automatically.
- Reference counting is the primary mechanism.
- Garbage collection handles circular references.
- Generators reduce memory usage.
- `tracemalloc` helps profile memory consumption.

---

# reference_counting.py

```python
import sys

a = [1, 2, 3]

print("Initial References:")
print(sys.getrefcount(a))

b = a

print("After assigning b:")
print(sys.getrefcount(a))

del b

print("After deleting b:")
print(sys.getrefcount(a))
```
