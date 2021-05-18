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

   @commands.Cog.listener()
    async def on_message(self, ctx, message):
        bad_words = ["suicide", "Suicide", "i want to kill myself", "i want to die", "I want to die", "I want to kill myself"]

        for word in bad_words:
            if message.content.count(word) > 0:
                em = discord.Embed(title="Helplines", description="This bot has automatically detected a keyword related to suicide Please listen to me. Your life is important. I understand you don't feel like you matter right know, but I can tell you with 100% confidence that you MATTER! Please just give the suicide prevention hotline just one more chance.", color=discord.Colour.purple())

                em.add_field(name="**U.S.**", value="Call (800) 273-8255 or Text HOME to 741741", inline=False)
                em.add_field(name="**U.K.**", value="Call 116-123 or Text SHOUT to 85258", inline=False)
                em.add_field(name="**Canada**", value="Call (833) 456-4566 Text a message to 45645", inline=False)
                em.add_field(name="**Switzerland**", value="Call 143", inline=False)
                em.add_field(name="**Germany**", value="Call 08001810771", inline=False)
                em.add_field(name="**Didnt find your Country above?**", value="Didnt find your Country above? DM carter.py#0001 for suggestions", inline=False)
                em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

                await message.channel.send(embed=em)


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
