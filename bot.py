##           made by zog / liam gould            ##

## This is my first bot so sorry for whacky code ##
## I promise to make it better in the future!    ##
## Also follow me on twitter lol @zoggeneral     ##

#imports

import discord
import random
import praw
import time
import os

#actual code

client = discord.Client()

commandstxt = """```
prefix is s;

commands are NOT case sensitive

s;commands - Sends .txt file containing list of commands
s;source - Sends a link to the bot's source code
s;playing [text] - changes the bots game activity to your text

FILE COMMANDS
s;fetch [file name] - Sends the desired file. You must know the filename before using the command
s;upload [file] - The file you sent is uploaded to the bot.
s;randfile [amount] - Sends the amount of random files in the storage bot directory. If no amount is provided it defaults to 1. Caps out at 5 to prevent spam.
s;date - Sends stats of the directory.
s;dir - Sends the list of files in the directory.

More commands will be added soon!
```
"""

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game("Use s;commands"))

@client.event
async def on_message(message):
    
    txt = str(message.content).lower()
    members = message.guild.members
    
    if str(message.author) != "Storage bot#0957":
        try:
            if message.content.find("s;commands") != -1:
                await message.channel.send(commandstxt)

            if message.content.find("s;source") != -1:
                await message.channel.send("All storage bot code is here: \nhttps://github.com/flygon13/StorageBot")
                
            if message.content.find("s;upload") != -1:
                if len(message.attachments) == 0:
                    await message.channel.send("No attachments in command")
                else:
                    for file in message.attachments:
                        if file.filename in os.listdir():
                            newname = file.filename[:file.filename.find(".") - 1] + "(" + str(os.listdir().count(file.filename) + 1) + ")" + str(os.path.splitext(file.filename)[1])
                            await file.save(newname)
                            await message.channel.send(newname + " has been uploaded")
                        else:
                            await file.save(file.filename)
                            await message.channel.send(file.filename + " has been uploaded")

            if message.content.find("s;fetch") != -1:
                upload = open(txt[7:],"rb")
                await message.channel.send(file = discord.File(upload,txt[7:]))
                upload.close()

            if message.content.find("s;randfile") != -1:
                count = 0
                if len(message.content[10:]) == 0:
                    count = 1
                else:
                    count = int(message.content[10:])
                    if count > 5:
                        await message.channel.send("The amount of files the bot sends caps at 5.")
                        count = 5
                for i in range(count):
                    rand = random.choice(os.listdir()) # i would put this with the upload variable but i need a file name for the message
                    upload = open(rand,"rb")
                    await message.channel.send(file = discord.File(upload,rand))
                    upload.close()
                
            if message.content.find("s;data") != -1:
                size = os.path.getsize(os.getcwd())
                data = ""
                data += "Currently " + str(len(os.listdir())) + " files in the dir \n" #os.getcwd())
                data += "dir is currently " + str(size / 1000) + "KB"
                await message.channel.send(data)
                
            if message.content.find("s;dir") != -1:
                await message.channel.send(str(os.listdir()))                
        except Exception as e:
            await message.channel.send("An error has occured \nProcess ending with this error: "+str(e))


client.run("NjYxMzI5NTExNTIyMTA3NDEz.Xgp2QQ.DH14HrGN3nKjYLPEeGhhdhXOlbU")
