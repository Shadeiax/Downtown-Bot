# Import librarys
import discord
from discord.ext import commands

# Specify Token
TOKEN = "TOKEN"

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
<<<<<<< HEAD
@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')


# async def on_member_update(before, after):
#     if str(before.roel) == 'Level 9':
#         if str(after.role) == "VIP's"




client.run('ODM0ODQ2NTM2OTEwODk3MTkz.YIG1bQ.cnBtyNMeVTAJLfjwbmto7AJUvfg')
=======
@client.event
async def on_member_update(before, after):
    
client.run('TOKEN')
>>>>>>> 98b12eacd1e584575b6882ddd340b450164dc6f5
