from pymongo import MongoClient
from bson.objectid import ObjectId


def update_price(product_id: str, new_price: float):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    filter = {'_id': ObjectId(product_id)}
    new_values = {'$set': {'price': new_price}}

    result = collection_products.update_one(filter, new_values)

    return print(f'{result.modified_count} documents have been updated')


update_price('644048e5c9140041fe050557', 2.5)
