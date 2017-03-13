from datetime import datetime

from pymongo import MongoClient

client = MongoClient()
db = client.test
import time

start = time.time() * 1000
print(start)

for k in range(0, 100000):
    result = db.restaurants.insert_one(
        {"_id": str(k),
         "address": {
             "street": "2 Avenue",
             "zipcode": "10075",
             "building": "1480",
             "coord": [-73.9557413, 40.7720266]
         },
         "borough": "Manhattan",
         "cuisine": "Italian",
         "grades": [
             {
                 "date": datetime.strptime("2014-10-01", "%Y-%m-%d"),
                 "grade": "A",
                 "score": 11
             },
             {
                 "date": datetime.strptime("2014-01-16", "%Y-%m-%d"),
                 "grade": "B",
                 "score": 17
             }
         ],
         "name": "Vella",
         "restaurant_id": "41704620"
         }
    )
print(time.time() * 1000 - start)
# print(result)
