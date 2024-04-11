from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient("mongodb+srv://[USERNAME]:[PASSWORD]@[YOUR_HOST:PORT]/?retryWrites=true&w=majority", server_api=ServerApi('1'))

# Access a database from the client 
db = client["YOUR_DATABASE_NAME"]
user = db["COLLECTION_TO_ACCESS"] # Example Users

# Define Class to use to map Mongodb Data for user login
class User:
    """Class Definition to handle Flask login for user"""
    def __init__(self, username, id):
        self.username = username
        self.id = id
    
    @staticmethod 
    def is_authenticated():
        return True
    
    @staticmethod
    def is_active():
        return True
    
    @staticmethod
    def is_anonymous():
        return False
    
    def get_id(self):
        return self.id
