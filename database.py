from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")

db = client["adaptive_test"]

questions_collection = db["questions"]
sessions_collection = db["sessions"]