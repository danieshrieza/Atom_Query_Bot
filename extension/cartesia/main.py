from discord import Interaction, app_commands
import discord
from discord.ext import commands
import matplotlib.pyplot as plt
import numpy as np


# NOTE : Class for Plot
class Plot(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to plot linear graph
    @ app_commands.command(
        description="Plot a linear graph."
    )
    async def linear_equation(self, ctx: Interaction, gradient: float, y_intercept: float):

        x = np.linspace(-20, 20, 100)
        y = gradient*x+y_intercept

        file = discord.File("./image/linear.png")

        plt.plot(x, y, color="green", label=f"y = {gradient}x + {y_intercept}")
        plt.title(f"Graph of y = {gradient}x + {y_intercept}")

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/linear.png")
        plt.close()

        # await ctx.response.defer()
        # message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        # await ctx.channel.send(file = file)
        # await message.delete()

        await ctx.response.send_message(file=file)


    # NOTE : Command to plot quadratic graph
    @ app_commands.command(
        description="Plot a quadratic graph."
    )
    async def quadratic_equation(self, ctx: Interaction, a: float, b: float, c: float):

        x = np.linspace(-20, 20, 100)
        y = (a*x)**2+(b*x)+c

        file = discord.File("./image/quad.png")
        plt.plot(x, y, color="red", label=f"y = {a}x² + {b}x + {c}")
        plt.title(f'Graph of y = {a}x² + {b}x + {c}')

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/quad.png")
        plt.close()

        # await ctx.response.defer()
        # message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        # await ctx.channel.send(file=file)
        # await message.delete()

        await ctx.response.send_message(file=file)


    # NOTE : Command to plot cubic graph
    @ app_commands.command(
        description="Plot a cubic graph."
    )
    async def cubic_equation(self, ctx: Interaction, a: float, b: float, c: float, d: float):

        x = np.linspace(-20, 20, 100)
        y = (a*x)**3+(b*x)**2+(c*x)+d

        file = discord.File("./image/cube.png")

        plt.plot(x, y, color="blue", label=f'y = {a}x³ + {b}x² + {c}x + {d}')
        plt.title(f"Graph of y = {a}x³ + {b}x² + {c}x + {d}")

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/cube.png")
        plt.close()

        # await ctx.response.defer()
        # message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        # await ctx.channel.send(file=file)
        # await message.delete()
        
        await ctx.response.send_message(file=file)


    # NOTE : Command to plot reciprocal graph
    @ app_commands.command(
        description="Plot a reciprocal graph."
    )
    async def reciprocal_equation(self, ctx: Interaction, numerator: float, denominator: float):

        x = np.linspace(-20, 20, 100)
        y = numerator/(denominator*x)

        file = discord.File("./image/reci.png")

        plt.plot(x, y, color="yellow", label=f"y = {numerator}/{denominator}x")
        plt.title(f"y = {numerator}/{denominator}x")

        plt.xlabel("x", color="#1C2833")
        plt.ylabel("y", color="#1C2833")

        plt.legend(loc="upper left")
        plt.grid()

        plt.savefig("./image/reci.png")
        plt.close()

        # await ctx.response.defer()
        # message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        # await ctx.channel.send(file=file)
        # await message.delete()
        
        await ctx.response.send_message(file=file)


# NOTE : Add Plot to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Plot(bot))
