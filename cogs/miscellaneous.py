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

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Print "Admin cog is loaded" to command line
    @commands.Cog.listener()
    async def on_ready(self):
        print('Misc cog is loaded')
    
    # Cog Ping
    @commands.command()
    async def mping(self, ctx):
        em = discord.Embed(title="Misc Cog Ping", description="Ping!", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em) 

    # Workinprogress
    @commands.command(aliases=['wip'])
    async def workinprogress(self, ctx):
        em = discord.Embed(title = "Work In Progress", description="", color=discord.Colour.purple())

        em.add_field(name="**Error Handling**", value="Add an error handling system that displays why a command is not working", inline=False)
        em.add_field(name="**Website Dashboard**", value="Create a website dashboard to custmize the bot's expirence", inline=False)
        em.add_field(name="**Fun Commands**", value="**DONE:** Add fun commands like .8ball and others", inline=False)

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

    # About command
    @commands.command()
    async def about(self, ctx):
        em = discord.Embed(title = "About", description="", color=discord.Colour.purple())

        em.add_field(name="**Library**", value="discord.py")
        em.add_field(name="**Creators**", value="carter.py#0001, (っ◔◡◔)っʏᴜɴɢʙᴇᴀᴛᴢ#3040")

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)
    
    # Invite link command
    @commands.command(aliases=['link'])
    async def invite(self, ctx):
        em = discord.Embed(title="Invite Link", description="The invite link for the Downtown Bot can be accessed at https://www.relaxed-downtown.ml", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

    # Playlist command
    @commands.command()
    async def playlist(self, ctx):
        em = discord.Embed(title="Playlist", description="", color=discord.Colour.purple())

        em.add_field(name='Spotify', value='Listen to the offical Relaxed Downtown playlist on Spotify at: https://open.spotify.com/playlist/3VGaCebHKvTCnLNdcnglbB?si=b610100948354a72', inline=False)
        em.add_field(name='Apple Music ', value='Listen to the offical Relaxed Downtown playlist on Apple Music at: https://music.apple.com/ch/playlist/favourite-songs-of-relaxed-downtown/pl.u-PDb44aEILVBdexv', inline=False)
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Misc(client))
