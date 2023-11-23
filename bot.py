# v08.01 - Created by Richard Mongrolle - Open Source ;)

# 0 - CONFIG

# -----------------------
# 0.1 - Import
# os = for use "config" file
import os

# discord.py = actually v2.2
import discord
from discord.utils import get
from discord.ui import Button, View
from discord.ext import commands

# interactions = for add interactions between stuff like buttons and the user
import interactions

# datetime = for see the actual datetime
from datetime import datetime, timezone

# python-dateutil = for the parsing date
from dateutil import parser

# pytz = python timezone
import pytz

# io = binary classes, used for the attachements on Discord
import io

# langdeteect = detect the language
from langdetect import detect

# googletrans = translate content
from googletrans import Translator

# argparse = for add some parameters into commands
import argparse

# logging = for logging tasks to a file
import logging

# python-dotenv = load in the venv the config
from dotenv import load_dotenv
load_dotenv(dotenv_path="config_debug")

# -----------------------
# 0.2 - Load token security (don't add it on your repository)
token = os.getenv("TOKEN")

# -----------------------
# 0.3 - Save time
global time_now
time_now = datetime.now().strftime("%H:%M:%S")

# -----------------------
# 0.4 - Start the bot with the prefix and all intents

'''
STABLE MODE
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
'''

'''
DEBUG MODE
'''
bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

bot.created_post_id = None

# Display in console when the bot is ON
@bot.event
async def on_ready():
    print("\n--- BOT - Status: Online --- Version: v08.01 " , time_now , "---\n")

# ==============================

# 1 - LOGS

# -----------------------
# 1.1 - Configure logging to a file
logging.basicConfig(filename='bot_tasks.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# -----------------------
# 1.2 - Function to log tasks and send logs to a specified Discord channel
async def log_task(ctx, task_name, details):
    # Log the task with the current timestamp
    logging.info(f'Channel Name: {ctx.channel.name} - User: {ctx.author.name} - Task: {task_name} - {details}')

    # Specify the Discord channel ID where you want to send logs
    log_channel_id = 1172745374902005870

    # Send the log to the specified Discord channel
    log_channel = ctx.guild.get_channel(log_channel_id)
    if log_channel:
        log_message = f'**Channel Name:** `{ctx.channel.name}` - **User:** `{ctx.author.name}` - **Command:** `{task_name}` - **Content:** `{details}`\n.'
        await log_channel.send(log_message)

# ==============================

# 2 - COMMANDS

# Function for checking the "Admin" role
def check_role(ctx):
    # Retrieve the server (guild) from the context
    guild = ctx.guild

    # Get the "Leaders" role by its name
    admin_role = discord.utils.get(guild.roles, name="Leaders")

    # Check if the command author has the good role
    return admin_role in ctx.author.roles

# -----------------------
# 2.1 - Configure logging when the bot receives the 'ano' command
@bot.command(name='ano')
@commands.check(check_role)
async def anonymize(ctx):
    """
    Write the message directly by the bot.
    Usage: !ano <Your message>
    """
    # Check if the command is in a text channel
    if isinstance(ctx.channel, discord.TextChannel):
        # Delete the message
        await ctx.message.delete()

        # Extract the text after "!ano" and remove leading/trailing spaces
        content_without_command = ctx.message.content[len('!ano'):].strip()

        # Call the log_task function
        await log_task(ctx, 'Anonymize', f'{content_without_command}')

        # Rewrite the message without displaying the command
        await ctx.send(content_without_command)

# -----------------------
# 2.2 - Configure logging when the bot receives the 'delete' command
@bot.command(name='delete')
@commands.check(check_role)
async def delete_messages(ctx, num_messages: int):
    """
    Delete a specified number of messages.
    Usage: !delete <Number messages>
    """
    # Check if the command is in a text channel
    if isinstance(ctx.channel, discord.TextChannel):
        # Delete the command message
        await ctx.message.delete()

        # Check if the number of messages to delete is greater than 0
        if num_messages > 0:
            # Fetch the last 'num_messages' messages in the channel
            messages = ctx.channel.history(limit=num_messages)

            # Use an async for loop to extract messages from the async generator
            messages_list = []
            async for message in messages:
                messages_list.append(message)
                if len(messages_list) == num_messages + 1:
                    break  # Stop after fetching the required number of messages

            # Delete the fetched messages
            for message in messages_list:
                await message.delete()

            # Call the log_task function
            await log_task(ctx, 'Delete messages', f'{num_messages}')
        else:
            # Send the warning message and delete it after 10 seconds
            await ctx.send("Please provide a valid number of messages to delete (greater than 0).", delete_after=10)

# -----------------------
# 2.3 - Configure logging when the bot receives the 'rewrite' command
@bot.command(name='rewrite')
@commands.check(check_role)
async def rewrite_message(ctx, user_id: int, message_id: int):
    """
    Rewrite a specified message.
    Usage: !rewrite <Member ID> <Message ID>
    """
    # Check if the command is in a text channel
    if isinstance(ctx.channel, discord.TextChannel):
        # Delete the command message
        await ctx.message.delete()

        try:
            # Fetch the user by ID
            user = await bot.fetch_user(user_id)

            # Fetch the message with the specified ID
            message = await ctx.channel.fetch_message(message_id)

            # Check if the user and message are found
            if user and message:
                # Check if the message is sent by the specified user
                if message.author.id == user.id:
                    # Delete the original message
                    await message.delete()

                    # Send a new message mimicking the original content
                    if message.content:
                        await ctx.send(content=message.content)

                    # Check if the original message has attachments (images)
                    if message.attachments:
                        for attachment in message.attachments:
                            # Download the attachment
                            attachment_content = await attachment.read()

                            # Send the attachment with the new message
                            await ctx.send(file=discord.File(io.BytesIO(attachment_content), filename=attachment.filename))

                    # Call the log_task function
                    await log_task(ctx, 'Rewrite message', f'User ID: {user.id}, Message ID: {message.id}')
                else:
                    # Send an error message if the message is not from the specified user
                    await ctx.send("You can only rewrite messages from the specified user.", delete_after=10)
            else:
                # Send an error message if the user or message is not found
                await ctx.send("User or message not found.", delete_after=10)
        except discord.NotFound:
            # Send an error message if the user or message is not found
            await ctx.send("User or message not found.", delete_after=10)

# ==============================

# 3 - EVENTS

# -----------------------
# 3.1 - Sending a private welcome message to new members

bot.created_post_id = None

@bot.event
async def on_member_join(member):
    # Specify the message you want to send to new members
    welcome_message = f"# Welcome to the **[CON] Conquerors server**! \nHello {member.mention}! We're glad to have you here. :)\nIf you want to be **recruited** (including if you're already in the alliance ingame): https://discord.com/channels/1153929255126835293/1171661982097752164 \nIf you have any **problem**: https://discord.com/channels/1153929255126835293/1171659185725915146 \nAnd, be sure to have read ours **rules**: https://discord.com/channels/1153929255126835293/1176645239662977044 \nLet's talk now! :)"

    # Send the welcome message as a private message to the new user
    await member.send(welcome_message)

# ==============================

# TOKEN = security ID of the bot /!\ CONFIDENTIAL /!\
bot.run(token)