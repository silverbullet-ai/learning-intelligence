# Python Multiprocessing

## Overview

Multiprocessing allows multiple processes to execute simultaneously.

### Key Topics

- Process Creation
- start()
- join()
- CPU-Bound Tasks
- Parallel Execution
- GIL
- Process Isolation

### Example

```python
from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(i)

p = Process(target=print_numbers)
p.start()
p.join()
```

### Advantages

- True parallel execution
- Better CPU utilization
- Ideal for CPU-intensive workloads

### Limitations

- Higher memory usage
- Process creation overhead

## Common Mistake: Naming Your File multiprocessing.py

When working with the `multiprocessing` module, avoid naming your file:

```python
multiprocessing.py
```

Python searches for modules in the following order:

1. Current directory
2. Installed packages
3. Standard library

If your file is named:

```python
multiprocessing.py
```

then:

```python
import multiprocessing
```

imports your own file instead of Python's built-in module.

This creates a circular import problem.

### Example

File:

```python
multiprocessing.py
```

Code:

```python
import multiprocessing

print(multiprocessing.Process)
```

### Possible Error:

```markdown
AttributeError:
partially initialized module 'multiprocessing'
has no attribute 'Process'
```

### Why It Happens

```markdown
multiprocessing.py
        ↓
import multiprocessing
        ↓
imports itself
        ↓
circular import
```

### Fix

Rename the file:

`Bad`

```python
multiprocessing.py
```

`Good`

```python
multiprocessing_example.py
process_demo.py
multiprocessing_demo.py
```

Then remove:

```markdown
__pycache__/
```

or any generated:

```markdown
*.pyc
```

files before running again.

### Similar Names to Avoid

```markdown
threading.py
logging.py
json.py
time.py
random.py
numpy.py
pandas.py
matplotlib.py
seaborn.py
```

These names can shadow Python libraries and produce confusing import errors.

### Real-World Applications

- Machine Learning
- Data Analysis
- Scientific Computing
- Image Processing
- Video Rendering

### Practice Assignment (Solved)
#### Problem

Create two processes:

- Process 1 prints numbers
- Process 2 prints letters

Run both processes simultaneously.

Solution
```python
from multiprocessing import Process

def print_numbers():
    for i in range(5):
        print(i)

def print_letters():
    for letter in "ABCDE":
        print(letter)

p1 = Process(target=print_numbers)
p2 = Process(target=print_letters)

p1.start()
p2.start()

p1.join()
p2.join()

print("Completed")
```

### Key Takeaways

- Multiprocessing uses multiple processes.
- Each process has its own memory space.
- Processes run independently.
- Multiprocessing is best suited for CPU-bound workloads.
- It bypasses Python's GIL limitations.
- Processes are heavier than threads.

### Concepts Covered

- Multiprocessing
- Process Creation
- Process Lifecycle
- Main Process
- start()
- join()
- CPU-Bound Tasks
- Parallel Execution
- Process Isolation
- GIL
- Process Communication Basics