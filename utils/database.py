from pymongo import MongoClient

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017/")
db = client["sentiment_analysis_db"]
users_collection = db["users"]

def get_user(username):
    """Retrieve user details from MongoDB."""
    return users_collection.find_one({"username": username})

def check_credentials(username, password):
    """Check if the entered username and password match (without hashing)."""
    user = get_user(username)
    
    if user and "password" in user and user["password"]:  # Ensure password exists
        return user["password"] == password  # Direct comparison (No Hashing)

    return False  # Invalid credentials
