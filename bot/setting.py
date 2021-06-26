import asyncio
import discord
import logging
import requests
import random
from random import seed
from random import randint
from discord.ext import commands

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='../discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

prefix = "ad"

bot = commands.Bot(command_prefix=prefix)

bot.remove_command("help")

@bot.event
async def on_ready():
    # changes bot status
    await bot.change_presence(activity=discord.Game("Advertising to servers"))
    # below contacts airtable to edit the tables
    servers = bot.guilds
    # GETs all records in the table to check if all servers bot is in, is in the table
    headers = {
        'Authorization': 'Bearer keyBZeqZsQTYXemrk',
    }

    params = (
        ('maxRecords', 999),
        ('view', 'Grid view'),
    )
    response = requests.get('https://api.airtable.com/v0/appTJLFldOxuL7FEU/Table%201', headers=headers,
                            params=params)
    print("Get Response: " + str(response))
    data = response.json()
    plan_types = {}
    for iniGET in range(len(data["records"])):
        planid = str(data["records"][iniGET]["fields"]["guild_id"]) + str(data["records"][iniGET]["fields"]["guild_id2"])
        plan_types.update({str(planid): data["records"][iniGET]["fields"]["plan_type"]})
    # DELETEs all records to replace with the updated set of servers
    for k in range(len(data["records"])):
        records = data["records"][k]["id"]
        headers = {
            'Authorization': 'Bearer keyBZeqZsQTYXemrk',
        }

        response = requests.delete('https://api.airtable.com/v0/appTJLFldOxuL7FEU/Table%201/' + records,
                                   headers=headers)
        print("Delete Reponse: " + str(response))
    # POSTs updated list of servers the bot is in
    for i in range(len(servers)):
        id = list(str(servers[i].id))
        idsplit1 = []
        idsplit2 = []
        for split_id in range(len(id)):
            if p <= 8:
                idsplit1.append(id[split_id])
            else:
                idsplit2.append(id[split_id])
        id1 = str()
        id2 = str()
        for id_stitch in range(len(idsplit1)):
            id1 = id1 + idsplit1[id_stitch]
            id2 = id2 + idsplit2[id_stitch]
        id = id1 + id2
        plan = plan_types.get(str(id))
        headers = {
            'Authorization': 'Bearer keyBZeqZsQTYXemrk',
            'Content-Type': 'application/json',
        }

        data = '{ "records": [ { "fields": { "guild_id": ' + str(id1) + ', "guild_id2": ' + str(
            id2) + ', "plan_type": ' + str(plan) + '} }] }'

        response = requests.post('https://api.airtable.com/v0/appTJLFldOxuL7FEU/Table%201', headers=headers,
                                 data=data)
        print("Post Response: " + str(response))
    # returns updated version of the table
    headers = {
        'Authorization': 'Bearer keyBZeqZsQTYXemrk',
    }

    params = (
        ('maxRecords', 3),
        ('view', 'Grid view'),
    )
    response = requests.get('https://api.airtable.com/v0/appTJLFldOxuL7FEU/Table%201', headers=headers,
                            params=params)
    print("Get Response: " + str(response))
    data = response.json()
    for finalGET in range(len(servers)):
        records1 = str(data["records"][finalGET]["fields"]["guild_id"])
        records2 = str(data["records"][finalGET]["fields"]["guild_id2"])
        records = records1 + records2
    # prints that the bot is ready to go
    print("Status: OK")




@bot.command()
async def help(command, *, msg=''):
    embed = discord.Embed(
        colour=discord.Colour.red()
    )
    embed.set_author(name="chAD help")
    if msg == '':
        embed.add_field(name="setfreq", ari='Change frequency of ad (minimum premium plan required). Usage: adsetfreq [frequency]', inline="False")