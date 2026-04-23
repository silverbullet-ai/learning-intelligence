# Python Basics – Loops

---

## Overview

Loops are used to execute a block of code multiple times.

Types covered:

- for loop
- while loop
- loop control statements (break, continue, pass)
- nested loops

---

## For Loop

### Definition

Used to iterate over a sequence (range, string, list, etc.)

---

### Basic Syntax

```python
for i in range(5):
    print(i)
```

Output:

```
0 1 2 3 4
```

---

## range() Explained

```
range(start, stop, step)
```

### Examples:

```
range(5)        # 0 to 4
range(1, 6)     # 1 to 5
range(1, 10, 2) # 1,3,5,7,9
```

---

## Reverse Loop

```python
for i in range(10, 0, -1):
    print(i)
```

---

## Loop Through String

```python
name = "Aahish"

for ch in name:
    print(ch)
```

---

## While Loop

### Definition

Executes while condition is True

### Example

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### Important

Always update the variable → otherwise infinite loop

---

## Loop Control Statements

### break

Exit loop immediately

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

---

### continue

Skip current iteration

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

---

### pass

Placeholder (does nothing)

```python
for i in range(5):
    if i == 3:
        pass
    print(i)
```

---

## Nested Loops

### Definition

Loop inside another loop

### Example

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

---

## Flow

- Outer loop runs  
- Inner loop completes fully each time  

---

## Practical Example – Sum of N Numbers

### While Loop

```python
n = 10
total = 0
count = 1

while count <= n:
    total += count
    count += 1

print(total)
```

---

### For Loop

```python
total = 0

for i in range(1, 11):
    total += i

print(total)
```

---

## Practical Example – Prime Numbers

```python
for num in range(1, 101):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
```

---

## Important Concept

👉 for...else runs when the loop does NOT break

---

## Common Errors

- Infinite loops (missing increment)  
- Incorrect range values  
- Indentation mistakes  
- Misuse of break/continue  

---

## Best Practices

- Use for when iterations are known  
- Use while for condition-based loops  
- Avoid deep nesting  
- Keep logic readable  
