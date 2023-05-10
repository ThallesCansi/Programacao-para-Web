from typing import List
from Product import Product
from ProductRepo import ProductRepo


def showMenu():
    print("Options Menu")
    print("-"*30)
    print("1. List Products")
    print("2. Insert Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Product Details")
    print("6. Close")


def showProductsTable(products: List[Product]):
    print("PRODUCTS")
    print("-"*19)
    print("ID".center(6), "NAME".ljust(12))
    print("-"*19)
    for p in products:
        print(f"{str(p.id).zfill(2).center(6)} {str(p.name).ljust(12)}")


def processOption(option):
    if (option == 1):
        products = ProductRepo.getAll()
        showProductsTable(products)


option = -1
while (option != 6):
    showMenu()
    option = int(input("Your Option: "))
    processOption(option)
