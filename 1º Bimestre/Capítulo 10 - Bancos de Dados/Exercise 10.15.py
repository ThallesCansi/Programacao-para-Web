from pymongo import MongoClient
from bson.objectid import ObjectId


def delete_product(product_id: str):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_produtcts = db['products']
    
    filter = {'_id': ObjectId(product_id)}
    
    result = collection_produtcts.delete_one(filter)
    
    print(f'{result.deleted_count} documents has been deleted')


delete_product('644048e5c9140041fe050557')
