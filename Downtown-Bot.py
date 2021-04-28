# Import librarys
import discord
from discord.ext import commands
import random
import asyncio
import json

# Bot prefix
client = commands.Bot(command_prefix = ".")

# Remove help
client.remove_command("help")

# Print 'Bot is ready.' in command line
@client.event
async def on_ready():
    print('The bot is ready.')

async def ch_pr():
    await client.wait_until_ready()
    
    statuses = [f"on {len(client.guilds)} servers | .help", "made using discord.py", "www.downtownbot.ml",f"{round(client.latency * 1000)}ms ping" ]

    while not client.is_closed():

        status = random.choice(statuses)
        
        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(20)

# Ping/ms command
@client.command(aliases=['ms'])
async def ping(ctx):
    await ctx.send(f'The bot has {round(client.latency * 1000)}ms ping.')
    print('Ping/ms command has executed')

# Invite link command
@client.command(aliases=['link'])
async def invite(ctx):
    em = discord.Embed(title="Invite Link", description="The invite link for the Downtown Bot can be accessed at https://www.downtownbot.ml", color=discord.Colour.purple())
    
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")
    
    await ctx.send(embed=em)
    print('Invite/link command has executed')

# Kick command
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    print('Kick command has executed')

# Ban command
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    print('Ban command has executed')

# Help command
@client.group(invoke_without_command=True)
async def help(ctx):
    
    em = discord.Embed(title="Help", description="Use .help <command> for extended information on a command", color=discord.Colour.purple())
    
    em.add_field(name="Moderation", value="kick, ban")
    em.add_field(name="Fun", value="invite, ping" )
    
    await ctx.send(embed=em)
    print('Help command has executed')

# Help kick command 
@help.command()
async def kick(ctx):
    em = discord.Embed(title = "Kick", description="Kicks a member from the guild", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.kick <member> [reason]`")

    await ctx.send(embed=em)
    print("Help kick command has executed")

# Help ban command
@help.command()
async def ban(ctx):
    em = discord.Embed(title = "Ban", description="Bans a member from the guild", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.ban <member> [reason]`")

    await ctx.send(embed=em)
    print("Help ban command has executed")

# Help ping command
@help.command(aliases=['ms'])
async def ping(ctx):
    em = discord.Embed(title = "Ping/ms", description="Displays the current ping of the bot", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.ping/ms`")

    await ctx.send(embed=em)
    print("Help ping/ms command has executed")

# Help ping command
@help.command(aliases=['link'])
async def invite(ctx):
    em = discord.Embed(title = "Invite/link", description="Displays the invite link of Downtown Bot and Relaxed Downtown", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.invite/link`")

    await ctx.send(embed=em)
    print("Help invite/link command has executed")




# # (RD Only) VIP role 🌟
# @client.event
# async def on_member_update(before, after, guild):
#     role = after.guild.get_role(834942375377764352)
#     print(role, before.roles, after.roles)
#     if role in after.roles and role not in before.roles:
#         await after.edit(nick=f"🌟 {after.nick}")

client.loop.create_task(ch_pr())
client.run('ODM0ODQ2NTM2OTEwODk3MTkz.YIG1bQ.AqCnQgMx7U7esXlhebz6QTzky9k')
