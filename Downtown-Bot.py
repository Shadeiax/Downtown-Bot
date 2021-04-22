import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "rd.")

# Print 'Bot is ready.' in command line
@client.event
async def on_ready():
    print('The bot is ready.')

# Ping/ms command
@client.command(aliases=['ms'])
async def ping(ctx):
    await ctx.send(f'The bot has {round(client.latency * 1000)}ms ping.')
    print('Ping/ms command executed.')
# Invite link command
@client.command()
async def invite(ctx):     
    await ctx.send('The invite link to Relaxed Downtown is: https://discord.gg/NAhTTaaJuv')                         
    print('Invite command executed.')
client.run('ODM0ODQ2NTM2OTEwODk3MTkz.YIG1bQ._uT3DyCT8UFNm6-Pi53yzFMGANI')