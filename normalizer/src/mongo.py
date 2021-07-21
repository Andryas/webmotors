from pymongo import MongoClient
from settings import *

# INFO: https://stackoverflow.com/questions/41607517/do-i-need-to-close-pymongo-session

class mongo():
    conn = None

    def __init__(self):
        self.connect()

    @classmethod
    def connect(self):
        if self.conn is None:
            self.conn = MongoClient('mongodb://' + USER_MONGO + ':' + PASSWORD_MONGO + '@' + HOST_MONGO + ':27017/' + SERVER_MONGO)
            self.conn = self.conn[DATABASE_MONGO]
        return self.conn

    def find(self, collection, query = None, fields = None, **kwargs):
        return(list(self.conn[collection].find(query, fields, **kwargs)))

    def insert_one(self, collection, **kwargs):
        return(list(self.conn[collection].insert_one(**kwargs)))

    def update_one(self, collection, query, update):
        return(list(self.conn[collection].update_one(query, update)))
