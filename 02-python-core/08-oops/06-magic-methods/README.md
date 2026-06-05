# Python OOPs — Magic Methods (Dunder Methods)

---

# What are Magic Methods?

Magic Methods are special methods in Python that:

- Start with double underscores (`__`)
- End with double underscores (`__`)

Because of the double underscores, they are also called:

> Dunder Methods
> (Double Under)

---

# Definition

Magic methods are special methods that allow us to define how objects behave with Python's built-in operations.

They control:

- Object creation
- String representation
- Arithmetic operations
- Comparisons
- Length calculations
- Iteration
- Operator overloading

and much more.

---

# Why Are They Called Magic?

Python automatically calls them behind the scenes.

Example:

```python
print(obj)
```

Internally Python executes:

```python
obj.__str__()
```

automatically.

---

# Common Magic Methods

| Magic Method   | Purpose                             |
| -------------- | ----------------------------------- |
| `__init__()` | Constructor                         |
| `__str__()`  | User-friendly string representation |
| `__repr__()` | Official string representation      |
| `__len__()`  | Length of object                    |
| `__add__()`  | Addition (`+`)                    |
| `__sub__()`  | Subtraction (`-`)                 |
| `__mul__()`  | Multiplication (`*`)              |
| `__eq__()`   | Equality comparison                 |
| `__lt__()`   | Less than (`<`)                   |
| `__gt__()`   | Greater than (`>`)                |

---

# Viewing Magic Methods

```python
class Person:
    pass

print(dir(Person))
```

Output (partial):

```python
[
 '__init__',
 '__str__',
 '__repr__',
 '__eq__',
 '__lt__',
 '__gt__',
 ...
]
```

---

# 1.  `__init__()` Method

## Purpose

Constructor of a class.

Automatically runs when an object is created.

---

## Example

```python
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

Object Creation:

```python
p1 = Person("Aahish", 23)
```

---

# 2.  `__str__()` Method

## Purpose

Provides a readable string representation of an object.

Used when:

```python
print(obj)
str(obj)
```

are called.

---

## Without `__str__()`

```python
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age


p1 = Person("Aahish", 23)

print(p1)
```

Output:

```plaintext
<__main__.Person object at 0x00000123>
```

Not very useful.

---

## With `__str__()`

```python
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        return f"{self.name}, {self.age} years old"
```

Output:

```python
p1 = Person("Aahish", 23)

print(p1)
```

```plaintext
Aahish, 23 years old
```

---

# 3.  `__repr__()` Method

## Purpose

Returns an official string representation of an object.

Mostly used for:

- Debugging
- Logging
- Developers

---

## Example

```python
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __repr__(self):

        return f"Person(name='{self.name}', age={self.age})"
```

Output:

```python
p1 = Person("Aahish", 23)

print(repr(p1))
```

```plaintext
Person(name='Aahish', age=23)
```

---

# `__str__()` vs `__repr__()`

| `__str__()`       | `__repr__()`     |
| ------------------- | ------------------ |
| For users           | For developers     |
| Friendly output     | Detailed output    |
| Used by `print()` | Used by `repr()` |
| Human-readable      | Debug-oriented     |

---

## Example

```python
class Person:

    def __str__(self):

        return "User View"

    def __repr__(self):

        return "Developer View"
```

```python
print(person)
```

Output:

```plaintext
User View
```

```python
repr(person)
```

Output:

```plaintext
Developer View
```

---

# Overriding Magic Methods

Magic methods already exist.

We can customize their behavior.

This is called:

> Overriding Magic Methods

---

## Example

Default output:

```python
print(person)
```

```plaintext
<__main__.Person object at 0x12345>
```

After overriding:

```python
def __str__(self):

    return f"{self.name}"
```

Output:

```plaintext
Aahish
```

---

# Why Override Magic Methods?

To:

- Improve readability
- Customize behavior
- Improve debugging
- Improve maintainability
- Make objects behave naturally

---

# Complete Example

```python
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def __str__(self):

        return f"{self.name}, {self.age} years old"

    def __repr__(self):

        return f"Person(name='{self.name}', age={self.age})"


person = Person("Aahish", 23)

print(person)
print(repr(person))
```

Output:

```plaintext
Aahish, 23 years old
Person(name='Aahish', age=23)
```

---

# Real-Life Analogy

Imagine an employee.

### User View (`__str__()`)

```plaintext
Aahish - AI Engineer
```

### HR View (`__repr__()`)

```plaintext
Employee(
    id=101,
    name='Aahish',
    department='AI',
    salary=50000
)
```

Different audiences need different information.

---

# Why Magic Methods Matter

Magic methods allow custom objects to work naturally with Python syntax.

Example:

```python
len(obj)
```

calls:

```python
obj.__len__()
```

---

```python
obj1 + obj2
```

calls:

```python
obj1.__add__(obj2)
```

---

```python
obj1 == obj2
```

calls:

```python
obj1.__eq__(obj2)
```

---

# Important Interview Questions

### What are Magic Methods?

Magic methods are special Python methods that define object behavior for built-in operations.

---

### Why are they called Dunder Methods?

Because they start and end with:

```python
__
```

Example:

```python
__init__
__str__
__repr__
```

---

### What is `__init__()`?

Constructor method.

Runs automatically during object creation.

---

### What is `__str__()`?

Returns a user-friendly string representation.

Used by:

```python
print(obj)
```

---

### What is `__repr__()`?

Returns a developer-friendly representation.

Used by:

```python
repr(obj)
```

---

### Can We Override Magic Methods?

✅ Yes

That is one of their primary purposes.

---

# Practice Assignments

### 1. Book Class

Create:

```python
Book
```

Attributes:

- title
- author

Override:

```python
__str__()
```

Output:

```plaintext
Atomic Habits by James Clear
```

---

### 2. Student Class

Override:

```python
__repr__()
```

Output:

```plaintext
Student(name='Aahish', marks=95)
```

---

### 3. Car Class

Override:

```python
__str__()
```

Output:

```plaintext
Lamborghini Revuelto
```

---

### 4. Laptop Class

Implement:

- `__str__()`
- `__repr__()`

---

### 5. Movie Class

Display:

```plaintext
Interstellar (2014)
```

using:

```python
__str__()
```

---

# ⚡ Quick Revision

| Method         | Purpose                   |
| -------------- | ------------------------- |
| `__init__()` | Object creation           |
| `__str__()`  | User-friendly output      |
| `__repr__()` | Developer-friendly output |
| Magic Method   | Built-in special method   |
| Dunder Method  | Double underscore method  |

---

# One-Line Summary

> Magic methods (dunder methods) are special Python methods that allow us to customize how objects behave with built-in operations such as object creation, printing, comparisons, arithmetic operations, and much more.
>
