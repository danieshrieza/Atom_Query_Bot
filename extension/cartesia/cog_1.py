from nextcord import Interaction
import nextcord
from nextcord.ext import commands
import matplotlib.pyplot as plt
import numpy as np
from config import guild_id


# NOTE : Class for Plot 
class Plot(commands.Cog) :


    # NOTE : Initialize parameter for class 
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to plot linear graph 
    @ nextcord.slash_command(
        description = "Plot a linear graph using the equation y = mx + c."
    )

    async def linear_equation(self, ctx : Interaction, gradient : float, y_intercept : float) :

        x = np.linspace(-20, 20, 100)
        y = gradient * x + y_intercept

        file = nextcord.File("./image/linear.png")

        plt.plot(x, y, color = "green", label = f"y = {gradient}x + {y_intercept}")
        plt.title(f"Graph of y = {gradient}x + {y_intercept}") 

        plt.xlabel("x", color = "#1C2833")
        plt.ylabel("y", color = "#1C2833")

        plt.legend(loc = "upper left")
        plt.grid()

        plt.savefig("./image/linear.png")
        plt.close()

        await ctx.response.defer()
        message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        await ctx.channel.send(file = file)
        await message.delete()


    # NOTE : Command to plot quadratic graph 
    @ nextcord.slash_command(
        description = "Plot a quadratic graph using the equation y = ax² + bx + c."
    )

    async def quadratic_equation(self, ctx : Interaction, a : float, b : float, c : float) :

        x = np.linspace(-20, 20, 100)
        y = (a * x) ** 2 + (b * x) + c

        file = nextcord.File("./image/quad.png")
        plt.plot(x, y, color = "red", label = f"y = {a}x² + {b}x + {c}")
        plt.title(f'Graph of y = {a}x² + {b}x + {c}') 

        plt.xlabel("x", color = "#1C2833")
        plt.ylabel("y", color = "#1C2833")

        plt.legend(loc = "upper left")
        plt.grid()

        plt.savefig("./image/quad.png")
        plt.close()

        await ctx.response.defer()
        message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        await ctx.channel.send(file = file)
        await message.delete()


    # NOTE : Command to plot cubic graph 
    @ nextcord.slash_command(
        description = "Plot a cubic graph using the equation y = ax³ + bx² + cx + d."
    )

    async def cubic_equation(self, ctx : Interaction, a : float, b : float, c : float, d : float) :

        x = np.linspace(-20, 20, 100)
        y = (a * x) ** 3 + (b * x) ** 2 + (c * x) + d

        file = nextcord.File("./image/cube.png")

        plt.plot(x, y, color = "blue", label = f'y = {a}x³ + {b}x² + {c}x + {d}')
        plt.title(f"Graph of y = {a}x³ + {b}x² + {c}x + {d}") 

        plt.xlabel("x", color = "#1C2833")
        plt.ylabel("y", color = "#1C2833")

        plt.legend(loc = "upper left")
        plt.grid()

        plt.savefig("./image/cube.png")
        plt.close()

        await ctx.response.defer()
        message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        await ctx.channel.send(file = file)
        await message.delete()


    # NOTE : Command to plot reciprocal graph 
    @ nextcord.slash_command( 
        description = "Plot a reciprocal graph using the equation y = 1/x."
    )

    async def reciprocal_equation(self, ctx : Interaction, numerator : float, denominator : float) :

        x = np.linspace(-20, 20, 100)
        y = numerator / (denominator * x)

        file = nextcord.File("./image/reci.png")

        plt.plot(x, y, color = "yellow", label = f"y = {numerator}/{denominator}x")
        plt.title(f"y = {numerator}/{denominator}x")

        plt.xlabel("x", color = "#1C2833")
        plt.ylabel("y", color = "#1C2833")

        plt.legend(loc = "upper left")
        plt.grid()

        plt.savefig("./image/reci.png")
        plt.close()
        
        await ctx.response.defer()
        message = await ctx.channel.fetch_message(int(ctx.channel.last_message_id))

        await ctx.channel.send(file = file)
        await message.delete()      


# NOTE : Add Plot to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(Plot(bot))