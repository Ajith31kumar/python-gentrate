from pymongo import MongoClient
from datetime import datetime

# MongoDB Atlas Connection
client = MongoClient("mongodb+srv://ajithkumar06952:iX6dwVyeuroNNfxZ@cluster0.kvv4r.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["test"]
collection = db["results"]

# JSON Data
data = {

    "name": "Abhishek",
    "email": "abhikkek@gmail.com",
    "gender": "Male",
    "phone": "9025057299",
    "age": 21,
    "results": [
        {"attempt": 1, "result": "❌ "},
        {"attempt": 2, "result": "❌ "},
        {"attempt": 3, "result": "✅ 0.540 sec"},
        {"attempt": 4, "result": "✅ 0.443 sec"},
        {"attempt": 5, "result": "✅ 0.441 sec"}
    ],
    "createdAt": datetime.utcnow(),
    "updatedAt": datetime.utcnow()
}

# Insert into MongoDB
collection.insert_one(data)

print("✅ Data Inserted Successfully into MongoDB Atlas!")
