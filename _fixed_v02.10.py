bot_version = "v02.10"
print("\n--- BOT - Version: " , bot_version , " - File: _fixed_v02_10.py ---\n") # Coma! \n for line break

import discord

# 0.1 - All intents are loaded
client = discord.Client(intents=discord.Intents.all())

# 0.2 - Starting
@client.event
async def on_ready():
	print("\n--- BOT - Status: Online ---\n")

# ------------------------------

# 1.01 - Commands
@client.event
async def on_message(message):
    if message.content.startswith("!del"):
        print ("\n[Content] " , message.content )
        print ("[ID] " , message.id , "\n")
        await message.delete()
        await message.channel.send("[DEBUG] Message deleted!")

# ------------------------------

# TOKEN
<<<<<<< HEAD
client.run("") # Add your token here
=======
client.run("")
>>>>>>> 77a0c8941925532dbc726590712fcb978903b076
