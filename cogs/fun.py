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

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Print "Fun cog is loaded" to command line
    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cog is loaded')
    
    # Cog Ping
    @commands.command()
    async def fping(self, ctx):
        em = discord.Embed(title="Fun Cog Ping", description="Ping!", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

    # 8ball Command
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
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

    # Coinflip command
    @commands.command(aliases=['cf'])
    async def coinflip(self, ctx):
        responses = [
                        'Heads',
                        'Tails']

        em = discord.Embed(title = "Coinflip", description="", color=discord.Colour.purple())

        em.add_field(name="**Outcome**", value=f"{random.choice(responses)}", inline=False)
        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Fun(client))