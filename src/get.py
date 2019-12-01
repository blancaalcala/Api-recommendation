import requests
import json

def getMessages(chat_id):
    url=f"http://localhost:8080/chat/{chat_id}/list"
    mes = requests.get(url).text
    mes = json.loads(mes)
    message_list = mes['list'][0]
    return message_list['messages']