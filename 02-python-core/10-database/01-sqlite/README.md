# SQLite with Python

## Overview

SQLite is a lightweight, serverless relational database that comes bundled with Python through the built-in `sqlite3` module.

Unlike traditional database systems, SQLite stores the entire database in a single file and requires no separate database server.

SQLite is commonly used for:

- Learning SQL
- Local applications
- Desktop software
- Data analysis projects
- Embedded systems
- Prototyping databases

---

## What is SQL?

SQL (Structured Query Language) is the standard language used for:

- Creating databases
- Managing databases
- Querying data
- Updating records
- Deleting records

---

## Importing SQLite

```python
import sqlite3
```

SQLite is included with Python and requires no additional installation.

---

## Creating a Database Connection

```python
import sqlite3

connection = sqlite3.connect("example.db")
```

If the database does not exist, SQLite automatically creates it.

---

## Creating a Cursor

```python
cursor = connection.cursor()
```

The cursor acts as an interface between Python and the database.

---

## Creating Tables

```python
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
""")

connection.commit()
```

---

## CRUD Operations

CRUD stands for:

- Create
- Read
- Update
- Delete

These are the most common database operations.

### Create (INSERT)

```python
cursor.execute("""
INSERT INTO employees
(name, age, department)
VALUES
('Aahish', 24, 'AI')
""")

connection.commit()
```

### Read (SELECT)

```python
cursor.execute("""
SELECT * FROM employees
""")

rows = cursor.fetchall()

for row in rows:
    print(row)
```

### Update

```python
cursor.execute("""
UPDATE employees
SET age = 23
WHERE name = 'Manav'
""")

connection.commit()
```

### Delete

```python
cursor.execute("""
DELETE FROM employees
WHERE name = 'Raj'
""")

connection.commit()
```

---

## Bulk Inserts

For multiple records use:

```python
cursor.executemany(
    """
    INSERT INTO sales
    (date, product, sales, region)
    VALUES (?, ?, ?, ?)
    """,
    sales_data
)

connection.commit()
```

Benefits:

- Faster execution
- Cleaner code
- Recommended for large datasets

---

## Fetching Data

### fetchall()

```python
rows = cursor.fetchall()
```

Returns all rows.

### fetchone()

```python
row = cursor.fetchone()
```

Returns a single row.

---

## Parameterized Queries

Avoid string formatting in SQL statements.

Preferred:

```python
cursor.execute(
    """
    SELECT *
    FROM employees
    WHERE name = ?
    """,
    ("Aahish",)
)
```

Benefits:

- Prevents SQL Injection
- Cleaner code
- Recommended for production applications

---

## Closing Connections

```python
connection.close()
```

Always close database connections when finished.

---

## SQLite Workflow

```text
Connect Database
        ↓
Create Cursor
        ↓
Create Table
        ↓
Insert Records
        ↓
Query Records
        ↓
Update Records
        ↓
Delete Records
        ↓
Commit Changes
        ↓
Close Connection
```

---

## Common SQLite Methods

| Method               | Purpose                 |
| -------------------- | ----------------------- |
| sqlite3.connect()    | Connect/Create Database |
| connection.cursor()  | Create Cursor           |
| cursor.execute()     | Execute Query           |
| cursor.executemany() | Bulk Insert             |
| cursor.fetchall()    | Retrieve Rows           |
| connection.commit()  | Save Changes            |
| connection.close()   | Close Database          |

---

## Practice Assignment (Solved)

### Problem

Create a Student database with:

- id
- name
- course

Insert three students and display all records.

### Solution

```python
import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT
)
""")

students = [
    ("Aahish", "AI"),
    ("Manav", "Software Development"),
    ("Raj", "Data Science")
]

cursor.executemany(
    """
    INSERT INTO students
    (name, course)
    VALUES (?, ?)
    """,
    students
)

connection.commit()

cursor.execute(
    """
    SELECT * FROM students
    """
)

for row in cursor.fetchall():
    print(row)

connection.close()
```

---

## Key Takeaways

- SQLite is included with Python.
- Databases are stored in a single file.
- CRUD operations form the foundation of database programming.
- `executemany()` is preferred for bulk inserts.
- Always use parameterized queries when accepting user input.
- SQLite is ideal for learning databases and building small-to-medium applications.
