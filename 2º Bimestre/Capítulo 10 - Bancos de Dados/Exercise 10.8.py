import sqlite3


def average_price_report():
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("SELECT ROUND(AVG(price), 2) FROM products")
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def above_average_products():
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE price > ?",
                   (average_price_report()[0][0], ))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


print(above_average_products())
