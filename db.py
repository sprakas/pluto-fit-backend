from pymongo import MongoClient
import certifi
from config import MONGO_DB_NAME, MONGO_URI

client = MongoClient(MONGO_URI, tls=True, tlsCAFile=certifi.where())

db = client[MONGO_DB_NAME]
users = db["users"]