import sqlite3


def delete_product(product_id: int):
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", (product_id, ))
    connection.commit()
    connection.close()


delete_product(int(input('Enter the ID of the product you want to delete: ')))
