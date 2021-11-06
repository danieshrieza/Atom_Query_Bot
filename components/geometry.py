from datetime import datetime, timezone
import discord
from discord.ext import commands
from discord_slash import cog_ext

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

    # ? <--- Initialize variable for class
    def __init__(self, client):
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ? <--- Command to calculate circumference of a circle using diameter or radius
    @ cog_ext.cog_slash(description = "Calculate the circumference of a circle using diameter or radius")
    async def circle_circumference(self,ctx, radius : float = None, diameter : float = None) :
        if (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"22/7 × {diameter}"
            eval = 22/7 * diameter
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"2 × 22/7 × {radius}"
            eval = 2 * 22/7 * radius
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

    # ? <--- Commmand to calculate area of a circle
    @ cog_ext.cog_slash(description = "Calculate the area of a circle.")
    async def area_circle(self,ctx,radius : float = None, diameter : float = None) :
        if (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"22/7 × {radius}²"
            eval = 22/7 * radius ** 2
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"22/7 × ({diameter}/2)²"
            eval = 22/7 * (diameter/2) ** 2
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :", value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

    # ? <--- Command to calculate area of a quadrilateral
    @ cog_ext.cog_slash(description = "Calculate the area of a rectangle, a square or a quadrilateral.")
    async def area_quadrilateral(self,ctx,length : float, width : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"{length} × {width}"
        eval = length * width
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate area of a triangle
    @ cog_ext.cog_slash(description = "Calculate the area of a triangle.")
    async def area_triangle(self,ctx,base : float, height : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"1/2 × {base} × {height}"
        eval = 1/2 * base * height
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate area of a parallelogram
    @ cog_ext.cog_slash(description = "Calculate the area of a parallelogram.")
    async def area_parallelogram(self,ctx,base : float, height : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"{base} × {height}"
        eval = base * height
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate area of a kite
    @ cog_ext.cog_slash(description = "Calculate the area of a kite.")
    async def area_kite(self,ctx,long_diagonal : float, short_diagonal : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"1/2 × {long_diagonal} × {short_diagonal}"
        eval = 1/2 * long_diagonal * short_diagonal   
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate area of a trampezium
    @ cog_ext.cog_slash(description = "Calculate the area of a trampezium.")
    async def area_trampezium(self,ctx,first_parallel : float, second_parallel : float, height : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"1/2 × ({first_parallel + second_parallel}) × {height}"
        eval = 1/2 * (first_parallel + second_parallel) * height
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate surface area of a quadrilateral
    @ cog_ext.cog_slash(description = "Calculate the surface area of a cuboid.")
    async def surface_area_quadrilateral(self,ctx,length : float, width : float, height : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"2({length} * {width}) + 2({length} × {height}) + 2({width} × {height})"
        eval = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate surface area of pyramid 
    @ cog_ext.cog_slash(description = "Calculate the surface area of a pyramid.")
    async def surface_area_pyramid(self,ctx,length : float, width : float, face_height : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"2(1/2 × {face_height} × {length/2}) + 2(1/2 × {face_height} × {width/2}) + ({length} × {width})"
        eval = 2 * (1/2 * face_height * (length/2)) + 2 * (1/2 * face_height *(width/2)) + (length * width)
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate surface area of a cylinder
    @ cog_ext.cog_slash(description = "Calculate the surface area of a cylinder.")
    async def surface_area_cylinder(self,ctx, height : float, radius : float = None, diameter : float = None) :
        if (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"(2 × 22/7 × {radius}²) + (2 × 22/7 × {radius} × {height})"
            eval = (2 * 22/7 * (radius ** 2)) + (2 * 22/7 * radius * height)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"(2 × 22/7 × ({diameter}/2)²) + (2 × 22/7 × ({diameter}/2) × {height})"
            eval = (2 * 22/7 * ((diameter/2) ** 2)) + (2 * 22/7 * (diameter/2) * height)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

    # ? <--- Command to calculate surface area of a cone
    @ cog_ext.cog_slash(description = "Calculate the surface area of a cone.")
    async def surface_area_cone(self,ctx, slant_height : float, radius : float = None, diameter : float = None) :
        if (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"(22/7 × {radius}²) + (22/7 × {radius} × {slant_height})"
            eval = (22/7 * (radius ** 2)) + (22/7 * radius * slant_height)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"(22/7 × ({diameter}/2)²) + (22/7 × ({diameter}/2) × {slant_height})"
            eval = (22/7 * ((diameter/2) ** 2)) + (22/7 * (diameter/2) * slant_height)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

    # ? <--- Command to calculte surface area of a sphere
    @ cog_ext.cog_slash(description = "Calculate the surface area of a sphere.")
    async def surface_area_sphere(self,ctx,radius : float = None, diameter : float = None) :
        if (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"4 × 22/7 × {radius}²"
            eval = 4 * 22/7 * (radius ** 2)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"4 × 22/7 × ({diameter}/2)²"
            eval = 4 * 22/7 * ((diameter/2) ** 2)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

    # ? <--- Command to calculate volume of a cube or a cuboid
    @ cog_ext.cog_slash(description = "Calculate the volume of a cube or a cuboid.")
    async def volume_quadrilateral(self,ctx,length : float, width : float, height : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"{length} × {width} × {height}"
        eval = length * width * height 
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate volume of a pyramid
    @ cog_ext.cog_slash(description = "Calculate the volume of a pyramid.")
    async def volume_pyramid(self,ctx,length : float,width : float,height : float) :
        emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
        exp = f"1/3 × {length} × {width} × {height}"
        eval = 1/3 * length * width * height
        emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.send(embed = emby_ctx)

    # ? <--- Command to calculate volume of a cylinder
    @ cog_ext.cog_slash(description = "Calculate the volume of a cylinder.")
    async def volume_cylinder(self, ctx, height : float, radius : float = None, diameter : float = None) :
        if (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"22/7 × {radius}² × {height}"
            eval = 22/7 * (radius ** 2) * height
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"22/7 × ({diameter}/2)² × {height} "
            eval = 22/7 * ((diameter/2) ** 2) * height
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

    # ? <--- Command to calculate volume of a cone
    @ cog_ext.cog_slash(description = "Calculate the volume of a cone.")
    async def volume_cone(self, ctx, height : float, radius : float = None, diameter : float = None) :
        if (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"1/3 × 22/7 × {radius}² × {height}"
            eval = 1/3 * 22/7 * (radius ** 2) * height
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"1/3 × 22/7 × ({diameter}/2)² × {height}"
            eval = 1/3 * 22/7 * ((diameter/2) ** 2) * height
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

    # ? <--- Command to calculate volume of a sphere
    @ cog_ext.cog_slash(description = "Calculate the volume of a sphere.")
    async def volume_sphere(self, ctx, radius : float = None, diameter : float = None) :
        if (diameter == None and radius != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"4/3 × 22/7 × {radius}²"
            eval = 4/3 * 22/7 * (radius ** 2)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        elif (radius == None and diameter != None) :
            emby_ctx = discord.Embed(title = "Geometry Query", description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(157,34,53))
            exp = f"4/3 × 22/7 × {diameter}/2²"
            eval = 4/3 * 22/7 * ((diameter/2) ** 2)
            emby_ctx.set_author(name = f"@{ctx.author.name} query.", icon_url = ctx.author.avatar_url)
            emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
            emby_ctx.add_field(name = "Output :" , value = f"`{eval}`", inline = True)
            emby_ctx.set_thumbnail(url = self.link)
            await ctx.send(embed = emby_ctx)
        else :
            await ctx.send("Please provide input for only one optional argument.")

# ! <--- Add Geometry_Calculation into the bot
def setup(client):
  client.add_cog(Geometry_Calculation(client))