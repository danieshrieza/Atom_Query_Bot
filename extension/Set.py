from nextcord import Interaction, SlashOption, slash_command
import nextcord
from nextcord.ext import commands
import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

from config import _linearOperation, _setOperation, _quadOperation, GUILD_ID


class Set(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    @ slash_command(
        description="Calculate the distance, midpoint and gradient or plot a linear graph.",
        guild_ids=[GUILD_ID]
    )
    async def linearequation(
        self,
        interaction: Interaction,
        type: int = SlashOption(
            description="The type of calculation to be evaluated.", required=True, choices=_linearOperation),
        m: float = SlashOption(
            description="The gradient of the line.", required=False, default=None),
        c: float = SlashOption(
            description="The y-intercept of the line.", required=False, default=None),
        y_2: float = SlashOption(
            description="The y-coordinate of the second point.", required=False, default=None),
        y_1: float = SlashOption(
            description="The y-coordinate of the first point.", required=False, default=None),
        x_2: float = SlashOption(
            description="The x-coordinate of the second point.", required=False, default=None),
        x_1: float = SlashOption(
            description="The x-coordinate of the first point.", required=False, default=None),
    ):

        if type == 1 and (m and c) is not None:

            x = np.linspace(-20, 20, 100)
            y = m * x + c

            file = nextcord.File("./image/linear.png")

            plt.plot(x, y, color="green", label=f"y = {m}x + {c}")
            plt.title(f"Graph of y = {m}x + {c}")

            plt.xlabel("x", color="#1C2833")
            plt.ylabel("y", color="#1C2833")

            plt.legend(loc="upper left")
            plt.grid()

            plt.savefig("./image/linear.png")
            plt.close()

            await interaction.response.send_message(file=file)

        elif type == 2 and (x_2 and x_1 and y_2 and y_1) is not None:

            formula = "√(x_2 - x_1)² + (y_2 - y_1)²"
            evalu = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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

        elif type == 3 and (x_2 and x_1 and y_2 and y_1) is not None:

            formula = "(x_1 + x_2 / 2, y_1 + y_2 / 2)"
            evalu = ((x_1 + x_2) / 2, (y_1 + y_2) / 2)

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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

        elif type == 4 and (x_2 and x_1 and y_2 and y_1) is not None:

            formula = "(y_2 - y_1) / (x_2 - x_ 1)"
            evalu = (y_2 - y_1) / (x_2 - x_1)

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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
        description="Plot a quadratic graph.",
        guild_ids=[GUILD_ID]
    )
    async def quadraticequation(
        self,
        interaction: Interaction,
        a: float = SlashOption(
            description="The width of the parabola.", required=True),
        b: float = SlashOption(
            description="The position of axis of symmetry of the parabola.", required=True),
        c: float = SlashOption(
            description="The y-intercept of the parabola.", required=True),
        type: int = SlashOption(
            description="The type of calculation to be evaluated.", required=True, choices=_quadOperation)
    ):

        if type == 1:

            x = np.linspace(-20, 20, 100)
            y = (a * x ** 2) + (b * x) + c

            file = nextcord.File("./image/quad.png")

            plt.plot(x, y, color="red", label=f"y = {a}x² + {b}x + {c}")
            plt.title(f'Graph of y = {a}x² + {b}x + {c}')

            plt.xlabel("x", color="#1C2833")
            plt.ylabel("y", color="#1C2833")

            plt.legend(loc="upper left")
            plt.grid()

            plt.savefig("./image/quad.png")
            plt.close()

            await interaction.response.send_message(file=file)

        elif type == 2:

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
            )

            try:

                root1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / 2*a
                root2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / 2 * a

                if root1 == root2:

                    embed.add_field(
                        name="Input :",
                        value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Nature of roots :",
                        value=f"```Python\n Two equal real roots \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Roots : ",
                        value=f"```Python\n {root1} \n```",
                        inline=True
                    )

                    await interaction.response.send_message(embed=embed)

                else:

                    embed.add_field(
                        name="Input :",
                        value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Nature of roots :",
                        value=f"```Python\n Two distinct real roots \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Roots :",
                        value=f"```Python\n {root1} and {root2} \n```",
                        inline=True
                    )

                    await interaction.response.send_message(embed=embed)

            except ValueError:

                root1 = (-b + cmath.sqrt((b ** 2) - (4 * a * c))) / 2*a
                root2 = (-b - cmath.sqrt((b ** 2) - (4 * a * c))) / 2*a

                embed.add_field(
                    name="Input :",
                    value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                    inline=False
                )

                embed.add_field(
                    name="Nature of roots :",
                    value=f"```Python\n Imaginary roots \n```",
                    inline=False
                )

                embed.add_field(
                    name="Roots :",
                    value=f"```Python\n {root1} and {root2} \n```",
                    inline=True
                )

                await interaction.response.send_message(embed=embed)

        elif type == 3:

            SOR = -(b / a)
            POR = c / a

            embed.add_field(
                name="Input :",
                value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                inline=False
            )

            embed.add_field(
                name="Sum of roots :",
                value=f"```Python\n {SOR} \n```",
                inline=False
            )

            embed.add_field(
                name="Product of roots :",
                value=f"```Python\n {POR} \n```",
                inline=False
            )

            embed.add_field(
                name="New quadratic equation :",
                value=f"```Python\n y = x² - {SOR}x + {POR} \n```",
                inline=True
            )

            await interaction.response.send_message(embed=embed)

        elif type == 4:

            h = -b / (2 * a)
            k = (a * h ** 2) + (b * h) + c

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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

        elif type == 5:

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
            )

            try:

                p = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                q = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

                if p == q:

                    embed.add_field(
                        name="Input :",
                        value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Output :",
                        value=f"```Python\n y = {a}(x - {p})² \n```",
                        inline=True
                    )

                    await interaction.response.send_message(embed=embed)

                else:

                    embed.add_field(
                        name="Input :",
                        value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                        inline=False
                    )

                    embed.add_field(
                        name="Output :",
                        value=f"```Python\n y = {a}(x - {p})(x - {q}) \n```",
                        inline=True
                    )

                    await interaction.response.send_message(embed=embed)

            except ValueError:

                p = (-b + cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
                q = (-b - cmath.sqrt((b ** 2) - (4 * a * c))) / (2 * a)

                embed.add_field(
                    name="Input :",
                    value=f"```Python\n y = {a}x² + {b}x + {c} \n```",
                    inline=False
                )

                embed.add_field(
                    name="Ouput",
                    value=f"```Python\n y = {a}(x - {p})(x - {q}) \n```",
                    inline=True
                )

                await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Check if a value is subset or an element of a set",
        guild_ids=[GUILD_ID]
    )
    async def setoperation(
        self, interaction: Interaction,
        a: str = SlashOption(
            description="The first set. (Smaller than B)", required=True),
        b: str = SlashOption(
            description="The second set.", required=True),
        type: int = SlashOption(
            description="The type of calculation to be evaluated.", required=True, choices=_setOperation)
    ):

        A = "".join(a).split(" ")
        B = "".join(b).split(" ")

        if type == 1:

            _truth = [True for i in A if i in B]

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 2:

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 3:

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        elif type == 4:

            embed = nextcord.Embed(
                title="Cartesian Query",
                description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
                timestamp=nextcord.utils.utcnow(),
                colour=nextcord.Color.from_rgb(127, 0, 255)
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

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Set(bot))
