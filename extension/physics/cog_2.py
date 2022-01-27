from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import guild_id


# NOTE : Class for EnergyAndForce
class EnergyAndForce(commands.Cog) :


    # NOTE : Initialize parameter for class
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate moment of force of an object 
    @ nextcord.slash_command(
        description = "Calculate the moment of force of an object."
    )

    async def moment_of_force(self, ctx : Interaction, force : float, perpendicular_distance : float) :

        exp = f"{force} N × {perpendicular_distance} m "
        evalu = force * perpendicular_distance

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} N m`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate the pressure acts on an object 
    @ nextcord.slash_command(
        description = "Calculate the pressure acts on an object."
    )

    async def pressure(self, ctx : Interaction, force : float, surface_area : float) :

        exp = f"{force} N ÷ {surface_area} m²"
        evalu = force/surface_area

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )
        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} N/m²`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)
    

    # NOTE : Command to calculate the density of an object 
    @ nextcord.slash_command(
        description = "Calculate the density of an object."
    )

    async def density(self, ctx : Interaction, mass : float, volume : float) :

        exp = f'{mass} g ÷ {volume} cm³'
        evalu = mass/volume

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{exp}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} g/cm³`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


# NOTE : Add EnergyAndForce to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(EnergyAndForce(bot))