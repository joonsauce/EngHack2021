from setting import *

def getRandomAtt():
    data = getData("ads")
    x = len(data["records"])
    num = randint(0, x)
    return data["records"][num]["fields"]

def sendAD():
    embed = discord.Embed(
        color=discord.Colour.dark_red()
    )

    dictionary = getRandomAtt()

    embed.set_author(name="Advertisement from {}".format(dictionary["compName"]))
    embed.set_image(url=dictionary["imgLink"])

    embed.add_field(name='What is {}?'.format(dictionary["compName"]),
                    value=dictionary["msgFromSponsor"] + " " + dictionary["link2sponsor"],
                    inline=False)
    return embed

def getData(type):
    if type == "ud":
        url = api_link
    else:
        url = api_link2

    response = requests.get(url=url,
                            headers=header1,
                            params=params)
    print("Get Response: " + str(response))
    data = response.json()
    return data

def addMoney(server):
    data = getData("ud")
    # updates amount of money in airtable
    for serverIDGET in range(len(data["records"])):
        serverID1 = str(data["records"][serverIDGET]["fields"]["guild_id"])
        serverID = serverID1 + str(data["records"][serverIDGET]["fields"]["guild_id2"])
        if serverID == server:
            record_id = data["records"][serverIDGET]["id"]
            current_money = data["records"][serverIDGET]["fields"]["plan_type"]
            break
        else:
            pass
    money = current_money + 0.01

    updateData(serverID1, 0, money, record_id)

def updateData(serverID1, type, value, record_id):
    if type == 0:
        data = '{"fields": { "guild_id": ' + str(serverID1) + ', "plan_type": ' + str(value) + '}}'
    else:
        data = '{"fields": { "guild_id": ' + str(serverID1) + ', "text_count": ' + str(value) + '}}'

    url = api_link + str(record_id)
    response = requests.patch(url=url,
                              headers=header2,
                              data=data)
    print("Update Response: " + str(response))