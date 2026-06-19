# Multithreading in Python

## Overview

Multithreading is a technique that allows multiple threads to execute concurrently within the same process.

It is mainly used to:

* Improve application responsiveness
* Improve throughput
* Utilize waiting time efficiently
* Perform multiple tasks concurrently

Multithreading is particularly useful for I/O-bound operations.

---

## When to Use Multithreading?

### 1. I/O-Bound Tasks

I/O-bound tasks spend more time waiting than computing.

Examples:

* Reading files
* Writing files
* Downloading data
* API calls
* Database operations
* Network requests

During waiting periods, another thread can execute.

---

### 2. Concurrent Execution

When multiple independent tasks can run concurrently.

Examples:

* Downloading multiple files
* Handling multiple user requests
* Reading multiple files simultaneously
* Logging while processing data

Multithreading improves throughput by allowing tasks to progress together.

---

## Python Threading Module

Python provides the built-in `threading` module.

```python
import threading
```

---

## Creating Threads

Threads are created using the `Thread` class.

```python
import threading

thread = threading.Thread(
    target=my_function
)
```

### target Parameter

Specifies the function the thread should execute.

```python
threading.Thread(
    target=print_numbers
)
```

---

## Starting Threads

Use `start()` to begin execution.

```python
thread.start()
```

Example:

```python
t1.start()
t2.start()
```

---

## Waiting for Completion

Use `join()` to wait for a thread to finish.

```python
thread.join()
```

Example:

```python
t1.join()
t2.join()
```

The main thread waits until all worker threads complete execution.

---

## Thread Lifecycle

```text
Create Thread
      ↓
Start Thread
      ↓
Execute Task
      ↓
Join Thread
      ↓
Terminate
```

---

## Example

```python
import threading
import time


def print_numbers():
    for i in range(5):
        print(f"Number: {i}")
        time.sleep(2)


def print_letters():
    for letter in "ABCDE":
        print(f"Letter: {letter}")
        time.sleep(2)


t1 = threading.Thread(
    target=print_numbers
)

t2 = threading.Thread(
    target=print_letters
)

t1.start()
t2.start()

t1.join()
t2.join()

print("Done")
```

---

## Why Multithreading Helps

Consider:

```python
time.sleep(2)
```

While one thread is waiting:

```text
Thread 1
   Waiting...
```

Another thread can execute:

```text
Thread 2
   Running...
```

This reduces idle waiting time and improves throughput.

---

## Main Thread

Every Python program starts with one thread:

```text
Main Thread
```

Creating additional threads:

```text
Main Thread
    │
    ├── Thread 1
    ├── Thread 2
    └── Thread 3
```

The main thread typically waits for worker threads using:

```python
join()
```

before exiting.

---

## Important Methods

### Create Thread

```python
threading.Thread()
```

---

### Start Thread

```python
thread.start()
```

Starts execution.

---

### Join Thread

```python
thread.join()
```

Waits for completion.

---

### Sleep

```python
time.sleep(seconds)
```

Pauses execution temporarily.

---

## Advantages

* Better responsiveness
* Improved throughput
* Efficient handling of I/O operations
* Reduced waiting time
* Concurrent execution of independent tasks

---

## Limitations

* Not ideal for CPU-intensive tasks
* Thread synchronization issues may occur
* Shared memory can lead to race conditions
* Python's GIL limits true parallel CPU execution

Multiprocessing is often preferred for CPU-bound workloads.

---

## Real-World Applications

Multithreading is commonly used in:

* Web Servers
* File Download Managers
* API Clients
* Network Applications
* GUI Applications
* Logging Systems

Typical examples:

* Downloading multiple files simultaneously
* Handling multiple client requests
* Reading and writing files concurrently
* Background processing tasks

---

## Practice Assignment (Solved)

### Problem

Create two threads:

* One prints numbers from 1 to 5
* One prints letters A to E

Both should execute concurrently.

### Solution

```python
import threading
import time


def print_numbers():
    for i in range(1, 6):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in "ABCDE":
        print(letter)
        time.sleep(1)


t1 = threading.Thread(
    target=print_numbers
)

t2 = threading.Thread(
    target=print_letters
)

t1.start()
t2.start()

t1.join()
t2.join()

print("Completed")
```

---

## Key Takeaways

* Multithreading allows multiple threads to execute concurrently.
* Threads are lightweight compared to processes.
* Threads share the same memory space.
* The `threading` module provides thread support in Python.
* Use `start()` to begin execution and `join()` to wait for completion.
* Multithreading is best suited for I/O-bound tasks.
* Python's GIL limits true parallel CPU execution.

---

## Concepts Covered

* Concurrency
* Multithreading
* Thread Lifecycle
* Main Thread
* Thread Creation
* start()
* join()
* sleep()
* I/O-Bound Tasks
* Concurrent Execution
* Threading Module
* Thread Synchronization Basics
* GIL (Introduction)
