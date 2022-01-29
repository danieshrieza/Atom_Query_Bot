from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
import math
from nextcord import Interaction
from config import guild_id


# NOTE : Class for TrigRatios 
class TrigRatios(commands.Cog):


    # NOTE : Initialize parameter for class 
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to find sine of a triangle 
    @ commands.command(
        # description ="Calculate the sine of a triangle."
    )

    async def sine(self,ctx : Interaction, number : float) :

        exp = f"sin {number}°"
        evalu = math.sin(number)

        embed_msg = nextcord.Embed(
            title = "Trigonometry Query", 
            # description ="The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(139, 0, 0)
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


    # NOTE : Command to find cosine of a triangle 
    @ commands.command(
        # description ="Calculate the cosine of a triangle."
    )

    async def cosine(self, ctx : Interaction, number : float) :

        exp = f"cos {number}°"
        evalu = math.cos(number)

        embed_msg = nextcord.Embed(
            title = "Trigonometry Query", 
            # description ="The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(139, 0, 0)
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


    # NOTE : Command to find tangent of a triangle 
    @ commands.command(
        # description ="Calculate the tangent of a triangle."
    )

    async def tangent(self, ctx : Interaction, number : float) :

        exp = f"tan {number}°"
        evalu = math.tan(number)

        embed_msg = nextcord.Embed(
            title = "Trigonometry Query", 
            # description ="The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(139, 0, 0)
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


# NOTE : Add TrigRatios to the bot 
def setup(bot : commands.Bot):
  bot.add_cog(TrigRatios(bot))