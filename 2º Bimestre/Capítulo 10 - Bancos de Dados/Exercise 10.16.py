from pymongo import MongoClient


def list_products():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    results = collection_products.find()

    for result in results:
        print(f"{result['name']} - {result['price']}")


list_products()
