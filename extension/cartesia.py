import discord
from discord.ext import commands
from discord_slash import cog_ext
import matplotlib.pyplot as plt
from discord.ext.commands.context import Context
import numpy as np

# ! <--- Class for Cartesian_Query
class Cartesian_Query(commands.Cog) :

    """
    Cartesian_Query is a class that contains coordinate geometry related commands.

    Commands :
    -----------

    linear_function : return `image` embed

    quadratic_function : return `image` embed

    cubic_function : return `image` embed

    reciprocal_function : return `image` embed
    """

    # ? <--- Initialize variable for class
    def __init__(self, bot) :
        
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ? <--- Command to plot linear graph
    @ cog_ext.cog_slash(description = "Plot a linear graph using the equation y = mx + c.")
    async def linear_function(self, ctx : Context, gradient : int, y_intercept : int) :

        x = np.linspace(-20, 20, 100)
        y = gradient * x + y_intercept
        file = discord.File("./image/linear.png", filename = './image/linear.png')

        plt.plot(x, y, '-r', label = f'y = {gradient}x + {y_intercept}')
        plt.title(f'Graph of y = {gradient}x + {y_intercept}') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/linear.png")
        plt.close()

        await ctx.send(file = file)

    # ? <--- Command to plot quadratic graph
    @ cog_ext.cog_slash(description = "Plot a quadratic graph using the equation y = ax² + bx + c.")
    async def quadratic_function(self, ctx : Context, a : int, b : int, c : int) :

        x = np.linspace(-20, 20, 100)
        y = (a * x) ** 2 + (b * x) + c
        file = discord.File("./image/quad.png", filename = './image/quad.png')

        plt.plot(x, y, '-r', label = f'y = {a}x² + {b}x + {c}')
        plt.title(f'Graph of y = {a}x² + {b}x + {c}') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/quad.png")
        plt.close()

        await ctx.send(file = file)

    # ? <--- Command to plot cubic graph
    @ cog_ext.cog_slash(description = "Plot a cubic graph using the equation y = ax³ + bx² + cx + d.")
    async def cubic_function(self, ctx : Context, a : int, b : int, c : int, d : int) :

        x = np.linspace(-20, 20, 100)
        y = (a * x) ** 3 + (b * x) ** 2 + (c * x) + d
        file = discord.File("./image/cube.png", filename = './image/cube.png')

        plt.plot(x, y, '-r', label = f'y = {a}x³ + {b}x² + {c}x + {d}')
        plt.title(f'Graph of y = {a}x³ + {b}x² + {c}x + {d}') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/cube.png")
        plt.close()

        await ctx.send(file = file)

    # ? <--- Command to plot reciprocal graph
    @ cog_ext.cog_slash(description = "Plot a reciprocal graph using the equation y = 1/x.")
    async def reciprocal_function(self, ctx) :

        x = np.linspace(-20, 20, 100)
        y = 1/x
        file = discord.File("./image/reci.png", filename = './image/reci.png')

        plt.plot(x, y, '-r', label = f'y = 1/x')
        plt.title(f'Graph of y = 1/x') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/reci.png")
        plt.close()
        
        await ctx.send(file = file)

# ! <--- Add Cartesian_Query into the bot
def setup(bot) :
    bot.add_cog(Cartesian_Query(bot))