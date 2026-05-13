# Python Basics – Control Flow (Conditional Statements)

---

## Overview

Control flow determines how a program executes based on conditions.

Concepts covered:

- if
- else
- elif
- nested conditions

---

## if Statement

### Definition

Executes a block only if the condition is True.

### Example

```python
age = 20

if age >= 18:
    print("You can vote")
```

---

## else Statement

### Definition

Executes when the if condition is False.

### Example

```python
age = 16

if age >= 18:
    print("Eligible for voting")
else:
    print("You are a minor")
```

---

## elif Statement

### 📌 Definition

Used to check multiple conditions.

### 🧩 Example

```python
age = 20

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
```

---

## Flow Logic

- Conditions are checked top to bottom  
- First True condition executes  
- Remaining conditions are skipped  

---

## Nested Conditional Statements

### Definition

An if inside another if.

### Example

```python
num = int(input("Enter number: "))

if num > 0:
    print("Positive")

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Zero or Negative")
```

---

## Key Idea

- Outer condition runs first  
- Inner condition runs only if outer is True  

---

## Practical Example – Leap Year

```python
year = int(input("Enter year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
```

---

## Common Errors

### Missing Colon

```python
if age > 18   # ERROR
```

### Wrong Indentation

```python
if age > 18:
print("Hello")  # ERROR
```

### Logical Mistakes

- Incorrect condition order  
- Missing elif  
- Improper nesting  

---

## Best Practices

- Keep conditions simple and readable  
- Maintain proper indentation  
- Avoid deep unnecessary nesting  
- Use meaningful conditions  

---

## Quick Revision

- if → checks condition  
- else → fallback  
- elif → multiple conditions  
- Nested → conditions inside conditions  
- Indentation defines structure  
