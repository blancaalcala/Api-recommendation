import requests
import pandas as pd
import post_functions

chats = pd.DataFrame(columns=["INFO","ID"])
users = pd.DataFrame(columns=["INFO","ID"])
messages = pd.DataFrame(columns=["INFO","ID"])


#name = input("Introduce the name of the user: ")
names = ["Antonio","Carlos","Pepe","Alvaro"]
for n in names:
    username,user_id = createUser(n)
    users = appendInfo(username,user_id ,users)
    
chatname,chat_id = createChat("datamad1019",['5de2f69b964f3f7b725bf4b3','5de2f69b964f3f7b725bf4b4'])
chats = appendInfo(chatname,chat_id,chats)

addUser(chats.loc[0].ID,[users.loc[0].ID,users.loc[1].ID])

message,message_id= addMessage(chats.loc[1].ID,"i am very tired",users.loc[2].ID)
messages = appendInfo(message,message_id,messages)