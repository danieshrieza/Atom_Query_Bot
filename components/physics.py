import discord
from discord.ext import commands
from discord_slash import cog_ext

# ! <--- Class for Physics_Calculation
class Physics_Calculation(commands.Cog) :

    """
    Physics_Calculation is a class that contains physics related math command.

    Commands :
    --------
    speed : return `str` embed  

    electric_current : return `str` embed

    electric_voltage : `str` embed

    electric_resistance : `str` embed

    moment_of_force : `str` embed

    pressure : `str` embed

    density : `str` embed
    """

    # ? <--- Initialize variable for class
    def __init__(self, client) :
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

    # ? <--- Command to calculate speed of an object
    @ cog_ext.cog_slash(description = "Calculate the speed of an object using any distance and time unit.")
    async def speed(self, ctx, distance : float, time : float) :
        self.exp = f"{distance} ÷ {time}"
        self.eval = distance/time
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} m/s`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to calculate electric current of an object
    @ cog_ext.cog_slash(description = "Calculate the electric current of an object.")
    async def electric_current(self, ctx, electric_voltage : float, electric_resistance : float ) :
        self.exp = f"{electric_voltage} V ÷ {electric_resistance} Ω"
        self.eval = electric_voltage/electric_resistance
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} A`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to calculate electric voltage of an object
    @ cog_ext.cog_slash(description = "Calculate the electric voltage of an object.")
    async def electric_voltage(self, ctx, electric_current : float, electric_resistance : float ) :
        self.exp = f"{electric_current} A × {electric_resistance} Ω"
        self.eval = electric_current * electric_resistance
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} V`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to calculate electric resisteance of an object
    @ cog_ext.cog_slash(description = "Calculate the electric resistance of an object.")
    async def electric_resistance(self, ctx, electric_voltage : float, electric_current : float ) :
        self.exp = f"{electric_voltage} V ÷ {electric_current} A"
        self.eval = electric_voltage/electric_current
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :" , value = f"`{self.eval} Ω`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to calculate moment of force of an object
    @ cog_ext.cog_slash(description = "Calculate the moment of force of an object.")
    async def moment_of_force(self, ctx, force : float, perpendicular_distance : float) :
        self.exp = f"{force} N × {perpendicular_distance} m "
        self.eval = force * perpendicular_distance
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.eval} N m`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

    # ? <--- Command to calculate the pressure acts on an object
    @ cog_ext.cog_slash(description = "Calculate the pressure acts on an object.")
    async def pressure(self, ctx, force : float, surface_area : float) :
        self.exp = f"{force} N ÷ {surface_area} m²"
        self.eval = force/surface_area
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.eval} N/m²`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)
    
    # ? <--- Command to calculate the density of an object
    @ cog_ext.cog_slash(description = "Calculate the density of an object.")
    async def density(self, ctx, mass : float, volume : float) :
        self.exp = f'{mass} g ÷ {volume} cm³'
        self.eval = mass/volume
        self.user = ctx.author
        self.embed = discord.Embed(title = "Physics Query", colour = discord.Color.from_rgb(64,224,208))
        self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = f"Output :", value = f"`{self.eval} g/cm³`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

# ! <--- Add Physics_Calculation into the bot
def setup(client) :
    client.add_cog(Physics_Calculation(client))


