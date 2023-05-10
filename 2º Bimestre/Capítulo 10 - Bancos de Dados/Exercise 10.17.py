from pymongo import MongoClient


def average_price_report():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_products = db['products']

    average_price = collection_products.aggregate([
        {'$group': {'_id': None, 'averagePrice': {'$avg': '$price'}}}
    ])

    return print(f"The average price of the products is: {average_price.next()['averagePrice']}")


average_price_report()
