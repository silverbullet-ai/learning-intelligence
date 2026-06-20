# Concurrency Comparison

## Overview

Python provides multiple approaches for concurrent execution:

- Multithreading
- Multiprocessing
- ThreadPoolExecutor
- ProcessPoolExecutor

Choosing the correct approach depends on the nature of the task.

---

# Concurrency vs Parallelism

## Concurrency

Concurrency means multiple tasks make progress during overlapping periods of time.

Tasks may switch between each other.

### Example

```text
Task A
Task B
Task A
Task B
```

## Parallelism

Parallelism means multiple tasks execute simultaneously.

### Example

```text
CPU Core 1 → Task A
CPU Core 2 → Task B
```

Both tasks run at the same time.

---

# CPU-Bound vs I/O-Bound Tasks

## CPU-Bound Tasks

Spend most time performing computations.

### Examples

- Prime Number Calculation
- Matrix Multiplication
- Machine Learning Training
- Video Encoding
- Image Processing

### Recommended

- Multiprocessing
- ProcessPoolExecutor

## I/O-Bound Tasks

Spend most time waiting.

### Examples

- API Calls
- File Reading
- Database Queries
- Web Scraping
- Network Requests

### Recommended

- Multithreading
- ThreadPoolExecutor

---

# Global Interpreter Lock (GIL)

Python uses the Global Interpreter Lock (GIL).

The GIL allows only one thread to execute Python bytecode at a time.

Because of this:

```text
CPU-Intensive Tasks
       ↓
Multithreading
       ↓
Limited Performance Gain
```

Multiprocessing bypasses this limitation because each process has its own Python interpreter.

---

# Multithreading vs Multiprocessing

| Feature | Multithreading | Multiprocessing |
|----------|---------------|----------------|
| Unit | Thread | Process |
| Memory | Shared | Separate |
| Context Switch | Faster | Slower |
| Resource Usage | Lower | Higher |
| Communication | Easier | More Complex |
| CPU Core Utilization | Limited by GIL | Multiple Cores |
| Best For | I/O-Bound | CPU-Bound |

---

# ThreadPoolExecutor vs ProcessPoolExecutor

| Feature | ThreadPoolExecutor | ProcessPoolExecutor |
|----------|-------------------|--------------------|
| Uses | Threads | Processes |
| Memory | Shared | Separate |
| Best For | I/O Tasks | CPU Tasks |
| GIL Limitation | Yes | No |
| Creation Cost | Lower | Higher |
| Parallelism | Concurrent | True Parallel |

---

# Decision Guide

## Use Multithreading

When working with:

- API Calls
- Database Queries
- File Operations
- Logging
- Web Scraping

## Use Multiprocessing

When working with:

- Data Processing
- Machine Learning
- Scientific Computing
- Simulations
- Heavy Calculations

## Use ThreadPoolExecutor

When:

- Many small I/O tasks exist
- Automatic thread management is desired

## Use ProcessPoolExecutor

When:

- CPU-intensive workloads exist
- Multiple CPU cores should be utilized

---

# Quick Comparison

```text
API Calls
    ↓
ThreadPoolExecutor

Web Scraping
    ↓
ThreadPoolExecutor

Machine Learning
    ↓
ProcessPoolExecutor

Image Processing
    ↓
ProcessPoolExecutor
```

---

# Practice Assignment (Solved)

## Problem

Determine which technique should be used.

1. Downloading 100 files
2. Training a machine learning model
3. Reading multiple CSV files
4. Prime number computation

## Solution

| Task | Recommended |
|--------|------------|
| Downloading Files | ThreadPoolExecutor |
| ML Training | ProcessPoolExecutor |
| Reading CSV Files | ThreadPoolExecutor |
| Prime Computation | ProcessPoolExecutor |

---

# Key Takeaways

- Concurrency is not the same as parallelism.
- Multithreading is best for I/O-bound tasks.
- Multiprocessing is best for CPU-bound tasks.
- GIL limits thread performance for CPU-heavy workloads.
- Executors simplify thread and process management.
- Choosing the correct model improves application performance.

---

# Concepts Covered

- Concurrency
- Parallelism
- CPU-Bound Tasks
- I/O-Bound Tasks
- GIL
- Multithreading
- Multiprocessing
- ThreadPoolExecutor
- ProcessPoolExecutor
- Performance Considerations
