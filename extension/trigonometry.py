from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
import math
from nextcord import Interaction

# ! <--- Class for Trigonometry_Calculation --->
class Trigonometry_Calculation(commands.Cog):

    # ! <--- Initialize variable for class --->
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ! <--- Command to find sine of a triangle --->
    @ nextcord.slash_command(description = "Calculate the sine of a triangle.")
    async def sin(self,ctx : Interaction, number : float) :

        exp = f"sin {number}°"
        evalu = math.sin(number)

        embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)

    # ! <--- Command to find cosine of a triangle --->
    @ nextcord.slash_command(description = "Calculate the cosine of a triangle.")
    async def cos(self, ctx : Interaction, number : float) :

        exp = f"cos {number}°"
        evalu = math.cos(number)

        embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)

    # ! <--- Command to find tangent of a triangle --->
    @ nextcord.slash_command(description = "Calculate the tangent of a triangle.")
    async def tan(self, ctx : Interaction, number : float) :

        exp = f"tan {number}°"
        evalu = math.tan(number)

        embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
        timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)

    # ! <--- Command to find the hypotenuse, height or the base of a triangle using Pythagoras Theorem --->
    @ nextcord.slash_command(description = "Calculate the Pythagoras Theorem.")
    async def pythagoras_theorem(self, ctx : Interaction, height : float = None, base : float = None, hypotenuse : float = None) :

        if (hypotenuse == None and height != None and base != None) :

            exp = f"√{base}² + {height}²"
            evalu = math.sqrt((base ** 2) + (height ** 2))

            embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
            embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        elif (height == None and hypotenuse != None and base != None) :

            if hypotenuse > base :

                exp = f"√{hypotenuse}² - {base}²"
                evalu = math.sqrt((hypotenuse ** 2) - (base ** 2))

                embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
                embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
                embed_msg.set_thumbnail(url = self.link)

                await ctx.response.send_message(embed = embed_msg)

            else :

                exp = f"√{base}² - {hypotenuse}²"
                evalu = math.sqrt((base ** 2) - (hypotenuse ** 2))

                embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
                embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
                embed_msg.set_thumbnail(url = self.link)

                await ctx.response.send_message(embed = embed_msg)

        elif (base == None and hypotenuse != None and height != None) :

            if hypotenuse > height :

                exp = f"√{hypotenuse}² - {height}²"
                evalu = math.sqrt((hypotenuse ** 2) - (height ** 2))

                embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
                embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
                embed_msg.set_thumbnail(url = self.link)

                await ctx.response.send_message(embed = embed_msg)

            else :

                exp = f"√{height}² - {hypotenuse}²"
                evalu = math.sqrt((height ** 2) - (hypotenuse ** 2))

                embed_msg = nextcord.Embed(title = "Trigonometry Query", description = "The requested `Trigonometry Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), colour = nextcord.Color.from_rgb(139,0,0))
                embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
                embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
                embed_msg.set_thumbnail(url = self.link)

                await ctx.response.send_message(embed = embed_msg)
        else :
            await ctx.response.send_message("Please provide input for only one optional argument.")

# ! <--- Add Triginometry_Calculation into the bot --->
def setup(bot : commands.Bot):
  bot.add_cog(Trigonometry_Calculation(bot))