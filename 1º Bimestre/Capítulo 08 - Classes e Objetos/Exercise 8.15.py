class Product:
    def __init__(self, name: str, price: float, stock: int) -> None:
        self.name = name
        self.price = price
        self.stock = stock

    def showData(self):
        print(f'Product {self.name} is worth $ {self.price} and has {self.stock} in stock')

class ImportedProduct(Product):
    def __init__(self, name: str, price: float, stock: int, tax: float) -> None:
        super().__init__(name, price, stock)
        self.tax = tax

    def finalPrice(self):
        finalProduct = self.price + (self.tax * self.price)
        print(f'Tax price: $ {finalProduct:.2f}')

product1 = ImportedProduct(input('Enter product name: '),
                           float(input('Enter price product: ')),
                           int(input('Enter the stock of product: ')),
                           float(input('Enter the tax of this product: ')))

product1.showData()
product1.finalPrice()