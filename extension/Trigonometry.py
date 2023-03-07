import discord
from discord.ext import commands
import math
from discord import Interaction, app_commands
from config import GUILD_ID, _trigonometric_ratio, IMAGE_LINK


class Trigonometry(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @ commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} is succesfully loaded into bot.")

    @ app_commands.command(description="Calculate the hypotenuse of a triangle.")
    @ app_commands.describe(a="The height of the triangle.")
    @ app_commands.describe(b="The base length of the triangle.")
    async def pythagoras_theorem(
        self,
        interaction: Interaction,
        a: float,
        b: float
    ):

        formula = "c = √a² + b²"
        c = math.sqrt((a ** 2) + (b ** 2))

        embed = discord.Embed(
            title="Trigonometry Query",
            description="Query has been **successfully** evaluated.",
            timestamp=discord.utils.utcnow(),
            colour=discord.Color.from_rgb(139, 0, 0)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {c} \n```",
            inline=True
        )

        embed.set_thumbnail(url=IMAGE_LINK)

        await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the sine, cosine, or tangent of a value.")
    @ app_commands.describe(number="The number to find the value of its sine, cosine or tangent.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _trigonometric_ratio
    ])
    async def trigonometry_ratio(
        self,
        interaction: Interaction,
        number: float,
        type: app_commands.Choice[int]
    ):

        if type == 1:

            formula = f"sin {number}°"
            evalu = math.sin(number)

            embed = discord.Embed(
                title="Trigonometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(139, 0, 0)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {evalu} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = f"cos {number}°"
            evalu = math.cos(number)

            embed = discord.Embed(
                title="Trigonometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(139, 0, 0)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {evalu} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 3:

            formula = f"tan {number}°"
            evalu = math.tan(number)

            embed = discord.Embed(
                title="Trigonometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(139, 0, 0)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
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
    await bot.add_cog(Trigonometry(bot))
