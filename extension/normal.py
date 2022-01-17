import nextcord
from nextcord.ext import commands
import math
import random
from datetime import datetime, timezone
from nextcord import Interaction


# ! <--- Class for Basic_Calculation --->
class Basic_Calculation(commands.Cog):


    # ! <--- Initialize variable and function for class --->
    def __init__(self, bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # ! <--- Command to calculate queries from user --->
    @ nextcord.slash_command(
        name = "calculate",
        description = "Calculate your math's query."
    )

    async def cal(self, ctx : Interaction, query : str) :

        expliteral = ("").join(query)
        exppoet = expliteral.replace("*","×").replace("/", "÷")
        evalu = eval(expliteral)

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exppoet}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to generate random number --->
    @ nextcord.slash_command(
        name = "random number generator",
        description = "Generate randomly selected numbers from input range."
    )

    async def generator(self, ctx : Interaction, starting_point: float, ending_point : float) :

        exp = f"Generate number between {starting_point} and {ending_point}."
        evalu = f"{random.random(starting_point,ending_point)}"

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to square a number --->
    @ nextcord.slash_command(
        name = "square",
        description = "Squared number from user."
    )

    async def square(self, ctx : Interaction, base : float) :

        exp = f"{base}²"
        evalu = f"{base ** 2}" 

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to cube a number --->
    @ nextcord.slash_command(
        name = "cube",
        description = "Cubed number from user."
    )

    async def cube(self, ctx : Interaction, base : float) :

        exp = f"{base}³"
        evalu = f"{base ** 3}"

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to power a base using user's exponent --->
    @ nextcord.slash_command(
        name = "variable power",
        description = "Power the user's base to the exponent."
    )

    async def variable_power(self, ctx : Interaction, base : float, exponent : float) :

        exp = f"{base} ** {exponent}"
        evalu = f"{base ** exponent}"

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to square root a number --->
    @ nextcord.slash_command(
        name = "square root", 
        description = "Square root user's number."
    )

    async def square_root(self, ctx : Interaction, radicand : float) :

        exp = f"√{radicand}"
        evalu = f"{math.sqrt(radicand)}" 

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to cube root a number --->
    @ nextcord.slash_command(
        name = "cube root", 
        description = "Cube root user's number."
    )

    async def cube_root(self, ctx : Interaction, radicand : float) :

        exp = f"³√{radicand}"
        evalu = f"{radicand ** 1./3.}"

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to root a radicand using a radical --->
    @ nextcord.slash_command(
        name = "variable root", 
        description = "Radical(root) user's radicand(number)."
    )

    async def variable_root(self, ctx : Interaction, radicand : float, radical: float) :

        exp = f"{radicand} ** 1/{radical}"
        evalu = f"{radicand ** 1./radical}"

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"`{exp}`", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to find factor a number --->
    @ nextcord.slash_command(
        name = "factor", 
        description = "Find the factor of a number."
    )

    async def factor(self, ctx : Interaction, number : int) :

        evalu = []
        for i in range(1, number + 1) :
            if number % i == 0 :
                eval.append(i)

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :", value = f"Factor of `{number}`.", inline = False)
        embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to find common factor of multiple number --->
    @ nextcord.slash_command(
        name = "common factor", 
        description = "Find the common factor of multiple number."
    )

    async def common_factor(self, ctx : Interaction, number_1 : int, number_2 : int, number_3 : int = None) :

        if (number_3 == None and number_1 > 0 and number_2 > 0) :

            evalu = []
            for i in range(1, min(number_1, number_2) + 1) :
                if number_1 % i == number_2 % i == 0 :
                    eval.append(i)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :", value = f"Common Factor of `{number_1}` and `{number_2}`.", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        elif (number_3 != None and number_1 > 0 and number_2 > 0) :

            evalu = []
            for i in range(1, min(number_1, number_2, number_3) + 1) :
                if number_1 % i == number_2 % i == number_3 % i == 0 :
                    eval.append(i)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :", value = f"Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide only two input.")


    # ! <--- Command to find highest common factor of multiple number --->
    @ nextcord.slash_command(
        name = "highest common factor", 
        description = "Find the highest common factor of multiple number."
    )

    async def highest_common_factor(self, ctx : Interaction, number_1 : int, number_2 : int, number_3 : int = None) :

        if (number_3 == None and number_1 > 0 and number_2 > 0) :

            evalu = math.gcd(number_1, number_2)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :", value = f"Highest Common Factor of `{number_1}` and `{number_2}`.", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        elif (number_3 != None and number_1 > 0 and number_2 > 0) :

            evalu = math.gcd(math.gcd(number_1, number_2), number_3)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :",value = f"Highest Common Factor of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            embed_msg.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide valid input.")

    # ! <--- Command to find multiple of a number --->
    @ nextcord.slash_command(
        name = "multiple",
        description = "Find the multiple of a number."
    )

    async def multiple(self, ctx : Interaction, number : int, number_range : int) :

        evalu = []

        for i in range(1, number_range + 1) :
            evalu.append(number * i)

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(name = "Input :",value = f"Multiple of `{number}`.", inline = False)
        embed_msg.add_field(name = "Output :" , value = f"`{evalu}`", inline = True)
        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # ! <--- Command to find common multiple of multiple number --->
    @ nextcord.slash_command(
        name = "common_multiple", 
        description = "Find the common multiple of 2 or 3 numbers."
    )

    async def common_multiple(self, ctx : Interaction, number_1 : int, number_2 : int, number_range : int, number_3 : int = None) :

        if (number_3 == None and number_1 > 0 and number_2 > 0 and number_range > 0) :

            arr = []
            evalu = math.lcm(number_1, number_2)

            for i in range(1, number_range + 1) :
                arr.append(evalu * i)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :", value = f"Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{arr}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        elif (number_3 != None and number_1 > 0 and number_2 > 0 and number_range > 0) :

            arr = []
            evalu = math.lcm(math.lcm(number_1, number_2), number_3)

            for i in range(1, number_range + 1) :
                arr.append(evalu * i)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :", value = f"Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{arr}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide valid input.")


    # ! <--- Command to find the lowest common multiple of multiple number --->
    @ nextcord.slash_command(
        name = "lowest common multiple", 
        description = "Find the lowest common multiple of 2 or 3 numbers."
    )

    async def lowest_common_multiple(self, ctx : Interaction, number_1 : int, number_2 : int, number_3 : int) :

        if (number_3 == None and number_1 > 0 and number_2 > 0) :

            evalu = math.lcm(number_1, number_2)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}` and `{number_2}`.", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        elif (number_3 != None and number_1 > 0 and number_2 > 0) :

            evalu = math.lcm(math.lcm(number_1, number_2), number_3)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(name = "Input :", value = f"Lowest Common Multiple of `{number_1}`, `{number_2}` and `{number_3}`.", inline = False)
            embed_msg.add_field(name = "Output :", value = f"`{evalu}`", inline = True)
            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide valid input.")


# ! <--- Add Basic_Calculation into the bot --->
def setup(bot : commands.Bot): 
  bot.add_cog(Basic_Calculation(bot))