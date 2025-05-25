from services.MongoDB import client
from models.Items import Item
import json

db = client["SaveTheVillageDB"]
items_collection = db["items"]

def get_items():
    items = items_collection.find()
    return list(items)

print(get_items())

