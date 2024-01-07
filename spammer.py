import requests
import random
import time

count = 0
targetCount = 1

message_delay = 1

message_content = ""

with open("channels.txt", "r") as channels_file:
    channelIDs = [int(line.strip()) for line in channels_file.readlines()]

url_base = "https://discord.com/api/v9/channels/{}/messages"

with open("proxies.txt", "r") as proxies_file:
    proxies = proxies_file.read().splitlines()

headers = {
    "Authorization": "DISCORD-TOKEN",
    "Content-Type": "application/json"
}

while count < targetCount:
    for channelID in channelIDs:
        url = url_base.format(channelID)
        payload = {
            "content": message_content
        }
        
        proxy = {
            'http': f'http://{random.choice(proxies)}'
        }

        try:
            res = requests.post(url, json=payload, headers=headers, proxies=proxy, timeout=5)
            
            if res.status_code == 200:
                print(f"Message sent to channel {channelID}")
            else:
                print(f"Failed to send message to channel {channelID}. Status code: {res.status_code}")
        
        except requests.RequestException as e:
            print(f"Request failed for channel {channelID}. Error: {e}")

    count += 1
    time.sleep(message_delay)
