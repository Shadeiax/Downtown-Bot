import discord
from discord.ext import commands
import random

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

# Kick command
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

# Ban command
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
# Embed code (copy and paste if needed)
@client.command()
async def displayembed(ctx):
    embed = discord.Embed(
        title = 'Title',
        description = 'This is a description', 
        colour = discord.Colour.blue()

    )

    embed.set_footer(text='This is a footer')
    embed.set_image(url='https://cdn.discordapp.com/avatars/721341252649353256/a1c0f7f4b214c93425d7599da9e5f32d.png?size=256')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/721341252649353256/a1c0f7f4b214c93425d7599da9e5f32d.png?size=256')
    embed.set_author(name='LAX#0001', icon_url='https://cdn.discordapp.com/avatars/721341252649353256/a1c0f7f4b214c93425d7599da9e5f32d.png?size=256')
    embed.add_field(name='Feild Name', value='Field Value', inline=False)
    embed.add_field(name='Feild Name', value='Field Value', inline=True)
    embed.add_field(name='Feild Name', value='Field Value', inline=True)
    
    await ctx.send(embed=embed)

@client.command()
async def docs(ctx):
    docs = discord.Embed(
        title = 'Help',
        descrition = 'Ultimate Bot is the most feature-rich homemeade bot on Discord!', 
        color = discord.Colour.blue()

    )
    await ctx.send(embed=docs)





# Unban command
# @client.command()
# async def unban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     memver_name, member_discriminator = member.split('#')
    
#     for ban_entry in banned_users:
#         use = ban_entry.banned_users

#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#                 await ctx.guild.unban(user)
#                 await ctx.send(f'Unbanned {user.name}#{user.discriminator}')

client.run('ODM0NDk4Mzk0ODQ0MTY4MjAz.YIBxMQ.8kdP181iHFlGOLLWIpXNBkCk_Tg')
