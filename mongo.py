from pymongo import MongoClient
from bson.objectid import ObjectId


class CollConection:

    def __init__(self,dbName,collection):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection=self.db[collection]

    def addDocument(self,document):
        a=self.collection.insert_one(document)
        print(a.inserted_id)
        return a.inserted_id
    
    def addUser(self,user):
        document={'username':user}
        a=self.collection.insert_one(document)
        return {a.inserted_id}

    def addChat(self,chat):
        document={'chatname':chat}
        a=self.collection.insert_one(document)
        return {a.inserted_id}

    def addUsertoChat(self,user,chat):
        document = {'user_id':user}
        a=self.collection.update_one(
        {'_id':ObjectId(chat)},
        {'$set':{'user_id':user}})
        return {"user_id":user}

    def addMessagetoChat(self,user,chat,text):
        User = {'user_id':user}
        Message = {'message':text}
        a=self.collection.update_one(
        {'_id':ObjectId(chat)},
        {'$set':[{'user_id':user},{'message':Message}]})
        return {"message_id":message}


    






