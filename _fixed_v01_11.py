bot_version = "v01.11"
print("\n--- BOT - Version: " , bot_version , " - File: _fixed_v01_11.py ---\n") # Coma! \n for line break

import discord

# 0.1 - All intents are loaded
client = discord.Client(intents=discord.Intents.all())

# 0.2 - Starting
@client.event
async def on_ready():
	print("\n--- BOT - Status: Online ---\n")

# 0.3 - Variables
count_messages = 0


# ------------------------------

# 1.01 - Messages event

@client.event
async def on_message(message):
    global count_messages
    if message.content.lower() == "ping":
        print ("message.content == 'ping' -> true") # Display a message into the console
        await message.channel.send("Pong")
        count_messages += 1
        print ("[ Message number " , count_messages , " ]") # Use coma for separate STR to VAR

# ------------------------------

# TOKEN
client.run("")
