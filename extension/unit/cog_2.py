from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from fraction import Fraction
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for Mass_Volume_Frac
class MassAndVolumeAndFrac(commands.Cog) :


    # NOTE : Initialize parameter for class
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    
    # NOTE : Command convert g to kg 
    @ nextcord.slash_command(
        description = "Convert gram to kilogram."
    )

    async def g_to_kg(self, ctx : Interaction, gram : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{gram}` g", 
            inline = False
        )
        
        embed_msg.add_field(
            name = "Output :", 
            value = f"`{gram / 1000}` kg", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to convert kg to g 
    @ nextcord.slash_command(
        description = "Convert kilogram to gram."
    )

    async def kg_to_g(self, ctx : Interaction, kilogram : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{kilogram}` kg", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{kilogram * 1000}` g", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to convert ml to l 
    @ nextcord.slash_command( 
        description = "Convert mililitre to litre."
    )

    async def ml_to_l(self, ctx : Interaction, millilitre : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{millilitre}` ml", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{millilitre/1000}` l", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to convert l to ml 
    @ nextcord.slash_command(
        description = "Convert litre to mililitre."
    )

    async def l_to_ml(self, ctx : Interaction, litre : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{litre}` l", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{litre * 1000}` ml", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to convert decimal to fraction 
    @ nextcord.slash_command(
        description = "Convert a decimal number to fraction."
    )

    async def deci_to_frac(self, ctx : Interaction, decimal : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{decimal}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{Fraction(str(decimal)).limit_denominator()}`", 
            inline = True
        )
        
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to convert fraction to decimal 
    @ nextcord.slash_command(
        description = "Convert a fraction value to a decimal number."
    )

    async def frac_to_deci(self, ctx : Interaction, numerator : int, denominator : int) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{numerator}/{denominator}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{numerator/denominator}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)
        
        await ctx.response.send_message(embed = embed_msg)


# NOTE : Add MassAndVolumeAndFrac to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(MassAndVolumeAndFrac(bot))