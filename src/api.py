from bottle import route, run, get, post, request
from mongo import CollConection
import os

@post('/user/create')
def adduser():
    username=request.forms.get("username")
    return str(collUser.addUser(username))

@get("/user/<user_id>/recommend")
def getuserrecommendation(user_id):
    users = collMessage.getUserRecommendation(user_id)
    users_list = []
    for u in users.values():
        users_list.append(collUser.getUser(u)['user']['username'])
    return {'Recommended users':users_list}

@post('/chat/create')
def addchat():
    chat=request.forms.get("chatname")
    user_list=request.forms.getlist("users")
    return str(collChat.addChat(chat,user_list))

@post('/chat/<chat_id>/adduser')
def addusertochat(chat_id):
    user_id=request.forms.getlist("userid")
    return collChat.addUsertoChat(user_id,chat_id)

@post('/chat/<chat_id>/addmessage')
def addmessage(chat_id):
    message=request.forms.get("message")
    user_id=request.forms.get("user_id")
    message_id = str(collMessage.addMessage(message,user_id))
    return collChat.addMessagetoChat(message,user_id,chat_id,message_id)

@get("/chat/<chat_id>/list")
def getchat(chat_id):   
    return collChat.getMessages(chat_id)

@get("/chat/<chat_id>/sentiment")
def getchatsentiment(chat_id):
    return collChat.getChatSentiment(chat_id)
    


collUser=CollConection('API','user')
collChat=CollConection('API','chat')
collMessage=CollConection('API','message')

port = int(os.getenv('PORT', 8080))
host = os.getenv('IP','0.0.0.0')
run(host=host, port=port, debug=True)