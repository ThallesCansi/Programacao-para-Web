from pymongo import MongoClient


def associate_product_category(product_id: int, category_id: int):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']
    collection_categories = db['categories']
    product_category = db['product_category']

    product = collection_products.find_one({'_id': product_id})
    category = collection_categories.find_one({'_id': category_id})

    if not product:
        print('This product does not exist.')
        return

    if not category:
        print('This category does not exist')
        return

    document = {'productId': product_id, 'categoryId': category_id}
    product_category.insert_one(document)


associate_product_category(2, 1)
