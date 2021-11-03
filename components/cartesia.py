import discord
from discord.ext import commands
from discord_slash import cog_ext
import matplotlib.pyplot as plt
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
    def __init__(self, client) :
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

    # ? <--- Command to plot linear graph
    @ cog_ext.cog_slash(description = "Plot a linear graph using the equation y = mx + c.")
    async def linear_function(self, ctx, gradient : int, y_intercept : int) :
        self.embed = discord.Embed(title = "Cartesian Query", colour = discord.Color.from_rgb(255,0,255))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        x = np.linspace(-5,5,100)
        y = gradient * x + y_intercept
        plt.plot(x, y, '-r', label = f'y = {gradient}x + {y_intercept}')
        plt.title(f'Graph of y = {gradient}x + {y_intercept}') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/linear.png")
        plt.close()
        self.embed.set_image(url = "https://replit.com/@DanieshNoor/testbot#image/linear.png")
        await ctx.send(embed = self.embed)

    # ? <--- Command to plot quadratic graph
    @ cog_ext.cog_slash(description = "Plot a quadratic graph using the equation y = ax² + bx + c.")
    async def quadratic_function(self, ctx, a : int, b : int, c : int) :
        self.embed = discord.Embed(title = "Cartesian Query", colour = discord.Color.from_rgb(255,0,255))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        x = np.linspace(-5,5,100)
        y = (a * x) ** 2 + (b * x) + c
        plt.plot(x, y, '-r', label = f'y = {a}x² + {b}x + {c}')
        plt.title(f'Graph of y = {a}x² + {b}x + {c}') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/quad.png")
        plt.close()
        self.embed.set_image(url = "https://replit.com/@DanieshNoor/testbot#image/quad.png")
        await ctx.send(embed = self.embed)

    # ? <--- Command to plot quadratic graph
    @ cog_ext.cog_slash(description = "Plot a cubic graph using the equation y = ax³ + bx² + cx + d.")
    async def cubic_function(self, ctx, a : int, b : int, c : int, d : int) :
        self.embed = discord.Embed(title = "Cartesian Query", colour = discord.Color.from_rgb(255,0,255))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        x = np.linspace(-5,5,100)
        y = (a * x) ** 3 + (b * x) ** 2 + (c * x) + d
        plt.plot(x, y, '-r', label = f'y = {a}x³ + {b}x² + {c}x + {d}')
        plt.title(f'Graph of y = {a}x³ + {b}x² + {c}x + {d}') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/cube.png")
        plt.close()
        self.embed.set_image(url = "https://replit.com/@DanieshNoor/testbot#image/cube.png")
        await ctx.send(embed = self.embed)

    # ? <--- Command to plot reciprocal graph
    @ cog_ext.cog_slash(description = "Plot a reciprocal graph using the equation y = 1/x.")
    async def reciprocal_function(self, ctx) :
        self.embed = discord.Embed(title = "Cartesian Query", colour = discord.Color.from_rgb(255,0,255))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = ctx.author.avatar_url)
        x = np.linspace(-5,5,100)
        y = 1/x
        plt.plot(x, y, '-r', label = f'y = 1/x')
        plt.title(f'Graph of y = 1/x') 
        plt.xlabel('x', color='#1C2833')
        plt.ylabel('y', color='#1C2833')
        plt.legend(loc='upper left')
        plt.grid()
        plt.savefig("./image/reci.png")
        plt.close()
        self.embed.set_image(url = "https://replit.com/@DanieshNoor/testbot#image/reci.png")
        await ctx.send(embed = self.embed)

# ! <--- Add Cartesian_Query into the bot
def setup(client) :
    client.add_cog(Cartesian_Query(client))