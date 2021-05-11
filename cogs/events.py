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

class Event(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Print "Fun cog is loaded" to command line
    @commands.Cog.listener()
    async def on_ready(self):
        print('Events cog is loaded')
    
    # Cog Ping
    @commands.command()
    async def eping(self, ctx):
        em = discord.Embed(title="Event Cog Ping", description="Ping!", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            em = discord.Embed(title="Command Error", description="You do not have the required permissions to do that (`MissingPremissions`)", color=discord.Colour.purple())

            em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

            await ctx.send(embed=em)
        elif isinstance(error, commands.MissingRequiredArgument):
            em = discord.Embed(title="Command Error", description="You are missing a required argument (`MissingRequiredArgument`)", color=discord.Colour.purple())

            em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

            await ctx.send(embed=em)

    # (RD Only) VIP role 🌟
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        role = after.guild.get_role(795321686517874698)
        print(role, before.roles, after.roles, before.display_name, after.display_name)
        if role in after.roles and role not in before.roles:
            await after.edit(nick=f"🌟 {after.display_name}")
            await after.send("```Hey! You! Yeah You! 😎\n\nLets go you just reached the VIP Status on Relaxed Downtown! 💜 \nAnd Yes we have some Premium features on Relaxed Downtown for VIP users: \n \n-Hidden VIP Chats ⭐ (You can find the VIP category under the Minigames category) \n \n-You can now request a nickname! (The text channel for that can be found in the Support category) 🦋\n \n-Question Of The Day :question: (Can be found in the Off-Topic Category) \n \n-Color Roles (can be found in the category User info) ```")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        mention=member.mention
        guild=member.guild

        em = discord.Embed(title=":warning:WARNING READ BEFORE JOINING THE SERVER!:warning:", description="Always be careful what data about yourself you disclose! There are bad people everywhere who pretend to be users of your age to harm you! Never give your exact location! And if you don't feel comfortable introducing yourself in our introduction channel then you don't have to do it! \n **The Downtown Team Is NOT Liable!**", color=discord.Colour.purple())

        em.set_thumbnail(url="http://relaxed-downtown.ml/img/ezgif-4-08d6e14f8d30.gif")

        await member.send(embed=em)

def setup(client):
    client.add_cog(Event(client))