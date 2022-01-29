from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for BasicPhysics 
class BasicPhysics(commands.Cog) :


    # NOTE : Initialize parameter for class 
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate speed of an object 
    @ nextcord.slash_command(
        description = "Calculate the speed of an object using any distance and time unit."
    )

    async def speed(self, ctx : Interaction, distance : float, time : float) :

        exp = f"{distance} ÷ {time}"
        evalu = distance/time

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} m/s`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate electric current of an object 
    @ nextcord.slash_command(
        description = "Calculate the electric current of an object."
    )

    async def electric_current(self, ctx : Interaction, electric_voltage : float, electric_resistance : float ) :

        exp = f"{electric_voltage} V ÷ {electric_resistance} Ω"
        evalu = electric_voltage/electric_resistance

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} A`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate electric voltage of an object 
    @ nextcord.slash_command(
        description = "Calculate the electric voltage of an object."
    )

    async def electric_voltage(self, ctx : Interaction, electric_current : float, electric_resistance : float ) :

        exp = f"{electric_current} A × {electric_resistance} Ω"
        evalu = electric_current * electric_resistance

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} V`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to calculate electric resistance of an object 
    @ nextcord.slash_command(
        description = "Calculate the electric resistance of an object."
    )

    async def electric_resistance(self, ctx : Interaction, electric_voltage : float, electric_current : float ) :

        exp = f"{electric_voltage} V ÷ {electric_current} A"
        evalu = electric_voltage/electric_current

        embed_msg = nextcord.Embed(
            title = "Physics Query", 
            description = "The requested `Physics Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"``` {exp} ```", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu} Ω`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


# NOTE : Add BasicPhysics to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(BasicPhysics(bot))


