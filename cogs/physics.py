import discord
from discord.ext import commands
import math
import random
from discord_slash import cog_ext

# ! <--- Class for Physics_Calculation
class Physics_Calculation(commands.Cog) :

    def __init__(self, client) :
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

    @ cog_ext.cog_slash(description = "Calculate the speed of an object using any distance and time unit")
    async def speed(self, ctx, distance : float, time : float, distance_unit : str, time_unit : str) :
        self.exp = f"{distance}/{time} {distance_unit}/{time_unit}"
        self.evalu = (distance/time)
        self.User = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

def setup(client) :
    client.add_cog(Physics_Calculation(client))


