# Python Advanced Concepts — Iterators

---

## What are Iterators?

An iterator is an object that allows you to traverse through elements of a collection one element at a time.

Iterators provide:

- Efficient looping
- Better memory management
- Lazy evaluation (lazy loading)

---

## Why Do We Need Iterators?

Normally we write:

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(num)
```

Python automatically handles iteration for us.

Internally, however, the `for` loop uses an iterator.

---

## Iterable vs Iterator

| Iterable                 | Iterator                            |
| ------------------------ | ----------------------------------- |
| Can be iterated over     | Performs actual iteration           |
| Uses `iter()`          | Uses `next()`                     |
| List, Tuple, Set, String | list_iterator, tuple_iterator, etc. |

Example:

```python
numbers = [1, 2, 3]
```

This is an iterable.

Convert it into an iterator:

```python
iterator = iter(numbers)
```

Now it becomes an iterator.

---

## Creating an Iterator

```python
numbers = [1, 2, 3, 4, 5]

iterator = iter(numbers)
```

Check type:

```python
print(type(iterator))
```

Output:

```plaintext
<class 'list_iterator'>
```

---

## Accessing Elements Using next()

```python
numbers = [1, 2, 3]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```plaintext
1
2
3
```

Each call moves the iterator forward.

---

## Internal Working

```plaintext
[1, 2, 3, 4, 5]

 ↑
Current Position
```

After calling:

```python
next(iterator)
```

Pointer moves to the next element.

---

## StopIteration Exception

When all elements are exhausted:

```python
next(iterator)
```

raises:

```plaintext
StopIteration
```

Example:

```python
numbers = [1]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
```

Output:

```plaintext
1
StopIteration
```

---

## Handling StopIteration

```python
numbers = [1, 2]

iterator = iter(numbers)

try:

    while True:
        print(next(iterator))

except StopIteration:
    print("Iterator exhausted")
```

Output:

```plaintext
1
2
Iterator exhausted
```

---

## Lazy Evaluation (Lazy Loading)

Iterators do not load everything at once.

Instead:

```python
next(iterator)
```

fetches only the next value when needed.

Benefits:

- Memory efficient
- Faster for large datasets
- Better performance

---

## How for Loops Work Internally

When Python sees:

```python
for num in numbers:
    print(num)
```

It internally behaves like:

```python
iterator = iter(numbers)

while True:

    try:
        num = next(iterator)
        print(num)

    except StopIteration:
        break
```

---

## Iterators with Strings

```python
name = "Python"

iterator = iter(name)

print(next(iterator))
```

Output:

```plaintext
P
```

---

## Iterators with Tuples

```python
numbers = (10, 20, 30)

iterator = iter(numbers)

print(next(iterator))
```

Output:

```plaintext
10
```

---

## Iterators with Dictionaries

```python
student = {
    "name": "Aahish",
    "age": 23
}

iterator = iter(student)

print(next(iterator))
```

Output:

```plaintext
name
```

---

## Built-in Functions Returning Iterators

### map()

```python
map(lambda x: x * 2, numbers)
```

---

### filter()

```python
filter(lambda x: x % 2 == 0, numbers)
```

---

### zip()

```python
zip(list1, list2)
```

---

### enumerate()

```python
enumerate(numbers)
```

These functions return iterators and use lazy evaluation.

---

## Real-World Uses

### Reading Large Files

```python
for line in file:
    print(line)
```

---

### Database Records

```python
for row in result:
    print(row)
```

---

### Machine Learning Pipelines

```python
for batch in dataloader:
    train(batch)
```

---

### Streaming Data

```python
for packet in stream:
    process(packet)
```

---

## Common Interview Questions

### What is an Iterator?

An object that allows sequential access to elements one at a time.

---

### Difference Between Iterable and Iterator?

Iterable:

- list
- tuple
- string
- set

Iterator:

```python
iter(list)
iter(tuple)
```

---

### Which Functions are Used with Iterators?

```python
iter()
next()
```

---

### Which Exception Signals End of Iteration?

```plaintext
StopIteration
```

---

### Why Are Iterators Memory Efficient?

Because they use lazy evaluation and fetch values only when needed.

---

## Practice Assignment

### Recreate a for Loop Manually

Using:

- `iter()`
- `next()`
- `while True`
- `StopIteration`

Print all elements of:

```python
[10, 20, 30, 40, 50]
```

without using a `for` loop.

---

## Related Topics

Iterators connect several important Python concepts:

- Loops
- Functions
- Lambda Functions
- map()
- filter()
- Generators

Many built-in Python functions return iterators:

```python
map()
filter()
zip()
enumerate()
```

Understanding iterators makes it easier to learn:

- Generators
- Decorators
- Async Programming
- Data Processing Pipelines

---

## One-Line Summary

An iterator is an object that enables sequential access to elements one at a time using `iter()` and `next()`, providing efficient looping and memory management through lazy evaluation.
