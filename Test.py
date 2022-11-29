import requests
import json
import discord


#Scraping Messages
def get_msgs(channelID):
    #Discord Auth code for test account
    headers = { 'authorization': 'MTA0Njk1ODgzMjY0MDg1MjAyOQ.Gk01lg.8dOUWq2l4zSPqvJa31rEL17cC67mCKHntmWNw4' }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers)
    jsonobj = json.loads(r.text)
    for key in jsonobj:
        print(key, '\n')

get_msgs(1046959546574311527)
#Gets full message information!