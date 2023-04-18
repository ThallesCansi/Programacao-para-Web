import sqlite3

connection = sqlite3.connect('store.db')
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL NOT NULL);
    """)

connection.commit()
connection.close()
