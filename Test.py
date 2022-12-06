import requests
import json
import discord
from discord.ext import commands,tasks

#Discord bot setup!!
TOKEN = 'post discord token here'
client = discord.Client()


#Message fetcher
def fetchMessages(channelid):
    headers = {
        'authorization': 'post auth key here'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=50', headers=headers)
    jsonobject = json.loads(r.text)
    content = []
    for value in jsonobject:
        if value['content'].strip():
            content.append(value['content'])
    return content


#Connect to discord bot and use message fetcher function to post the scraped messages.
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    for msgs in fetchMessages('1049502790386462732'):
        await client.get_channel(1049502824570040370).send(msgs)

client.run(TOKEN)