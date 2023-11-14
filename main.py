# v04.03 - Created by Richard Mongrolle - Open Source ;)

# 0 - Config

# 0.1 - Import
# os = for use "config" file
import os

# datetime = 
from datetime import datetime

# discord = actually v2.2
import discord

# dotenv = load in the venv the config
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

# 0.2 - Load all intents (and not only defaults)
client = discord.Client(intents=discord.Intents.all())

# 0.3 - Load token security (don't add it on your repository)
token = os.getenv("TOKEN")

# 0.4 - Save time
global time_now
time_now = datetime.now().strftime("%H:%M:%S")

# 0.5 - Display in console when the bot is ON
@client.event
async def on_ready():
	print("\n--- BOT - Status: Online ---" , time_now , "---\n")

# ==============================

# 1 - Commands

# 1.01 - !del
@client.event
async def on_message(message):
    if message.content.startswith("!ano "):
        print ("\n" , time_now , " --- ", message.content )
        
        bot_message = message.content.replace("!ano ", '')

        await message.channel.send( bot_message )

        await message.delete()
    
    if message.content.startswith("!rewrite "):
        print ("\n" , time_now , " --- ", message.content )

        await message.delete(1172740959885332510)

    if message.content.startswith("!grouplist "):
        print ("\n" , time_now , " --- ", message.content )

        bot_message = message.content.replace("!grouplist ", '')

        if role.name() == bot_message:
            bot_send = role.members()
            await message.channel.send()
        else:
            await message.channel.send('Ups! Wrong role name.', delete_after=10)

# ==============================

# TOKEN = security ID of the bot /!\ CONFIDENTIAL /!\
client.run(token)