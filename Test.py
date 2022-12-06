import requests
import json
import discord

#Discord bot setup!!
TOKEN = 'MTA0OTUxMzc2Nzc0ODI0NzU1Mg.GDvAUH.4hfqn3GCTJBSj_KWUxM6vILkXVjxzsiTHhfo3w'
client = discord.Client()


#Message fetcher
def fetchMessages(channelid):
    messages = 0
    headers = {
        'authorization': 'MjAzNTMxMDI2NzAwNDM1NDU2.GPiVs6.sWsrUKz4o5PqO5_YcJOxr1TSbQJe_rJM8b9lP4'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=50', headers=headers)
    jsonobj = json.loads(r.text)
    for vals in jsonobj:
        messages += 1
        content = (vals['content'])
    return content
fetchMessages('1049502790386462732')

def test():
    for num in range(6):
        return 'test'
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    await client.get_channel(1049502824570040370).send(fetchMessages('1049502790386462732'))
client.run(TOKEN)