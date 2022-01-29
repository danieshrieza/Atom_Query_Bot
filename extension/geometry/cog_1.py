from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import guild_id


# NOTE : Class for SurfaceAndVolume 
class SurfaceAndVolume(commands.Cog) :


    # NOTE : Initialize parameter for class 
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate surface area of a quadrilateral 
    @ commands.command(
        # description ="Calculate the surface area of a cuboid."
    )

    async def surface_area_quadrilateral(self, ctx : Interaction, length : float, width : float, height : float) :

        exp = f"2({length} × {width}) + 2({length} × {height}) + 2({width} × {height})"
        evalu = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate surface area of pyramid 
    @ commands.command(
        # description ="Calculate the surface area of a pyramid."
    )

    async def surface_area_pyramid(self, ctx : Interaction, length : float, width : float, face_height : float) :

        exp = f"2(1/2 × {face_height} × {length/2}) + 2(1/2 × {face_height} × {width/2}) + ({length} × {width})"
        evalu = 2 * (1/2 * face_height * (length/2)) + 2 * (1/2 * face_height *(width/2)) + (length * width)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate surface area of a cylinder 
    @ commands.command( 
        # description ="Calculate the surface area of a cylinder."
    )

    async def surface_area_cylinder(self, ctx : Interaction, height : float, radius : float) :

        exp = f"(2 × 22/7 × {radius}²) + (2 × 22/7 × {radius} × {height})"
        evalu = (2 * 22/7 * (radius ** 2)) + (2 * 22/7 * radius * height)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate surface area of a cone 
    @ commands.command(
        # description ="Calculate the surface area of a cone."
    )

    async def surface_area_cone(self, ctx : Interaction, slant_height : float, radius : float) :

        exp = f"(22/7 × {radius}²) + (22/7 × {radius} × {slant_height})"
        evalu = (22/7 * (radius ** 2)) + (22/7 * radius * slant_height)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculte surface area of a sphere 
    @ commands.command(
        # description ="Calculate the surface area of a sphere."
    )

    async def surface_area_sphere(self, ctx : Interaction, radius : float) :

        exp = f"4 × 22/7 × {radius}²"
        evalu = 4 * 22/7 * (radius ** 2)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate volume of a cube or a cuboid 
    @ commands.command(
        # description ="Calculate the volume of a cube or a cuboid."
    )

    async def volume_quadrilateral(self, ctx : Interaction, length : float, width : float, height : float) :

        exp = f"{length} × {width} × {height}"
        evalu = length * width * height 

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate volume of a pyramid 
    @ commands.command(
        # description ="Calculate the volume of a pyramid."
    )

    async def volume_pyramid(self, ctx : Interaction, length : float, width : float, height : float) :

        exp = f"1/3 × {length} × {width} × {height}"
        evalu = 1/3 * length * width * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate volume of a cylinder 
    @ commands.command(
        # description ="Calculate the volume of a cylinder."
    )

    async def volume_cylinder(self, ctx : Interaction, height : float, radius : float) :

        exp = f"22/7 × {radius}² × {height}"
        evalu = 22/7 * (radius ** 2) * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate volume of a cone 
    @ commands.command(
        # description ="Calculate the volume of a cone."
    )

    async def volume_cone(self, ctx : Interaction, height : float, radius : float) :

        exp = f"1/3 × 22/7 × {radius}² × {height}"
        evalu = 1/3 * 22/7 * (radius ** 2) * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate volume of a sphere 
    @ commands.command( 
        # description ="Calculate the volume of a sphere."
    )

    async def volume_sphere(self, ctx : Interaction, radius : float) :

        exp = f"4/3 × 22/7 × {radius}²"
        evalu = 4/3 * 22/7 * (radius ** 2)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            # description ="The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157, 34, 53)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


# NOTE : Add SurfaceAndVolume to the bot 
def setup(bot : commands.Bot):
  bot.add_cog(SurfaceAndVolume(bot))