from pymongo import MongoClient

class Database:
    client = MongoClient('mongodb://localhost:27017/')
    db = client["mcoc"]