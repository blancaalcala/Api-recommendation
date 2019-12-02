from pymongo import MongoClient
from bson.objectid import ObjectId
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
import os
from dotenv import load_dotenv
load_dotenv()


sid = SentimentIntensityAnalyzer()


class CollConection:

    def __init__(self,dbName,collection):
        self.client = MongoClient(os.getenv('mongo'))
        self.db = self.client[dbName]
        self.collection=self.db[collection]
    
    def addUser(self,user):
        document={'username':user}
        a=self.collection.insert_one(document)
        return a.inserted_id

    def getUser(self,user):
        x = list(self.collection.find({'_id':ObjectId(user)}))[0]
        return {'user':x}
    
    def getUserRecommendation(self,user_id):
        info = {}
        x=list(self.collection.find({},{'message':1,'user_id':1,'_id':0}))
        for i in x:
            if i['user_id'] not in info.keys():
                info[i['user_id']] = i['message']
            else:
                info[i['user_id']] = info[i['user_id']]+" "+i['message']
        count_vectorizer = CountVectorizer(stop_words='english')
        count_vectorizer = CountVectorizer()
        sparse_matrix = count_vectorizer.fit_transform(info.values())
        info_matrix = sparse_matrix.todense()
        df = pd.DataFrame(info_matrix, columns=count_vectorizer.get_feature_names(), index=info.keys())
        similarity_matrix = distance(df, df)
        sim_df = pd.DataFrame(similarity_matrix, columns=info.keys(), index=info.keys())
        recom = sim_df[user_id].sort_values(ascending=False)[1:]
        users = recom.keys()
        recommendations = {}
        for i in range(3):
            recommendations[f"user{i}"] = users[i]
        return recommendations

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

    def addMessage(self,message,user):
        a=self.collection.insert_one({'message':message})
        b=self.collection.update(
        {'_id':a.inserted_id},
        {'$set':{'user_id':user}})
        return a.inserted_id

    def addMessagetoChat(self,message,user,chat,message_id):
        document = {'message':message}
        x = list(self.collection.find({},{'users_list':1,'_id':0}))
        users_list = x[0]['users_list']
        if user in users_list:
            a=self.collection.update(
            {'_id':ObjectId(chat)},
            {'$push':{'messages':message}})
            return message_id
        else:
            raise TypeError("The user doesnt belong to this chat")

    def getMessages(self,chat):
        x = list(self.collection.find({'_id':ObjectId(chat)},{'messages':1,'_id':0}))
        return {'list':x}

    def getChatSentiment(self,chat):
        mes = self.getMessages(chat)['list'][0]
        message_list = mes['messages']
        message_string = " ".join(message_list)
        print(message_string)
        return sid.polarity_scores(message_string)

    
    






