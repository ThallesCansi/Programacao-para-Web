from pymongo import MongoClient


def search_product(product_id: int):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    results = collection_products.find(
        {'_id': product_id})

    for result in results:
        return print(f"Name: {result['name']} \nPrice: $ {result['price']}")

    client.close()


search_product(1)
