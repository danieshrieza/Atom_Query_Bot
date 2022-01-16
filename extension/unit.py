from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from fraction import Fraction
from nextcord.ext.commands.context import Context

# ! <--- Class for Unit_Converter --->
class Unit_Converter(commands.Cog):

    # ! <---  Initialize variable for class --->
    def __init__(self, bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ! <--- Command to convert mm to cm --->
    @ nextcord.slash_command(description = "Convert milimeter to centimeter.")
    async def mm_cm(self, ctx : Context, milimeter : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{milimeter}` mm", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{milimeter/10}` cm", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to convert cm to m --->
    @ nextcord.slash_command(description = "Convert centimeter to meter.")
    async def cm_m(self, ctx : Context, centimeter : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{centimeter}` cm", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{centimeter/100}` m", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        
    # ! <--- Command to m to km --->
    @ nextcord.slash_command(description = "Convert meter to kilometer.")
    async def m_km(self, ctx : Context, meter : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{meter}` m", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{meter/1000}` km", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        
    # ! <--- Command to km to m --->
    @ nextcord.slash_command(description = "Convert kilometer to meter.")
    async def km_m(self, ctx : Context, kilometer : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :", value = f"`{kilometer}` km", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{kilometer * 1000}` m", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        
    # ! <--- Command to convert m to cm --->
    @ nextcord.slash_command(description = "Convert meter to centimeter.")
    async def m_cm(self, ctx : Context, meter : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{meter}` m", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{meter * 100}` cm", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        
    # ! <--- Command to convert cm to mm --->
    @ nextcord.slash_command(description = "Convert centimeter to milimeter.")
    async def cm_mm(self, ctx : Context, centimeter : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :", value = f"`{centimeter}` cm", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{centimeter * 10}` mm", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command convert g to kg --->
    @ nextcord.slash_command(description = "Convert gram to kilogram.")
    async def g_kg(self, ctx : Context, gram : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{gram}` g", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{gram / 1000}` kg", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to convert kg to g --->
    @ nextcord.slash_command(description = "Convert kilogram to gram.")
    async def kg_g(self, ctx : Context, kilogram : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{kilogram}` kg", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{kilogram * 1000}` g", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to convert ml to l --->
    @ nextcord.slash_command(description = "Convert mililitre to litre.")
    async def ml_l(self, ctx : Context, mililitre : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{mililitre}` ml", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{mililitre/1000}` l", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to convert l to ml --->
    @ nextcord.slash_command(description = "Convert litre to mililitre.")
    async def l_ml(self, ctx : Context, litre : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{litre}` l", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{litre * 1000}` ml", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to convert decimal to fraction --->
    @ nextcord.slash_command(description = "Convert a decimal number to fraction.")
    async def decimal_fraction(self, ctx : Context, decimal : float) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{decimal}`", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{Fraction(str(decimal)).limit_denominator()}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to convert fraction to decimal --->
    @ nextcord.slash_command(description = "Convert a fraction value to a decimal number.")
    async def fraction_decimal(self, ctx : Context, numerator : int, denominator : int) :

        embed_msg = nextcord.Embed(title = "Unit Converter", description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc),colour = nextcord.Color.from_rgb(178,34,34))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{numerator}/{denominator}`", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{numerator/denominator}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)
        
        await ctx.send(embed = embed_msg)

# ! <--- Add Unit_Converter into the bot --->
def setup(bot):
  bot.add_cog(Unit_Converter(bot))