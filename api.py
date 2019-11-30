from bottle import route, run, get, post, request
from mongo import CollConection



#@get("/user/<user_id>/recommend")
#def 

@post('/user/create')
def adduser():
    username=request.forms.get("username")
    return {
        "user_id": str(collUser.addUser(username))}

@post('/chat/create')
def addchat():
    chatname=request.forms.get("chatname")
    return {
        "chat_id": str(collChat.addChat(chatname))}

@post('/chat/<chat_id>/adduser')
def addusertochat(chat_id):
    user_id=request.forms.getlist("userid")
    return collChat.addUsertoChat(user_id,chat_id)

@post('/message/<userid>/create')
def addmessage(userid):
    message=request.forms.get("message")
    return collMessage.addMessage(message,userid)

@post('/chat/<chat_id>/addmessage')
def addMessagetoChat(chat_id):
    message=request.forms.get("message")
    return collChat.addMessagetoChat(chat_id,message)


collUser=CollConection('API','user')
collChat=CollConection('API','chat')
collMessage=CollConection('API','message')


run(host='0.0.0.0', port=8080)

