from pymongo import MongoClient
from bson.objectid import ObjectId
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import get as G

sid = SentimentIntensityAnalyzer()


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

    def getMessages(self,chat):
        x = list(self.collection.find({'_id':ObjectId(chat)},{'messages':1,'_id':0}))
        return {'list':x}

    def getChatSentiment(self,chat):
        message_list = G.getMessages(chat)
        message_string = ""
        for m in message_list:
            message_string += m+" "
        return sid.polarity_scores(message_string)

    
    






