from datetime import datetime, timezone
import discord
from discord.ext import commands
from discord_slash import cog_ext
from discord.ext.commands.context import Context

# ! <--- Class for Geometry_Calculation 
class Geometry_Calculation(commands.Cog) :

    """
    Geometry_Calculation is a class that contains geometry related commands.

    Commands :
    ----------

    circle_circumference : return `str` embed

    area_circle : return `str` embed

    area_quadrilateral : return `str` embed

    area_triangle : return `str` embed

    area_parallelogram : return `str` embed

    area_kite : return `str` embed

    area_trampezium : return `str` embed

    surface_area_quadrilateral : return `str` embed

    surface_area_triangle : return `str` embed

    surface_area_cylinder : return `str` embed

    surface_area_cone : return `str` embed

    volume_quadrilateral : return `str` embed

    volume_triangle : return `str` embed

    volume_parallelogram : return `str` embed

    volume_kite : return `str` embed

    volume_trampezium : return `str` embed

    """

    # ! <--- Initialize variable for class
    def __init__(self, bot) :
        
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ! <--- Command to calculate circumference of a circle using diameter or radius
    @ cog_ext.cog_slash(description = "Calculate the circumference of a circle using diameter or radius")
    async def circle_circumference(self,ctx : Context, radius : float = None, diameter : float = None) :

        if (radius == None and diameter != None) :

            exp = f"22/7 × {diameter}"
            evalu = 22/7 * diameter

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (diameter == None and radius != None) :

            exp = f"2 × 22/7 × {radius}"
            evalu = 2 * 22/7 * radius

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide input for only one optional argument.")

    # ! <--- Commmand to calculate area of a circle
    @ cog_ext.cog_slash(description = "Calculate the area of a circle.")
    async def area_circle(self, ctx : Context, radius : float = None, diameter : float = None) :

        if (diameter == None and radius != None) :

            exp = f"22/7 × {radius}²"
            evalu = 22/7 * radius ** 2

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (radius == None and diameter != None) :

            exp = f"22/7 × ({diameter}/2)²"
            evalu = 22/7 * (diameter/2) ** 2

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide input for only one optional argument.")

    # ! <--- Command to calculate area of a quadrilateral
    @ cog_ext.cog_slash(description = "Calculate the area of a rectangle, a square or a quadrilateral.")
    async def area_quadrilateral(self, ctx : Context, length : float, width : float) :

        exp = f"{length} × {width}"
        evalu = length * width

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate area of a triangle
    @ cog_ext.cog_slash(description = "Calculate the area of a triangle.")
    async def area_triangle(self, ctx : Context, base : float, height : float) :

        exp = f"1/2 × {base} × {height}"
        evalu = 1/2 * base * height

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate area of a parallelogram
    @ cog_ext.cog_slash(description = "Calculate the area of a parallelogram.")
    async def area_parallelogram(self, ctx : Context, base : float, height : float) :

        exp = f"{base} × {height}"
        evalu = base * height

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate area of a kite
    @ cog_ext.cog_slash(description = "Calculate the area of a kite.")
    async def area_kite(self, ctx : Context, long_diagonal : float, short_diagonal : float) :

        exp = f"1/2 × {long_diagonal} × {short_diagonal}"
        evalu = 1/2 * long_diagonal * short_diagonal   

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate area of a trampezium
    @ cog_ext.cog_slash(description = "Calculate the area of a trampezium.")
    async def area_trampezium(self, ctx : Context, first_parallel : float, second_parallel : float, height : float) :

        exp = f"1/2 × ({first_parallel + second_parallel}) × {height}"
        evalu = 1/2 * (first_parallel + second_parallel) * height

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate surface area of a quadrilateral
    @ cog_ext.cog_slash(description = "Calculate the surface area of a cuboid.")
    async def surface_area_quadrilateral(self, ctx : Context,length : float, width : float, height : float) :

        exp = f"2({length} * {width}) + 2({length} × {height}) + 2({width} × {height})"
        evalu = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate surface area of pyramid 
    @ cog_ext.cog_slash(description = "Calculate the surface area of a pyramid.")
    async def surface_area_pyramid(self, ctx : Context, length : float, width : float, face_height : float) :

        exp = f"2(1/2 × {face_height} × {length/2}) + 2(1/2 × {face_height} × {width/2}) + ({length} × {width})"
        evalu = 2 * (1/2 * face_height * (length/2)) + 2 * (1/2 * face_height *(width/2)) + (length * width)

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate surface area of a cylinder
    @ cog_ext.cog_slash(description = "Calculate the surface area of a cylinder.")
    async def surface_area_cylinder(self, ctx : Context, height : float, radius : float = None, diameter : float = None) :

        if (diameter == None and radius != None) :

            exp = f"(2 × 22/7 × {radius}²) + (2 × 22/7 × {radius} × {height})"
            evalu = (2 * 22/7 * (radius ** 2)) + (2 * 22/7 * radius * height)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (radius == None and diameter != None) :

            exp = f"(2 × 22/7 × ({diameter}/2)²) + (2 × 22/7 × ({diameter}/2) × {height})"
            evalu = (2 * 22/7 * ((diameter/2) ** 2)) + (2 * 22/7 * (diameter/2) * height)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide input for only one optional argument.")

    # ! <--- Command to calculate surface area of a cone
    @ cog_ext.cog_slash(description = "Calculate the surface area of a cone.")
    async def surface_area_cone(self, ctx : Context, slant_height : float, radius : float = None, diameter : float = None) :

        if (diameter == None and radius != None) :

            exp = f"(22/7 × {radius}²) + (22/7 × {radius} × {slant_height})"
            evalu = (22/7 * (radius ** 2)) + (22/7 * radius * slant_height)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (radius == None and diameter != None) :

            exp = f"(22/7 × ({diameter}/2)²) + (22/7 × ({diameter}/2) × {slant_height})"
            evalu = (22/7 * ((diameter/2) ** 2)) + (22/7 * (diameter/2) * slant_height)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide input for only one optional argument.")

    # ! <--- Command to calculte surface area of a sphere
    @ cog_ext.cog_slash(description = "Calculate the surface area of a sphere.")
    async def surface_area_sphere(self, ctx : Context, radius : float = None, diameter : float = None) :

        if (diameter == None and radius != None) :

            exp = f"4 × 22/7 × {radius}²"
            evalu = 4 * 22/7 * (radius ** 2)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (radius == None and diameter != None) :

            exp = f"4 × 22/7 × ({diameter}/2)²"
            evalu = 4 * 22/7 * ((diameter/2) ** 2)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide input for only one optional argument.")

    # ! <--- Command to calculate volume of a cube or a cuboid
    @ cog_ext.cog_slash(description = "Calculate the volume of a cube or a cuboid.")
    async def volume_quadrilateral(self, ctx : Context, length : float, width : float, height : float) :

        exp = f"{length} × {width} × {height}"
        evalu = length * width * height 

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate volume of a pyramid
    @ cog_ext.cog_slash(description = "Calculate the volume of a pyramid.")
    async def volume_pyramid(self, ctx : Context, length : float, width : float, height : float) :

        exp = f"1/3 × {length} × {width} × {height}"
        evalu = 1/3 * length * width * height

        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate volume of a cylinder
    @ cog_ext.cog_slash(description = "Calculate the volume of a cylinder.")
    async def volume_cylinder(self, ctx : Context, height : float, radius : float = None, diameter : float = None) :

        if (diameter == None and radius != None) :

            exp = f"22/7 × {radius}² × {height}"
            evalu = 22/7 * (radius ** 2) * height

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (radius == None and diameter != None) :

            exp = f"22/7 × ({diameter}/2)² × {height} "
            evalu = 22/7 * ((diameter/2) ** 2) * height

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide input for only one optional argument.")

    # ! <--- Command to calculate volume of a cone
    @ cog_ext.cog_slash(description = "Calculate the volume of a cone.")
    async def volume_cone(self, ctx : Context, height : float, radius : float = None, diameter : float = None) :

        if (diameter == None and radius != None) :

            exp = f"1/3 × 22/7 × {radius}² × {height}"
            evalu = 1/3 * 22/7 * (radius ** 2) * height

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (radius == None and diameter != None) :

            exp = f"1/3 × 22/7 × ({diameter}/2)² × {height}"
            evalu = 1/3 * 22/7 * ((diameter/2) ** 2) * height

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :

            await ctx.send("Please provide input for only one optional argument.")

    # ! <--- Command to calculate volume of a sphere
    @ cog_ext.cog_slash(description = "Calculate the volume of a sphere.")
    async def volume_sphere(self, ctx : Context, radius : float = None, diameter : float = None) :

        if (diameter == None and radius != None) :

            exp = f"4/3 × 22/7 × {radius}²"
            evalu = 4/3 * 22/7 * (radius ** 2)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        elif (radius == None and diameter != None) :

            exp = f"4/3 × 22/7 × {diameter}/2²"
            evalu = 4/3 * 22/7 * ((diameter/2) ** 2)

            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluuated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)

            await ctx.send(embed = emby_ctx)

        else :
            
            await ctx.send("Please provide input for only one optional argument.")

# ! <--- Add Geometry_Calculation into the bot
def setup(bot):
  bot.add_cog(Geometry_Calculation(bot))