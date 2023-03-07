import discord
from discord.ext import commands
import math

from discord import Interaction, app_commands
from config import GUILD_ID, IMAGE_LINK


class Query(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @ commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} is succesfully loaded into bot.")

    # @ app_commands.command(
    #     description="Calculate your math's query.",
    #
    # )
    # async def calculate(self, interaction: Interaction, query: str):

    #     expliteral = ("").join(query)
    #     exppoet = expliteral.replace("*", "×").replace("/", "÷")
    #     evalu = eval(expliteral)

    #     embed = discord.Embed(
    #         title="Math Query",
    #         description="The requested `Math Query` have been evaluated by **Atom Query**",
    #         timestamp=discord.utils.format_dt(
    #             datetime.now(timezone.utc), style="f"),
    #         colour=discord.Color.from_rgb(179, 27, 27)
    #     )

    #     embed.add_field(
    #         name="Input :",
    #         value=f"```Python\n {exppoet} \n```",
    #         inline=False
    #     )

    #     embed.add_field(
    #         name="Output :",
    #         value=f"```Python\n {evalu} \n```",
    #         inline=True
    #     )

    #     embed.set_thumbnail(url=IMAGE_LINK)

    #     await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Raise the base to the index.")
    @ app_commands.describe(base="The base of the indices.")
    @ app_commands.describe(exponent="The number of times to multiply the base.")
    async def index(
        self,
        interaction: Interaction,
        base: float,
        exponent: float
    ):

        exp = f"{base} ** {exponent}"
        evalu = base ** exponent

        embed = discord.Embed(
            title="Math Query",
            description="Query has been **successfully** evaluated.",
            timestamp=discord.utils.utcnow(),
            colour=discord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=IMAGE_LINK)

        await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Factorise the radicand to the exponent.")
    @ app_commands.describe(radicand="The number to factor into the same base.")
    @ app_commands.describe(index="The index to factor the number.")
    async def radical(
        self,
        interaction: Interaction,
        radicand: float,
        index: float
    ):

        exp = f"{radicand} ** 1 / {index}"
        evalu = radicand ** (1. / index)

        embed = discord.Embed(
            title="Math Query",
            description="Query has been **successfully** evaluated.",
            timestamp=discord.utils.utcnow(),
            colour=discord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=IMAGE_LINK)

        await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Find the number of time a number multiplied itself.")
    @ app_commands.describe(base="The base of the logarithm.")
    @ app_commands.describe(radicand="The number to find the index.")
    async def logarithm(
        self,
        interaction: Interaction,
        base: float,
        radicand: float
    ):

        exp = f"log {base} {radicand}"
        evalu = math.log(radicand, base)

        embed = discord.Embed(
            title="Math Query",
            description="Query has been **successfully** evaluated.",
            timestamp=discord.utils.utcnow(),
            colour=discord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=IMAGE_LINK)

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Query(bot))
