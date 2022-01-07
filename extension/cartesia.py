import discord
from discord.ext import commands
from discord_slash import cog_ext
import matplotlib.pyplot as plt
from discord.ext.commands.context import Context
import numpy as np
import math
from datetime import datetime, timezone

# ! <--- Class for Cartesian_Query --->
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

    # ! <--- Initialize variable for class --->
    def __init__(self, bot) :
        
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ! <--- Command to plot linear graph --->
    @ cog_ext.cog_slash(description = "Plot a linear graph using the equation y = mx + c.")
    async def linear_function(self, ctx : Context, gradient : float, y_intercept : float) :

        x = np.linspace(-20, 20, 100)
        y = gradient * x + y_intercept
        file = discord.File("./image/linear.png", filename = './image/linear.png')

        plt.plot(x, y, color = 'green', label = f'y = {gradient}x + {y_intercept}')
        plt.title(f'Graph of y = {gradient}x + {y_intercept}') 
        plt.xlabel('x', color = '#1C2833')
        plt.ylabel('y', color = '#1C2833')
        plt.legend(loc = 'upper left')
        plt.grid()
        plt.savefig("./image/linear.png")
        plt.close()

        await ctx.send(file = file)

    # ! <--- Command to plot quadratic graph --->
    @ cog_ext.cog_slash(description = "Plot a quadratic graph using the equation y = ax² + bx + c.")
    async def quadratic_function(self, ctx : Context, a : float, b : float, c : float) :

        x = np.linspace(-20, 20, 100)
        y = (a * x) ** 2 + (b * x) + c
        file = discord.File("./image/quad.png", filename = './image/quad.png')

        plt.plot(x, y, color = "red", label = f'y = {a}x² + {b}x + {c}')
        plt.title(f'Graph of y = {a}x² + {b}x + {c}') 
        plt.xlabel('x', color = '#1C2833')
        plt.ylabel('y', color = '#1C2833')
        plt.legend(loc = 'upper left')
        plt.grid()
        plt.savefig("./image/quad.png")
        plt.close()

        await ctx.send(file = file)

    # ! <--- Command to plot cubic graph --->
    @ cog_ext.cog_slash(description = "Plot a cubic graph using the equation y = ax³ + bx² + cx + d.")
    async def cubic_function(self, ctx : Context, a : float, b : float, c : float, d : float) :

        x = np.linspace(-20, 20, 100)
        y = (a * x) ** 3 + (b * x) ** 2 + (c * x) + d
        file = discord.File("./image/cube.png", filename = './image/cube.png')

        plt.plot(x, y, color = "blue", label = f'y = {a}x³ + {b}x² + {c}x + {d}')
        plt.title(f'Graph of y = {a}x³ + {b}x² + {c}x + {d}') 
        plt.xlabel('x', color = '#1C2833')
        plt.ylabel('y', color = '#1C2833')
        plt.legend(loc = 'upper left')
        plt.grid()
        plt.savefig("./image/cube.png")
        plt.close()

        await ctx.send(file = file)

    # ! <--- Command to plot reciprocal graph --->
    @ cog_ext.cog_slash(description = "Plot a reciprocal graph using the equation y = 1/x.")
    async def reciprocal_function(self, ctx : Context, numerator : float, denominator : float) :

        x = np.linspace(-20, 20, 100)
        y = numerator / (denominator * x)
        file = discord.File("./image/reci.png", filename = './image/reci.png')

        plt.plot(x, y, color = "yellow", label = f'y = {numerator}/{denominator}x')
        plt.title(f'y = {numerator}/{denominator}x') 
        plt.xlabel('x', color = '#1C2833')
        plt.ylabel('y', color = '#1C2833')
        plt.legend(loc = 'upper left')
        plt.grid()
        plt.savefig("./image/reci.png")
        plt.close()
        
        await ctx.send(file = file)


    # ! <--- Command to calculate distance between two points on a Cartesian Plane --->
    @ cog_ext.cog_slash(description = "Calculate the distance between two points.")
    async def distance(self, ctx : Context, x_2 : float, x_1 : float, y_2 : float, y_1 : float) :

        exp = f"√({x_2} - {x_1})² + ({y_2} - {y_1})²"
        evalu = math.sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

        emby_ctx = discord.Embed(title = "Cartesian Query", description = "The requested `Cartesian Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(127, 0, 255))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu} A`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate gradient of a line --->
    @ cog_ext.cog_slash(description = "Calculate the gradient of a line.")
    async def gradient(self, ctx : Context, y_2 : float, y_1 : float, x_2 : float, x_1 : float) :

        exp = f"{y_2} - {y_1} ÷ {x_2} - {x_1}"
        evalu = (y_2 - y_1) / (x_2 - x_1)

        emby_ctx = discord.Embed(title = "Cartesian Query", description = "The requested `Cartesian Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(127, 0, 255))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu} A`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)

    # ! <--- Command to calculate the midpoint of two point --->
    @ cog_ext.cog_slash(description = "Calculate the midpoint of two point.")
    async def midpoint(self, ctx : Context, x_1 : float, x_2 : float, y_1 : float, y_2 : float) :

        exp = f"(({x_1} + {x_2}) ÷ 2, ({y_1} + {y_2}) ÷ 2)"
        evalu = ((x_1 + x_2) / 2, (y_1 + y_2) / 2)

        emby_ctx = discord.Embed(title = "Cartesian Query", description = "The requested `Cartesian Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = discord.Color.from_rgb(127, 0, 255))
        emby_ctx.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        emby_ctx.add_field(name = "Input :",value = f"`{exp}`", inline = False)
        emby_ctx.add_field(name = "Output :" , value = f"`{evalu} A`", inline = True)
        emby_ctx.set_thumbnail(url = self.link)

        await ctx.send(embed = emby_ctx)      

# ! <--- Add Cartesian_Query into the bot
def setup(bot) :
    bot.add_cog(Cartesian_Query(bot))