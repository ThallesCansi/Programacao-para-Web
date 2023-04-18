import sqlite3


def list_products():
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products ORDER BY name")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


print(list_products())
