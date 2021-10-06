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

    @ commands.is_owner()
    @ cog_ext.cog_slash(description = "Calculate the speed of an object using any distance and time unit.")
    async def speed(self, ctx, distance : float, time : float, distance_unit : str, time_unit : str) :
        self.exp = f"{distance} ÷ {time} {distance_unit}/{time_unit}"
        self.eval = (distance/time)
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} {distance_unit}/{time_unit}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    @ commands.is_owner()
    @ cog_ext.cog_slash(description = "Calculate the electric current of an object.")
    async def electric_current(self, ctx, electric_voltage : float, electric_resistance : float ) :
        self.exp = f"{electric_voltage} V ÷ {electric_resistance} Ω"
        self.eval = f'{electric_voltage/electric_resistance}'
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} A`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    @ commands.is_owner()
    @ cog_ext.cog_slash(description = "Calculate the electric voltage of an object.")
    async def electric_voltage(self, ctx, electric_current : float, electric_resistance : float ) :
        self.exp = (f"{electric_current} A × {electric_resistance} Ω")
        self.eval = f'{electric_current * electric_resistance}'
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} V`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    @ commands.is_owner()
    @ cog_ext.cog_slash(description = "Calculate the electric resistance of an object.")
    async def electric_resistance(self, ctx, electric_voltage : float, electric_current : float ) :
        self.exp = (f"{electric_voltage} V ÷ {electric_current} A")
        self.eval = f'{electric_voltage/electric_current}'
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} A`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    @ commands.is_owner()
    @ cog_ext.cog_slash(description = "Calculate the electric resistance of an object.")
    async def electric_resistance(self, ctx, electric_voltage : float, electric_current : float ) :
        self.exp = (f"{electric_voltage} V ÷ {electric_current} A")
        self.eval = f'{electric_voltage/electric_current}'
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} Ω`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    @ commands.is_owner()
    @ cog_ext.cog_slash(description = "Calculate the electric resistance of an object.")
    async def moment_of_force(self, ctx, force : float, perpendicular_distance : float ) :
        self.exp = f"{force} N × {perpendicular_distance} m "
        self.eval = f'{force * perpendicular_distance}'
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} N m`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

def setup(client) :
    client.add_cog(Physics_Calculation(client))


