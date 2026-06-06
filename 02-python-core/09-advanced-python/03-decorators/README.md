# Python Advanced Concepts — Decorators

---

## What are Decorators?

A decorator is a powerful Python feature that allows you to modify or extend the behavior of a function or method without changing its original code.

Decorators are commonly used to:

- Add extra functionality
- Execute code before a function runs
- Execute code after a function runs
- Keep code reusable and clean

---

## Why Decorators?

Without decorators:

```python
def hello():

    print("Hello")


print("Before")
hello()
print("After")
```

If multiple functions require the same behavior, code repetition occurs.

Decorators solve this problem.

---

## Functions are First-Class Objects

Functions can be:

- Assigned to variables
- Passed as arguments
- Returned from functions

Example:

```python
def welcome():

    return "Welcome to Python"


copy_func = welcome

print(copy_func())
```

Output:

```plaintext
Welcome to Python
```

---

## Closures

A closure is a function inside another function.

Example:

```python
def main_welcome():

    def sub_welcome():

        print("Welcome to Python")

    return sub_welcome
```

Usage:

```python
func = main_welcome()
func()
```

Output:

```plaintext
Welcome to Python
```

---

## Closure Accessing Outer Variables

```python
def main_welcome(message):

    def sub_welcome():

        print(message)

    return sub_welcome
```

Usage:

```python
func = main_welcome("Hello Everyone")
func()
```

Output:

```plaintext
Hello Everyone
```

Inner functions can access variables from outer functions.

---

## Functions as Arguments

```python
def main(func):

    func("Welcome")
```

Usage:

```python
main(print)
```

Output:

```plaintext
Welcome
```

---

## Building a Decorator

```python
def decorator(func):

    def wrapper():

        print("Before Function")

        func()

        print("After Function")

    return wrapper
```

---

## Using a Decorator

```python
@decorator
def say_hello():

    print("Hello")
```

Calling:

```python
say_hello()
```

Output:

```plaintext
Before Function
Hello
After Function
```

---

## What Does @ Mean?

This:

```python
@decorator
def say_hello():

    print("Hello")
```

is equivalent to:

```python
def say_hello():

    print("Hello")


say_hello = decorator(say_hello)
```

Python automatically passes the function into the decorator.

---

## Decorator Flow

```plaintext
say_hello()
    ↓
wrapper()
    ↓
Before Function
    ↓
Original Function
    ↓
After Function
```

---

## Decorators with Arguments

```python
def repeat(n):

    def decorator(func):

        def wrapper():

            for _ in range(n):
                func()

        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def say_hello():

    print("Hello")
```

Output:

```plaintext
Hello
Hello
Hello
```

---

## Decorators with *args and **kwargs

To support any function signature:

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper
```

This is the most common pattern used in real projects.

---

## Real-World Uses

### Logging

```python
@log
def login():
    pass
```

### Authentication

```python
@login_required
def dashboard():
    pass
```

### Timing Execution

```python
@timer
def process():
    pass
```

### Validation

```python
@validate_input
def submit():
    pass
```

---

## Flask Example

```python
@app.route("/")
def home():

    return "Hello"
```

`@app.route()` is a decorator.

---

## Common Decorator Template

```python
def decorator(func):

    def wrapper(*args, **kwargs):

        # Before

        result = func(*args, **kwargs)

        # After

        return result

    return wrapper
```

---

## Interview Questions

### What is a Decorator?

A decorator is a function that modifies or extends another function's behavior without changing its source code.

---

### What is a Closure?

A function defined inside another function that can access variables from the outer function.

---

### Why are Decorators Useful?

- Code reusability
- Cleaner code
- Logging
- Authentication
- Validation
- Performance monitoring

---

### What does @decorator mean?

```python
@decorator
def func():
    pass
```

Equivalent to:

```python
func = decorator(func)
```

---

## Practice Assignment

### Function Execution Timer

Create a decorator named `timer`.

Requirements:

- Print "Function Started"
- Execute the function
- Print "Function Finished"

Apply it to:

```python
def greet():

    print("Hello Aahish")
```

Expected Output:

```plaintext
Function Started
Hello Aahish
Function Finished
```

---

## Related Topics

Decorators are built on:

- Functions
- Closures
- First-Class Objects
- Arguments (`*args`, `**kwargs`)

They are heavily used before learning:

- Context Managers
- Flask
- Django
- FastAPI
- Async Python

Relationship:

```plaintext
Functions
    ↓
Closures
    ↓
Decorators
```

---

## One-Line Summary

Decorators are built using closures and function objects, allowing us to add functionality before or after a function executes without modifying the original function itself.
