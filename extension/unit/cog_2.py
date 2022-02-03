from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from fraction import Fraction
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for Mass_Volume_Frac
class MassAndVolumeAndFrac(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command convert g to kg
    @ nextcord.slash_command(
        description = "Convert gram to kilogram."
    )
    async def g_to_kg(self, ctx: Interaction, gram: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {gram} g \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {gram / 1000} kg \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert kg to g
    @ nextcord.slash_command(
        description = "Convert kilogram to gram."
    )
    async def kg_to_g(self, ctx: Interaction, kilogram: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {kilogram} kg \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {kilogram * 1000} g \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert ml to l
    @ nextcord.slash_command(
        description = "Convert mililitre to litre."
    )
    async def ml_to_l(self, ctx: Interaction, millilitre: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {millilitre} ml \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {millilitre/1000} l \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert l to ml
    @ nextcord.slash_command(
        description = "Convert litre to mililitre."
    )
    async def l_to_ml(self, ctx: Interaction, litre: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {litre} l \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {litre * 1000} ml \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert decimal to fraction
    @ nextcord.slash_command(
        description = "Convert a decimal number to fraction."
    )
    async def deci_to_frac(self, ctx: Interaction, decimal: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {decimal} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {Fraction(str(decimal))} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert fraction to decimal
    @ nextcord.slash_command(
        description = "Convert a fraction value to a decimal number."
    )
    async def frac_to_deci(self, ctx: Interaction, numerator: int, denominator: int):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {numerator}/{denominator} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {numerator/denominator} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert Newton to kilogram
    @ nextcord.slash_command(
        description = "Convert Newton to kilogram."
    )
    async def N_to_kg(self, ctx: Interaction, newton: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {newton} N \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {newton / 9.8} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert kg to Newton
    @ nextcord.slash_command(
        description = "Convert kilogram to Newton."
    )
    async def kg_to_N(self, ctx: Interaction, kilogram: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {kilogram} kg \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {kilogram * 9.8} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert Astronomical Unit to kilometer
    @ nextcord.slash_command(
        description = "Convert Astronomical Unit to kilometer."
    )
    async def au_to_km(self, ctx: Interaction, au: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {au} A.U \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {au * (1.5 * 10 ** 8)} km \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert kilometer to Astronomical Unit
    @ nextcord.slash_command(
        description = "Convert kilometer to Astronomical Unit."
    )
    async def km_to_au(self, ctx: Interaction, km: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {km} km \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {km / (1.5 * 10 ** 8)} A.U \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert Light Year to kilometer
    @ nextcord.slash_command(
        description = "Convert Light Year to kilometer."
    )
    async def ly_to_km(self, ctx: Interaction, ly: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {ly} ly \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {ly * (9.5 * 10 ** 12)} km \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert kilometer to Light Year
    @ nextcord.slash_command(
        description = "Convert kilometer to Light Year."
    )
    async def km_to_ly(self, ctx: Interaction, km: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {km} km \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {km / (9.5 * 10 ** 12)} km \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


# NOTE : Add MassAndVolumeAndFrac to the bot
def setup(bot: commands.Bot):
    bot.add_cog(MassAndVolumeAndFrac(bot))
