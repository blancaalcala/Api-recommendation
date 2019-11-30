from pymongo import MongoClient
from bson.objectid import ObjectId


class CollConection:

    def __init__(self,dbName,collection):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection=self.db[collection]
    
    def addUser(self,user):
        document={'username':user}
        a=self.collection.insert_one(document)
        return a.inserted_id

    def addChat(self,chat,user):
        a=self.collection.insert_one({'chatname':chat})
        b=self.collection.update_one(
        {'_id':ObjectId(a.inserted_id)},
        {'$set':{'users_list':user}})
        return a.inserted_id

    def addUsertoChat(self,user,chat):
        a=self.collection.update(
        {'_id':ObjectId(chat)},
        {'$push':{'users_list':{'$each':user}}})
        return chat

    def addMessage(self,message):
        a=self.collection.insert_one({'message':message})
        return a.inserted_id

    def addMessagetoChat(self,message,user,chat,message_id):
        document = {'message':message}
        a=self.collection.update(
        {'_id':ObjectId(chat)},
        {'$push':{'messages':message}})
        return message_id
    
    






