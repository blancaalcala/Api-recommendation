from pymongo import MongoClient
from bson.objectid import ObjectId

users = []
messages = []
chats = []


class CollConection:

    def __init__(self,dbName,collection):
        self.client = MongoClient()
        self.db = self.client[dbName]
        self.collection=self.db[collection]
    
    def addUser(self,user):
        document={'username':user}
        a=self.collection.insert_one(document)
        users.append([user,a.inserted_id])
        return users

    def addChat(self,chat):
        document={'chatname':chat}
        a=self.collection.insert_one(document)
        chats.append([chat,a.inserted_id])
        return chats

    def addUsertoChat(self,user,chat):
        document = {'user_id':user}
        a=self.collection.update_one(
        {'_id':ObjectId(chat)},
        {'$set':{'user_id':user}})
        return {"user_id":user}

    def addMessage(self,message,user):
        document={'message':message}
        a=self.collection.insert_one(document)
        b=self.collection.update_one(
        {'_id':ObjectId(a.inserted_id)},
        {'$set':{'user_id':user}})
        messages.append([message,a.inserted_id])
        return messages

    def addMessagetoChat(self,chat,message):
        chatid = {'chatid':chat}
        message = {'messageid':message}
        a=self.collection.update_one(
        {'_id':chatid['chatid']},
        {'$set':(message)})
        print(message)

    






