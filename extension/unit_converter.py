import discord
from discord.ext import commands
from discord import Interaction, app_commands
from config import _prefix, _si_unit, GUILD_ID, IMAGE_LINK


class Unit_Converter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @ commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} is succesfully loaded into bot.")

    def search_unit(v: int, d: list):

        for key, value in d:
            if value == v:
                return key

    @ app_commands.command(description="Convert S.I unit from one prefix to another.")
    @ app_commands.guilds(GUILD_ID)
    @ app_commands.describe(init_value="The initial value before conversion.")
    @ app_commands.describe(final_prefix="The final prefix to convert to from initial prefix.")
    @ app_commands.describe(si_unit="The physical quantity of the value.")
    @ app_commands.choices(init_prefix=[
        app_commands.Choice(name=name, value=prefix) for name, prefix in _prefix
    ])
    @ app_commands.choices(final_prefix=[
        app_commands.Choice(name=name, value=prefix) for name, prefix in _prefix
    ])
    @ app_commands.choices(si_unit=[
        app_commands.Choice(name=name, value=unit) for name, unit in _si_unit
    ])
    async def prefix_converter(
        self,
        interaction: Interaction,
        init_value: float,
        init_prefix: app_commands.Choice[float],
        final_prefix: app_commands.Choice[float],
        si_unit: app_commands.Choice[str]
    ):

        if init_prefix > final_prefix:

            final_value = init_value * (final_prefix / init_prefix)

            embed = discord.Embed(
                title=f"Unit Converter",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(178, 34, 34)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {init_value} {Unit_Converter.search_unit(v=init_prefix, d=_prefix)}{si_unit} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {final_value} {Unit_Converter.search_unit(v=final_prefix, d=_prefix)}{si_unit} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif init_prefix < final_prefix:

            final_value = init_value / (final_prefix / init_prefix)

            embed = discord.Embed(
                title="Unit Converter",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(178, 34, 34)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {init_value} {Unit_Converter.search_unit(v=init_prefix, d=_prefix)}{si_unit} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {final_value} {Unit_Converter.search_unit(v=final_prefix, d=_prefix)}{si_unit} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        else:

            embed = discord.Embed(
                title="Unit Converter",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(178, 34, 34)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {init_value} {Unit_Converter.search_unit(v=init_prefix, d=_prefix)}{si_unit} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {final_value} {Unit_Converter.search_unit(v=final_prefix, d=_prefix)}{si_unit} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Unit_Converter(bot))
