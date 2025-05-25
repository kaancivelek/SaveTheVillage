import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()  # .env dosyasını yükle


uri = os.getenv("MONGO_URI")


client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("MongoDB bağlantısı başarılı!")
except Exception as e:
    print("Bağlantı hatası:", e)
