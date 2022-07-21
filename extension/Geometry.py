from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, slash_command
from config import (_curve, _four_side, _tri, _cylinder, _cone, GUILD_ID)
from math import pi


class Geometry(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    @ slash_command(
        description="Calculate the circumference, and area of a circle or the surface area, and volume of a sphere.",
        guild_ids=[GUILD_ID]
    )
    async def circleandsphere(self, interaction: Interaction, r: float = SlashOption(description="The radius of the circle or the sphere."), type: str = SlashOption(description="The type of calculation to be evaluated.", required=True, choices=_curve)):

        if type == 1:

            formula = "C = 2πr"
            C = 2 * pi * r

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {C} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "A = πr²"
            A = pi * r ** 2

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 3:

            formula = "A = 4πr²"
            A = 4 * pi * r ** 2

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 4:

            formula = "V = 4/3πr³"
            V = 4/3 * pi * r ** 3

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {V} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the area of a square or the surface area, and volume of a cube.",
        guild_ids=[GUILD_ID]
    )
    async def squareandcube(self, interaction: Interaction, l: float = SlashOption(description="The length of the square or the cube."), type: str = SlashOption(description="The type of calculation to be evaluated.", required=True, choices=_four_side)):

        if type == 1:

            formula = "A = l²"
            A = l ** 2

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "A = 6(l²)"
            A = 6 * (l ** 2)

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 3:

            formula = "V = l³"
            V = l ** 3

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {V} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the area of a parallelogram.",
        guild_ids=[GUILD_ID]
    )
    async def areaofparallelogram(self, interaction: Interaction, b: float = SlashOption(description="The base length of the parallogram."), h: float = SlashOption(description="The height of the parallogram.")):

        formula = "A = bh"
        A = b * h

        embed = nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated ",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {A} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the area of a kite.",
        guild_ids=[GUILD_ID]
    )
    async def areaofkite(self, interaction: Interaction, p: float = SlashOption(description="The length of the horizontal side."), q: float = SlashOption(description="The length of the vertical length.")):

        formula = "A = pq / 2"
        A = (p * q) / 2

        embed = nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated ",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {A} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the area of a trampezium.",
        guild_ids=[GUILD_ID]
    )
    async def areaoftrampezium(self, interaction: Interaction, a: float = SlashOption(description="The length of the first parallel side."), b: float = SlashOption(description="The length of the second parallel side."), h: float = SlashOption(description="The height of the trampezium.")):

        formula = "A = (a + b)h / 2"
        A = (a + b) * h / 2

        embed = nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated ",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {A} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the area of triangle or the surface area, and the volume of a pyramid.",
        guild_ids=[GUILD_ID]
    )
    async def triangleandpyramid(self, interaction: Interaction, l: float = SlashOption(description="The length of the triangle or the pyramid."), w: float = SlashOption(description="The width of the triangle or the pyramid."), s: float = SlashOption(description="The slant height of the triangle face on the pyramid.", default=None, required=False), h: float = SlashOption(description="The height of the pyramid.", default=None, required=False), type: str = SlashOption(description="The type of calculation to be evaluated.", required=True, choices=_tri)):

        if type == 1:

            formula = "A = lw / 2"
            A = (l * w) / 2

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2 and s != None:

            formula = "A = 4lw + sl + sw"
            A = (4 * (l * w)) + (s * l) + (s * w)

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 3 and h != None:

            formula = "V = lwh / 3"
            V = (l * w * h) / 3

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {V} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the surface area, and the volume of a cylinder.",
        guild_ids=[GUILD_ID]
    )
    async def cylinder(self, interaction: Interaction, h: float = SlashOption(description="The height of the cylinder."), r: float = SlashOption(description="The radius of the cylinder."), type: str = SlashOption(description="The type of calculation to be evaluated.", required=True, choices=_cylinder)):

        if type == 1:

            formula = "A = 2πr² + 2πrh"
            A = (2 * pi * r ** 2) + (2 * pi * r * h)

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "V = πr²h"
            V = pi * r ** 2 * h

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {V} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the surface area, and volume of a cone.",
        guild_ids=[GUILD_ID]
    )
    async def cone(self, interaction: Interaction, r: float = SlashOption(description="The radius of the cone."), s: float = SlashOption(description="The slant height of the cone.", default=None, required=False), h: float = SlashOption(description="The height of the cone.", default=None, required=False), type: str = SlashOption(name="The type of calculation to be evaluated.", required=True, choices=_cone)):

        if type == 1 and s != None:

            formula = "A = πr² + πrs"
            A = (pi * r ** 2) + (pi * r * s)

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {A} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2 and h != None:

            formula = f"V = πr²h / 3"
            V = (pi * r ** 2 * h) / 3

            embed = nextcord.Embed(
                title="Geometry Query",
                description="The requested `Geometry Query` have been evaluated ",
                timestamp=nextcord.utils.format_dt(
                    dt=datetime.now(timezone.utc), style="f"),
                colour=nextcord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {V} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Geometry(bot))
