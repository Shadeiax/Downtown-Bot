# Import librarys
import discord
from discord.ext import commands

# Bot prefix
client = commands.Bot(command_prefix = ".")

# Print 'Bot is ready.' in command line
@client.event
async def on_ready():
    print('The bot is ready.')

# Ping/ms command
@client.command(aliases=['ms'])
async def ping(ctx):
    await ctx.send(f'The bot has {round(client.latency * 1000)}ms ping.')

# Invite link command
@client.command()
async def invite(ctx):     
    await ctx.send('The invite link to Relaxed Downtown is: https://discord.gg/NAhTTaaJuv')                         

# VIP auto nickname
@client.event
async def on_member_update(before, after):
    
client.run('ODM0NDk4Mzk0ODQ0MTY4MjAz.YIBxMQ.8kdP181iHFlGOLLWIpXNBkCk_Tg')
