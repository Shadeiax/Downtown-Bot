# Import librarys
import discord
from discord.ext import commands

# Bot prefix
client = commands.Bot(command_prefix = ".")

# Remove help
client.remove_command("help")

# Print 'Bot is ready.' in command line
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="downtownbot.ml | .help"))
    print('The bot is ready.')

# Ping/ms command
@client.command(aliases=['ms'])
async def ping(ctx):
    await ctx.send(f'The bot has {round(client.latency * 1000)}ms ping.')
    print('Ping/ms command has executed')

# Invite link command
@client.command(aliases=['link'])
async def invite(ctx):
    await ctx.send('Go to https://www.downtownbot.ml to invite the bot to your server and join the support server!')
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
    
    em = discord.Embed(title = "Help", description="Use .help <command> for extended information on a command", color=discord.Colour.purple())
    
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







# (RD Only) VIP role 🌟
@client.event
async def on_member_update(before, after, guild):
    role = after.guild.get_role(834942375377764352)
    print(role, before.roles, after.roles)
    if role in after.roles and role not in before.roles:
        await after.edit(nick=f"🌟 {after.nick}")

client.run('ODM0ODQ2NTM2OTEwODk3MTkz.YIG1bQ.r0qRBcEbPGh4MRSGlJZO1PfgnTU')
