from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["expenseDB"]
collection = db["expenses"]

data = {
    "category": "Food",
    "amount": 200,
    "description": "Lunch"
}

collection.insert_one(data)

print("Data inserted successfully")
