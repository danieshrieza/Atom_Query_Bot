from nextcord import Interaction, slash_command
import nextcord
from nextcord.ext import commands
import matplotlib.pyplot as plt
import numpy as np
import math
from datetime import datetime, timezone


# NOTE : Class for Plot
class Plot(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate distance between two points on a Cartesian Plane
    @ slash_command(
        description="Calculate the distance between two points."
    )
    async def distance_between_two_points(self, interaction: Interaction, x_2: float, x_1: float, y_2: float, y_1: float):

        exp=f"√({x_2} - {x_1})² + ({y_2} - {y_1})²"
        evalu=math.sqrt((x_2-x_1)**2+(y_2-y_1)**2)

        embed=nextcord.Embed(
            title="Cartesian Query",
            description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
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


    # NOTE : Command to calculate gradient of a line
    @ slash_command(
        description="Calculate the gradient of a line."
    )
    async def gradient_of_a_line(self, interaction: Interaction, y_2: float, y_1: float, x_2: float, x_1: float):

        exp=f"{y_2} - {y_1} ÷ {x_2} - {x_1}"
        evalu=(y_2-y_1)/(x_2-x_1)

        embed=nextcord.Embed(
            title="Cartesian Query",
            description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
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


    # NOTE : Command to calculate the midpoint of a line
    @ slash_command(
        description="Calculate the midpoint of a line."
    )
    async def midpoint_of_a_line(self, interaction: Interaction, x_1: float, x_2: float, y_1: float, y_2: float):

        exp=f"(({x_1} + {x_2}) ÷ 2, ({y_1} + {y_2}) ÷ 2)"
        evalu=((x_1+x_2)/2, (y_1 + y_2)/2)

        embed=nextcord.Embed(
            title="Cartesian Query",
            description="The requested `Cartesian Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
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


    # NOTE : Command to plot linear graph
    @ slash_command(
        description="Plot a linear graph."
    )
    async def linear_equation(self, interaction: Interaction, gradient: float, y_intercept: float):

        x=np.linspace(-20, 20, 100)
        y=gradient*x+y_intercept

        file=nextcord.File("./image/linear.png")

        plt.plot(x, y, color="green", label=f"y = {gradient}x + {y_intercept}")
        plt.title(f"Graph of y = {gradient}x + {y_intercept}")

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/linear.png")
        plt.close()

        # await interaction.response.defer()
        # message = await interaction.channel.fetch_message(int(interaction.channel.last_message_id))

        # await interaction.channel.send(file = file)
        # await message.delete()

        await interaction.response.send_message(file=file)


    # NOTE : Command to plot quadratic graph
    @ slash_command(
        description="Plot a quadratic graph."
    )
    async def quadratic_equation(self, interaction: Interaction, a: float, b: float, c: float):

        x=np.linspace(-20, 20, 100)
        y=(a*x)**2+(b*x)+c

        file=nextcord.File("./image/quad.png")
        
        plt.plot(x, y, color="red", label=f"y = {a}x² + {b}x + {c}")
        plt.title(f'Graph of y = {a}x² + {b}x + {c}')

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/quad.png")
        plt.close()

        # await interaction.response.defer()
        # message = await interaction.channel.fetch_message(int(interaction.channel.last_message_id))

        # await interaction.channel.send(file=file)
        # await message.delete()

        await interaction.response.send_message(file=file)


    # NOTE : Command to plot cubic graph
    @ slash_command(
        description="Plot a cubic graph."
    )
    async def cubic_equation(self, interaction: Interaction, a: float, b: float, c: float, d: float):

        x=np.linspace(-20, 20, 100)
        y=(a*x)**3+(b*x)**2+(c*x)+d

        file=nextcord.File("./image/cube.png")

        plt.plot(x, y, color="blue", label=f'y = {a}x³ + {b}x² + {c}x + {d}')
        plt.title(f"Graph of y = {a}x³ + {b}x² + {c}x + {d}")

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/cube.png")
        plt.close()

        # await interaction.response.defer()
        # message = await interaction.channel.fetch_message(int(interaction.channel.last_message_id))

        # await interaction.channel.send(file=file)
        # await message.delete()
        
        await interaction.response.send_message(file=file)


    # NOTE : Command to plot reciprocal graph
    @ slash_command(
        description="Plot a reciprocal graph."
    )
    async def reciprocal_equation(self, interaction: Interaction, numerator: float, denominator: float):

        x=np.linspace(-20, 20, 100)
        y=numerator/(denominator*x)

        file=nextcord.File("./image/reci.png")

        plt.plot(x, y, color="yellow", label=f"y = {numerator}/{denominator}x")
        plt.title(f"y = {numerator}/{denominator}x")

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/reci.png")
        plt.close()

        # await interaction.response.defer()
        # message = await interaction.channel.fetch_message(int(interaction.channel.last_message_id))

        # await interaction.channel.send(file=file)
        # await message.delete()
        
        await interaction.response.send_message(file=file)


# NOTE : Add Plot to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Plot(bot))
