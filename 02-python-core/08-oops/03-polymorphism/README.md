# Python OOPs — Polymorphism

---

# What is Polymorphism?

Polymorphism is:

> A core concept in Object Oriented Programming
> that allows objects of different classes
> to be treated as objects of a common superclass.

---

# Simple Meaning

If we split the word:

* Poly = Many
* Morph = Forms

So:

> Polymorphism means "many forms"

---

# Core Idea

Same method:

* different behavior

depending on:

* object
* class
* implementation

---

# Real World Example — Animal Sounds

Method:

* speak()

Dog:

* Woof

Cat:

* Meow

Same method:

* speak()

Different outputs:

* Woof / Meow

---

# Polymorphism Through Method Overriding

Most common type of polymorphism.

---

# What is Method Overriding?

Child class provides its own implementation
of a parent class method.

---

# Base Class Example

```python
class Animal:

    def speak(self):

        return "Sound of the animal"
```

---

# Derived Class — Dog

```python
class Dog(Animal):

    def speak(self):

        return "Woof!"
```

---

# Derived Class — Cat

```python
class Cat(Animal):

    def speak(self):

        return "Meow!"
```

---

# Creating Objects

```python
dog = Dog()
cat = Cat()
```

---

# Calling Methods

```python
print(dog.speak())
print(cat.speak())
```

### Output

```python
Woof!
Meow!
```

---

# Understanding What Happened

Parent class:

* speak()

Child classes:

* override the same method
* provide different implementations

This is:

* polymorphism

---

# Visual Understanding

```plaintext
Animal
   ↓
speak()

Dog → "Woof"
Cat → "Meow"
```

---

# Function Demonstrating Polymorphism

```python
def animal_speak(animal):

    print(animal.speak())
```

---

# Calling Function

```python
animal_speak(dog)
animal_speak(cat)
```

### Output

```python
Woof!
Meow!
```

---

# Why This is Powerful?

Same function:

* animal_speak()

works for:

* Dog object
* Cat object
* any Animal subclass

---

# Polymorphism with Functions & Methods

Another important example.

---

# Base Class — Shape

```python
class Shape:

    def area(self):

        return "Area of the figure"
```

---

# Derived Class — Rectangle

```python
class Rectangle(Shape):

    def __init__(self, width, height):

        self.width = width
        self.height = height

    def area(self):

        return self.width * self.height
```

---

# Derived Class — Circle

```python
class Circle(Shape):

    def __init__(self, radius):

        self.radius = radius

    def area(self):

        return 3.14 * self.radius * self.radius
```

---

# Polymorphic Function

```python
def print_area(shape):

    print(f"Area is {shape.area()}")
```

---

# Creating Objects

```python
rectangle = Rectangle(4, 5)
circle = Circle(3)
```

---

# Calling Function

```python
print_area(rectangle)
print_area(circle)
```

### Output

```python
Area is 20
Area is 28.26
```

---

# Important Understanding

Same function:

* print_area()

works differently for:

* Rectangle
* Circle

because each class implements:

* area()

differently.

---

# Abstract Base Classes (ABC)

Very important concept.

---

# What is Abstract Base Class?

A class used to define common methods
for related classes.

---

# Why Use ABC?

To:

* enforce consistency
* force method implementation
* create common interfaces

---

# Importing ABC

```python
from abc import ABC, abstractmethod
```

---

# Abstract Class Example

```python
class Vehicle(ABC):
```

---

# Abstract Method

```python
@abstractmethod
def start_engine(self):
    pass
```

---

# Important Understanding

Abstract methods:

* do not contain implementation

They act like:

* rules/contracts

---

# Child Class — Car

```python
class Car(Vehicle):

    def start_engine(self):

        return "Car engine started"
```

---

# Child Class — Motorcycle

```python
class Motorcycle(Vehicle):

    def start_engine(self):

        return "Motorcycle engine started"
```

---

# Creating Objects

```python
car = Car()
bike = Motorcycle()
```

---

# Calling Methods

```python
print(car.start_engine())
print(bike.start_engine())
```

### Output

```python
Car engine started
Motorcycle engine started
```

---

# Understanding ABC Properly

Parent abstract class:

* defines WHAT must exist

Child classes:

* define HOW it works

---

# Types of Polymorphism in Python

| Type                        | Description                      |
| --------------------------- | -------------------------------- |
| Method Overriding           | child redefines parent method    |
| Duck Typing                 | behavior matters                 |
| Operator Overloading        | same operator different behavior |
| Abstract Class Polymorphism | enforced implementation          |

---

# Operator Overloading Example

```python
print(2 + 3)
```

### Output

```python
5
```

---

# String Example

```python
print("Hello " + "World")
```

### Output

```python
Hello World
```

Same operator:

* +

Different behavior:

* integer addition
* string concatenation

This is also:

* polymorphism

---

# Advantages of Polymorphism

## 1. Flexibility

Same code works for different objects.

---

## 2. Reusability

Reusable functions.

---

## 3. Extensibility

Easy to add new classes.

---

## 4.  Maintainability

Cleaner architecture.

---

## 5.  Scalability

Helps in large applications.

---

# Common Mistakes

## Forgetting Method Override

```python
class Dog(Animal):
    pass
```

No custom behavior added.

---

## Forgetting self

Wrong:

```python
def speak():
```

Correct:

```python
def speak(self):
```

---

## Abstract Method Not Implemented

If child class does not implement:

* start_engine()

object creation fails.

---

# Difference Between Inheritance & Polymorphism

| Inheritance           | Polymorphism                   |
| --------------------- | ------------------------------ |
| Acquiring features    | Same method different behavior |
| Parent-child relation | Multiple forms                 |
| Code reuse            | Flexible behavior              |

---

# Real Industry Examples

## Payment Systems

Method:

* pay()

Classes:

* CreditCard
* UPI
* PayPal
* Crypto

Each class:

* implements pay() differently

---

## Notification System

Method:

* send()

Classes:

* EmailNotification
* SMSNotification
* PushNotification

---

## ML Frameworks

Method:

* fit()

Different ML models:

* LinearRegression
* DecisionTree
* RandomForest

All behave differently.

---

# Core Interview Understanding

If interviewer asks:

> What is polymorphism?

Best answer:

> Polymorphism allows the same method or interface
> to behave differently for different objects/classes.

---

# Practice Assignments

1. Vehicle System
2. Employee Salary
3. Shapes Area
4. Animal Sounds
5. Payment Gateway

---

# Core Things to Remember

| Concept           | Remember                      |
| ----------------- | ----------------------------- |
| Polymorphism      | many forms                    |
| Method Overriding | child custom behavior         |
| Same Method       | different outputs             |
| ABC               | enforce method implementation |
| Flexibility       | key advantage                 |

---

# Best Practices

* Use common interfaces
* Override methods meaningfully
* Avoid duplicate logic
* Use ABCs for large systems
* Keep designs modular
