import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
import requests
import os
import random
import time
import datetime
import threading
import sqlite3


''' 
	Sigsegv is a bot for Arik's discord server
	Author: AlenK123 AKA Melon Musk#1142
'''

THUMBNAIL_URL = "https://cdn1.macworld.co.uk/cmsdata/features/3608274/Terminalicon2_thumb800.png"

FSSONG = "https://www.youtube.com/watch?v=9sJUDx7iEJw"

OPEN = "I\'m sorry {} I\'m afraid I cant let you do that"

TRAGEDY = "Did you ever hear the Tragedy of Darth Plagueis the wise? I thought not. It's not a story the Jedi would tell you.\
 It's a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians\
 to create life... He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force\
 is a pathway to many abilities some consider to be unnatural. He became so powerful... the only thing he was afraid of was losing his power, which\
 eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. It's ironic\
 he could save others from death, but not himself."

HELP = "hello - Says hello\nbayad - Does bayad\n\
storythatthejediwonttellme - Tells you a sith legend\nsnap - Snaps the Cringe\ncaps <string> - Sends back what you say in\
 capital letters\nclickbait - Generates a clickbait for you\ndump <optional string> - Dumps the data of your string or random data\n\
freesoftware - Plays a nice song\naddrole <role name> - Adds a role\nfeedback <feedback> - You can describe errors or command ideas for\
 @Melon Musk#1142 and he will address it later\nopenthepodbaydoors - opens the pod bay doors"


def get_token():
	file = open("token.txt", "r")
	token = file.read()
	file.close()
	return token

Bot = Bot(command_prefix=">")
Bot.remove_command("help")


@Bot.event
async def on_ready():
	print('Logged in as {} ID: {} | Connected to {} servers | Connected to {} users'.format(Bot.user.name, Bot.user.id, len(Bot.guilds), len(set(Bot.get_all_members()))))
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(Bot.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(Bot.user.id))
	print('--------')

@Bot.event
async def on_message(message):
	if message.content.lower() == "fuck off" and message.author.mention == "<@198128099949412352>":
		await message.channel.send("Fuck Mode: Off")
	elif message.content.lower() == "fuck on" and message.author.mention == "<@198128099949412352>":
		await message.channel.send("Fuck Mode: On")
	await Bot.process_commands(message)

@Bot.command()
async def help(ctx, *args):
	block = discord.Embed(title="Command List:", description="", color=0xFFFFFF)
	commands_list = HELP.split("\n")
	for name_dis in commands_list:
		block.add_field(name=Bot.command_prefix + name_dis.split(" - ")[0], value=name_dis.split(" - ")[1], inline=False)
	block.set_thumbnail(url=THUMBNAIL_URL)
	await ctx.send(embed=block)

@Bot.command()
async def hello(ctx, *args):
	await ctx.send("Hello " + ctx.message.author.mention + "!")

@Bot.command()
async def storythatthejediwonttellme(ctx, *args):
	await ctx.send(TRAGEDY)

@Bot.command()
async def bayad(ctx, *args):
	await ctx.send(":sweat_drops: ")

@Bot.command()
async def snap(ctx, *args):
	with open("cc.gif", 'rb') as f:
		await ctx.send(file=discord.File(f, "cc.gif"))

@Bot.command()
async def caps(ctx, *args):
	msgstr = ""
	if len(args) > 0:
		for word in args:
			msgstr += (word + " ")
		await ctx.send(msgstr.upper())
	else:
		await ctx.send("Usge: `{}caps <string of letters to capitalize>`".format(Bot.command_prefix))

@Bot.command()
async def clickbait(ctx, *args):
	await ctx.send("Command is still in progress ;)")

@Bot.command()
async def dump(ctx, *args):
	hex_str = ""
	ascii_str = ""
	if len(args) > 0:
		ascii_str = ' '.join(args)
		for _char in ascii_str:
			hex_str += ("\\x%0.2X" % ord(_char))
	else: 
		for i in range(256):
			hex_str += ("\\x%0.2X" % random.randint(0 ,255))
	await ctx.send(hex_str)

@Bot.command()
async def freesoftware(ctx, *args):
	with open("rs.gif", 'rb') as f:
		await ctx.send(file=discord.File(f, "rs.gif"))

	author = ctx.message.author
	channel = author.voice.voice_channel
	await bot.join_voice_channel(channel)
	player = await vc.create_ytdl_player()
	player.start(FSSONG)
	

@Bot.command()
async def addrole(ctx, *args):
	await ctx.send("No")

@Bot.command()
async def feedback(ctx, *args):
	if len(args) > 0:
		blacklist = ["<@177737114790658048>"]
		with open("Feedback.txt", "w") as f:
			if ctx.message.author.mention in blacklist:
				await ctx.send("sorry blacklisted users cant give feedback")
			else:
				f.write(ctx.message.author.mention + ": " + ' '.join(args))
				await ctx.send("Thanks, " + ctx.message.author.mention + "! Melon will address it later!")
	else:
		await ctx.send("Usage: `{}feedback <Feedback description>`".format(Bot.command_prefix))

@Bot.command()
async def openthepodbaydoors(ctx, *args):
	await ctx.send(OPEN.format(ctx.message.author.mention))

@Bot.command()
async def terminal(ctx, *args):
	if (ctx.message.author.mention == "<@198128099949412352>"):
		gen_chnls = []
		for guild in Bot.guilds:
			for chnl in guild.channels:
				if isinstance(chnl, discord.channel.TextChannel) and chnl.name.lower() == "general":
					gen_chnls.append(chnl)
		rawMessage = ""
		if (args[0] == "broadcast"):
			for g_cnl in gen_chnls:
				await g_cnl.send(' '.join(args[1:]))
		elif (args[0] == "ls"):

			if (args[1] == "guilds"):
				rawMessage = str(Bot.guilds)

			elif (args[1] == "channels"):
				chnls = []
				for guild in Bot.guilds:
					for chnl in guild.channels:
						chnls.append(chnl)
				rawMessage = str(chnls)

			elif (args[1] == "members"):
				rawMessage = str(set(Bot.get_all_members()))

			splitMessage = 0
			attempts = 0
			while splitMessage != "":
				attempts += 1
				splitMessage = rawMessage[(1999 * attempts) - 1999:1999 * attempts]
				if splitMessage == "":
					pass
				else:
					await ctx.send(splitMessage)
Bot.run(get_token())
		
