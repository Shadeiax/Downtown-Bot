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

intents = discord.Intents.default()
intents.members = True

# Bot prefix
client = commands.Bot(command_prefix = ".", intents=intents)

# Remove help
client.remove_command("help")

# Print 'Bot is ready.' in command line
@client.event
async def on_ready():
    print('The bot is ready')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=".help"))

# (RD Only) VIP role 🌟
@client.event
async def on_member_update(before, after):
    role = after.guild.get_role(795321686517874698)
    print(role, before.roles, after.roles, before.display_name, after.display_name)
    if role in after.roles and role not in before.roles:
        await after.edit(nick=f"🌟 {after.display_name}")

# (RD Only) VIP auto DM 🌟
@client.event
async def on_member_update(before, after):
    role = after.guild.get_role(795321686517874698)
    print(role, before.roles, after.roles, before.display_name, after.display_name)
    if role in after.roles and role not in before.roles:
        await after.send("```Hey! You! Yeah You! 😎\n\nLets go you just reached the VIP Status on Relaxed Downtown! 💜 \nAnd Yes we have some Premium features on Relaxed Downtown for VIP users: \n \n-Hidden VIP Chats ⭐ (You can find the VIP category under the Minigames category) \n \n-You can now request a nickname! (The text channel for that can be found in the Support category) 🦋\n \n-Question Of The Day :question: (Can be found in the Off-Topic Category) \n \n-Color Roles (can be found in the category User info) ```")

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
    em = discord.Embed(title="Invite Link", description="The invite link for the Downtown Bot can be accessed at https://www.relaxed-downtown.ml", color=discord.Colour.purple())

    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print('Invite/link command has executed')

# Kick command
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

    em = discord.Embed(title="Member Kicked", description=f"{member} was kicked for {reason}", color=discord.Colour.purple())

    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)

    print('Kick command has executed')

# Ban command
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

    em = discord.Embed(title="Member Banned", description=f"{member} was banned for {reason}", color=discord.Colour.purple())

    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print('Ban command has executed')

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

# 8ball Command
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

# Coinflip command
@client.command(aliases=['cf'])
async def coinflip(ctx, *, question):
    responses = [
                    'Heads',
                    'Tails']

    em = discord.Embed(title = "Coinflip", description="", color=discord.Colour.purple())

    em.add_field(name="**Prediction**", value=f"{question}", inline=False)
    em.add_field(name="**Outcome**", value=f"{random.choice(responses)}", inline=False)
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print('Coinflip command executed')

# Dog command
@client.command(aliases=['doge'])
async def dog(ctx):
    responses = [
                    'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*',
                    'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/dog_cool_summer_slideshow/1800x1200_dog_cool_summer_other.jpg',
                    'https://i.guim.co.uk/img/media/fe1e34da640c5c56ed16f76ce6f994fa9343d09d/0_174_3408_2046/master/3408.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=0d3f33fb6aa6e0154b7713a00454c83d',
                    'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=0.672xw:1.00xh;0.166xw,0&resize=640:*',
                    'https://www.sciencemag.org/sites/default/files/styles/inline__450w__no_aspect/public/dogs_1280p_0.jpg?itok=h6VBayx-',
                    'https://i.insider.com/5484d9d1eab8ea3017b17e29?width=600&format=jpeg&auto=webp'
                                            ]

    em = discord.Embed(title = "Dog", description="", color=discord.Colour.purple())

    em.set_image(url=f"{random.choice(responses)}")

    await ctx.send(embed=em)
    print('Dog/doge command executed')

# Amphibian command
@client.command()
async def lizard(ctx):
    responses = [
                    'https://cdn.discordapp.com/attachments/837804364990513183/838099013454397520/image0.jpg',
                    'https://media.discordapp.net/attachments/837804364990513183/838099133189193728/image0.jpg?width=503&height=670',
                    'https://animals.sandiegozoo.org/sites/default/files/2016-11/animals_hero_lizards.jpg',
                    'https://images.unsplash.com/photo-1504450874802-0ba2bcd9b5ae?ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8bGl6YXJkfGVufDB8fDB8fA%3D%3D&ixlib=rb-1.2.1&w=1000&q=80',
                    'https://cdn.britannica.com/37/125637-050-775F1B98/Agama.jpg',
                    'https://static.scientificamerican.com/sciam/cache/file/35BB522C-1F80-4EA3-AD1A257F9B636908_source.jpg?w=590&h=800&47D6048D-D602-419B-B2B0A97B77D665FE'
                                            ]

    em = discord.Embed(title = "Lizard", description="", color=discord.Colour.purple())

    em.set_image(url=f"{random.choice(responses)}")

    await ctx.send(embed=em)
    print('Lizard command executed')

# Amphibian command
@client.command()
async def cat(ctx):
    responses = [
                    'https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png',
                    'https://c.files.bbci.co.uk/12A9B/production/_111434467_gettyimages-1143489763.jpg',
                    'https://static.scientificamerican.com/sciam/cache/file/92E141F8-36E4-4331-BB2EE42AC8674DD3_source.jpg',
                    'https://icatcare.org/app/uploads/2018/06/Layer-1704-1920x840.jpg',
                    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMkEG43ZrAEgJtx9uicyjBXIZNeAogYlNYYC9JCPMCC2yYj6_FptQC1uPYIVHaglnWy2E&usqp=CAU',
                    'https://www.humanesociety.org/sites/default/files/styles/1240x698/public/2020-07/kitten-510651.jpg?h=f54c7448&itok=ZhplzyJ9'
                                            ]

    em = discord.Embed(title = "Cat", description="", color=discord.Colour.purple())

    em.set_image(url=f"{random.choice(responses)}")

    await ctx.send(embed=em)
    print('Cat command executed')

