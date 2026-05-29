# Python OOPs — Classes & Objects

---

# What is OOPs?

OOPs stands for:

> Object Oriented Programming

It is a programming paradigm that uses:
- classes
- objects

to design applications.

---

# Why OOPs is Important

OOPs helps in:
- modeling real-world scenarios
- code reusability
- better structure
- modular programming
- scalability
- maintainability

---

# Real-World Examples

| Real World | OOP Representation |
|------------|-------------------|
| Car | Class |
| Audi/BMW | Objects |
| Dog | Class |
| Buddy/Lucy | Objects |
| Bank Account | Class |
| User Accounts | Objects |

---

# What is a Class?

A class is:

> A blueprint for creating objects.

A class contains:
- attributes (variables/properties)
- methods (functions/behaviors)

---

# Basic Class Syntax

```python
class ClassName:
    pass
```

---

## Example

```python
class Car:
    pass
```

---

## What is an Object?

An object is:

> An instance of a class.

---

## Creating Objects

```python
class Car:
    pass

audi = Car()
bmw = Car()
```

---

## Checking Object Type

```python
print(type(audi))
```

### Output

```python
<class '__main__.Car'>
```

---

## Printing Object

```python
print(audi)
```

### Output

```python
<__main__.Car object at memory_location>
```

---

## Attributes / Instance Variables

Attributes are:

> properties of an object

Examples:

- name
- age
- balance
- windows

---

## ⚠️ Bad Way of Creating Attributes

```python
audi.windows = 4
```

Why bad?

- inconsistent object structure
- difficult maintenance

---

## Constructor in Python

Very important concept.

---

## Constructor Method

```python
__init__()
```

This is called:

- constructor

---

## Purpose of Constructor

Used to:

- initialize object attributes
- set default values

---

## Constructor Syntax

```python
class Dog:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

---

## Meaning of self

`self` refers to:

- current object instance

Used to access:

- instance variables
- methods

---

## ⚠️ Important Note

`self` is NOT a keyword.

You can technically use another name, but:

- self is standard convention

---

## Creating Objects with Constructor

```python
dog1 = Dog("Spike", 7)
dog2 = Dog("Scooby Doo", 12)
```

---

## Accessing Attributes

```python
print(dog1.name)
print(dog1.age)
```

### Output

```python
Spike
7
```

---

## Instance Methods

Methods inside classes are called:

- instance methods

They define:

- behavior of objects

---

## Example

```python
class Dog:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    def bark(self):

        print(f"{self.name} says woof")
```

---

## Calling Methods

```python
dog1 = Dog("Spike", 7)

dog1.bark()
```

### Output

```python
Spike says woof
```

---

## dir() Function

Used to inspect:

- attributes
- methods
- built-in functionalities

### Example

```python
print(dir(dog1))
```

---

## Bank Account Example

Real-world OOP design example.

---

## Complete Program

```python
class BankAccount:

    def __init__(self, owner, balance=0):

        self.owner = owner
        self.balance = balance

    def deposit(self, amount):

        self.balance += amount

        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):

        if amount > self.balance:

            print("Insufficient funds")

        else:

            self.balance -= amount

            print(f"{amount} withdrawn. New balance: {self.balance}")

    def get_balance(self):

        return self.balance
```

---

## Creating Object

```python
account = BankAccount("Aahish", 50000)
```

---

## Accessing Balance

```python
print(account.balance)
```

### Output

```python
50000
```

---

## Deposit Money

```python
account.deposit(10000)
```

### Output

```python
10000 deposited. New balance: 60000
```

---

## Withdraw Money

```python
account.withdraw(3000)
```

### Output

```python
3000 withdrawn. New balance: 57000
```

---

## Get Final Balance

```python
print(account.get_balance())
```

### Output

```python
57000
```

---

## Important Concepts Covered

| Concept | Meaning |
|----------|----------|
| Class | blueprint |
| Object | instance of class |
| Constructor | initializes object |
| self | current object |
| Attributes | properties |
| Methods | behaviors |
| Instance Variable | object data |
| Instance Method | object functionality |

---

## Flow of Object Creation

```plaintext
Create Class
    ↓
Create Constructor
    ↓
Define Attributes
    ↓
Define Methods
    ↓
Create Object
    ↓
Call Methods
```

---

## Real-World Analogy — Car

### Class:

```python
Car
```

### Objects:

- Audi
- BMW
- Tesla

### Attributes:

- color
- speed
- doors

### Methods:

- start()
- stop()
- accelerate()

---

## Real-World Analogy — Student

### Class:

```python
Student
```

### Attributes:

- name
- roll_no
- marks

### Methods:

- study()
- attend_class()

---

## Important Notes About self

`self` allows access to:

- self.name
- self.balance
- self.age

inside methods.

Without self:

- instance variables cannot be accessed properly.

---

## Constructor Default Values

```python
def __init__(self, owner, balance=0):
```

If balance not provided:

- default balance = 0

---

## Key Advantages of OOPs

### 1. Reusability

Use same class to create multiple objects.

### 2. Better Organization

Code becomes modular.

### 3. Real-World Modeling

Easy representation of systems.

### 4.  Scalability

Large projects become manageable.

### 5.  Maintainability

Easy to debug and update.

---

## Common Mistakes

### Forgetting self

Wrong:

```python
def bark():
```

Correct:

```python
def bark(self):
```

---

### Forgetting Constructor Parameters

Wrong:

```python
Dog()
```

when constructor expects:

- name
- age

---

### Using Attributes Without self

Wrong:

```python
name = name
```

Correct:

```python
self.name = name
```

---

## 🧪 Practice Assignments

- Student Class
- Rectangle Class
- ATM Class
- Employee Class
- Book Class

---

## Core Things to Remember

| Concept | Remember |
|----------|-----------|
| Class | blueprint |
| Object | real instance |
| self | current object |
| init | constructor |
| Attributes | data |
| Methods | behavior |

---

## Best Practices

- Use constructors properly
- Keep classes modular
- Use meaningful method names
- Avoid unnecessary attributes
- Design reusable objects
