from pymongo import MongoClient


def update_price(product_id: int, new_price: float):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    filter = {'_id': product_id}
    new_values = {'$set': {'price': new_price}}

    result = collection_products.update_one(filter, new_values)

    return print(f'{result.modified_count} documents have been updated')


update_price(1, 2.5)
