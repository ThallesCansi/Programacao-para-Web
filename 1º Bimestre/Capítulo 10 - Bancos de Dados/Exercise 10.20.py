from pymongo import MongoClient
from bson.objectid import ObjectId


def associate_product_category(product_id: str, category_id: int):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    product = collection_products.find_one({'_id': ObjectId(product_id)})

    if not product:
        print('This product does not exist.')
        return

    collection_categories = product.get('categories', [])
    collection_categories.append(category_id)

    collection_products.update_one(
        {'_id': product_id}, {'$set': {'categories': collection_categories}})

    collection_categories = db['categories']
    document = {'_id': category_id, 'product_id': product_id}
    collection_categories.insert_one(document)


associate_product_category('6442e670aac7d8e079fe9491', 1)
