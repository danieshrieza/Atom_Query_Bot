
import discord
from discord.ext import commands
from discord import Interaction, app_commands
from config import (_circle, _square, _cube, _triangle,
                    _cylinder, _cone, _sphere, _pyramid, GUILD_ID, IMAGE_LINK)
from typing import Optional
from math import pi


class Geometry(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @ commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} is succesfully loaded into bot.")

    @ app_commands.command(description="Calculate the circumference of a circle or the area of a circle.")
    @ app_commands.describe(r="The radius of the circle.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _circle
    ])
    async def circle(
        self,
        interaction: Interaction,
        r: float,
        type: app_commands.Choice[int]
    ):

        if type == 1:

            formula = "C = 2πr"
            C = 2*pi*r

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "A = πr²"
            A = pi*r**2

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the surface area of a sphere or the volume of a sphere.")
    @ app_commands.describe(r="The radius of the sphere.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _circle
    ])
    async def sphere(
        self,
        interaction: Interaction,
        r: float,
        type: app_commands.Choice[int]
    ):

        if type == 1:

            formula = "A = 4πr²"
            A = 4*pi*r**2

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "V = 4/3πr³"
            V = (4/3)*pi*r**3

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the perimeter of a square or the area of a square.")
    @ app_commands.describe(l="The length of the square.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _square
    ])
    async def square(
        self,
        interaction: Interaction,
        l: float,
        type: app_commands.Choice[int]
    ):

        if type == 1:

            formula = "P = 4l"
            P = 4*l

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n {formula} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {P} \n```",
                inline=True
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "A = l²"
            A = l**2

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the surface area of a cube or the volume of a cube.")
    @ app_commands.describe(l="The length of the cube.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _cube
    ])
    async def cube(
        self,
        interaction: Interaction,
        l: float,
        type: app_commands.Choice[int]
    ):

        if type == 1:

            formula = "A = 6(l²)"
            A = 6*l**2

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "V = l³"
            V = l**3

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the area of a parallelogram.")
    @ app_commands.describe(b="The base length of the parallogram.")
    @ app_commands.describe(h="The height of the parallogram.")
    async def parallelogram(
        self,
        interaction: Interaction,
        b: float,
        h: float
    ):

        formula = "A = bh"
        A = b*h

        embed = discord.Embed(
            title="Geometry Query",
            description="Query has been **successfully** evaluated.",
            timestamp=discord.utils.utcnow(),
            colour=discord.Color.from_rgb(157, 34, 53)
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

        embed.set_thumbnail(url=IMAGE_LINK)

        await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the area of a kite.")
    @ app_commands.describe(p="The length of the horizontal side.")
    @ app_commands.describe(q="The length of the vertical length.")
    async def kite(
        self,
        interaction: Interaction,
        p: float,
        q: float
    ):

        formula = "A = pq / 2"
        A = (p*q) / 2

        embed = discord.Embed(
            title="Geometry Query",
            description="Query has been **successfully** evaluated.",
            timestamp=discord.utils.utcnow(),
            colour=discord.Color.from_rgb(157, 34, 53)
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

        embed.set_thumbnail(url=IMAGE_LINK)

        await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the area of a trapezium.")
    @ app_commands.describe(a="The length of the first parallel side.")
    @ app_commands.describe(b="The length of the second parallel side.")
    @ app_commands.describe(h="The height of the trapezium.")
    async def trapezium(
        self,
        interaction: Interaction,
        a: float,
        b: float,
        h: float
    ):

        formula = "A = (a + b)h / 2"
        A = (a+b)*h / 2

        embed = discord.Embed(
            title="Geometry Query",
            description="Query has been **successfully** evaluated.",
            timestamp=discord.utils.utcnow(),
            colour=discord.Color.from_rgb(157, 34, 53)
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

        embed.set_thumbnail(url=IMAGE_LINK)

        await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the perimeter of a triangle or the area of a triangle.")
    @ app_commands.describe(l="The length of the triangle.")
    @ app_commands.describe(w="The width of the triangle.")
    @ app_commands.describe(s1="The length of the first slant of the triangle.")
    @ app_commands.describe(s2="The length of the second slant of the triangle.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _triangle
    ])
    async def triangle(
        self,
        interaction: Interaction,
        l: float,
        w: Optional[float],
        s1: Optional[float],
        s2: Optional[float],
        type: app_commands.Choice[int],
    ):

        if type == 1 and s1 is not None and s2 is not None and w is None:

            formula = "P = l + s1 + s2"
            P = l + s1 + s2

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2 and s1 is None and s2 is None and w is not None:

            formula = "A = lw / 2"
            A = (l*w) / 2

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the surface area of a pyramid or the volume of a pyramid.")
    @ app_commands.describe(l="The length of the pyramid.")
    @ app_commands.describe(w="The width of the pyramid.")
    @ app_commands.describe(h="The height of the pyramid.")
    @ app_commands.describe(s="The slant height of the triangular face of the pyramid.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _pyramid
    ])
    async def pyramid(
        self,
        interaction: Interaction,
        l: float,
        w: float,
        s: Optional[float],
        h: Optional[float],
        type: app_commands.Choice[int],
    ):

        if type == 1 and s is not None and w is not None and h is None:

            formula = "A = lw + ls + ws"
            A = l*w + l*s + w*s

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2 and s is None and h is not None and w is not None:

            formula = "V = 1/3lwh"
            V = (1/3)*l*w*h

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the surface area of a cylinder and the volume of a cylinder.")
    @ app_commands.describe(h="The height of the cylinder.")
    @ app_commands.describe(r="The radius of the cylinder.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _cylinder
    ])
    async def cylinder(
        self,
        interaction: Interaction,
        h: float,
        r: float,
        type: app_commands.Choice[int]
    ):

        if type == 1:

            formula = "A = 2πr² + 2πrh"
            A = (2*pi*r**2) + (2*pi*r*h)

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            formula = "V = πr²h"
            V = pi*r**2*h

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

    @ app_commands.command(description="Calculate the surface area of a cone and a volume of a cone.")
    @ app_commands.describe(r="The radius of the cone.")
    @ app_commands.describe(s="The slant height of the cone.")
    @ app_commands.describe(h="The height of the cone.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _cone
    ])
    async def cone(
        self,
        interaction: Interaction,
        r: float,
        s: Optional[float],
        h: Optional[float],
        type: app_commands.Choice[int]
    ):

        if type == 1 and s is not None and h is None:

            formula = "A = πr² + πrs"
            A = (pi*r**2) + (pi*r*s)

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 2 and h is not None and s is None:

            formula = f"V = πr²h / 3"
            V = (pi*r**2*h) / 3

            embed = discord.Embed(
                title="Geometry Query",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(157, 34, 53)
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

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot):
    await bot.add_cog(Geometry(bot))
