# Multiple Loggers in Python (`logging` Module)

## Overview

In small applications, a single logger may be sufficient. However, in large-scale applications, different modules or components often maintain their own loggers to improve organization, debugging, and log management.

Python's `logging` module allows the creation of multiple named loggers using the `getLogger()` method.

---

## Creating a Named Logger

```python
import logging

logger = logging.getLogger("authentication")
```

### Explanation

* `getLogger()` creates or retrieves a logger instance.
* `"authentication"` is the name of the logger.
* If a logger with the same name already exists, Python returns the existing logger instead of creating a new one.
* Named loggers help identify which module generated a log message.

---

## Why Use Multiple Loggers?

### 1. Better Organization

Each module can have its own logger.

Example:

```python
auth_logger = logging.getLogger("authentication")
db_logger = logging.getLogger("database")
api_logger = logging.getLogger("api")
```

Logs become easier to understand because each message is associated with a specific component.

---

### 2. Easier Debugging

When an issue occurs, developers can quickly identify the source module.

Example:

```python
auth_logger.error("Invalid credentials")
db_logger.error("Database connection failed")
```

Output:

```text
authentication - ERROR - Invalid credentials
database - ERROR - Database connection failed
```

---

### 3. Different Logging Levels per Module

Each logger can have its own logging level.

```python
auth_logger.setLevel(logging.DEBUG)
db_logger.setLevel(logging.ERROR)
```

Behavior:

* Authentication logs DEBUG and above.
* Database logs only ERROR and CRITICAL messages.

---

### 4. Separate Log Files

Different loggers can write to different files.

```python
auth_handler = logging.FileHandler("auth.log")
db_handler = logging.FileHandler("database.log")

auth_logger.addHandler(auth_handler)
db_logger.addHandler(db_handler)
```

Result:

```text
auth.log      -> Authentication logs
database.log  -> Database logs
```

---

## Example Project Structure

```text
project/
│
├── authentication.py
├── database.py
├── api.py
└── main.py
```

### authentication.py

```python
import logging

logger = logging.getLogger("authentication")

def login():
    logger.info("User logged in")
```

### database.py

```python
import logging

logger = logging.getLogger("database")

def connect():
    logger.info("Database connected")
```

### main.py

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s"
)

from authentication import login
from database import connect

login()
connect()
```

Output:

```text
authentication - INFO - User logged in
database - INFO - Database connected
```

---

## Logger Hierarchy

Loggers can be organized hierarchically using dot notation.

```python
logger = logging.getLogger("app.authentication")
```

Examples:

```python
app
├── app.authentication
├── app.database
└── app.api
```

Benefits:

* Child loggers inherit configuration from parent loggers.
* Easier centralized management.

Example:

```python
parent = logging.getLogger("app")
child = logging.getLogger("app.authentication")
```

The child logger inherits settings from `app`.

---

## Best Practices

### Use `__name__`

Instead of hardcoding names:

```python
logger = logging.getLogger(__name__)
```

Benefits:

* Automatically uses the module name.
* Makes code reusable.
* Avoids naming mistakes.

Example:

```python
# authentication.py

logger = logging.getLogger(__name__)
```

Logger name becomes:

```text
authentication
```

---

### Configure Logging Once

Logging configuration should typically be done only in the application's entry point.

```python
logging.basicConfig(...)
```

Avoid configuring logging repeatedly in every module.

---

### Keep Logger Names Meaningful

Good:

```python
logging.getLogger("authentication")
logging.getLogger("database")
logging.getLogger("api")
```

Avoid:

```python
logging.getLogger("logger1")
logging.getLogger("test")
```

---

## Key Points

* Multiple loggers help organize logs in large applications.
* Create named loggers using `logging.getLogger(name)`.
* Each module can maintain its own logger.
* Different loggers can have different levels and handlers.
* Logger names appear in log messages, making debugging easier.
* Use `__name__` for scalable and maintainable applications.
* Hierarchical logger names (e.g., `app.database`) support inheritance and centralized configuration.
