# v04.03 - Created by Richard Mongrolle - Open Source ;)

# 0 - Config

# 0.1 - Import
# os = for use "config" file
from imaplib import Commands
import os

# datetime = for see the actual datetime
from datetime import datetime

# numpy = for add some useful functions
import numpy as np

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

@client.event
async def on_message(message):
    if message.content.startswith("!ano "): # 1.01 - !ano
        print ("\n" , time_now , " --- ", message.content )
        
        bot_message = message.content.replace("!ano ", '')

        await message.channel.send( bot_message )

        await message.delete()
    
    if message.content.startswith("!rewrite "): # 1.02 - !rewrite
        print ("\n" , time_now , " --- ", message.content )

        await message.delete(1172740959885332510)

    if message.content.startswith("!delete "): # 1.03 - !delete
        number = int(message.content.split()[1])
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

    if message.content.startswith("!grouplist "): # 1.04 - !grouplist
        print ("\n" , time_now , " --- ", message.content )
        
        bot_message = message.content.replace("!grouplist ", '')

        async def getuser(ctx, role: discord.Role):
            await ctx.send("\n".join(str(member) for member in role.members))

        send_message = getuser(role='Conquerors')

        print("\n", send_message, "\n")

        await message.channel.send( send_message )

        """
        if discord.Role.name() == bot_message:
            bot_send = discord.Role.members()
            await message.channel.send()
        else:
            await message.channel.send('Ups! Wrong role name.', delete_after=10)
        """
# ==============================

# TOKEN = security ID of the bot /!\ CONFIDENTIAL /!\
client.run(token)