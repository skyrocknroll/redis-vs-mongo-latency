from datetime import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient

client = MongoClient()
db = client.test
import time

start = time.time() * 1000
print(start)

for k in range(0, 100000):
    for result in db.restaurants.find({"_id": str(k)}):
        result
print(time.time() * 1000 - start)