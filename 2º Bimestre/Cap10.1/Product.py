class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        text = f"Id: {self.id}\nName: {self.name}\nPrice: {self.price}\nStock: {self.stock}"
        return text.strip()
