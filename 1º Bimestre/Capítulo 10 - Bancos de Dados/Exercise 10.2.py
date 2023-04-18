import sqlite3

connection = sqlite3.connect('store.db')
cursor = connection.cursor()

cursor.execute(
    "INSERT INTO products (name, price) VALUES (?, ?)", (('Water', 3.00)))
cursor.execute(
    "INSERT INTO products (name, price) VALUES (?, ?)", (('Apple', 3.95)))
cursor.execute(
    "INSERT INTO products (name, price) VALUES (?, ?)", (('Strawberry', 3.25)))

connection.commit()
connection.close()
