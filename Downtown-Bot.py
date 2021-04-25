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

@client.event
async def on_member_update(before, after):
    role = after.guild.get_role(834942375377764352)
    if role in after.roles and role not in before.roles:
        print(role, before.roles, after.roles)
        after.edit(nick=f"🌟 {after.nick}")





client.run('TOKEN')

