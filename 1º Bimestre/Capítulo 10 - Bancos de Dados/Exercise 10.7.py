import sqlite3


def average_price_report():
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("SELECT ROUND(AVG(price), 2) FROM products")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


print(average_price_report())
