# Python Standard Library — Definitions & Syntax

---

# array Module

## Definition
Used for:
- creating arrays
- storing same datatype elements efficiently

## Import
```python
import array
```

## Syntax
```python
arr = array.array('i', [1, 2, 3, 4])
```

---

# math Module

## Definition
Provides:
- mathematical operations
- constants
- advanced math functions

## Import
```python
import math
```

## Syntax
```python
math.sqrt(16)
math.pi
math.ceil(4.2)
math.floor(4.8)
math.factorial(5)
math.pow(2, 3)
```

---

# random Module

## Definition
Used for:
- generating random values
- games
- simulations
- password generators

## Import
```python
import random
```

## Syntax
```python
random.randint(1, 10)

random.choice(["apple", "banana", "cherry"])
```

---

# os Module

## Definition
Used for:
- file handling
- directory management
- system operations

## Import
```python
import os
```

## Syntax
```python
os.getcwd()

os.mkdir("test_dir")

os.listdir()

os.remove("file.txt")

os.rmdir("folder_name")
```

---

# shutil Module

## Definition
Used for:
- advanced file operations
- copying files
- moving files

## Import
```python
import shutil
```

## Syntax
```python
shutil.copyfile("source.txt", "destination.txt")
```

---

# json Module

## Definition
Used for:
- API data handling
- JSON conversion
- data exchange

## Import
```python
import json
```

## Syntax
```python
data = {
    "name": "Aahish",
    "age": 23
}

json_str = json.dumps(data)

parsed_data = json.loads(json_str)
```

---

# csv Module

## Definition
Used for:
- CSV file handling
- tabular data
- spreadsheet operations

## Import
```python
import csv
```

## Syntax
```python
with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["name", "age"])
    writer.writerow(["Aahish", 23])
```

```python
with open("example.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)
```

---

# datetime Module

## Definition
Used for:
- dates
- time calculations
- scheduling
- timestamps

## Import
```python
from datetime import datetime, timedelta
```

## Syntax
```python
now = datetime.now()

yesterday = now - timedelta(days=1)
```

---

# time Module

## Definition
Used for:
- delays
- timers
- execution timing

## Import
```python
import time
```

## Syntax
```python
time.time()

time.sleep(2)
```

---

# re Module (Regular Expressions)

## Definition
Used for:
- pattern matching
- validation
- searching text
- extracting data

## Import
```python
import re
```

## Syntax
```python
pattern = r"\d+"

text = "There are 123 apples"

match = re.search(pattern, text)

print(match.group())
```

---

# Important Regex Patterns

| Pattern | Meaning |
|---|---|
| `\d` | digit |
| `\w` | word character |
| `\s` | whitespace |
| `.` | any character |
| `+` | one or more |
