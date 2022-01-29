from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for PerimeterAndArea
class PerimeterAndArea(commands.Cog) :


    # NOTE : Initialize parameter for class
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate circumference of a circle using radius 
    @ nextcord.slash_command(
        description = "Calculate the circumference of a circle using radius."
    )

    async def circumference_circle_radius(self, ctx : Interaction, radius : float) :
            
        exp = f"2 × 22/7 × {radius}"
        evalu = 2 * 22/7 * radius

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
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


    # NOTE : Commmand to calculate area of a circle 
    @ nextcord.slash_command( 
        description = "Calculate the area of a circle."
    )
    
    async def area_circle(self, ctx : Interaction, radius : float) :

        exp = f"22/7 × {radius}²"
        evalu = 22/7 * radius ** 2

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
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


    # NOTE : Command to calculate area of a quadrilateral 
    @ nextcord.slash_command( 
        description = "Calculate the area of a rectangle, a square or a quadrilateral."
    )

    async def area_quadrilateral(self, ctx : Interaction, length : float, width : float) :

        exp = f"{length} × {width}"
        evalu = length * width

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
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


    # NOTE : Command to calculate area of a triangle 
    @ nextcord.slash_command(
        description = "Calculate the area of a triangle."
    )

    async def area_triangle(self, ctx : Interaction, base : float, height : float) :

        exp = f"1/2 × {base} × {height}"
        evalu = 1/2 * base * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
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


    # NOTE : Command to calculate area of a parallelogram 
    @ nextcord.slash_command( 
        description = "Calculate the area of a parallelogram."
    )

    async def area_parallelogram(self, ctx : Interaction, base : float, height : float) :

        exp = f"{base} × {height}"
        evalu = base * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
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


    # NOTE : Command to calculate area of a kite 
    @ nextcord.slash_command(
        description = "Calculate the area of a kite."
    )

    async def area_kite(self, ctx : Interaction, long_diagonal : float, short_diagonal : float) :

        exp = f"1/2 × {long_diagonal} × {short_diagonal}"
        evalu = 1/2 * long_diagonal * short_diagonal   

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
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


    # NOTE : Command to calculate area of a trampezium 
    @ nextcord.slash_command(
        description = "Calculate the area of a trampezium."
    )

    async def area_trampezium(self, ctx : Interaction, first_parallel : float, second_parallel : float, height : float) :

        exp = f"1/2 × ({first_parallel + second_parallel}) × {height}"
        evalu = 1/2 * (first_parallel + second_parallel) * height

        embed_msg = nextcord.Embed(
            title = "Geometry Query", 
            description = "The requested `Geometry Query` have been evaluated by **Atom Query**", 
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

# NOTE : Add PerimeterAndArea to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(PerimeterAndArea(bot))