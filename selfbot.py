#Coded By Aura
#Prefix (/)
import discord
import asyncio
import os
import random
import time
import sys, traceback
from discord.ext import commands, tasks
from itertools import cycle

bot = commands.Bot("/", self_bot=True)


@bot.event
async def on_ready():

 await bot.change_presence(activity=discord.Game(name='Watching The FBI', type=3, url='https://twitch.tv/kraken'))
 print(" ▄████▄   ▒█████   ███▄    █  ███▄    █ ▓█████  ▄████▄  ▄▄▄█████▓▓█████ ▓█████▄")
 print("▒██▀ ▀█  ▒██▒  ██▒ ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▒██▀ ▀█  ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌")
 print("▒▓█    ▄ ▒██░  ██▒▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▒▓█    ▄ ▒ ▓██░ ▒░▒███   ░██   █▌")
 print("▒▓▓▄ ▄██▒▒██   ██░▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌")
 print("▒ ▓███▀ ░░ ████▓▒░▒██░   ▓██░▒██░   ▓██░░▒████▒▒ ▓███▀ ░  ▒██▒ ░ ░▒████▒░▒████▓ ")
 print("░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ░▒ ▒  ░  ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒ ")
 print("  ░  ▒     ░ ▒ ▒░ ░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░  ▒       ░     ░ ░  ░ ░ ▒  ▒")
 print("                              Coded By Aura")
 print("                                   <3")

#I Hope You Enjoy This Selfbot As Much As I Did Coding It
#Selfbots Are Against Discords TOS :/
#This Is For Educational Puporses I Guess lmao.
#Connected By Aura <3
#Language Python Duh!

@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def load(ctx, extension):
        bot.load_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endwith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command()
async def ping(ctx):
    await ctx.send(f'\n```\n----------\nPong!\nResponse Time {round(bot.latency * 1000)}ms\nConnected To Server\n----------\n```')

@bot.command()
async def purge(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    #Purge Command

@bot.command()
async def ban(ctx, member : discord.Member ):
    await member.ban()
    await ctx.send("Banned! :wave:")
    #ban command

@bot.command()
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.send("Kicked! :wave:")
    #kick command

@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question):
  responses = ['It is certain.',
               'It is decidedly so.',
               'Without a doubt.',
               'Yes - definitely.',
               'You may rely on it.',
               'As I see it, yes.',
               'Most likely.',
               'Outlook good.',
               'Yes.',
               'Signs point to yes.',
               'Reply hazy, try again.',
               'Ask again later.',
               'Better not tell you now.',
               'Cannot predict now.',
               'Concentrate and ask again.',
               'Dont count on it.',
               'My reply is no.',
               'My sources say no.',
               'Outlook not so good.',
               'Very doubtful.',]

  
  await ctx.send(f'```\nQuestion : {question}\n\nAnswer : {random.choice(responses)}\n```')

  #8ball command

@bot.command()
async def anime(ctx):
    responses = ['https://media.giphy.com/media/f0yOYF0EtwSVa/giphy.gif',
                 'https://media.giphy.com/media/UYzNgRSTf9X1e/giphy.gif',
                 'https://media.giphy.com/media/DeBBINXN86r8Q/giphy.gif',
                 'https://media.giphy.com/media/7hW7hXXri33NK/giphy.gif',
                 'https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif',
                 'https://media.discordapp.net/attachments/561513392402202636/599655606617636864/1520666958_violet_3.gif?width=400&height=226',
                 'https://media.discordapp.net/attachments/590265983248236575/599655841188020225/rage_quit.gif?width=400&height=225',
                 'https://cdn.discordapp.com/attachments/590265983248236575/599655905554071602/tohru.gif',
                 'https://media.discordapp.net/attachments/590265983248236575/599655718991298570/anime_violet.gif?width=400&height=215',
                 'https://media.discordapp.net/attachments/590265983248236575/599655722984275972/cute.gif?width=400&height=225',
                 'https://media.discordapp.net/attachments/590265983248236575/599657446067273760/kyokai.gif',
                 'https://media.discordapp.net/attachments/590265983248236575/599655989268185088/violet.gif?format=png&width=267&height=300',]
                 
                 
                 

    await ctx.send(f'Here You Go! <3\n{random.choice(responses)}')
    #anime pictures cause yano

      

bot.run("ENTER TOKEN HERE", bot=False)
