# Python OOPs — Inheritance

---

# What is Inheritance?

Inheritance is:

> A fundamental concept in Object Oriented Programming
> that allows a class to inherit attributes and methods
> from another class.

---

# Real-World Analogy

Inheritance works similar to real life.

Examples:
- children inherit parent properties
- child gets access to parent features

Similarly in Python:
- child class inherits parent attributes and methods

---

# Why Inheritance?

Inheritance helps in:
- code reusability
- avoiding duplicate code
- scalability
- maintainability
- extending functionality

---

# Basic Terminologies

| Concept | Meaning |
|---------|----------|
| Parent Class | Base Class |
| Child Class | Derived Class |
| Inheritance | Acquiring properties/methods |

---

# Parent Class Example

```python
class Car:

    def __init__(self, windows, doors, engine_type):

        self.windows = windows
        self.doors = doors
        self.engine_type = engine_type

    def drive(self):

        print(f"The person will drive the {self.engine_type} car")
```

---

## Creating Parent Object

```python
car1 = Car(4, 5, "petrol")
```

---

## Calling Parent Method

```python
car1.drive()
```

### Output

```python
The person will drive the petrol car
```

---

# Single Inheritance

Single inheritance means:

> One child class inherits one parent class

---

## Child Class Example — Tesla

```python
class Tesla(Car):
```

Here:

- Tesla inherits Car

---

## Tesla Class Complete Example

```python
class Tesla(Car):

    def __init__(self, windows, doors, engine_type, is_self_driving):

        super().__init__(windows, doors, engine_type)

        self.is_self_driving = is_self_driving

    def self_driving(self):

        print(f"Tesla supports self driving: {self.is_self_driving}")
```

---

# super() Keyword

Very important concept.

`super()` is used to:

- access parent class constructor
- access parent methods

---

## Meaning of This Line

```python
super().__init__(windows, doors, engine_type)
```

calls:

- parent class constructor

---

## Why Use super()?

Without `super()`:

- child class cannot initialize parent attributes properly

---

## Creating Tesla Object

```python
tesla1 = Tesla(4, 5, "electric", True)
```

---

## Calling Child Method

```python
tesla1.self_driving()
```

### Output

```python
Tesla supports self driving: True
```

---

## Calling Parent Method from Child Object

```python
tesla1.drive()
```

### Output

```python
The person will drive the electric car
```

---

# Important Understanding

Child class inherits:

- attributes
- methods

from parent class.

---

## Flow of Single Inheritance

```plaintext
Parent Class
    ↓
Child Class inherits Parent
    ↓
Child gets Parent Features
    ↓
Child can add Extra Features
```

---

# Multiple Inheritance

Multiple inheritance means:

> A class inherits from more than one base class

---

## Example Structure

```plaintext
Animal → Base Class 1
Pet    → Base Class 2

Dog    → Child Class
```

---

## Base Class 1 — Animal

```python
class Animal:

    def __init__(self, name):

        self.name = name

    def speak(self):

        print("Subclasses must implement this method")
```

---

## Base Class 2 — Pet

```python
class Pet:

    def __init__(self, owner):

        self.owner = owner
```

---

# Child Class with Multiple Inheritance

```python
class Dog(Animal, Pet):
```

Dog inherits:

- Animal
- Pet

---

## Complete Multiple Inheritance Example

```python
class Dog(Animal, Pet):

    def __init__(self, name, owner):

        Animal.__init__(self, name)
        Pet.__init__(self, owner)

    def speak(self):

        return f"{self.name} says woof"
```

---

# Important Point

In multiple inheritance:

`super()` becomes more complex

So direct parent calls are often used:

```python
Animal.__init__(self, name)
Pet.__init__(self, owner)
```

---

## Creating Object

```python
dog = Dog("Spike", "Aahish")
```

---

## Calling Method

```python
print(dog.speak())
```

### Output

```python
Spike says woof
```

---

## Accessing Parent Attribute

```python
print(dog.owner)
```

### Output

```python
Aahish
```

---

# Method Overriding

Very important concept.

---

## What is Method Overriding?

When child class defines:

- same method as parent class

child method gets higher priority.

---

## Example

Parent:

```python
def speak(self):
```

Child:

```python
def speak(self):
```

Child version executes first.

---

# Why?

Because:

- child class customizes parent behavior

---

## Important OOP Concepts Covered

| Concept | Meaning |
|----------|----------|
| Parent Class | base class |
| Child Class | derived class |
| Single Inheritance | one parent |
| Multiple Inheritance | multiple parents |
| super() | access parent |
| Method Overriding | redefine methods |

---

## Real-World Analogy — Vehicle System

### Parent:

```python
Vehicle
```

### Children:

- Car
- Bike
- Truck

### Shared Features:

- speed
- engine
- fuel

### Child Features:

- sports mode
- self-driving
- cargo system

---

## Real-World Analogy — Banking System

### Parent:

```python
Account
```

### Children:

- SavingsAccount
- CurrentAccount

---

## Real-World Analogy — Employee System

### Parent:

```python
Employee
```

### Children:

- Manager
- Developer
- Tester

---

# Advantages of Inheritance

### 1. Code Reusability

Reuse parent code.

### 2. Avoid Duplication

No need to rewrite same logic.

### 3.  Better Organization

Hierarchical structure.

### 4.  Easy Maintenance

Changes in parent affect all children.

### 5.  Extensibility

Easy to add features.

---

## Common Mistakes

### Forgetting Parent Constructor

Wrong:

```python
class Tesla(Car):

    def __init__(self):
        pass
```

Correct:

```python
super().__init__()
```

---

### Forgetting self

Wrong:

```python
def drive():
```

Correct:

```python
def drive(self):
```

---

### Not Passing Parent Parameters

Wrong:

```python
Tesla()
```

when constructor expects:

- windows
- doors
- engine_type

---

# Difference Between Single & Multiple Inheritance

| Feature | Single | Multiple |
|----------|---------|-----------|
| Parent Classes | One | More than one |
| Complexity | Simple | More complex |
| super() Usage | Easy | Careful handling needed |

---

## Practice Assignments

- Person → Student
- Vehicle → Bike
- Employee → Manager
- Animal + Pet → Cat
- Shape → Rectangle

---

# Core Things to Remember

| Concept | Remember |
|----------|-----------|
| Parent Class | reusable base |
| Child Class | extends parent |
| super() | parent access |
| Overriding | custom child behavior |
| Single Inheritance | one parent |
| Multiple Inheritance | multiple parents |

---

## Best Practices

- Reuse logic through inheritance
- Avoid unnecessary duplication
- Use overriding carefully
- Keep inheritance hierarchies simple
- Prefer composition when inheritance becomes too complex
