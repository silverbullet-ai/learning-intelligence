# Python Data Structures – Lists

---

## Overview

A list is an ordered and mutable collection of items.

### Key Properties

- Ordered (index-based)
- Mutable (modifiable)
- Supports mixed data types

---

## Creating Lists

```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4]
mixed = [1, "Aahish", 3.14, True]
```

---

## Accessing Elements

### Indexing

```python
fruits[0]  # apple
fruits[2]  # cherry
```

### Negative Indexing

```python
fruits[-1]  # last item
fruits[-2]  # second last
```

👉 Very useful in real-world coding.

---

## Slicing (IMPORTANT)

```python
fruits[1:3]
fruits[:3]
fruits[2:]
```

### Step Slicing

```python
numbers[::2]
numbers[::-1]
```

👉 Structure:

```python
[start:end:step]
```

---

## Modifying Lists

```python
fruits[1] = "watermelon"
```

---

## Important List Methods

### append()

```
#Syntax

list.append('item')
```

```python
#Example
fruits.append("orange")     # Adds an element at the end of the list.
```

### insert()

```
#Syntax

list_name.insert(index, 'item')
```

```python
#Example
fruits.insert(1, "kiwi")    # Inserts an element at a specific index position.
```

### remove()

```
#Syntax

list_name.remove('item')
```

```python
#Example
fruits.remove("banana")     # Removes the first matching element from the list.
```

### pop()

```
#Syntax

list_name.pop()
```

```python
#Example
fruits.pop()    # Removes and returns the last element.
```

### index()

```
#Syntax

list_name.index('item')
```

```python
#Example
fruits.index("apple")   # Returns the index position of a specified element.
```

### count()

```
#Syntax
list_name.count('item')
```

```python
#Example
fruits.count("banana")      # Returns the number of times an element appears in the list.
```

### sort()

```
#Syntax
list_name.sort()
```

```python
#Example
fruits.sort()       # Sorts the list elements in ascending order.
```

### reverse()

```
#Syntax

list_name.reverse()
```

```python
#Example
fruits.reverse()    # Reverses the order of elements in the list.
```

### clear()

```
#Syntax

list_name.clear()
```

```python
#Example
fruits.clear()  # Removes all elements from the list.
```

---

## ⚠️ Important Mistake

```python
fruits[1:] = "watermelon"
```

👉 Breaks string into characters.

```python
['w', 'a', 't', 'e', 'r', 'm', 'e', 'l', 'o', 'n']
```

### Correct:

```python
fruits[1:] = ["watermelon"]
```

---

## Iterating Over Lists

### Basic Loop

```python
for fruit in fruits:
    print(fruit)
```

### With Index

```python
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

---

## List Comprehension (VERY IMPORTANT)

### Basic Syntax

```python
[expression for item in iterable]

#Example
squares = [x**2 for x in range(10)]
```

### With Condition

```python
[expression for item in iterable if condition]

#Example
evens = [x for x in range(10) if x % 2 == 0]
```

### With Function

```python
[function for item in iterable]

#Example
words = ["hello", "python"]

lengths = [len(word) for word in words]
```

---

## Nested List Comprehension

```python
[expression for item_1 in iterable_1 for item_2 in iterable_2]

#Example
list1 = [1, 2]
list2 = ["A", "B"]

pairs = [[i, j] for i in list1 for j in list2]
```

### Output

```python
[[1, 'A'], [1, 'B'], [2, 'A'], [2, 'B']]
```

---

## Common Errors

- Index out of range  
- Wrong slicing  
- Missing brackets in comprehension  
- Assigning string instead of list  

---

## Best Practices

- Prefer list comprehension for cleaner code  
- Avoid unnecessary loops  
- Keep lists readable  
- Avoid excessive nesting  

---

## Real-World Insight

Lists are heavily used in:

- Data preprocessing  
- Feature engineering  
- Batch operations  
- ML pipelines  

### Example:

```python
features = [x * 2 for x in data if x > 0]
```

👉 This resembles real preprocessing logic used in AI systems.