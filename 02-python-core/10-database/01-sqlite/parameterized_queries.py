import sqlite3

connection = sqlite3.connect("employees.db")
cursor = connection.cursor()

name = "Aahish"

cursor.execute(
    """
    SELECT *
    FROM employees
    WHERE name = ?
    """,
    (name,)
)

for row in cursor.fetchall():
    print(row)

connection.close()