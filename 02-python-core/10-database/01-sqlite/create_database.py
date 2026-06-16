import sqlite3

connection = sqlite3.connect("employees.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT
)
""")

connection.commit()

print("Database and table created successfully.")

connection.close()