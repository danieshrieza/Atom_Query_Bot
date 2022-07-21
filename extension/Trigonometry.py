from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
import math
from nextcord import Interaction, SlashOption, slash_command
from config import GUILD_ID


class Trigonometry(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    @ slash_command(
        description="Calculate the hypotenuse of a triangle.",
        guild_ids=[GUILD_ID]
    )
    async def pythagorastheorem(self, interaction: Interaction, height: float = SlashOption(description="The height of the triangle."), base: float = SlashOption(description="The base length of the triangle.")):

        formula = "c = √a² + b²"
        c = math.sqrt((base ** 2) + (height ** 2))

        embed = nextcord.Embed(
            title="Trigonometry Query",
            description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(139, 0, 0)
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

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the sine of a value.",
        guild_ids=[GUILD_ID]
    )
    async def trigonometryratio(self, interaction: Interaction, number: float = SlashOption(description="The number to find the sine of.")):

        formula = f"sin {number}°"
        evalu = math.sin(number)

        embed = nextcord.Embed(
            title="Trigonometry Query",
            description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(139, 0, 0)
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

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the cosine of a value.",
        guild_ids=[GUILD_ID]
    )
    async def cosine(self, interaction: Interaction, number: float = SlashOption(description="The number to find the cosine of.")):

        formula = f"cos {number}°"
        evalu = math.cos(number)

        embed = nextcord.Embed(
            title="Trigonometry Query",
            description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(139, 0, 0)
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

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the tangent of a value.",
        guild_ids=[GUILD_ID]
    )
    async def tangent(self, interaction: Interaction, number: float = SlashOption(description="The number to find the tangent of.")):

        formula = f"tan {number}°"
        evalu = math.tan(number)

        embed = nextcord.Embed(
            title="Trigonometry Query",
            description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(139, 0, 0)
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

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Trigonometry(bot))
