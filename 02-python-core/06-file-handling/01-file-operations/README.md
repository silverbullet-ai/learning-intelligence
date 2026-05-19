# Python File Operations

---

## Overview

File handling is one of the most important concepts in Python.

Used in:
- data science
- backend development
- AI pipelines
- automation
- logging systems
- databases
- configuration management

---

# What is File Handling?

File handling allows us to:
- create files
- read files
- write files
- append data
- work with binary files

---

# Types of Files

| Type | Example |
|------|----------|
| Text Files | `.txt`, `.csv`, `.json` |
| Binary Files | `.bin`, images, audio |

---

# Opening a File

Python uses:

```python
open()
```

Most commonly used with:

```python
with open()
```

because it automatically closes the file.

---

## Basic Syntax

```python
with open("filename.txt", "mode") as file:
    # operations
```

---

## File Modes

| Mode | Meaning |
|------|----------|
| r | read |
| w | write |
| a | append |
| rb | read binary |
| wb | write binary |
| w+ | read + write |

---

## Reading Entire File

```python
with open("example.txt", "r") as file:
    content = file.read()

print(content)
```

---

## Important

```python
file.read()
```

reads the ENTIRE file content.

---

## ⚠️ Common Error

If file does not exist:

```python
FileNotFoundError
```

---

## Reading File Line by Line

```python
with open("example.txt", "r") as file:

    for line in file:
        print(line.strip())
```

---

## strip()

Removes:

- newline characters
- spaces

---

## Writing to a File

```python
with open("example.txt", "w") as file:

    file.write("Hello World\n")
    file.write("This is new line")
```

---

## ⚠️ Important Understanding

`w` mode:

- overwrites file completely
- old content deleted

---

## Append Mode

Used when:

- old content should remain
- new content should be added

### Example

```python
with open("example.txt", "a") as file:

    file.write("\nAppend operation taking place")
```

---

## Append Mode (a)

- preserves old content
- adds new content at end

---

## Writing Multiple Lines

```python
lines = [
    "First line\n",
    "Second line\n",
    "Third line\n"
]

with open("example.txt", "a") as file:
    file.writelines(lines)
```

---

## writelines()

Writes an entire collection of lines.

---

## Binary File Handling

Binary files store:

- bytes
- non-text data

Examples:

- images
- videos
- audio
- ML models

---

## Writing Binary File

```python
with open("example.bin", "wb") as file:
    file.write(b"Hello World")
```

---

## Important

```python
b"Hello World"
```

means:

- bytes

---

## Reading Binary File

```python
with open("example.bin", "rb") as file:

    content = file.read()

print(content)
```

### Output

```python
b'Hello World'
```

---

## Copying Content Between Files

```python
with open("source.txt", "r") as source_file:

    content = source_file.read()

with open("destination.txt", "w") as destination_file:

    destination_file.write(content)
```

---

## Real Usage

Used in:

- backups
- ETL pipelines
- report generation
- migrations

---

## Counting Lines, Words, Characters

```python
with open("example.txt", "r") as file:

    content = file.read()

    lines = content.splitlines()
    words = content.split()
    characters = len(content)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)
```

---

## W+ Mode

`w+` allows:

- writing
- reading

BOTH together.

---

## ⚠️ Important

If file exists:

- old content removed

If file does not exist:

- file created

---

## Cursor Problem in w+

After writing:

- cursor stays at END

So immediate reading gives:

- empty output

---

## Solution → seek(0)

```python
file.seek(0)
```

Moves cursor to beginning.

---

## Correct Example

```python
with open("example.txt", "w+") as file:

    file.write("Hello World\n")
    file.write("This is new line")

    file.seek(0)

    content = file.read()

    print(content)
```

---

## MOST IMPORTANT CONCEPT

| Function | Purpose |
|----------|----------|
| seek(0) | move cursor to beginning |
| read() | read content |
| write() | write content |

---

## File Cursor

Every file has a cursor pointer.

After writing:

- cursor moves to end

`seek(0)` moves cursor back to beginning.

---

## Common File Methods

| Method | Purpose |
|--------|----------|
| read() | read entire file |
| readline() | read one line |
| readlines() | read all lines |
| write() | write text |
| writelines() | write multiple lines |
| seek() | move cursor |
| close() | close file |

---

## Best Practice

Always use:

```python
with open()
```

because:

- automatic closing
- memory safe
- avoids corruption

---

## Bad Practice

```python
file = open("test.txt")
```

---

## Good Practice

```python
with open("test.txt") as file:
```

---

## Real-World Usage

File handling is heavily used in:

- AI datasets
- logs
- report generation
- APIs
- ML model saving
- chatbot memory systems

---

## Important Errors

| Error | Meaning |
|------|----------|
| FileNotFoundError | file does not exist |
| PermissionError | permission denied |
| UnicodeDecodeError | encoding mismatch |

---

## Practice Assignments

- Create Notes App
- Word Counter
- File Copier
- Student Result Logger
- Binary Reader
- Search Word in File

---

## Best Practices

- Always use with open()
- Use append carefully
- Handle exceptions properly
- Understand cursor behavior
- Prefer modular file operations
