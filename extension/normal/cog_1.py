import nextcord
from nextcord.ext import commands
import math
import random
from datetime import datetime, timezone
from nextcord import Interaction
from config import guild_id
from nextcord.ext.commands.context import Context


# NOTE : Class for Basic
class Basic(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate queries from user
    @ nextcord.slash_command(
        description = "Calculate your math's query."
    )
    async def calculate(self, ctx: Interaction, query: str):

        expliteral = ("").join(query)
        exppoet = expliteral.replace("*", "×").replace("/", "÷")
        evalu = eval(expliteral)

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exppoet} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to generate random number
    @ nextcord.slash_command(
        description = "Generate random integer number from input range."
    )
    async def number_generator(self, ctx: Interaction, starting_point: int, ending_point: int):

        exp = f"Generate number between {starting_point} and {ending_point}."
        evalu = f"{random.randint(starting_point, ending_point)}"

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exp} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to square a number
    @ nextcord.slash_command(
        description = "Squared number from user."
    )
    async def square(self, ctx: Interaction, base: float):

        exp = f"{base}²"
        evalu = f"{base ** 2}"

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exp} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to cube a number
    @ nextcord.slash_command(
        description = "Cubed number from user."
    )

    async def cube(self, ctx: Interaction, base: float): 

        exp = f"{base}³"
        evalu = f"{base ** 3}"

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exp} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to power a base using user's exponent
    @ nextcord.slash_command(
        description = "Power the user's base to the exponent."
    )
    async def variable_power(self, ctx: Interaction, base: float, exponent: float): 

        exp = f"{base} ** {exponent}"
        evalu = f"{base ** exponent}"

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exp} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to square root a number
    @ nextcord.slash_command(
        description = "Square root user's number."
    )
    async def square_root(self, ctx: Interaction, radicand: float): 

        exp = f"√{radicand}"
        evalu = f"{math.sqrt(radicand)}"

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exp} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to cube root a number
    @ nextcord.slash_command(
        description = "Cube root user's number."
    )
    async def cube_root(self, ctx: Interaction, radicand: float): 

        exp = f"³√{radicand}"
        evalu = f"{radicand ** 1./3.}"

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exp} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


    # NOTE : Command to root a radicand using a radical
    @ nextcord.slash_command(
        description = "Radical(root) user's radicand(number)."
    )
    async def variable_root(self, ctx: Interaction, radicand: float, radical: float): 

        exp = f"{radicand} ** 1/{radical}"
        evalu = f"{radicand ** 1./radical}"

        embed = nextcord.Embed(
            title = "Math Query",
            description = "The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp = datetime.now(timezone.utc),
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name = "Input :",
            value = f"```Python\n {exp} \n```",
            inline = False
        )

        embed.add_field(
            name = "Output :",
            value = f"```Python\n {evalu} \n```",
            inline = True
        )

        embed.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed)


# NOTE : Add Basic to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Basic(bot))
