import sqlite3

connection = sqlite3.connect("employees.db")
cursor = connection.cursor()

# INSERT
cursor.execute("""
INSERT INTO employees(name, age, department)
VALUES('Aahish', 24, 'AI')
""")

connection.commit()

# READ
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)

# UPDATE
cursor.execute("""
UPDATE employees
SET age = 25
WHERE name = 'Aahish'
""")

connection.commit()

# DELETE
cursor.execute("""
DELETE FROM employees
WHERE name = 'Aahish'
""")

connection.commit()

connection.close()