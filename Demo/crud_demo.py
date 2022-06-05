import os
from dotenv import load_dotenv
import pymongo as pymongo

"""
If you want to participate in the live demo, you will need to create a MongoDB database. 
I will use MongoDB Atlas for this, as it is a free service.

Check out https://www.mongodb.com/docs/manual/installation/ for instructions on how to install MongoDB.
"""

load_dotenv()
client = pymongo.MongoClient(os.environ.get("atlasConnection"))
db = client.ePortfolio


def read():
    cursor = db.inventory.find({})
    for doc in cursor:
        print(doc)


read()
