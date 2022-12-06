import requests
import json
import discord
from discord.ext import commands,tasks

#Discord bot setup!!
TOKEN = 'MTA0OTUxMzc2Nzc0ODI0NzU1Mg.GL6QEH.7oy9Ukmo9f_wlE07CfGuYzpl7J3OsIs6x6UIuU'
client = discord.Client()


#Message fetcher
def fetchMessages(channelid):
    headers = {
        'authorization': 'MjAzNTMxMDI2NzAwNDM1NDU2.GVABcf.HpYB-uz0PTtpmJ6apJAXXO_O2eDBudnd04aIDI'
    }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelid}/messages?limit=50', headers=headers)
    jsonobj = json.loads(r.text)
    content = []
    for val in jsonobj:
        if val['content'].strip():
            content.append(val['content'])
    return content


print(fetchMessages('1049502790386462732'))



@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    for msgs in fetchMessages('1049502790386462732'):
        await client.get_channel(1049502824570040370).send(msgs)
    # channel = client.get_channel(1049502824570040370)
    # index = 0
    # # while index < len(fetchMessages('1049502790386462732')):
    # #     message = (fetchMessages('1049502790386462732'))[index]
    # #     channel.send(message)
    # #     index +- 1


client.run(TOKEN)