import sqlite3


def search_products(product_id: int):
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM products WHERE id = ?", (product_id, ))
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


print(search_products(int(input('Enter the ID of the product you want to see: '))))
