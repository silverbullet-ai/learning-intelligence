# Multithreading & Multiprocessing

## Overview

Multithreading and multiprocessing are techniques used to improve the efficiency and performance of applications.

Before learning them, it is important to understand:

* Program
* Process
* Thread

These concepts form the foundation of concurrent and parallel execution.

---

## Program

A program is a sequence of instructions written in a programming language.

Examples:

* Python Script
* Google Chrome
* Microsoft Excel
* Visual Studio Code

A program is a passive entity stored on disk until it is executed.

---

## Process

A process is an instance of a program that is currently being executed.

Example:

```text
Google Chrome.exe
       ↓
Running Chrome Window
```

Each running application becomes a process.

Examples:

* Chrome Browser
* Excel
* Calculator
* VS Code
* Notepad

---

## Resources Used by a Process

A process contains several resources:

### Code Segment

Contains the actual program instructions.

### Data Segment

Stores:

* Global Variables
* Static Variables

### Heap Memory

Used for:

* Dynamic Memory Allocation
* Runtime Object Creation

### Stack

Stores:

* Local Variables
* Function Calls

### Registers

Small CPU memory locations used for temporary storage during execution.

---

## Process Characteristics

### Separate Memory Space

Every process has its own memory space.

```text
Process A
   Memory Space A

Process B
   Memory Space B
```

---

### Process Isolation

One process cannot directly corrupt another process because both have separate memory spaces.

Example:

```text
Chrome Window 1 crashes
       ↓
Chrome Window 2 continues running
```

---

### Context Switching Overhead

Switching between processes requires more resources because each process has its own memory space.

This makes process switching slower compared to thread switching.

---

## Thread

A thread is the smallest unit of execution within a process.

A process may contain one or more threads.

### Definition

A thread is a unit of execution inside a process.

---

## Single-Threaded Process

A process containing only one thread.

```text
Process
   │
   └── Thread 1
```

Only one task executes at a time.

---

## Multi-Threaded Process

A process containing multiple threads.

```text
Process
   │
   ├── Thread 1
   ├── Thread 2
   ├── Thread 3
   └── Thread 4
```

Multiple tasks can execute concurrently.

---

## Resources Shared by Threads

Threads share:

* Code Segment
* Data Segment
* Heap Memory

Each thread has its own:

* Stack
* Registers

```text
Process
│
├── Shared Code Segment
├── Shared Data Segment
├── Shared Heap
│
├── Thread 1
│     ├── Stack
│     └── Registers
│
└── Thread 2
      ├── Stack
      └── Registers
```

---

## Real-World Examples

### MS Paint

Process:

```text
MS Paint
```

Thread Examples:

* Draw Rectangle
* Draw Circle
* Fill Color
* Erase

Each operation can be handled by separate threads within the same process.

---

### Microsoft Excel

Process:

```text
Microsoft Excel
```

Thread Examples:

* Formatting Text
* Calculating Formula
* Saving Workbook
* Refreshing Data

---

## Process vs Thread

| Process                  | Thread                             |
| ------------------------ | ---------------------------------- |
| Instance of a program    | Unit of execution inside a process |
| Separate memory space    | Shared memory space                |
| Heavyweight              | Lightweight                        |
| Slower context switching | Faster context switching           |
| Higher resource usage    | Lower resource usage               |
| Independent              | Dependent on process               |

---

## Key Takeaways

* A program is a sequence of instructions.
* A process is a running instance of a program.
* A thread is the smallest unit of execution within a process.
* Processes have separate memory spaces.
* Threads share process resources.
* Thread switching is faster than process switching.
* Multithreading and multiprocessing are built on these concepts.

---

## Interview Questions

### Q1. What is the difference between a program and a process?

A program is a set of instructions stored on disk, while a process is a running instance of that program.

---

### Q2. What is a thread?

A thread is the smallest unit of execution within a process.

---

### Q3. Why are threads faster than processes?

Threads share the same memory space, making context switching faster and requiring fewer resources.

---

### Q4. What resources are shared between threads?

* Code Segment
* Data Segment
* Heap Memory

---

### Q5. What resources are private to each thread?

* Stack
* Registers

---

## Concepts Covered

* Program
* Process
* Thread
* Process Memory Layout
* Code Segment
* Data Segment
* Heap Memory
* Stack
* Registers
* Process Isolation
* Context Switching
* Single-Threaded Process
* Multi-Threaded Process
* Process vs Thread
* Shared Resources
* Private Resources
