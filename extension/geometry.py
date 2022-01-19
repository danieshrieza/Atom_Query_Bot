from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction


# <--- Class for Geometry_Calculation --->
class Geometry_Calculation(commands.Cog) :


    # <--- Initialize variable for class --->
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # <--- Command to calculate circumference of a circle using radius --->
    @ nextcord.slash_command(
        description = "Calculate the circumference of a circle using radius."
    )

    async def circumference_of_a_circle_radius(self, ctx : Interaction, radius : float) :
            
        exp = f"2 × 22/7 × {radius}"
        evalu = 2 * 22/7 * radius

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate circumference of a circle using diameter --->
    @ nextcord.slash_command(
        description = "Calculate the circumference of a circle using diameter."
    )

    async def circumference_of_a_circle_diameter(self, ctx : Interaction, diameter : float) :
            
        exp = f"22/7 × {diameter}"
        evalu = 22/7 * diameter

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Commmand to calculate area of a circle --->
    @ nextcord.slash_command( 
        description = "Calculate the area of a circle."
    )
    
    async def area_of_a_circle(self, ctx : Interaction, radius : float) :

        exp = f"22/7 × {radius}²"
        evalu = 22/7 * radius ** 2

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate area of a quadrilateral --->
    @ nextcord.slash_command( 
        description = "Calculate the area of a rectangle, a square or a quadrilateral."
    )

    async def area_of_a_quadrilateral(self, ctx : Interaction, length : float, width : float) :

        exp = f"{length} × {width}"
        evalu = length * width

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate area of a triangle --->
    @ nextcord.slash_command(
        description = "Calculate the area of a triangle."
    )

    async def area_of_a_triangle(self, ctx : Interaction, base : float, height : float) :

        exp = f"1/2 × {base} × {height}"
        evalu = 1/2 * base * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate area of a parallelogram --->
    @ nextcord.slash_command( 
        description = "Calculate the area of a parallelogram."
    )

    async def area_of_a_parallelogram(self, ctx : Interaction, base : float, height : float) :

        exp = f"{base} × {height}"
        evalu = base * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate area of a kite --->
    @ nextcord.slash_command(
        description = "Calculate the area of a kite."
    )

    async def area_of_a_kite(self, ctx : Interaction, long_diagonal : float, short_diagonal : float) :

        exp = f"1/2 × {long_diagonal} × {short_diagonal}"
        evalu = 1/2 * long_diagonal * short_diagonal   

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate area of a trampezium --->
    @ nextcord.slash_command(
        description = "Calculate the area of a trampezium."
    )

    async def area_of_a_trampezium(self, ctx : Interaction, first_parallel : float, second_parallel : float, height : float) :

        exp = f"1/2 × ({first_parallel + second_parallel}) × {height}"
        evalu = 1/2 * (first_parallel + second_parallel) * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate surface area of a quadrilateral --->
    @ nextcord.slash_command(
        description = "Calculate the surface area of a cuboid."
    )

    async def surface_area_of_a_quadrilateral(self, ctx : Interaction, length : float, width : float, height : float) :

        exp = f"2({length} × {width}) + 2({length} × {height}) + 2({width} × {height})"
        evalu = 2 * (length * width) + 2 * (length * height) + 2 * (width * height)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate surface area of pyramid --->
    @ nextcord.slash_command(
        description = "Calculate the surface area of a pyramid."
    )

    async def surface_area_of_a_pyramid(self, ctx : Interaction, length : float, width : float, face_height : float) :

        exp = f"2(1/2 × {face_height} × {length/2}) + 2(1/2 × {face_height} × {width/2}) + ({length} × {width})"
        evalu = 2 * (1/2 * face_height * (length/2)) + 2 * (1/2 * face_height *(width/2)) + (length * width)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate surface area of a cylinder --->
    @ nextcord.slash_command( 
        description = "Calculate the surface area of a cylinder."
    )

    async def surface_area_of_a_cylinder(self, ctx : Interaction, height : float, radius : float) :

        exp = f"(2 × 22/7 × {radius}²) + (2 × 22/7 × {radius} × {height})"
        evalu = (2 * 22/7 * (radius ** 2)) + (2 * 22/7 * radius * height)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate surface area of a cone --->
    @ nextcord.slash_command(
        description = "Calculate the surface area of a cone."
    )

    async def surface_area_of_a_cone(self, ctx : Interaction, slant_height : float, radius : float) :

        exp = f"(22/7 × {radius}²) + (22/7 × {radius} × {slant_height})"
        evalu = (22/7 * (radius ** 2)) + (22/7 * radius * slant_height)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculte surface area of a sphere --->
    @ nextcord.slash_command(
        description = "Calculate the surface area of a sphere."
    )

    async def surface_area_of_a_sphere(self, ctx : Interaction, radius : float) :

        exp = f"4 × 22/7 × {radius}²"
        evalu = 4 * 22/7 * (radius ** 2)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate volume of a cube or a cuboid --->
    @ nextcord.slash_command(
        description = "Calculate the volume of a cube or a cuboid."
    )

    async def volume_of_a_quadrilateral(self, ctx : Interaction, length : float, width : float, height : float) :

        exp = f"{length} × {width} × {height}"
        evalu = length * width * height 

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate volume of a pyramid --->
    @ nextcord.slash_command(
        description = "Calculate the volume of a pyramid."
    )

    async def volume_of_a_pyramid(self, ctx : Interaction, length : float, width : float, height : float) :

        exp = f"1/3 × {length} × {width} × {height}"
        evalu = 1/3 * length * width * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate volume of a cylinder --->
    @ nextcord.slash_command(
        description = "Calculate the volume of a cylinder."
    )

    async def volume_of_a_cylinder(self, ctx : Interaction, height : float, radius : float) :

        exp = f"22/7 × {radius}² × {height}"
        evalu = 22/7 * (radius ** 2) * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate volume of a cone --->
    @ nextcord.slash_command(
        description = "Calculate the volume of a cone."
    )

    async def volume_of_a_cone(self, ctx : Interaction, height : float, radius : float) :

        exp = f"1/3 × 22/7 × {radius}² × {height}"
        evalu = 1/3 * 22/7 * (radius ** 2) * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


    # <--- Command to calculate volume of a sphere --->
    @ nextcord.slash_command( 
        description = "Calculate the volume of a sphere."
    )

    async def volume_of_a_sphere(self, ctx : Interaction, radius : float) :

        exp = f"4/3 × 22/7 × {radius}²"
        evalu = 4/3 * 22/7 * (radius ** 2)

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(157,34,53)
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


# <--- Add Geometry_Calculation into the bot --->
def setup(bot : commands.Bot):
  bot.add_cog(Geometry_Calculation(bot))