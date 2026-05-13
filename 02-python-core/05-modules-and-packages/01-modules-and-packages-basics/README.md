# Modules and Packages in Python

---

## Overview

Python has a massive ecosystem of:
- modules
- libraries
- packages

These help developers:
- reuse code
- avoid writing everything from scratch
- build scalable applications faster

---

# What are Modules?

A module is:

> A Python file containing functions, variables, or classes.

Example:

```python
math.py
```

---

## Why Modules Exist

Without modules:

- repeated code
- huge messy files
- poor organization

With modules:

- reusable code
- organized structure
- modular development

---

## What are Packages?

A package is:

A collection of modules organized in folders.

Packages help build:

- large applications
- scalable systems
- structured codebases

---

## Real Industry Insight

Large systems are built using:

- packages
- subpackages
- modules

layered together.

---

## Importing Modules

Basic syntax:

```python
import math
```

---

## Accessing Functions

```python
math.sqrt(16)
```

### Output

```python
4.0
```

---

## Import Specific Functions

Instead of importing entire module:

```python
from math import sqrt, pi
```

Now directly use:

```python
sqrt(25)
pi
```

---

## Important Understanding

```python
from module import function
```

means:

- import only specific things
- cleaner access
- less typing

---

## Viewing Available Functions

```python
math.
```

Shows:

- built-in methods
- constants
- functions

inside module.

---

## Import Everything (*)

```python
from math import *
```

Now directly use:

```python
sqrt(16)
```

without math.

---

## Important Note

Avoid overusing:

```python
import *
```

Why?

- namespace pollution
- difficult debugging
- unclear origins

---

## Aliasing Modules

Very common in industry.

### Syntax

```python
import numpy as np
```

---

## Why Use Alias?

Instead of:

```python
numpy.array()
```

write:

```python
np.array()
```

Cleaner and shorter.

---

## Industry Standard Aliases

| Module | Alias |
|--------|--------|
| numpy | np |
| pandas | pd |
| matplotlib.pyplot | plt |

---

## Installing Packages

Some packages are NOT installed by default.

Example:

```python
import numpy
```

may fail.

---

## Install Using pip

```bash
pip install numpy
```

---

## Install from requirements.txt

```bash
pip install -r requirements.txt
```

---

## What is requirements.txt?

A file containing project dependencies.

Example:

```txt
numpy
pandas
matplotlib
```

---

## Using NumPy Example

```python
import numpy as np

arr = np.array([1,2,3,4])
```

### Output

```python
array([1,2,3,4])
```

---

## Creating Your Own Module

Very important concept.

### File Structure

```plaintext
project/
│
├── maths.py
```

---

### maths.py

```python
def addition(a, b):

    return a + b
```

---

### Importing Custom Module

```python
from maths import addition
```

### Using

```python
addition(2,3)
```

### Output

```python
5
```

---

## Creating Packages

To make a folder a package:

Add `__init__.py`

---

### Structure

```plaintext
package/
│
├── __init__.py
├── maths.py
```

---

## 🔥 Why __init__.py Matters

It tells Python:

> “This folder should behave as a package.”

---

## Creating Subpackages

### Structure

```plaintext
package/
│
├── __init__.py
│
└── subpackage/
    ├── __init__.py
    └── mult.py
```

---

### mult.py

```python
def multiply(a,b):

    return a*b
```

---

### Importing from Subpackage

```python
from package.subpackage.mult import multiply
```

### Using

```python
multiply(4,5)
```

### Output

```python
20
```

---

## MOST IMPORTANT PACKAGE CONCEPT

Python recognizes folders as packages ONLY IF:

```python
__init__.py
```

exists.

---

## Running Python Files

Execute Python file:

```bash
python test.py
```

---

## Important

You must:

- navigate to correct folder
- run from proper directory

---

## Real-World Project Structure

```plaintext
project/
│
├── data/
├── preprocessing/
├── models/
├── training/
├── utils/
├── evaluation/
```

Each folder may itself be a package.

---

## Common Beginner Mistakes

### Forgetting __init__.py

Python won’t recognize package correctly.

---

### Wrong Import Path

```python
from package.math import add
```

Path must match folder structure.

---

### Installing Package Outside Environment

Very common issue.

---

### Importing Uninstalled Module

Example:

```python
ModuleNotFoundError
```

---

## Mental Model

| Concept | Real-Life Analogy |
|----------|-------------------|
| module | single toolbox |
| package | warehouse of toolboxes |

---

## Most Important Concepts

- Modules = Python files
- Packages = folders of modules
- __init__.py defines package
- import brings external code
- pip install installs packages
- Aliases simplify code

---

## Practice Assignments

- Create calculator module
- Create geometry package
- Create subpackage structure
- Use math module
- Install NumPy and test arrays

---

## Best Practices

- Organize related logic into modules
- Use packages for scalability
- Avoid import *
- Use aliases consistently
- Keep imports readable

