# Python Exception Handling

---

## Overview

Exception handling in Python allows us to:
- handle errors gracefully
- prevent program crashes
- continue execution safely
- provide meaningful error messages

---

# What is an Exception?

An exception is:

> An event that disrupts the normal flow of a program.

---

# Why Exception Handling is Important

Without exception handling:
- programs crash immediately
- execution stops completely
- users see ugly error messages

With exception handling:
- errors are handled safely
- applications become reliable
- users get meaningful feedback

---

# Common Exceptions in Python

| Exception | Meaning |
|-----------|----------|
| `ZeroDivisionError` | division by zero |
| `NameError` | variable not defined |
| `ValueError` | invalid value |
| `TypeError` | wrong datatype |
| `FileNotFoundError` | file missing |
| `IndexError` | invalid index |
| `KeyError` | invalid dictionary key |

---

# Basic Try-Except Syntax

```python
try:

    # risky code

except:

    # error handling code
```

---

## Example — NameError

```python
try:

    a = b

except:

    print("Variable is not assigned")
```

### Output

```python
Variable is not assigned
```

---

## What Happened?

```python
a = b
```

raises:

```python
NameError
```

But instead of crashing:

- exception gets handled
- custom message displayed

---

## Catching Specific Exceptions

### Syntax

```python
try:

    risky code

except ExceptionType as variable:

    handling code
```

### Example

```python
try:

    a = b

except NameError as e:

    print(e)
```

### Output

```python
name 'b' is not defined
```

---

## Meaning of as e

```python
except NameError as e
```

stores exception message inside:

```python
e
```

---

## Example — ZeroDivisionError

```python
try:

    result = 10 / 0

except ZeroDivisionError as e:

    print(e)
    print("Denominator must be greater than zero")
```

---

## Multiple Exception Blocks

```python
try:

    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:

    print("Invalid number")

except ZeroDivisionError:

    print("Cannot divide by zero")
```

---

## Parent Exception Class

All exceptions derive from:

```python
Exception
```

### Example

```python
try:

    a = b

except Exception as e:

    print(e)
```

---

## Why Important?

Catches:

- ANY exception

Useful for:

- debugging
- generic handling

---

## ⚠️ Important Rule

Always place:

```python
except Exception
```

LAST.

Because it catches EVERYTHING.

---

## Else Block

### Syntax

```python
try:

    risky code

except:

    handling

else:

    success block
```

---

## Meaning of Else

Runs ONLY IF:

- no exception occurs

### Example

```python
try:

    num = int(input("Enter number: "))
    result = 10 / num

except ValueError:

    print("Invalid number")

except ZeroDivisionError:

    print("Cannot divide by zero")

else:

    print("Result =", result)
```

---

## Finally Block

VERY IMPORTANT.

### Syntax

```python
try:

    risky code

except:

    handling

finally:

    cleanup code
```

---

## Meaning of Finally

`finally` ALWAYS executes:

- whether error occurs or not

### Example

```python
try:

    num = int(input("Enter number: "))
    result = 10 / num

except ZeroDivisionError:

    print("Cannot divide by zero")

finally:

    print("Execution complete")
```

---

## Real-World Importance of Finally

Used for:

- closing files
- closing database connections
- releasing resources
- closing network connections

---

## Complete Flow

```plaintext
try
 ↓
exception?
 ↓
yes → except
no  → else
 ↓
finally always executes
```

---

## File Handling + Exception Handling

Very important real-world example.

```python
try:

    file = open("example.txt", "r")

    content = file.read()

    print(content)

except FileNotFoundError:

    print("File does not exist")

finally:

    if 'file' in locals() and not file.closed:

        file.close()

        print("File closed")
```

---

## Meaning of locals()

```python
locals()
```

returns:

- dictionary of local variables

Used to check:

- whether variable exists or not

---

## Real-World Applications

Exception handling is heavily used in:

- banking systems
- backend APIs
- AI systems
- payment gateways
- login systems
- file processing systems

---

## Best Practices

### Catch Specific Exceptions

GOOD:

```python
except ZeroDivisionError:
```

BAD:

```python
except:
```

---

### Use Finally for Cleanup

Always close:

- files
- APIs
- database connections

---

### Provide Meaningful Messages

Instead of:

```python
division by zero
```

show:

```python
Please enter denominator greater than zero
```

---

### Use Generic Exception Carefully

```python
except Exception as e:
```

Useful for:

- debugging
- unknown errors

---

## Common Mistakes

### Wrong Exception Order

```python
except Exception:
except ValueError:
```

Wrong because generic exception catches everything first.

---

### Using Bare except

```python
except:
```

Bad practice.

---

### Not Closing Files

Can cause:

- memory leaks
- locked resources

---

## Practice Assignments

- Safe Calculator
- File Reader
- Login Validation System
- List Index Handler
- Dictionary Key Handler

---

## Core Keywords

| Keyword | Purpose |
|----------|----------|
| try | risky code |
| except | handle error |
| else | runs if no error |
| finally | always executes |

---

## Best Practices

- Handle specific exceptions first
- Keep error messages meaningful
- Always clean up resources
- Use finally for critical cleanup
- Avoid hiding all exceptions blindly
