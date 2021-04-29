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
    em = discord.Embed(title="Ping", description=f"The bot's ping is currently `{round(client.latency * 1000)}ms`", color=discord.Colour.purple())
    
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")
    
    await ctx.send(embed=em)
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
    
    em = discord.Embed(title="Member Kicked", description=f"{member} was kick for {reason}", color=discord.Colour.purple())
    
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")
    
    await ctx.send(embed=em)
    
    print('Kick command has executed')

# Ban command
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    
    em = discord.Embed(title="Member Banned", description=f"{member} was kick for {reason}", color=discord.Colour.purple())
    
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")
    
    await ctx.send(embed=em)
    print('Ban command has executed')

# Help command
@client.group(invoke_without_command=True)
async def help(ctx):
    
    em = discord.Embed(title="Help", description="Use .help <command> for extended information on a command", color=discord.Colour.purple())
    
    em.add_field(name="Moderation", value="kick, ban")
    em.add_field(name="Fun", value="8ball" )
    em.add_field(name="Misc", value="invite, ping, about, workinprogress" )
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

# About command

@client.command()
async def about(ctx):
    em = discord.Embed(title = "About", description="", color=discord.Colour.purple())

    em.add_field(name="**Library**", value="discord.py")
    em.add_field(name="**Creators**", value="carter.py#0001, (っ◔◡◔)っʏᴜɴɢʙᴇᴀᴛᴢ#3040")    

    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("About command has executed")

# Workinprogress
@client.command(aliases=['wip'])
async def workinprogress(ctx):
    em = discord.Embed(title = "Work In Progress", description="", color=discord.Colour.purple())

    em.add_field(name="**Error Handling**", value="Add an error handling system that displays why a command is not working", inline=False)
    em.add_field(name="**Website Dashboard**", value="Create a website dashboard to custmize the bot's expirence", inline=False)
    em.add_field(name="**Fun Commands**", value="**DONE:** Add fun commands like .8ball and others", inline=False)    

    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Workinprogress command has executed")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = [
                    'As I see it, yes.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    'Don’t count on it.',
                    'It is certain.',
                    'It is decidedly so.',
                    'Most likely.',
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Outlook good.',
                    'Reply hazy, try again.',
                    'Signs point to yes.',
                    'Very doubtful.',
                    'Without a doubt.',
                    'Yes.',
                    'Yes – definitely.',
                    'You may rely on it.']
    em = discord.Embed(title = "8ball", description="", color=discord.Colour.purple())

    em.add_field(name="**Question**", value=f"{question}", inline=False)
    em.add_field(name="**Answer**", value=f"{random.choice(responses)}", inline=False)
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print('8ball command executed')



# # (RD Only) VIP role 🌟
# @client.event
# async def on_member_update(before, after, guild):
#     role = after.guild.get_role(834942375377764352)
#     print(role, before.roles, after.roles)
#     if role in after.roles and role not in before.roles:
#         await after.edit(nick=f"🌟 {after.nick}")

client.loop.create_task(ch_pr())
client.run('ODM0ODQ2NTM2OTEwODk3MTkz.YIG1bQ.nSR-AlX696BmJT6CNGqS2Ih2Ba4')
