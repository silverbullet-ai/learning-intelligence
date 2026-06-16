import sqlite3

connection = sqlite3.connect("students.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
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
    INSERT INTO students(name, course)
    VALUES (?, ?)
    """,
    students
)

connection.commit()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

connection.close()