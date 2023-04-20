from pymongo import MongoClient
from bson.objectid import ObjectId


def search_product(product_id: str):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    results = collection_products.find(
        {'_id': ObjectId(product_id)})

    for result in results:
        return print(f"Name: {result['name']} \nPrice: $ {result['price']}")

    client.close()


search_product('644048e5c9140041fe050557')
