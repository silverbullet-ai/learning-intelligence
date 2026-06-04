# Python OOPs — Encapsulation

---

# What is Encapsulation?

Encapsulation is:

> The concept of wrapping data (variables) and methods together into a single unit.

In OOP:

> Data + Methods = Class

---

# Simple Meaning

Think about:

- Washing Machine
- ATM Machine
- Car

You can:

Press buttons

Use features

Cannot directly access internal circuitry

This is exactly:

> Encapsulation

---

# Official Definition

Encapsulation:

> Bundles data and methods together and restricts direct access to some object components.

### Purpose

- Protect data
- Prevent accidental modification
- Improve security
- Improve maintainability

---

# Why Encapsulation?

Without encapsulation:

```python
person.age = -500
```

Anyone can modify data incorrectly.

With encapsulation:

- Setter methods validate data before modification.
- Data remains protected.

---

# Access Modifiers in Python

Python supports three levels of access.

| Type | Symbol |
|--------|--------|
| Public | variable |
| Protected | _variable |
| Private | __variable |

---

# 1. Public Variables

Most open access level.

## Example

```python
class Person:

    def __init__(self, name, age):

        self.name = name
        self.age = age
```

### Creating Object

```python
person = Person("Aahish", 23)
```

### Accessing Variables

```python
print(person.name)
print(person.age)
```

### Output

```python
Aahish
23
```

### Characteristics

✅ Accessible everywhere

✅ Accessible outside class

✅ Accessible inside class

✅ Accessible in child class

---

# 2. Private Variables

Private variables cannot be directly accessed outside the class.

## Syntax

```python
__variable
```

---

## Example

```python
class Person:

    def __init__(self, name, age):

        self.__name = name
        self.__age = age
```

---

### Object Creation

```python
person = Person("Aahish", 23)
```

---

### Direct Access

```python
print(person.__name)
```

### Output

```python
AttributeError
```

---

# Name Mangling

Python internally changes:

```python
__name
```

to

```python
_Person__name
```

and

```python
__age
```

to

```python
_Person__age
```

---

### Using dir()

```python
print(dir(person))
```

Output will contain:

```python
_Person__name
_Person__age
```

---

### Characteristics

✅ Accessible inside class

❌ Not directly accessible outside class

❌ Not directly accessible in child class

---

# 3. Protected Variables

Protected variables use:

```python
_variable
```

Single underscore.

---

## Example

```python
class Person:

    def __init__(self, name):

        self._name = name
```

---

### Child Class

```python
class Employee(Person):
    pass
```

---

### Access

```python
employee = Employee("Aahish")

print(employee._name)
```

### Output

```python
Aahish
```

---

### Characteristics

✅ Accessible inside class

✅ Accessible in child class

⚠️ Should not be accessed directly outside class

---

# Public vs Protected vs Private

| Access Level | Outside Class | Child Class |
|-------------|--------------|-------------|
| Public | ✅ | ✅ |
| Protected | ⚠️ Possible but discouraged | ✅ |
| Private | ❌ | ❌ |

---

# Getter and Setter Methods

One of the most important interview topics.

---

# Why Getters and Setters?

Private variables cannot be accessed directly.

Therefore:

- Getter → Read data
- Setter → Modify data

---

## Example Class

```python
class Person:

    def __init__(self, name, age):

        self.__name = name
        self.__age = age
```

---

# Getter Method

```python
def get_name(self):

    return self.__name
```

### Usage

```python
print(person.get_name())
```

### Output

```python
Aahish
```

---

# Setter Method

```python
def set_name(self, name):

    self.__name = name
```

### Usage

```python
person.set_name("Aayan")
```

---

### Updated Value

```python
print(person.get_name())
```

Output:

```python
Aayan
```

---

# Validation with Setter

```python
def set_age(self, age):

    if age > 0:

        self.__age = age

    else:

        print("Age cannot be negative")
```

---

### Valid Input

```python
person.set_age(22)
```

---

### Invalid Input

```python
person.set_age(-5)
```

Output:

```python
Age cannot be negative
```

---

# Complete Example

```python
class Person:

    def __init__(self, name, age):

        self.__name = name
        self.__age = age

    def get_name(self):

        return self.__name

    def get_age(self):

        return self.__age

    def set_name(self, name):

        self.__name = name

    def set_age(self, age):

        if age > 0:

            self.__age = age

        else:

            print("Age cannot be negative")
```

---

# Using the Class

```python
person = Person("Aahish", 23)

print(person.get_name())

print(person.get_age())

person.set_age(22)

print(person.get_age())

person.set_age(-5)
```

### Output

```python
Aahish
23
22
Age cannot be negative
```

---

# Real-World Example — ATM Machine

Private Data:

- Balance
- PIN
- Account Details

User cannot directly do:

```python
account.balance = 1000000
```

Instead:

- withdraw()
- deposit()
- check_balance()

provide controlled access.

---

# Real-World Example — Washing Machine

Visible:

- Start Button
- Mode Selection
- Timer

Hidden:

- Motor Logic
- Water Control Logic
- Electrical Components

This is encapsulation.

---

# Advantages of Encapsulation

## 1.  Data Hiding

Protects sensitive information.

---

## 2.  Better Security

Prevents accidental modifications.

---

## 3.  Better Validation

Setter methods validate input.

---

## 4.  Improved Maintainability

Internal changes remain hidden.

---

## 5.  Better Reusability

Classes become modular and reusable.

---

# Common Interview Questions

### What is Encapsulation?

Encapsulation is the process of wrapping data and methods together into a single unit and restricting direct access to internal data.

---

### Why Use Encapsulation?

- Protect data
- Improve security
- Controlled access
- Better maintainability

---

### Difference Between Public and Private Variables

| Public | Private |
|----------|----------|
| Accessible everywhere | Hidden outside class |
| No restriction | Controlled access |

---

### What are Getters and Setters?

| Method | Purpose |
|----------|----------|
| Getter | Retrieve data |
| Setter | Modify data |

---

# Practice Assignments

### 1. Bank Account System

Create:

- Private balance
- Private account number

Methods:

- deposit()
- withdraw()
- get_balance()

---

### 2. Student System

Private:

- name
- marks

Validation:

- Marks between 0 and 100

---

### 3. Employee System

Private:

- salary

Validation:

- Salary cannot be negative

---

### 4. ATM Simulation

Private:

- pin
- balance

Methods:

- change_pin()
- withdraw()
- deposit()

---

### 5. Product Inventory

Private:

- quantity

Validation:

- Quantity cannot be negative

---

# Quick Revision

| Concept | Symbol |
|----------|----------|
| Public | variable |
| Protected | _variable |
| Private | __variable |
| Getter | Read private data |
| Setter | Modify private data |
| Encapsulation | Data + Methods together |

---

# One-Line Summary

> Encapsulation protects data by hiding internal implementation details and allowing controlled access through methods such as getters and setters.