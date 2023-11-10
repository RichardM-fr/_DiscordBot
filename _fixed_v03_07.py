bot_version = "v03.07"
print("\n--- BOT - Version: " , bot_version , " - File: main.py ---\n") # Coma! \n for line break

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
    if message.content.startswith("!del "):
        print ("\n[Content] " , message.content )
        print ("[ID] " , message.id , "\n")
        
        bot_message = message.content.replace("!del ", '')

        await message.channel.send( bot_message )

        await message.delete()
        # await message.channel.send("[DEBUG] Message deleted!")

# ------------------------------

# TOKEN
client.run("MTE3MTk1NDE0Mzk2ODEwNDQ1OA.G9lh8n.KOH9tRkCIVIYOuCyFamlMxv69fYPqxRI499ICE")