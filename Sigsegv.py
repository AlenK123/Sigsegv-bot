import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import requests
import os
import random
from pathlib import Path


''' 
	Sigsegv is a bot for Arik's discord server
	Author: AlenK123 AKA Melon Musk#1142
'''
def get_token():
    file = open("token.txt", "r")
    token = file.read()
    file.close()
    return token



TOKEN = get_token()

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
		