from pymongo import MongoClient


def insert_category(category_id: int, category_name: str):
    client = MongoClient('mongodb://localhost:27017/')
    db = client['store']
    collection_categories = db['categories']

    if 'categories' not in db.list_collection_names():
        collection_categories = db.create_collection('categories')

    document = {'_id': category_id, 'name': category_name}
    collection_categories.insert_one(document)


insert_category(1, 'Frutas')
