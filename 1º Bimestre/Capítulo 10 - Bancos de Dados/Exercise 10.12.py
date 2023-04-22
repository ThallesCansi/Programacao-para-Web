from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['store']
collection_products = db['products']

document = {
    "_id": 1,
    "name": 'Water',
    "price": 3.00
}
resultado = collection_products.insert_one(document)

document = {
    "_id": 2,
    "name": 'Apple',
    "price": 3.95
}
resultado = collection_products.insert_one(document)

document = {
    "_id": 3,
    "name": 'Strawberry',
    "price": 3.25
}
resultado = collection_products.insert_one(document)
