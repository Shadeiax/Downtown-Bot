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

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Print "Admin cog is loaded" to command line
    @commands.Cog.listener()
    async def on_ready(self):
        print('Admin cog is loaded')
    
    # Cog Ping
    @commands.command()
    async def aping(self, ctx):
        em = discord.Embed(title="Admin Cog Ping", description="Ping!", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em) 

    # Kick command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)

        em = discord.Embed(title="Member Kicked", description=f"{member} was kicked for {reason}", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

    # Ban command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)

        em = discord.Embed(title="Member Banned", description=f"{member} was banned for {reason}", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Admin(client))
