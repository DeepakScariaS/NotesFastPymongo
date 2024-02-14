from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:admin@cluster0.5nzqe2m.mongodb.net/?retryWrites=true&w=majority")

db = client.todo_db

collection_name = db["notes_collection"]