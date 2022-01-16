from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands.context import Context

# ! <--- Class for Physics_Calculation --->
class Physics_Calculation(commands.Cog) :

    # ! <--- Initialize variable for class --->
    def __init__(self, bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ! <--- Command to calculate speed of an object --->
    @ nextcord.slash_command(description = "Calculate the speed of an object using any distance and time unit.")
    async def speed(self, ctx : Context, distance : float, time : float) :

        exp = f"{distance} ÷ {time}"
        evalu = distance/time

        embed_msg = nextcord.Embed(title = "Physics Query", description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(127, 0, 255))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{evalu} m/s`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to calculate electric current of an object --->
    @ nextcord.slash_command(description = "Calculate the electric current of an object.")
    async def electric_current(self, ctx : Context, electric_voltage : float, electric_resistance : float ) :

        exp = f"{electric_voltage} V ÷ {electric_resistance} Ω"
        evalu = electric_voltage/electric_resistance

        embed_msg = nextcord.Embed(title = "Physics Query", description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(127, 0, 255))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{evalu} A`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to calculate electric voltage of an object --->
    @ nextcord.slash_command(description = "Calculate the electric voltage of an object.")
    async def electric_voltage(self, ctx : Context, electric_current : float, electric_resistance : float ) :

        exp = f"{electric_current} A × {electric_resistance} Ω"
        evalu = electric_current * electric_resistance

        embed_msg = nextcord.Embed(title = "Physics Query", description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(127, 0, 255))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{evalu} V`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to calculate electric resisteance of an object --->
    @ nextcord.slash_command(description = "Calculate the electric resistance of an object.")
    async def electric_resistance(self, ctx : Context, electric_voltage : float, electric_current : float ) :

        exp = f"{electric_voltage} V ÷ {electric_current} A"
        evalu = electric_voltage/electric_current

        embed_msg = nextcord.Embed(title = "Physics Query", description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(127, 0, 255))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{evalu} Ω`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to calculate moment of force of an object --->
    @ nextcord.slash_command(description = "Calculate the moment of force of an object.")
    async def moment_of_force(self, ctx : Context, force : float, perpendicular_distance : float) :

        exp = f"{force} N × {perpendicular_distance} m "
        evalu = force * perpendicular_distance

        embed_msg = nextcord.Embed(title = "Physics Query", description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(127, 0, 255))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu} N m`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

    # ! <--- Command to calculate the pressure acts on an object --->
    @ nextcord.slash_command(description = "Calculate the pressure acts on an object.")
    async def pressure(self, ctx : Context, force : float, surface_area : float) :

        exp = f"{force} N ÷ {surface_area} m²"
        evalu = force/surface_area

        embed_msg = nextcord.Embed(title = "Physics Query", description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(127, 0, 255))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu} N/m²`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
    
    # ! <--- Command to calculate the density of an object --->
    @ nextcord.slash_command(description = "Calculate the density of an object.")
    async def density(self, ctx : Context, mass : float, volume : float) :

        exp = f'{mass} g ÷ {volume} cm³'
        evalu = mass/volume

        embed_msg = nextcord.Embed(title = "Physics Query", description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(127, 0, 255))
        embed_msg.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = f"Output :", value = f"`{evalu} g/cm³`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)

# ! <--- Add Physics_Calculation into the bot
def setup(bot) :
    bot.add_cog(Physics_Calculation(bot))


