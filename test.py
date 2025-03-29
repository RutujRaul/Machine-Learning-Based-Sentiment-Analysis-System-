from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
db = client["sentiment_analysis_db"]
db["users"].delete_many({})  # Delete all users

db["users"].insert_one({"username": "admin", "password": "admin123"})  # Insert admin user
print("Admin user added successfully!")