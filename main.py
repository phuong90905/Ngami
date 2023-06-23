from vars import vars
import requests
import json

channel_id = "1030421197885816863" #channeld_id goes here. Channel id can be copied from the client by enabling dev mode.
msglimit = 100 #set number of msgs to fetch. Default is set to None.

def generate_route(channelid,msglimit=None): 
    return f"{vars['discord_api']}{vars['channels'](channelid) }{vars['messages']}{vars['limit'](msglimit) if msglimit else ''}"

headers = {
    "authorization" : vars['auth_token']
}

r = requests.get(generate_route(channel_id,msglimit),headers=headers)
response = json.loads(r.text)
print(response)
