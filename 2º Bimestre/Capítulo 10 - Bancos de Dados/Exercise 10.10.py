import sqlite3


def associate_product_category(product_id: int, category_id: int):
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS product_category (
                       product_id INTEGER NOT NULL,
                       category_id INTEGER NOT NULL,
                       UNIQUE (product_id, category_id))
                       """)
    cursor.execute("INSERT INTO product_category VALUES (?, ?)",
                   (product_id, category_id))
    connection.commit()
    connection.close()


associate_product_category(2, 1)
