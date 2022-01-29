from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for Length 
class Length(commands.Cog):


    # NOTE :  Initialize parameter for class 
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to convert mm to cm 
    @ commands.command(
        # description ="Convert milimeter to centimeter."
    )

    async def mm_to_cm(self, ctx : Context, milimeter : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            # description ="The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{milimeter}` mm", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{milimeter/10}` cm", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)


    # NOTE : Command to convert cm to m 
    @ commands.command( 
        # description ="Convert centimeter to meter."
    )

    async def cm_to_m(self, ctx : Context, centimeter : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            # description ="The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{centimeter}` cm", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{centimeter/100}` m", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        

    # NOTE : Command to m to km 
    @ commands.command(
        # description ="Convert meter to kilometer."
    )

    async def m_to_km(self, ctx : Context, meter : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            # description ="The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{meter}` m", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{meter/1000}` km", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        

    # NOTE : Command to km to m 
    @ commands.command(
        # description ="Convert kilometer to meter."
    )

    async def km_to_m(self, ctx : Context, kilometer : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            # description ="The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{kilometer}` km", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{kilometer * 1000}` m", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        

    # NOTE : Command to convert m to cm 
    @ commands.command( 
        # description ="Convert meter to centimeter."
    )

    async def m_to_cm(self, ctx : Context, meter : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            # description ="The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{meter}` m", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{meter * 100}` cm", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)
        

    # NOTE : Command to convert cm to mm 
    @ commands.command(
        # description ="Convert centimeter to milimeter."
    )

    async def cm_to_mm(self, ctx : Context, centimeter : float) :

        embed_msg = nextcord.Embed(
            title = "Unit Converter", 
            # description ="The requested `Unit Conversion` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(178, 34, 34)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{centimeter}` cm", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{centimeter * 10}` mm", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.send(embed = embed_msg)


# NOTE : Add Length to the bot 
def setup(bot : commands.Bot):
  bot.add_cog(Length(bot))