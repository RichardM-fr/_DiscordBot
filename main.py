# v04.01 - Created by Richard Mongrolle - Open Source ;)

# 0 - Config

# 0.1 - os = for use "config" file
import os

# 0.2 - discord = actually v2.2
import discord

# 0.3 - dotenv = load in the venv the config
from dotenv import load_dotenv
load_dotenv(dotenv_path="config")

# 0.4 - Load all intents (and not only defaults)
client = discord.Client(intents=discord.Intents.all())

# 0.5 - Load token security (don't add it on your repository)
token = os.getenv("TOKEN")

# 0.6 - Display in console when the bot is ON
@client.event
async def on_ready():
	print("\n--- BOT - Status: Online ---\n")

# ==============================

# 1 - Commands

# 1.01 - !del
@client.event
async def on_message(message):
    if message.content.startswith("!del "):
        print ("\n[Content] " , message.content )
        print ("[ID] " , message.id , "\n")
        
        bot_message = message.content.replace("!del ", '')

        await message.channel.send( bot_message )

        await message.delete()

# ==============================

# TOKEN = security ID of the bot /!\ CONFIDENTIAL /!\
client.run(token)