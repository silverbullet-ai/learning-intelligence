# Python OOPs — Abstraction

---

# What is Abstraction?

Abstraction is:

> The process of hiding complex implementation details and showing only the essential features of an object.

---

# Simple Meaning

As a user:

You should know:

✅ What something does

You do NOT need to know:

❌ How it does it internally

This is:

> Abstraction

---

# Official Definition

Abstraction is the concept of hiding complex implementation details and exposing only the necessary functionality.

---

# Why Do We Need Abstraction?

Abstraction helps us:

- Reduce complexity
- Improve maintainability
- Improve readability
- Focus on functionality
- Hide implementation details

---

# Real World Example — Washing Machine

Visible to User:

- Start Button
- Stop Button
- Timer
- Wash Mode
- Dryer Option

Hidden:

- Motor Control Logic
- Water Management
- Drum Rotation Algorithms
- Electrical Circuits

User simply presses:

```plaintext
Start
```

and clothes get washed.

This is abstraction.

---

# Real World Example — Mobile Phone

You click:

```plaintext
Camera App
```

Photo is taken.

Hidden details:

- Sensor Communication
- Image Processing
- Compression Algorithms
- Memory Allocation

---

# Real World Example — Laptop

You click:

```plaintext
Shutdown
```

Hidden details:

- Process Termination
- Memory Cleanup
- File Flushing
- Hardware Signaling

---

# Abstraction in Python

Python provides abstraction through:

```python
ABC
```

which stands for:

```plaintext
Abstract Base Class
```

---

# Importing ABC

```python
from abc import ABC, abstractmethod
```

---

# What is an Abstract Class?

An abstract class is:

> A blueprint class that contains abstract methods and may contain normal methods.

---

# Characteristics

✅ Cannot be instantiated directly

✅ Intended to be inherited

✅ Defines rules for child classes

---

# Creating an Abstract Class

```python
from abc import ABC

class Vehicle(ABC):
    pass
```

---

# Why Inherit ABC?

```python
class Vehicle(ABC)
```

tells Python:

> This class is an Abstract Base Class.

---

# What is an Abstract Method?

An abstract method is:

> A method declaration without implementation.

---

# Syntax

```python
@abstractmethod
def method_name(self):
    pass
```

---

# Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass
```

---

# Understanding This

Vehicle class says:

> Every vehicle must have a start_engine() method.

But it does NOT define:

> How it starts.

That responsibility belongs to child classes.

---

# Child Class Example — Car

```python
class Car(Vehicle):

    def start_engine(self):

        print("Car engine started")
```

---

# Creating Object

```python
car = Car()
```

---

# Calling Method

```python
car.start_engine()
```

### Output

```python
Car engine started
```

---

# What Happened?

Parent class:

```python
start_engine()
```

defined the rule.

Child class:

```python
Car
```

provided the implementation.

---

# Visual Representation

```plaintext
Vehicle
   │
   └── start_engine()  ← abstract
            │
            ▼
          Car
            │
            └── "Car engine started"
```

---

# Abstract Class with Normal Methods

Abstract classes may contain:

- Abstract Methods
- Normal Methods

---

## Example

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):

    def drive(self):

        print("Vehicle is used for driving")

    @abstractmethod
    def start_engine(self):
        pass
```

---

## Child Class

```python
class Car(Vehicle):

    def start_engine(self):

        print("Car engine started")
```

---

## Usage

```python
car = Car()

car.drive()
car.start_engine()
```

### Output

```python
Vehicle is used for driving
Car engine started
```

---

# Key Understanding

Parent provides:

```python
drive()
```

already implemented.

Child must implement:

```python
start_engine()
```

because it is abstract.

---

# Demonstration Function

```python
def operate_vehicle(vehicle):

    vehicle.start_engine()
```

---

## Usage

```python
car = Car()

operate_vehicle(car)
```

Output:

```python
Car engine started
```

---

# Why is This Abstraction?

Because:

```python
operate_vehicle()
```

does not care:

- how engine starts
- what vehicle type it is

It only knows:

```python
start_engine()
```

must exist.

---

# What Happens If Child Doesn't Implement?

```python
class Car(Vehicle):
    pass
```

Then:

```python
car = Car()
```

Produces:

```python
TypeError
```

because abstract methods remain unimplemented.

---

# Real Industry Examples

## Payment Gateway

Abstract Class:

```python
Payment
```

Method:

```python
pay()
```

Implementations:

- UPI
- Credit Card
- PayPal

---

## Notification System

Abstract Class:

```python
Notification
```

Method:

```python
send()
```

Implementations:

- EmailNotification
- SMSNotification
- PushNotification

---

## Database Systems

Abstract Class:

```python
Database
```

Method:

```python
connect()
```

Implementations:

- MySQL
- PostgreSQL
- MongoDB

---

# Advantages of Abstraction

## 1.  Reduces Complexity

Users see only required functionality.

---

## 2.  Improves Security

Implementation remains hidden.

---

## 3.  Better Maintainability

Internal code can change without affecting users.

---

## 4. Better Scalability

Easy to add new implementations.

---

## 5.  Standardized Design

All child classes follow common rules.

---

# Abstraction vs Encapsulation

| Abstraction | Encapsulation |
|------------|---------------|
| Hides implementation | Hides data |
| Focuses on functionality | Focuses on protection |
| Uses abstract classes | Uses access modifiers |
| "What to do" | "How to protect" |

---

# Easy Memory Trick

### Abstraction

What can I do?

Examples:

- Start Engine
- Make Payment
- Send Email

### Encapsulation

How is data protected?

Examples:

- Private Balance
- Private Password
- Private PIN

---

# Common Interview Questions

### What is Abstraction?

Abstraction is the process of hiding implementation details and exposing only essential functionality.

---

### How is Abstraction Achieved in Python?

Using:

- ABC
- @abstractmethod

from:

```python
abc
```

module.

---

### What is an Abstract Class?

A class containing one or more abstract methods that acts as a blueprint for child classes.

---

### Can Abstract Classes Have Normal Methods?

`Yes`

Example:

```python
drive()
```

---

### Can We Create Objects of Abstract Classes?

`No`

```python
vehicle = Vehicle()
```

Not allowed.

---

# Practice Assignments

1. Animal System
2. Payment Gateway
3. Employee System
4. Shape System
5. Vehicle System

---

# Quick Revision

| Concept | Meaning |
|----------|----------|
| Abstraction | Hide complexity |
| ABC | Abstract Base Class |
| @abstractmethod | Method without implementation |
| Child Class | Provides implementation |
| Goal | Show essential features only |

---

# One-Line Summary

> Abstraction hides complex implementation details and exposes only the essential functionality, making software simpler, cleaner, and easier to maintain.