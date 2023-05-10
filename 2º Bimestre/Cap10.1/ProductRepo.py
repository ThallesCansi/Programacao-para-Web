from typing import List
from Database import Database
from Product import Product


class ProductRepo:
    @classmethod
    def createTable(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        """
        conn = Database.createConnection()
        cursor = conn.cursor()
        tableCreated = (cursor.execute(sql).rowcount > 0)
        conn.commit()
        conn.close()
        return tableCreated

    @classmethod
    def insert(cls, product: Product) -> Product:
        sql = "INSERT INTO product (name, price, stock) VALUES (?, ?, ?)"
        conn = Database.createConnection()
        cursor = conn.cursor()
        result = cursor.execute(
            sql, (product.name, product.price, product.stock))
        if (result.rowcount > 0):
            product.id = result.lastrowid
        conn.commit()
        conn.close()
        return product

    @classmethod
    def update(cls, product: Product) -> Product:
        sql = "UPDATE product SET name=?, price=?, stock=? WHERE id=?"
        conn = Database.createConnection()
        cursor = conn.cursor()
        result = cursor.execute(
            sql, (product.name, product.price, product.stock, product.id))
        if (result.rowcount > 0):
            conn.commit()
            conn.close()
            return product
        else:
            conn.close()
            return None

    @classmethod
    def delete(cls, id: int) -> bool:
        sql = "DELETE FROM product WHERE id=?"
        conn = Database.createConnection()
        cursor = conn.cursor()
        result = cursor.execute(sql, (id, ))
        if (result.rowcount > 0):
            conn.commit()
            conn.close()
            return True
        else:
            conn.close()
            return False

    @classmethod
    def getAll(cls) -> List[Product]:
        sql = "SELECT id, name, price, stock FROM product"
        conn = Database.createConnection()
        cursor = conn.cursor()
        result = cursor.execute(sql).fetchall()
        objects = [Product(*x) for x in result]
        return objects

    @classmethod
    def getOne(cls, id: int) -> Product:
        sql = "SELECT id, name, price, stock FROM product WHERE id=?"
        conn = Database.createConnection()
        cursor = conn.cursor()
        result = cursor.execute(sql, (id, )).fetchone()
        object = Product(*result)
        return object

    @classmethod
    def getAllOrderedByNameAsc(cls) -> List[Product]:
        sql = "SELECT id, name, price, stock FROM product ORDER BY name ASC"
        conn = Database.createConnection()
        cursor = conn.cursor()
        result = cursor.execute(sql).fetchall()
        objects = [Product(*x) for x in result]
        return objects
