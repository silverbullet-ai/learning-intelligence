# Python Advanced Concepts — Generators

---

## What are Generators?

A generator is a special type of function that produces values one at a time using the `yield` keyword instead of `return`.

Generators are:

- Memory efficient
- Lazily evaluated
- Simpler than custom iterators
- Useful for large datasets and data streams

---

## Why Do We Need Generators?

Consider:

```python
numbers = [x for x in range(10000000)]
```

This stores all values in memory.

Generator version:

```python
def numbers():
    for i in range(10000000):
        yield i
```

Values are generated only when needed.

---

## Return vs Yield

### Using Return

```python
def square(n):
    for i in range(n):
        return i ** 2
```

Output:

```plaintext
0
```

`return` immediately terminates the function.

---

### Using Yield

```python
def square(n):
    for i in range(n):
        yield i ** 2
```

Output:

```plaintext
<generator object square at ...>
```

The function becomes a generator.

---

## Creating a Generator

```python
def square(n):
    for i in range(n):
        yield i ** 2

gen = square(5)
```

---

## Iterating Through a Generator

```python
for value in square(5):
    print(value)
```

Output:

```plaintext
0
1
4
9
16
```

---

## How Yield Works

```python
def square(n):
    for i in range(n):
        yield i ** 2
```

Execution:

```plaintext
yield 0 → pause

resume

yield 1 → pause

resume

yield 4 → pause
```

The function remembers where it stopped.

---

## Generator + next()

Generators are iterators.

```python
gen = square(3)

print(next(gen))
print(next(gen))
print(next(gen))
```

Output:

```plaintext
0
1
4
```

Next call:

```plaintext
StopIteration
```

---

## Multiple Yield Statements

```python
def my_generator():

    yield 1
    yield 2
    yield 3
```

Using:

```python
for value in my_generator():
    print(value)
```

Output:

```plaintext
1
2
3
```

---

## Memory Efficiency

List:

```python
numbers = [x*x for x in range(1000000)]
```

Stores one million values.

Generator:

```python
def squares():
    for x in range(1000000):
        yield x*x
```

Stores only the current value.

---

## State Preservation

Generators preserve execution state.

```python
def test():

    yield "A"
    yield "B"
```

Output:

```plaintext
A
B
```

The function resumes from where it paused.

---

## Generator Execution Flow

```plaintext
Start
  ↓
yield 1
  ↓ pause

resume
  ↓
yield 2
  ↓ pause

resume
  ↓
yield 3
  ↓ pause

StopIteration
```

---

## Practical Example: Reading Large Files

```python
def read_large_file(filepath):

    with open(filepath, "r") as file:

        for line in file:
            yield line
```

Usage:

```python
for line in read_large_file("large.txt"):
    print(line.strip())
```

Benefits:

- Low memory usage
- One line at a time
- Efficient processing

---

## Generator Expressions

### List Comprehension

```python
squares = [x*x for x in range(5)]
```

Output:

```plaintext
[0, 1, 4, 9, 16]
```

---

### Generator Expression

```python
squares = (x*x for x in range(5))
```

Output:

```plaintext
<generator object ...>
```

Generated lazily.

---

## Iterator vs Generator

| Iterator                                     | Generator                 |
| -------------------------------------------- | ------------------------- |
| Created using `iter()`                     | Created using `yield`   |
| More code required                           | Less code                 |
| Manual implementation                        | Automatic implementation  |
| More complex                                 | Easier to write           |
| Implements `__iter__()` and `__next__()` | Python handles internally |

---

## Similarities

Both:

- Support `next()`
- Work with `for` loops
- Raise `StopIteration`
- Use lazy evaluation

---

## Infinite Generators

```python
def count():

    num = 1

    while True:
        yield num
        num += 1
```

Usage:

```python
counter = count()

print(next(counter))
print(next(counter))
```

Output:

```plaintext
1
2
```

Can continue forever.

---

## Real-World Uses

### Reading Large Files

```python
yield line
```

### Data Streaming

```python
yield packet
```

### Machine Learning

```python
yield batch
```

### Log Processing

```python
yield log_entry
```

### Web Scraping

```python
yield webpage
```

### Infinite Sequences

```python
yield next_number
```

---

## Common Interview Questions

### What is a Generator?

A function that uses `yield` to generate values lazily.

---

### Difference Between Return and Yield?

| Return                  | Yield               |
| ----------------------- | ------------------- |
| Ends function           | Pauses function     |
| Returns one value       | Returns many values |
| Does not preserve state | Preserves state     |

---

### Are Generators Iterators?

Yes.

Every generator is an iterator.

---

### Why Are Generators Memory Efficient?

Values are generated only when needed.

---

### What Exception Signals End of a Generator?

```plaintext
StopIteration
```

---

## Practice Assignment

### Generate Even Numbers

Create a generator that yields all even numbers between 1 and 20.

Expected Output:

```plaintext
2
4
6
8
10
12
14
16
18
20
```

---

## Related Topics

Generators build directly on:

- Iterators
- Functions
- Loops
- Lazy Evaluation

Generators are often used before learning:

- Decorators
- Context Managers
- Async Programming
- Data Pipelines

Relationship:

```plaintext
Iterable
    ↓
Iterator
    ↓
Generator
```

---

## One-Line Summary

Generators are special functions that use the `yield` keyword to create iterators, generating values one at a time on demand, making them highly memory-efficient and ideal for large datasets and streaming data.
