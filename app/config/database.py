import pymongo
import os
password = os.getenv("MONGO_PASSWORD")
client = pymongo.MongoClient(f"mongodb+srv://test:123Am@apphouse.ylkbmq7.mongodb.net/?retryWrites=true&w=majority")


db = client["AppHouse"]
collection = db["users"]
