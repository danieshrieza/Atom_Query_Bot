from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for Length
class Length(commands.Cog):


    # NOTE :  Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to convert mm to cm
    @ nextcord.slash_command(
        description = "Convert milimeter to centimeter."
    )
    async def mm_to_cm(self, ctx: Interaction, milimeter: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {milimeter} mm \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {milimeter/10} cm \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert cm to m
    @ nextcord.slash_command(
        description = "Convert centimeter to meter."
    )
    async def cm_to_m(self, ctx: Interaction, centimeter: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {centimeter} cm \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {centimeter/100} m \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to m to km
    @ nextcord.slash_command(
        description = "Convert meter to kilometer."
    )
    async def m_to_km(self, ctx: Interaction, meter: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {meter} m \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {meter/1000} km \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to km to m
    @ nextcord.slash_command(
        description = "Convert kilometer to meter."
    )
    async def km_to_m(self, ctx: Interaction, kilometer: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {kilometer} km \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {kilometer * 1000} m \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert m to cm
    @ nextcord.slash_command(
        description = "Convert meter to centimeter."
    )
    async def m_to_cm(self, ctx: Interaction, meter: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {meter} m \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {meter * 100} cm \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to convert cm to mm
    @ nextcord.slash_command(
        description = "Convert centimeter to milimeter."
    )
    async def cm_to_mm(self, ctx: Interaction, centimeter: float):

        embed = nextcord.Embed(
            title = "Unit Converter",
            description = "The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {centimeter} cm \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {centimeter * 10} mm \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


# NOTE : Add Length to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Length(bot))
