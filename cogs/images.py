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

class Image(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # Print "Image cog is loaded" to command line
    @commands.Cog.listener()
    async def on_ready(self):
        print('Image cog is loaded')

    # Cog Ping
    @commands.command()
    async def iping(self, ctx):
        em = discord.Embed(title="Image Cog Ping", description="Ping!", color=discord.Colour.purple())

        em.set_thumbnail(url="https://cdn.discordapp.com/avatars/834846536910897193/e8dd4276ccb10157dcf76f8222c9354c.png?size=256")

        await ctx.send(embed=em)

    @commands.command()
    async def lizard(self, ctx):
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
    
    @commands.command(aliases=['doge'])
    async def dog(self, ctx):
        responses = [
                        'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=1.00xw:0.669xh;0,0.190xh&resize=1200:*',
                        'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/dog_cool_summer_slideshow/1800x1200_dog_cool_summer_other.jpg',
                        'https://i.guim.co.uk/img/media/fe1e34da640c5c56ed16f76ce6f994fa9343d09d/0_174_3408_2046/master/3408.jpg?width=1200&height=900&quality=85&auto=format&fit=crop&s=0d3f33fb6aa6e0154b7713a00454c83d',
                        'https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg?crop=0.672xw:1.00xh;0.166xw,0&resize=640:*',
                        'https://www.sciencemag.org/sites/default/files/styles/inline__450w__no_aspect/public/dogs_1280p_0.jpg?itok=h6VBayx-',
                        'https://i.insider.com/5484d9d1eab8ea3017b17e29?width=600&format=jpeg&auto=webp',
                        'https://cdn.discordapp.com/attachments/763833701468733443/842194860382879795/lp_image.JPG',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842195654062637086/image0.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842195654398312459/image1.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842195654641319956/image2.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842195654964805672/image3.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842196378376470548/image1.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842197015252303872/image0.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842197015533584454/image1.jpg'
                                                ]

        em = discord.Embed(title = "Dog", description="", color=discord.Colour.purple())

        em.set_image(url=f"{random.choice(responses)}")

        await ctx.send(embed=em)

    @commands.command()
    async def cat(self, ctx):
        responses = [
                        'https://icatcare.org/app/uploads/2018/06/Layer-1704-1200x630.jpg',
                        'https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png',
                        'https://cdn.mos.cms.futurecdn.net/VSy6kJDNq2pSXsCzb6cvYF.jpg',
                        'https://c.files.bbci.co.uk/12A9B/production/_111434467_gettyimages-1143489763.jpg',
                        'https://static.scientificamerican.com/sciam/cache/file/92E141F8-36E4-4331-BB2EE42AC8674DD3_source.jpg',
                        'https://img.webmd.com/dtmcms/live/webmd/consumer_assets/site_images/article_thumbnails/other/cat_relaxing_on_patio_other/1800x1200_cat_relaxing_on_patio_other.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/841789289594617916/image0.jpg',
                        'https://cdn.discordapp.com/attachments/792593317547343922/841789387754176552/image0.jpg',
                        'https://cdn.discordapp.com/attachments/763833701468733443/842194859313463336/IMG_2556.JPG',
                        'https://cdn.discordapp.com/attachments/763833701468733443/842194862560378910/IMG_1109.JPG',
                        'https://cdn.discordapp.com/attachments/792593317547343922/842196378033061928/image0.jpg'
                                                ]

        em = discord.Embed(title = "Cat", description="", color=discord.Colour.purple())

        em.set_image(url=f"{random.choice(responses)}")

        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Image(client))
