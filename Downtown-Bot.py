# Import librarys
import discord
from discord.ext import commands
import random
import asyncio
import json
import os
import nacl
import youtube_dl
from discord import FFmpegPCMAudio
from discord.utils import get

# Intents
intents = discord.Intents.default()
intents.members = True

# Bot prefix
client = commands.Bot(command_prefix = ".", intents=intents, case_insensitive=True)

# Cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

# Remove default help command
client.remove_command("help")

# Print 'Bot is ready.' in command line
@client.event
async def on_ready():
    print('The bot is ready')

# Changing Status
async def ch_pr():
    await client.wait_until_ready()
    
    statuses = [f"on {len(client.guilds)} servers | .help", "made using discord.py", "relaxed-downtown.ml",f"{round(client.latency * 1000)}ms ping | .help", f"with {len(set(client.get_all_members()))} members | .help"]

    while not client.is_closed():

        status = random.choice(statuses)
        
        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(15)

# Ping/ms command
@client.command(aliases=['ms'])
async def ping(ctx):
    em = discord.Embed(title="Ping", description=f"The bot's ping is currently `{round(client.latency * 1000)}ms`", color=discord.Colour.purple())

    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print('Ping/ms command has executed')

# Help command
@client.group(invoke_without_command=True)
async def help(ctx):

    em = discord.Embed(title="Help", description="Use .help <command> for extended information on a command", color=discord.Colour.purple())

    em.add_field(name="Moderation", value="kick, ban, unban")
    em.add_field(name="Fun", value="8ball, coinflip" )
    em.add_field(name="Images", value="dog, lizard, cat" )
    em.add_field(name="Misc", value="invite, ping, about, workinprogress, playlist" )
    # em.add_field(name="Music", value="play, pause, resume, stop" )
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print('Help command has executed')

# Help kick command
@help.command()
async def kick(ctx):
    em = discord.Embed(title = "Kick", description="Kicks a member from the guild", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.kick <member> [reason]`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help kick command has executed")

# Help ban command
@help.command()
async def ban(ctx):
    em = discord.Embed(title = "Ban", description="Bans a member from the guild", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.ban <member> [reason]`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help ban command has executed")

# Help ping command
@help.command(aliases=['ms'])
async def ping(ctx):
    em = discord.Embed(title = "Ping/ms", description="Displays the current ping of the bot", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.ping/ms`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help ping/ms command has executed")

# Help 8ball
@help.command(aliases=['8ball'])
async def _8ball(ctx):
    em = discord.Embed(title = "8ball", description="Answers a question with a random 8ball answer!", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.8ball <question>`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help 8ball command has executed")

# Help ping command
@help.command(aliases=['link'])
async def invite(ctx):
    em = discord.Embed(title = "Invite/link", description="Displays the invite link of Downtown Bot and Relaxed Downtown", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.invite/link`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help invite/link command has executed")

# Help about
@help.command()
async def about(ctx):
    em = discord.Embed(title = "About", description="Displays the infomation about the bot", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.about`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help about command has executed")

# Help workinprogres/wip
@help.command(aliases=['wip'])
async def workinprogress(ctx):
    em = discord.Embed(title = "Work In Progress", description="Displays the features that carter.py would like to add to the bot", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.workinprogress/wip`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help workinprogress/wip command has executed")

# Help coinflip
@help.command(aliases=['cf'])
async def coinflip(ctx):
    em = discord.Embed(title = "Coinflip", description="Displays a randomized coinflip", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.coinflip/cf <prediction>`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help coinflip/cf command has executed")

# Help dog
@help.command(aliases=['doge'])
async def dog(ctx):
    em = discord.Embed(title = "Dog", description="Displays a randomized dog image", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.dog/doge`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help dog/doge command has executed")

# Help amphibian
@help.command()
async def lizard(ctx):
    em = discord.Embed(title = "Lizard", description="Displays a randomized lizard image", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.lizard`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help lizard command has executed")

# Help playlist
@help.command()
async def spotify(ctx):
    em = discord.Embed(title = "Playlists", description="Displays the links for the offical Relaxed Downtown music!", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.playlist`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help playlist command has executed")

# Help music
# @help.command()
# async def play(ctx):
#     em = discord.Embed(title = "Play", description="Plays a specified YouTube video in the voice channel that you are connected to", color=discord.Colour.purple())

#     em.add_field(name="**Syntax**", value="`.play <url>`")
#     em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

#     await ctx.send(embed=em)
#     print("Help play command has executed")

# @help.command()
# async def pause(ctx):
#     em = discord.Embed(title = "Pause", description="Pauses any currently playing music", color=discord.Colour.purple())

#     em.add_field(name="**Syntax**", value="`.pause`")
#     em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

#     await ctx.send(embed=em)
#     print("Help pause command has executed")

# @help.command()
# async def resume(ctx):
#     em = discord.Embed(title = "Resume", description="Resumes any currently paused music", color=discord.Colour.purple())

#     em.add_field(name="**Syntax**", value="`.resume`")
#     em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

#     await ctx.send(embed=em)
#     print("Help resume command has executed")

# @help.command()
# async def leave(ctx):
#     em = discord.Embed(title = "Leave", description="Disconnects the bot from the current voice channel", color=discord.Colour.purple())

#     em.add_field(name="**Syntax**", value="`.leave`")
#     em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

#     await ctx.send(embed=em)
#     print("Help leave command has executed")

# @help.command()
# async def stop(ctx):
#     em = discord.Embed(title = "Stop", description="Stops the currently playing song and deletes it from the qeue", color=discord.Colour.purple())

#     em.add_field(name="**Syntax**", value="`.stop`")
#     em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

#     await ctx.send(embed=em)
#     print("Help stop command has executed")
    
@help.command()
async def cat(ctx):
        em = discord.Embed(title = "Cat", description="Displays a randomized cat image", color=discord.Colour.purple())

        em.add_field(name="**Syntax**", value="`.cat`")
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)
    
# Help unban command
@help.command()
async def unban(ctx):
    em = discord.Embed(title = "Unban", description="Unbans a member from the guild", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.unban <member>`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help unban command has executed")



with open('token.txt') as f:
    TOKEN = f.readline()

# Changing Status
client.loop.create_task(ch_pr())

# Make the client run
client.run(TOKEN)