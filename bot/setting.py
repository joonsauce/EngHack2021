import discord
import logging
import requests
import random
from random import seed
from random import randint
from discord.ext import commands
from secrets import *

# debug logger for bot
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='../discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# sets prefix for bot
prefix = "ad"

# initializes bot
bot = commands.Bot(command_prefix=prefix)

# removes help command to add our own help command
bot.remove_command("help")

# defines text counts to count until bot + $1
text_counts = {}
plan_types = {}

# defines different header types for api calls
header1 = {
        'Authorization': 'Bearer {}'.format(api_key),
        }
header2 = {
            'Authorization': 'Bearer {}'.format(api_key),
            'Content-Type': 'application/json',
        }

# defines certain parameters for api calls
params = (
        ('maxRecords', 999),
        ('view', 'Grid view'),
    )

# start up procedure for bot
@bot.event
async def on_ready():
    # changes bot status
    await bot.change_presence(activity=discord.Game("Advertising to servers"))
    # below contacts airtable to edit the tables
    servers = bot.guilds
    # GETs all records in the table to check if all servers bot is in, is in the table
    response = requests.get(url=api_link,
                            headers=header1,
                            params=params)
    print("Get Response: " + str(response))
    data = response.json()
    for u in range(len(data["records"])):
        planid = str(data["records"][u]["fields"]["guild_id"]) + str(data["records"][u]["fields"]["guild_id2"])
        plan_types.update({str(planid): data["records"][u]["fields"]["plan_type"]})
        text_counts.update({str(planid): data["records"][u]["fields"]["text_count"]})
    # DELETEs all records to replace with the updated set of servers
    for k in range(len(data["records"])):
        records = data["records"][k]["id"]

        response = requests.delete(url=api_link + records,
                                   headers=header1)
        print("Delete Reponse: " + str(response))

    # POSTs updated list of servers the bot is in
    for i in range(len(servers)):
        id = list(str(servers[i].id))
        idsplit1 = []
        idsplit2 = []
        for p in range(len(id)):
            if p <= 8:
                idsplit1.append(id[p])
            else:
                idsplit2.append(id[p])
        id1 = str()
        id2 = str()
        for r in range(len(idsplit1)):
            id1 = id1 + idsplit1[r]
            id2 = id2 + idsplit2[r]
        id = id1 + id2
        plan = plan_types.get(str(id))
        text = text_counts.get(str(id))
        if not plan:
            plan = 0
        else:
            pass
        if not text:
            text = 0
        else:
            pass

        data = '{ "records": [ { "fields": { "guild_id": ' + str(id1) + ', "guild_id2": ' + str(id2) + ', "plan_type": ' + str(plan) + ', "text_count": ' + str(text) + '} }] }'


        response = requests.post(url=api_link,
                                 headers=header2,
                                 data=data)
        print("Post Response: " + str(response))
    # returns updated version of the table
    response = requests.get(url=api_link,
                            headers=header1,
                            params=params)
    print("Get Response: " + str(response))
    data = response.json()
    for finalGET in range(len(servers)):
        records1 = str(data["records"][finalGET]["fields"]["guild_id"])
        records2 = str(data["records"][finalGET]["fields"]["guild_id2"])
        records = records1 + records2
    # prints that the bot is ready to go
    print("Status: OK")