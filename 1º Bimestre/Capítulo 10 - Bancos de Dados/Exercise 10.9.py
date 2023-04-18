import sqlite3


def insert_category(category_id: int, category_name: str):
    connection = sqlite3.connect('store.db')
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS categories (
                       category_id INTEGER PRIMARY KEY,
                       category_name TEXT NOT NULL);
                       """)
    cursor.execute(
        "INSERT INTO categories (category_id, category_name) VALUES (?, ?)", ((category_id, category_name)))
    connection.commit()
    connection.close()


insert_category(int(input('Enter the ID of the category you want to enter: ')), input(
    'Enter the category name: '))
