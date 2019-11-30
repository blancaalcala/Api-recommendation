from bottle import route, run, get, post, request
from mongo import CollConection



#@get("/user/<user_id>/recommend")
#def 

@post('/user/create')
def adduser():
    username=request.forms.get("username")
    return str(collUser.addUser(username))

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
    message_id = str(collMessage.addMessage(message))
    return collChat.addMessagetoChat(message,user_id,chat_id,message_id)


collUser=CollConection('API','user')
collChat=CollConection('API','chat')
collMessage=CollConection('API','message')



run(host='0.0.0.0', port=8080)

