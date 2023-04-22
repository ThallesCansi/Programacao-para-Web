from pymongo import MongoClient


def delete_product(product_id: int):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_produtcts = db['products']

    filter = {'_id': product_id}

    result = collection_produtcts.delete_one(filter)

    print(f'{result.deleted_count} documents has been deleted')


delete_product(1)
