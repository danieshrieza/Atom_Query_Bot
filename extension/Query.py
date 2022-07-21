import nextcord
from nextcord.ext import commands
import math
from datetime import datetime, timezone
from nextcord import Interaction, SlashOption, slash_command
from config import _factor, _multiple, GUILD_ID


class Query(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    @ slash_command(
        description="Find the factor of a number and common multiple or highest common multiple of two numbers.",
        guild_ids=[GUILD_ID]
    )
    async def factor(self, interaction: Interaction, number_1: int = SlashOption(description="The first number to find the factor."), number_2: int = SlashOption(description="The second number to find the factor. (Only fill this if you want to find the common factor or the highest common factor of two numbers)", required=False, default=None), type: str = SlashOption(name="The type of calculation to be evaluated.", required=True, choices=_factor)):

        if type == 1:

            arr = [i for i in range(1, number_1 + 1) if number_1 % i == 0]

            embed = nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n Factor of {number_1}. \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {arr} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2 and number_2 is not None:

            arr = [i for i in range(
                1, min(number_1, number_2) + 1) if number_1 % i == number_2 % i == 0]

            embed = nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n Common Factor of {number_1} and {number_2}. \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {arr} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 3 and number_2 is not None:

            evalu = math.gcd(number_1, number_2)

            embed = nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n Highest Common Factor of {number_1} and {number_2}. \n```",
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
        description="Find the multiple of a number and common multiple or lowest common multiple of two numbers.",
        guild_ids=[GUILD_ID]
    )
    async def multiple(self, interaction: Interaction, number_1: int = SlashOption(description="The first number to find the multiple."), number_range: int = SlashOption(description="The range of multiple to find."), number_2: int = SlashOption(description="The second number to find the multiple. (Only fill this if you want to find the common multiple or the lowest common multiple of two numbers)", required=False, default=None), type: str = SlashOption(name="The type of calculation to be evaluated.", required=True, choices=_multiple)):

        if type == 1:

            arr = [number_1 * i for i in range(1, number_range + 1)]

            embed = nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n Multiple of {number_1}. \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {arr} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2 and number_2 is not None:

            arr = [math.lcm(number_1, number_2) *
                   i for i in range(1, number_range + 1)]

            embed = nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n Common Multiple of {number_1} and {number_2}. \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {arr} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 3 and number_2 is not None:

            evalu = math.lcm(number_1, number_2)

            embed = nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n Lowest Common Multiple of {number_1} and {number_2}. \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {evalu} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

    # @ slash_command(
    #     description="Calculate your math's query.",
    #     guild_ids=[GUILD_ID]
    # )
    # async def calculate(self, interaction: Interaction, query: str):

    #     expliteral = ("").join(query)
    #     exppoet = expliteral.replace("*", "×").replace("/", "÷")
    #     evalu = eval(expliteral)

    #     embed = nextcord.Embed(
    #         title="Math Query",
    #         description="The requested `Math Query` have been evaluated by **Atom Query**",
    #         timestamp=nextcord.utils.format_dt(
    #             dt=datetime.now(timezone.utc), style="f"),
    #         colour=nextcord.Color.from_rgb(179, 27, 27)
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

    #     embed.set_thumbnail(url=self.link)

    #     await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Raise the base to the index.",
        guild_ids=[GUILD_ID]
    )
    async def index(self, interaction: Interaction, base: float = SlashOption(description="The base of the indices."), exponent: float = SlashOption(description="The number of times to multiply the base.")):

        exp = f"{base} ** {exponent}"
        evalu = base ** exponent

        embed = nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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

    @ slash_command(
        description="Factorise the radicand to the exponent.",
        guild_ids=[GUILD_ID]
    )
    async def radical(self, interaction: Interaction, radicand: float = SlashOption(description="The number to factor into the same base."), index: float = SlashOption(description="The index to factor the number.")):

        exp = f"{radicand} ** 1 / {index}"
        evalu = radicand ** (1. / index)

        embed = nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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

    @ slash_command(
        description="Find the number of time a number multiplied itself.",
        guild_ids=[GUILD_ID]
    )
    async def logarithm(self, interaction: Interaction, base: float = SlashOption(description="The base of the logarithm."), radicand: float = SlashOption(description="The number to find the index.")):

        exp = f"log{base} {radicand}"
        evalu = math.log(x=radicand, base=base)

        embed = nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


def setup(bot: commands.Bot):
    bot.add_cog(Query(bot))
