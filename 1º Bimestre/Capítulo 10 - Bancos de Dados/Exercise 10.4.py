import sqlite3


def update_price(product_id: int, new_price: float):
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("UPDATE products SET price = ? WHERE id = ?",
                   (new_price, product_id))
    connection.commit()
    connection.close()


update_price(int(input('Enter the ID of the product you want to update the price: ')), float(
    input('Enter new price: ')))
