from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['store']
collection_products = db['products']

document = {
    "name": 'Water',
    "price": 3.00
}
resultado = collection_products.insert_one(document)

document = {
    "name": 'Apple',
    "price": 3.95
}
resultado = collection_products.insert_one(document)

document = {
    "name": 'Strawberry',
    "price": 3.25
}
resultado = collection_products.insert_one(document)
