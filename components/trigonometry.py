import discord
from discord.ext import commands
import math
from discord_slash import cog_ext

# ! <--- Class for Trigonometry_Calculation
class Trigonometry_Calculation(commands.Cog):

    """
    Trigonometry_Calculation is a class that conatins trigonometry related commands.

    Commands : 
    ----------
    sin : return `str` embed

    cos : return `str` embed

    tan : return `str` embed

    pythagoras_theorem : return `str` embed
    """

    # ? <--- Initialize variable for class
    def __init__(self, client):
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

    # ? <--- Command to find sine of a triangle
    @ cog_ext.cog_slash(description = "Calculate the sine of a triangle.")
    async def sin(self,ctx, number : float):
        self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
        self.exp = f"sin {number}°"
        self.eval = math.sin(number)
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to find cosine of a triangle
    @ cog_ext.cog_slash(description = "Calculate the cosine of a triangle.")
    async def cos(self,ctx, number : float):
        self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
        self.exp = f"cos {number}°"
        self.eval = math.cos(number)
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to find tangent of a triangle
    @ cog_ext.cog_slash(description = "Calculate the tangent of a triangle.")
    async def tan(self,ctx, number : float):
        self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
        self.exp = f"tan {number}°"
        self.eval = math.tan(number)
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to find the hypotenuse, height or the base of a triangle using Pythagoras Theorem
    @ cog_ext.cog_slash(description = "Calculate the Pythagoras Theorem.")
    async def pythagoras_theorem(self,ctx, height : float = None, base : float = None, hypotenuse : float = None):
        if (hypotenuse == None and height != None and base != None) :
            self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
            self.exp = f"√{base}² + {height}²"
            self.eval = math.sqrt((base ** 2) + (height ** 2))
            self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
            self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
            self.embed.set_thumbnail(url = self.link)
            await ctx.send(embed = self.embed)
        elif (height == None and hypotenuse != None and base != None) :
            if hypotenuse > base :
                self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
                self.exp = f"√{hypotenuse}² - {base}²"
                self.eval = math.sqrt((hypotenuse ** 2) - (base ** 2))
                self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
                self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
                self.embed.set_thumbnail(url = self.link)
                await ctx.send(embed = self.embed)
            else :
                self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
                self.exp = f"√{base}² - {hypotenuse}²"
                self.eval = math.sqrt((base ** 2) - (hypotenuse ** 2))
                self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
                self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
                self.embed.set_thumbnail(url = self.link)
                await ctx.send(embed = self.embed)
        elif (base == None and hypotenuse != None and height != None) :
            if hypotenuse > height :
                self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
                self.exp = f"√{hypotenuse}² - {height}²"
                self.eval = math.sqrt((hypotenuse ** 2) - (height ** 2))
                self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
                self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
                self.embed.set_thumbnail(url = self.link)
                await ctx.send(embed = self.embed)
            else :
                self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
                self.exp = f"√{height}² - {hypotenuse}²"
                self.eval = math.sqrt((height ** 2) - (hypotenuse ** 2))
                self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
                self.embed.add_field(name = "Output :", value = f"`{self.eval}`", inline = True)
                self.embed.set_thumbnail(url = self.link)
                await ctx.send(embed = self.embed)
        else :
            await ctx.send("Please provide input for only one optional argument.")

# ! <--- Add Triginometry_Calculation into the bot
def setup(client):
  client.add_cog(Trigonometry_Calculation(client))