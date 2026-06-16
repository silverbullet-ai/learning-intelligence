import sqlite3

connection = sqlite3.connect("sales_data.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales(
    id INTEGER PRIMARY KEY,
    date TEXT,
    product TEXT,
    sales INTEGER,
    region TEXT
)
""")

sales_data = [
    ("2024-01-01", "Laptop", 1200, "North America"),
    ("2024-01-02", "Phone", 800, "Europe"),
    ("2024-01-03", "Tablet", 600, "Asia"),
]

cursor.executemany(
    """
    INSERT INTO sales
    (date, product, sales, region)
    VALUES (?, ?, ?, ?)
    """,
    sales_data
)

connection.commit()

cursor.execute("SELECT * FROM sales")

for row in cursor.fetchall():
    print(row)

connection.close()