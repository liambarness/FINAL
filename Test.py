import requests
import json
import discord


#Scraping Messages
def get_msgs(channelID):
    #Discord Auth code for test account
    headers = { 'authorization': 'MjAzNTMxMDI2NzAwNDM1NDU2.GQlTuX.WwrXcpk-vhrIMl132EK3oSp9gYUW3shxDdYK1I' }
    r = requests.get(f'https://discord.com/api/v9/channels/{channelID}/messages', headers=headers)
    jsonobj = json.loads(r.text)
    for key in jsonobj:
        print(key['content'], '\n')
        # print(key['username'], '\n')

get_msgs(1049502790386462732)
# #Gets full message information!
# {'id': '1046961031529902152', 'type': 0, 'content': 'e', 'channel_id': '1046959546574311527', 'author': {'id': '1046958832640852029', 'username': 'liamtestingaccount', 'avatar': 
# None, 'avatar_decoration': None, 'discriminator': '1139', 'public_flags': 0}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2022-11-29T01:29:21.512000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': []} 

# {'id': '1046961030284202045', 'type': 0, 'content': 'e', 'channel_id': '1046959546574311527', 'author': {'id': '1046958832640852029', 'username': 'liamtestingaccount', 'avatar': 
# None, 'avatar_decoration': None, 'discriminator': '1139', 'public_flags': 0}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2022-11-29T01:29:21.215000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': []}

# {'id': '1046961029239799839', 'type': 0, 'content': 'e', 'channel_id': '1046959546574311527', 'author': {'id': '1046958832640852029', 'username': 'liamtestingaccount', 'avatar': 
# None, 'avatar_decoration': None, 'discriminator': '1139', 'public_flags': 0}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2022-11-29T01:29:20.966000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': []}

# {'id': '1046961027578855496', 'type': 0, 'content': 'e', 'channel_id': '1046959546574311527', 'author': {'id': '1046958832640852029', 'username': 'liamtestingaccount', 'avatar': 
# None, 'avatar_decoration': None, 'discriminator': '1139', 'public_flags': 0}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2022-11-29T01:29:20.570000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': []}

# {'id': '1046961026320584824', 'type': 0, 'content': 'n', 'channel_id': '1046959546574311527', 'author': {'id': '1046958832640852029', 'username': 'liamtestingaccount', 'avatar': 
# None, 'avatar_decoration': None, 'discriminator': '1139', 'public_flags': 0}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2022-11-29T01:29:20.270000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': []}

# {'id': '1046959557932503170', 'type': 0, 'content': 'eee', 'channel_id': '1046959546574311527', 'author': {'id': '1046958832640852029', 'username': 'liamtestingaccount', 'avatar': None, 'avatar_decoration': None, 'discriminator': '1139', 'public_flags': 0}, 'attachments': [], 'embeds': [], 'mentions': [], 'mention_roles': [], 'pinned': False, 'mention_everyone': False, 'tts': False, 'timestamp': '2022-11-29T01:23:30.179000+00:00', 'edited_timestamp': None, 'flags': 0, 'components': []}