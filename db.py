import sqlite3

conn = sqlite3.connect('food.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS vendor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    food TEXT,
    location TEXT,
    contact TEXT
)
""")

conn.commit()
conn.close()

print("Database and Table Created Successfully!")