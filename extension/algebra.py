from discord import Interaction, app_commands
import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath
from typing import Optional
from config import GUILD_ID, _linear, IMAGE_LINK, _quadratic


class Algebra(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @ commands.Cog.listener()
    async def on_ready(self):
        await self.bot.tree.sync()
        print(f"{__name__} is succesfully loaded into bot.")

    @ app_commands.command(description="Calculate the distance, midpoint and gradient or plot a linear graph.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.describe(a1="The value of a from first equation.")
    @ app_commands.describe(b1="The value of b from first equation.")
    @ app_commands.describe(c1="The value of c from first equation.")
    @ app_commands.describe(a2="The value of a from second equation.")
    @ app_commands.describe(b2="The value of b from second equation.")
    @ app_commands.describe(c2="The value of c from second equation.")
    @ app_commands.describe(a3="The value of a from third equation.")
    @ app_commands.describe(b3="The value of b from third equation.")
    @ app_commands.describe(c3="The value of c from third equation.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _linear
    ])
    async def linear_equation(
            self,
            interaction: Interaction,
            type: app_commands.Choice[int],
            a1: float,
            b1: float,
            c1: float,
            d1: Optional[float],
            a2: Optional[float],
            b2: Optional[float],
            c2: Optional[float],
            d2: Optional[float],
            a3: Optional[float],
            b3: Optional[float],
            c3: Optional[float],
            d3: Optional[float]
    ):

        if type == 1 and (a1 and b1 and c1) is not None and (a2 and b2 and c2) is not None:
            left_hand_side = np.array([a1, b1], [a2, b2])
            right_hand_side = np.array([c1, c2])
            intersection = np.linalg.solve(left_hand_side, right_hand_side)

            embed = discord.Embed(
                title="Equation Solver",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(178, 34, 34)
            )

            embed.add_field(
                name="First equation :",
                value=f"```Python\n {a1}x + {b1}y = {c1} \n```",
                inline=False
            )

            embed.add_field(
                name="Second equation :",
                value=f"```Python\n {a2}x + {b2}y = {c2} \n```",
                inline=False
            )

            embed.add_field(
                name="Solution :",
                value=f"```Python\n {intersection} \n```",
                inline=False
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        if type == 2 and (a1 and b1 and c1 and d1) is not None and (a2 and b2 and c2 and d2) is not None and (a3 and b3 and c3 and d3) is not None:

            left_hand_side = np.array([a1, b1, c1], [a2, b2, c2], [a3, b3, c3])
            right_hand_side = np.array([d1, d2, d3])
            intersection = np.linalg.solve(left_hand_side, right_hand_side)

            embed = discord.Embed(
                title="Equation Solver",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(178, 34, 34)
            )

            embed.add_field(
                name="First equation :",
                value=f"```Python\n {a1}x + {b1}y + {c1}z = {d1} \n```",
                inline=False
            )

            embed.add_field(
                name="Second equation :",
                value=f"```Python\n {a2}x + {b2}y + {c2}z = {d2} \n```",
                inline=False
            )

            embed.add_field(
                name="Third equation :",
                value=f"```Python\n {a3}x + {b3}y + {c3}z = {d3} \n```",
                inline=False
            )

            embed.add_field(
                name="Solution :",
                value=f"```Python\n {intersection} \n```",
                inline=False
            )

            embed.set_thumbnail(url=IMAGE_LINK)

            await interaction.response.send_message(embed=embed)

        elif type == 3 and (a1 and b1 and c1) is not None:

            x = np.linspace(-20, 20, 100)
            m = -a1 / b1
            c = -c1 / b1
            y = m*x + c

            file = discord.File("./image/linear.png")

            plt.plot(x, y, color="green", label=f"y = {m}x + {c}")
            plt.title(f"Graph of y = {m}x + {c}")

            plt.xlabel("x", color="#1C2833")
            plt.ylabel("y", color="#1C2833")

            plt.legend(loc="upper left")
            plt.grid()

            plt.savefig("./image/linear.png")
            plt.close()

            await interaction.response.send_message(file=file)

    @ app_commands.command(description="Plot a quadratic graph.")
    @ app_commands.describe(a="The width of the parabola.")
    @ app_commands.describe(b="The position of axis of symmetry of the parabola.")
    @ app_commands.describe(c="The y-intercept of the parabola.")
    @ app_commands.describe(type="The type of calculation to be evaluated.")
    @ app_commands.choices(type=[
        app_commands.Choice(name=operation, value=choice) for operation, choice in _quadratic
    ])
    async def quadratic_equation(
        self,
        interaction: Interaction,
        a: float,
        b: float,
        c: float,
        type: app_commands.Choice[int]
    ):

        if type == 1:

            embed = discord.Embed(
                title="Equation Solver",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(127, 0, 255)
            )

            try:

                root1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / 2*a
                root2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / 2 * a

                embed.add_field(
                    name="Equation :",
                    value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                    inline=False
                )

                embed.add_field(
                    name="Roots :",
                    value=f"```Python\n x = {root1} or x = {root2} \n```",
                    inline=True
                )

                await interaction.response.send_message(embed=embed)

            except ValueError:

                root1 = (-b + cmath.sqrt((b ** 2) - (4 * a * c))) / 2*a
                root2 = (-b - cmath.sqrt((b ** 2) - (4 * a * c))) / 2*a

                embed.add_field(
                    name="Equation :",
                    value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                    inline=False
                )

                embed.add_field(
                    name="Roots :",
                    value=f"```Python\n x = {root1} or x = {root2} \n```",
                    inline=True
                )

                await interaction.response.send_message(embed=embed)

        elif type == 2:

            h = -b / (2 * a)
            k = (a * h ** 2) + (b * h) + c

            embed = discord.Embed(
                title="Equation Solver",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(127, 0, 255)
            )

            embed.add_field(
                name="Input :",
                value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n y = {a}(x - {h})² + {k} \n```",
                inline=True
            )

            await interaction.response.send_message(embed=embed)

        elif type == 3:

            embed = discord.Embed(
                title="Equation Solver",
                description="Query has been **successfully** evaluated.",
                timestamp=discord.utils.utcnow(),
                colour=discord.Color.from_rgb(127, 0, 255)
            )

            try:

                p = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                q = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

                if p == q:

                    embed.add_field(
                        name="Equation :",
                        value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Rewritten equation :",
                        value=f"```Python\n y = {a}(x - {p})² \n```",
                        inline=True
                    )

                    await interaction.response.send_message(embed=embed)

                else:

                    embed.add_field(
                        name="Equation :",
                        value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Rewritten equation :",
                        value=f"```Python\n y = {a}(x - {p})(x - {q}) \n```",
                        inline=True
                    )

                    await interaction.response.send_message(embed=embed)

            except ValueError:

                p = (-b + cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                q = (-b - cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

                embed.add_field(
                    name="Equation :",
                    value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                    inline=False
                )

                embed.add_field(
                    name="Rewritten equation :",
                    value=f"```Python\n y = {a}(x - {p})(x - {q}) \n```",
                    inline=True
                )

                await interaction.response.send_message(embed=embed)

        elif type == 4:

            x = np.linspace(-20, 20, 100)
            y = a*x**2 + b*x + c

            file = discord.File("./image/linear.png")

            plt.plot(x, y, color="green", label=f"y = {a}x² + {b}x + {c}")
            plt.title(f"Graph of y = {a}x² + {b}x + {c}")

            plt.xlabel("x", color="#1C2833")
            plt.ylabel("y", color="#1C2833")

            plt.legend(loc="upper left")
            plt.grid()

            plt.savefig("./image/quadratic.png")
            plt.close()

            await interaction.response.send_message(file=file)


async def setup(bot: commands.Bot):
    await bot.add_cog(Algebra(bot))
