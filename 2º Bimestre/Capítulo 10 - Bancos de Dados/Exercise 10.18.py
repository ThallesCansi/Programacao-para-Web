from pymongo import MongoClient


def average_price_report():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    average_price = collection_products.aggregate([
        {'$group': {'_id': None, 'averagePrice': {'$avg': '$price'}}}
    ])

    return average_price.next()['averagePrice']


def above_average_products():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    above_price = list(collection_products.aggregate([
        {'$match': {'price': {'$gt': average_price_report()}}}, {'$project': {
            '_id': 0, 'name': 1}}
    ]))

    return print(f"The above average products are: {[product['name'] for product in above_price]}")


above_average_products()
