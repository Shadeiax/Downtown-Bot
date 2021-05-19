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
import datetime

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

        em.timestamp = datetime.datetime.utcnow()
        em.set_footer(text="Downtown Bot", icon_url="https://raw.githubusercontent.com/carter-py/Downtown-Bot/main/Downtown-Bot-Logo.png")

        await ctx.send(embed=em) 

    # Kick command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.kick(reason=reason)

        em = discord.Embed(title="Member Kicked", description=f"{member} was kicked for {reason}", color=discord.Colour.purple())

        em.timestamp = datetime.datetime.utcnow()
        em.set_footer(text="Downtown Bot", icon_url="https://raw.githubusercontent.com/carter-py/Downtown-Bot/main/Downtown-Bot-Logo.png")

        await ctx.send(embed=em)

    # Ban command
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: commands.MemberConverter, *, reason=None):
        await member.ban(reason=reason)

        em = discord.Embed(title="Member Banned", description=f"{member} was banned for {reason}", color=discord.Colour.purple())

        em.timestamp = datetime.datetime.utcnow()
        em.set_footer(text="Downtown Bot", icon_url="https://raw.githubusercontent.com/carter-py/Downtown-Bot/main/Downtown-Bot-Logo.png")

        await ctx.send(embed=em)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.channel.send(f"Unbanned: {user.mention}")

def setup(client):
    client.add_cog(Admin(client))
