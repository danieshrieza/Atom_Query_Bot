from discord import Interaction, app_commands
import discord
from discord.ext import commands
import numpy as np
from config import _set_operation, GUILD_ID, IMAGE_LINK


class Set(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @ commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} is succesfully loaded into bot.")

    @ app_commands.command(description="Check if a value is subset or an element of a set")
    @ app_commands.describe(a="The first set.")
    @ app_commands.describe(b="The second set.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _set_operation
    ])
    async def set_operation(
        self, interaction: Interaction,
        a: str,
        b: str,
        type: app_commands.Choice[int]
    ):

        A = "".join(a).split(" ")
        B = "".join(b).split(" ")

        if type == 1:

            _truth = [True for i in A if i in B]

            embed = discord.Embed(
                title="Set Operation",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(127, 0, 255)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {a} ⊆ {b} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {True if len(_truth) == len(A) else False} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            embed = discord.Embed(
                title="Set Operation",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(127, 0, 255)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {a} ∈ {b} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {True if a in B else False} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 3:

            embed = discord.Embed(
                title="Set Operation",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(127, 0, 255)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {a} ∩ {b} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {np.intersect1d(ar1=A, ar2=B)} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 4:

            embed = discord.Embed(
                title="Set Operation",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(127, 0, 255)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {a} ∪ {b} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {np.union1d(ar1=A, ar2=B)} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Set(bot))
