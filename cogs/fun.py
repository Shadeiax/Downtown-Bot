import discord
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Fun cog is ready')

    @commands.command()
    async def _8ball(ctx, *, question, self):
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


def setup(client):
    client.add_cog(Fun(client))