def createUser(username):
    url="http://localhost:8080/user/create"
    params={'username':username}
    user = requests.post(url,data=params).text
    return username,user

def appendInfo(username,user_id,table):
    table = table.append({'INFO':username,'ID':user_id},ignore_index=True)
    pd.sa
    return table

def createChat(chatname,users):    
    url="http://localhost:8080/chat/create"
    params={'chatname':chatname,
           'users':users}
    chat = requests.post(url,data=params).text
    return chatname,chat

def addUser(chat,user_id):
    url=f"http://localhost:8080/chat/{chat}/adduser"
    params={'userid':user_id}
    requests.post(url,data=params).text
    return chat

def addMessage(chat,message,user_id):   
    url=f"http://localhost:8080/chat/{chat}/addmessage"
    params={'message':message,
           'user_id':user_id}
    message_id = requests.post(url,data=params).text
    return message,message_id