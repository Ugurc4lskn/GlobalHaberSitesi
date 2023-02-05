import requests
from json import loads

def readConfig() -> str:
        return loads(open("config.json", mode="r", encoding="utf-8").read())
   

 
    
def send_to_telegram(message, image):
    chatID = readConfig()["channel"]
    apiToken = readConfig()["token"]
    payload = {
            "chat_id": chatID ,
            "photo": image,
            "caption": message,
            'parse_mode': 'markdown',

        }

    requests.post(f"https://api.telegram.org/bot{apiToken}/sendPhoto", data=payload)