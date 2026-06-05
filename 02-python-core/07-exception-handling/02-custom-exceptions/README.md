# Python Exception Handling — Custom Exceptions

---

## What are Custom Exceptions?

A Custom Exception is a user-defined exception created to handle application-specific errors.

Python provides several built-in exceptions such as:

- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError

However, real-world applications often require custom business-rule validations that built-in exceptions cannot clearly represent.

---

## Why Use Custom Exceptions?

Custom exceptions help represent domain-specific errors such as:

- Invalid age
- Insufficient balance
- Unauthorized access
- Invalid employee ID
- Invalid product code
- Invalid marks
- Weak password

These are business logic errors rather than Python runtime errors.

---

## Real-World Example

Suppose an examination system has the following rule:

- Minimum Age = 20
- Maximum Age = 30

If a user enters:

- Age < 20
- Age > 30

The system should display:

```plaintext
Not eligible for this exam.
```

Instead of relying on a generic exception, we can create our own exception.

---

## Creating a Custom Exception

Custom exceptions are typically created by inheriting from Python's built-in `Exception` class.

```python
class Error(Exception):
    pass
```

---

## Creating a Specific Exception

```python
class DOBException(Error):
    pass
```

Hierarchy:

```plaintext
Exception
│
└── Error
    │
    └── DOBException
```

---

## Raising Exceptions

The `raise` keyword is used to manually generate an exception.

```python
raise DOBException
```

Or with a custom message:

```python
raise DOBException(
    "Age must be between 20 and 30"
)
```

---

## Example: Exam Eligibility Check

```python
class DOBException(Exception):
    pass

try:
    age = 35

    if not (20 <= age <= 30):
        raise DOBException(
            "Age must be between 20 and 30"
        )

except DOBException as e:
    print(e)
```

Output:

```plaintext
Age must be between 20 and 30
```

---

## Understanding `raise`

`raise` manually triggers an exception.

Examples:

```python
raise ValueError
```

```python
raise TypeError
```

```python
raise DOBException
```

When an exception is raised, normal program execution stops and control is transferred to the nearest matching `except` block.

---

## Why Use `try-except`?

Without handling:

```python
raise DOBException
```

Output:

```plaintext
Traceback...
DOBException
```

The program terminates.

With handling:

```python
try:
    raise DOBException
except DOBException:
    print("Handled successfully")
```

The exception is handled gracefully and the application can continue safely.

---

## Custom Exception with Message

```python
class DOBException(Exception):
    pass

try:
    age = 35

    if age > 30:
        raise DOBException(
            "Age must be between 20 and 30"
        )

except DOBException as e:
    print(e)
```

Output:

```plaintext
Age must be between 20 and 30
```

---

## Creating Better Custom Exception Classes

```python
class DOBException(Exception):

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
```

Usage:

```python
raise DOBException(
    "Invalid age for exam"
)
```

---

## Complete Example

```python
class DOBException(Exception):
    pass

try:
    year = int(input("Enter Birth Year: "))

    age = 2026 - year

    if 20 <= age <= 30:
        print("Age is valid")
        print("You can apply for the exam")

    else:
        raise DOBException(
            "Age must be between 20 and 30"
        )

except DOBException as e:
    print(e)
```

---

## Dynamic Year Calculation (Recommended)

Instead of hardcoding the year:

```python
age = 2026 - year
```

Use:

```python
from datetime import datetime

current_year = datetime.now().year
age = current_year - year
```

This keeps the program accurate in future years without modification.

---

## Real-World Examples

### Banking Application

```python
class InsufficientBalance(Exception):
    pass
```

Usage:

```python
raise InsufficientBalance(
    "Balance too low"
)
```

---

### Employee Management System

```python
class InvalidEmployeeID(Exception):
    pass
```

---

### E-Commerce Platform

```python
class ProductNotFound(Exception):
    pass
```

---

### Login System

```python
class UnauthorizedUser(Exception):
    pass
```

---

## Exception Handling Flow

```plaintext
Business Rule Validation
          │
          ▼
 Condition Fails?
          │
     Yes  ▼
   raise CustomException
          │
          ▼
 except CustomException
          │
          ▼
 Handle Gracefully
```

---

## Best Practices

✅ Create meaningful exception names

✅ Inherit from `Exception`

✅ Provide descriptive messages

✅ Catch specific exceptions

✅ Use custom exceptions for business rules

✅ Keep exception classes focused and reusable

---

## Common Interview Questions

### What is a Custom Exception?

A custom exception is a user-defined exception created by inheriting from Python's `Exception` class.

---

### Why Use Custom Exceptions?

- Business rule validation
- Better readability
- Cleaner architecture
- Better debugging
- More meaningful error messages

---

### How Do You Create a Custom Exception?

```python
class MyException(Exception):
    pass
```

---

### What Does `raise` Do?

`raise` manually generates an exception.

```python
raise MyException()
```

---

### Difference Between `raise` and `except`

| raise               | except             |
| ------------------- | ------------------ |
| Generates exception | Handles exception  |
| Starts error flow   | Catches error flow |

---

## Practice Assignments

### 1. InvalidAgeException

Create an exception where:

- Age must be 18 or above

---

### 2. InsufficientBalanceException

Create an exception where:

- Withdrawal amount cannot exceed balance

---

### 3. InvalidPasswordException

Create an exception where:

- Password length must be at least 8 characters

---

### 4. InvalidMarksException

Create an exception where:

- Marks must be between 0 and 100

---

### 5. NegativeNumberException

Create an exception where:

- Negative numbers are not allowed

Use:

```python
raise NegativeNumberException
```

when a negative value is entered.

---

## Key Takeaways

- Custom exceptions represent business logic errors.
- They inherit from Python's `Exception` class.
- Use `raise` to generate exceptions.
- Use `try-except` to handle them.
- Custom exceptions improve maintainability and readability.
- They are heavily used in real-world applications.

---

## Related Topics

Custom exceptions combine concepts from:

- Exception Handling
- Classes & Objects
- Inheritance

Because every custom exception is simply a class derived from Python's built-in `Exception` class.

```python
class CustomException(Exception):
    pass
```

Recommended review:

- Classes & Objects
- Inheritance

---

## One-Line Summary

Custom exceptions allow developers to create application-specific error types by inheriting from Python's `Exception` class and handling business logic errors gracefully.
