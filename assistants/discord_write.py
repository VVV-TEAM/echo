import requests
import json

with open("./keys.json") as file:
    data = json.load(file)

token = data["Discord_wyinpost_TOKEN"]

def write_discord(message, channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    message = {"content": message}
    header = {"authorization": token}
    r = requests.post(url, data=message, headers=header)
    if r.status_code == 200:
        print(f"Sent Message")
    else:
        print(f"Can't Send Message ")