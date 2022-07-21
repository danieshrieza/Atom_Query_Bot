from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, slash_command
from config import _prefix, _si_unit, GUILD_ID


class Converter(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    def search_unit(v: int, d: dict):

        for key, value in d.items():
            if value == v:
                return key

    @ slash_command(
        description="Convert S.I unit from one prefix to another.",
        guild_ids=[GUILD_ID]
    )
    async def si_prefix_converter(self, interaction: Interaction, init_value: float = SlashOption(description="The initial value before conversion."), init_prefix: int = SlashOption(description="The intial prefix before conversion e.g. nano.", required=True, choices=_prefix), final_prefix: int = SlashOption(description="The final prefix to convert to from initial prefix.", required=True, choices=_prefix), si_unit: str = SlashOption(description="The physical quantity of the value e.g. meter." ,required=True, choices=_si_unit)):

        if init_prefix == final_prefix:
            await interaction.response.send_message("You've chose the same unit before and after conversion")

        elif init_prefix > final_prefix:

            final_value = init_value * (final_prefix / init_prefix)

            embed = nextcord.Embed(
                title="Unit Converter",
                description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(178, 34, 34)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {init_value} {Converter.search_unit(v=init_prefix, d=_prefix)}{si_unit} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {final_value} {Converter.search_unit(v=final_prefix, d=_prefix)}{si_unit} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        else:

            final_value = init_value / (final_prefix / init_prefix)

            embed = nextcord.Embed(
                title="Unit Converter",
                description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(178, 34, 34)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {init_value} {Converter.search_unit(v=init_prefix, d=_prefix)}{si_unit} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {final_value} {Converter.search_unit(v=final_prefix, d=_prefix)}{si_unit} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Converter(bot))
