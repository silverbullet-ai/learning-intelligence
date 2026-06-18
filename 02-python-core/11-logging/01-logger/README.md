# Python Logging

## Overview

Logging is a mechanism used to record events that occur while a program is running.

It helps developers:

- Monitor application behavior
- Track program execution
- Debug issues
- Diagnose failures
- Maintain production systems

Python provides a built-in module called `logging` for handling application logs.

Unlike `print()`, logging allows different levels of messages and can store logs in files for later analysis.

---

## Importing Logging

```python
import logging
```

---

## Topics Covered

### Logging Basics

- logging module
- basicConfig()

### Logging Levels

- DEBUG
- INFO
- WARNING
- ERROR
- CRITICAL

### Log Message Formatting

- format
- datefmt

### File Logging

- filename
- filemode

Benefits:

- Module-wise logging
- Easier debugging
- Better organization
- Improved maintainability

Example:

```markdown
2026-06-01 | auth | INFO | User logged in
2026-06-01 | payment | ERROR | Payment failed
2026-06-01 | inventory | WARNING | Stock low
```

### Project Logging

- Centralized logger configuration
- Logging across multiple files

### Best Practices

- Logging vs print()
- Appropriate logging levels
- Production logging

---

## Logging Levels

Python provides multiple severity levels.

| Level    | Purpose                         |
| -------- | ------------------------------- |
| DEBUG    | Detailed diagnostic information |
| INFO     | General execution information   |
| WARNING  | Potential problem detected      |
| ERROR    | Operation failed                |
| CRITICAL | Severe failure                  |

### Severity Order

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

---

## Basic Configuration

Before generating log messages, configure logging.

```python
import logging

logging.basicConfig(
    level=logging.DEBUG
)
```

This determines:

- Minimum logging level
- Output destination
- Message formatting

---

## Creating Log Messages

### Debug

```python
logging.debug(
    "Debug message"
)
```

### Info

```python
logging.info(
    "Application started"
)
```

### Warning

```python
logging.warning(
    "Low disk space"
)
```

### Error

```python
logging.error(
    "Database connection failed"
)
```

### Critical

```python
logging.critical(
    "Application crashed"
)
```

---

## Custom Log Format

Customize log output using `format`.

```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s"
)
```

### Common Formatters

| Formatter     | Description |
| ------------- | ----------- |
| %(asctime)s   | Timestamp   |
| %(name)s      | Logger name |
| %(levelname)s | Log level   |
| %(message)s   | Log message |

---

## Custom Date Format

```python
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
```

### Common Date Symbols

| Symbol | Meaning |
| ------ | ------- |
| %Y     | Year    |
| %m     | Month   |
| %d     | Day     |
| %H     | Hour    |
| %M     | Minute  |
| %S     | Second  |

---

## Logging to a File

Store logs permanently in a file.

```python
import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
```

### Parameters

| Parameter    | Purpose        |
| ------------ | -------------- |
| filename     | Log file       |
| filemode="w" | Overwrite file |
| filemode="a" | Append to file |

---

## Example

```python
import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.DEBUG
)

logging.info("Application Started")
logging.warning("Low Memory")
logging.error("Database Error")
```

Generated file:

```text
app.log
```

---

## Project Structure

A common logging setup:

```text
project/
│
├── logs/
│   ├── app.log
│   └── logger.py
│
└── app.py
```

### logger.py

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s | %(message)s"
)
```

### app.py

```python
from logger import logging

logging.info(
    "Application Started"
)
```

---

## Logging vs Print

### Print

```python
print("Function Executed")
```

### Logging

```python
logging.info(
    "Function Executed"
)
```

Logging is preferred because:

- Supports severity levels
- Can write to files
- Easier debugging
- Better production monitoring

---

## Common Logging Methods

| Method                | Purpose             |
| --------------------- | ------------------- |
| logging.debug()       | Debug Messages      |
| logging.info()        | General Information |
| logging.warning()     | Warning Messages    |
| logging.error()       | Error Messages      |
| logging.critical()    | Critical Messages   |
| logging.basicConfig() | Configure Logging   |

---

## Real-World Applications

Logging is heavily used in:

- Web Applications
- APIs
- Data Pipelines
- Machine Learning Systems
- Monitoring & Alerting
- Enterprise Applications

Typical examples:

- User login tracking
- API request monitoring
- Database error tracking
- Model training logs
- Application health monitoring

---

## Practice Assignment (Solved)

### Problem

Create a logging system for a calculator application.

Log every multiplication operation into a file called `calculator.log`.

### Solution

```python
import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def multiply(a, b):
    result = a * b

    logging.info(
        f"{a} * {b} = {result}"
    )

    return result

print(multiply(5, 10))
```

### Generated Log

```text
2026-01-01 10:00:00 | INFO | 5 * 10 = 50
```

---

## Key Takeaways

- Logging is a professional alternative to print().
- Python provides a built-in logging module.
- Logging supports multiple severity levels.
- Logs can be written to files for monitoring and debugging.
- Custom formats improve readability.
- Logging is essential in production applications.

---

## Classes Reference

This module introduces:

- logging module
- basicConfig()
- Log Levels
- File Logging
- Custom Formatting
- Project Logging Structure