# Playlist command
@client.command()
async def playlist(ctx):
    em = discord.Embed(title="Playlist", description="", color=discord.Colour.purple())

    em.add_field(name='Spotify', value='Listen to the offical Relaxed Downtown playlist on Spotify at: https://open.spotify.com/playlist/3VGaCebHKvTCnLNdcnglbB?si=b610100948354a72', inline=False)
    em.add_field(name='Apple Music ', value='Listen to the offical Relaxed Downtown playlist on Apple Music at: https://music.apple.com/ch/playlist/favourite-songs-of-relaxed-downtown/pl.u-PDb44aEILVBdexv', inline=False)
    await ctx.send(embed=em)
    print('Playlist command executed')

# Music stuff

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}   

def endSong(guild, path):
    os.remove(path)                                   

@client.command(pass_context=True)
async def play(ctx, url):
    await ctx.send('Due to the file size of some YouTube videos, music can take up to 2 minutes to start playing')
    if not ctx.message.author.voice:
        await ctx.send('You are not connected to a voice channel') #message when you are not connected to any voice channel
        return

    else:
        channel = ctx.message.author.voice.channel

    voice_client = await channel.connect()

    guild = ctx.message.guild

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        file = ydl.extract_info(url, download=True)
        path = str(file['title']) + "-" + str(file['id'] + ".mp3")

    voice_client.play(discord.FFmpegPCMAudio(path), after=lambda x: endSong(guild, path))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

    await ctx.send(f'**Music: **{url}') #sends info about song playing right now

@client.command(pass_context=True)
async def lofi(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Lofi.webm')
        player = voice.play(source)
        await ctx.send(f"The bot is now playing lofi in {channel}")
    else:
        await ctx.send("You are not in a voice channel.  Join one to run the command!")

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()




# Help command
@client.group(invoke_without_command=True)
async def help(ctx):

    em = discord.Embed(title="Help", description="Use .help <command> for extended information on a command", color=discord.Colour.purple())

    em.add_field(name="Moderation", value="kick, ban")
    em.add_field(name="Fun", value="8ball, coinflip" )
    em.add_field(name="Images", value="dog, lizard" )
    em.add_field(name="Misc", value="invite, ping, about, workinprogress, playlist" )
    em.add_field(name="Music", value="play, lofi, pause, resume, stop" )
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
@help.command()
async def play(ctx):
    em = discord.Embed(title = "Play", description="Plays a specified YouTube video in the voice channel that you are connected to", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.play <url>`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help play command has executed")

@help.command()
async def lofi(ctx):
    em = discord.Embed(title = "Lofi", description="Plays a 2 hour long lofi flaylist in the voice channel that you are connected to", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.lofi`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help lofi command has executed")

@help.command()
async def pause(ctx):
    em = discord.Embed(title = "Pause", description="Pauses any currently playing music", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.pause`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help pause command has executed")

@help.command()
async def resume(ctx):
    em = discord.Embed(title = "Resume", description="Resumes any currently paused music", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.resume`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help resume command has executed")

@help.command()
async def leave(ctx):
    em = discord.Embed(title = "Leave", description="Disconnects the bot from the current voice channel", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.leave`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help leave command has executed")

@help.command()
async def stop(ctx):
    em = discord.Embed(title = "Stop", description="Stops the currently playing song and deletes it from the qeue", color=discord.Colour.purple())

    em.add_field(name="**Syntax**", value="`.stop`")
    em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

    await ctx.send(embed=em)
    print("Help stop command has executed")


# Suicide prevention
# @client.event
# async def on_message(message, ctx):
#     bad_words = ["suicide", "Suicide", "i want to kill myself", "i want to die", "I want to die", "I want to kill myself"]
#
#     for word in bad_words:
#         if message.content.count(word) > 0:
#             em = discord.Embed(title="Helplines", description="This bot has automatically detected a keyword related to suicide Please listen to me. Your life is important. I understand you don't feel like you matter right know, but I can tell you with 100% confidence that you MATTER! Please just give the suicide prevention hotline just one more chance.", color=discord.Colour.purple())
#
#             em.add_field(name="**U.S.**", value="Call (800) 273-8255 or Text HOME to 741741", inline=False)
#             em.add_field(name="**U.K.**", value="Call 116-123 or Text SHOUT to 85258", inline=False)
#             em.add_field(name="**Canada**", value="Call (833) 456-4566 Text a message to 45645", inline=False)
#             em.add_field(name="**Switzerland**", value="Call 143", inline=False)
#             em.add_field(name="**Germany**", value="Call 08001810771", inline=False)
#             em.add_field(name="**Didnt find your Country above?**", value="Didnt find your Country above? DM carter.py#0001 for suggestions", inline=False)
#             em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")
#
#             await message.channel.send(embed=em)
#
#     else:
#         return

with open('token.txt') as f:
    TOKEN = f.readline()
# Make the client run
client.run(TOKEN)
