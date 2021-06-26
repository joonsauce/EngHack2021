from setting import * 

message_counts = {"706326031551954975": 0, "857452766121295883": 0}


@bot.event
async def on_message(message):
    if bot.user.id == message.author.id:
        pass
    else:
        server_id = str(message.guild.id)
        if server_id in message_counts.keys():
            count = int(message_counts.get(server_id))
            count += 1
        else:
            count = 1
            message_counts.setdefault({server_id: count})
        if count > 4:
            ans = sendAD()
            await message.channel.send(embed=ans)
            message_counts.update({server_id: 0})
        else:
            message_counts.update({server_id: count})


advertisements = [ 
    {"compName": "NPX",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/114/highres/NPX_clear_background.png",  
    "msgFromSponsor": "We believe that Nuclear Energy is key in fighting the climate crisis. We are doing our part to make nuclear more cost effective by integrating modern tools and technologies into the way we operate nuclear plants with a focus on data security and regulatory compliance.",  
    "link2sponsor": "https://www.npxinnovation.ca/"},
    
    {"compName": "Cisco",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/118/highres/Cisco-logo.png",  
    "msgFromSponsor": "If anyone can lay claim to a 'heritage' in an industry as young as global networking, then it is Cisco. Not only does 85 percent of Internet traffic travel across Cisco's systems, we also use the Internet to run our own business online, from product orders and inventory management through to staff communications and travel expenses.",  
    "link2sponsor": "https://www.cisco.com/c/en_ca/index.html"},
    
    {"compName": "CCPPA",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/115/highres/image001.jpg",  
    "msgFromSponsor": "Our Vision is The Clear Choice is Concrete. CCPPA was established in 2013 to represent concrete pipe producers, precast concrete manufacturers and suppliers to the precast concrete industry. As a not-for-profit association, our Mission is Protect & Advance our Industry, and the interests of concrete pipe and precast concrete products used in Canada.",  
    "link2sponsor": "https://ccppa.ca/"},
    
    {"compName": "Kinross",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/116/highres/Kinross_1920x1080_Gold.png",  
    "msgFromSponsor": "Kinross offers a compelling investment opportunity as a senior gold producer with an excellent operational track record, strong balance sheet and commitment to responsible mining.",  
    "link2sponsor": "https://www.kinross.com/home/default.aspx"},
    
    {"compName": "U of W Faculty of Engineering",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/119/highres/waterloo_engineering_logo_rgb.jpg",  
    "msgFromSponsor": "Ranked among the top 50 engineering schools worldwide, Waterloo Engineering is committed to leading engineering education and research.\nWe are the largest engineering school in Canada, with over 10,500 students enrolled in 2020. In 2019/20, external research funding from Canadian and international partners exceeded $86.8 million, a strong indication of our extensive industry partnerships and the excellence of our engineering research programs.",  
    "link2sponsor": "https://uwaterloo.ca/engineering/"},
    
    {"compName": "FDM Group",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/113/highres/fdm-logo-black.png",  
    "msgFromSponsor": "FDM specialises in bridging the gap between university and the professional workplace. Gain industry training and commercial experience, get in touch to find out more! Support and Development. Hands-on Experience. Award-Winning Training. Multinational Clients.",  
    "link2sponsor": "https://www.fdmgroup.com/en-ca/ca-home/"},
    
    {"compName": "NERv Technology",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/117/highres/NERv.png",  
    "msgFromSponsor": "NERv’s smart monitoring helps detect early anastomotic postoperative complications. Platform sensing technology augments existing wound drains and catheters and delivers recovery data to healthcare providers. Find out how you can decrease surgeon’s response time, make patient recovery easier and save lives.",  
    "link2sponsor": "https://nervtechnology.com/"},
    
    {"compName": "Bloomberg",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/112/highres/Bloomberg-logo.png",  
    "msgFromSponsor": "Bloomberg L.P. provides financial software tools and enterprise applications such as analytics and equity trading platform, data services, and news to financial companies and organizations through the Bloomberg Terminal (via its Bloomberg Professional Service), its core revenue-generating product.[9] Bloomberg L.P. also includes a wire service (Bloomberg News), a global television network (Bloomberg Television), websites, radio stations (Bloomberg Radio), subscription-only newsletters, and two magazines: Bloomberg Businessweek and Bloomberg Markets.",  
    "link2sponsor": "https://www.bloomberg.com/canada"},
    
    {"compName": "10minuteninja",  
    "imgLink": "https://s3.amazonaws.com/challengepost/sponsors/logos/000/021/120/highres/Ninja_black.png",  
    "msgFromSponsor": "Daily essentials at your door in 10 minutes. $1.99 delivery fee, low prices. now serving UW & WLU.",  
    "link2sponsor": "https://www.ninjadelivery.ca/"}]

def getRandomAtt():   
    num = randint(0, 8) 
    #print(advertisements[num])
    return advertisements[num]

    

def sendAD():
    embed = discord.Embed(
        color=discord.Colour.dark_red()
    )

    dictionary = getRandomAtt()

    embed.set_author("Advertisement from {}".format(dictionary["name"]))
    embed.set_image(url=dictionary["link2sponsor"])

    embed.add_field(name='What is {}?'.format(dictionary["name"]), value=dictionary["msgFromSponsor"], inline=False)



def getIDFromAirTable(iniID):
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
    idList = []
    for airtblGET in range(len(data["response"])):
        records1 = str(data["records"][airtblGET]["fields"]["guild_id"])
        records2 = str(data["records"][airtblGET]["fields"]["guild_id2"])
        record = records1 + records2
        if record == iniID:
            break
        else:
            pass




   

def adSend(ctx,link,message):
    await ctx.send(link + "\n"+message)

    
    









   





    

    



bot.run('ODU4MjE3MTg3MTY0Njg0MzI5.YNa7Cg.xt-Vkr7vtw8-8w4yen833L9R8JM')