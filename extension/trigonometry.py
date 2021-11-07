from datetime import datetime, timezone
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
    def __init__(self, bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ? <--- Command to find sine of a triangle
    @ cog_ext.cog_slash(description = "Calculate the sine of a triangle.")
    async def sin(self,ctx, number : float):
        emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
        exp = f"sin {number}°"
        eval = math.sin(number)
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to find cosine of a triangle
    @ cog_ext.cog_slash(description = "Calculate the cosine of a triangle.")
    async def cos(self,ctx, number : float):
        emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
        exp = f"cos {number}°"
        eval = math.cos(number)
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to find tangent of a triangle
    @ cog_ext.cog_slash(description = "Calculate the tangent of a triangle.")
    async def tan(self,ctx, number : float):
        emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
        exp = f"tan {number}°"
        eval = math.tan(number)
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to find the hypotenuse, height or the base of a triangle using Pythagoras Theorem
    @ cog_ext.cog_slash(description = "Calculate the Pythagoras Theorem.")
    async def pythagoras_theorem(self,ctx, height : float = None, base : float = None, hypotenuse : float = None):
        if (hypotenuse == None and height != None and base != None) :
            emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
            exp = f"√{base}² + {height}²"
            eval = math.sqrt((base ** 2) + (height ** 2))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (height == None and hypotenuse != None and base != None) :
            if hypotenuse > base :
                emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
                exp = f"√{hypotenuse}² - {base}²"
                eval = math.sqrt((hypotenuse ** 2) - (base ** 2))
                emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
                emby_ctx.set_thumbnail(url = self.link)
                await ctx.send(embed = emby_ctx)
            else :
                emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
                exp = f"√{base}² - {hypotenuse}²"
                eval = math.sqrt((base ** 2) - (hypotenuse ** 2))
                emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
                emby_ctx.set_thumbnail(url = self.link)
                await ctx.send(embed = emby_ctx)
        elif (base == None and hypotenuse != None and height != None) :
            if hypotenuse > height :
                emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
                exp = f"√{hypotenuse}² - {height}²"
                eval = math.sqrt((hypotenuse ** 2) - (height ** 2))
                emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
                emby_ctx.set_thumbnail(url = self.link)
                await ctx.send(embed = emby_ctx)
            else :
                emby_ctx = discord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(139,0,0))
                exp = f"√{height}² - {hypotenuse}²"
                eval = math.sqrt((height ** 2) - (hypotenuse ** 2))
                emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
                emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
                emby_ctx.set_thumbnail(url = self.link)
                await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

# ! <--- Add Triginometry_Calculation into the bot
def setup(bot):
  bot.add_cog(Trigonometry_Calculation(bot))