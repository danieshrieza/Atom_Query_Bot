from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
import math
from nextcord import Interaction, slash_command


# NOTE : Class for TrigRatios
class TrigRatios(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to find sine of a triangle
    @ slash_command(
        description="Calculate the sine of a triangle."
    )
    async def sine(self, interaction: Interaction, number: float):

        exp=f"sin {number}°"
        evalu=math.sin(number)

        embed=nextcord.Embed(
            title="Trigonometry Query",
            description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(139, 0, 0)
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

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to find cosine of a triangle
    @ slash_command(
        description="Calculate the cosine of a triangle."
    )
    async def cosine(self, interaction: Interaction, number: float):

        exp=f"cos {number}°"
        evalu=math.cos(number)

        embed=nextcord.Embed(
            title="Trigonometry Query",
            description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(139, 0, 0)
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

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to find tangent of a triangle
    @ slash_command(
        description="Calculate the tangent of a triangle."
    )
    async def tangent(self, interaction: Interaction, number: float):

        exp=f"tan {number}°"
        evalu=math.tan(number)

        embed=nextcord.Embed(
            title="Trigonometry Query",
            description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(139, 0, 0)
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

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


# NOTE : Add TrigRatios to the bot
def setup(bot: commands.Bot):
    bot.add_cog(TrigRatios(bot))
