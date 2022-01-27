import nextcord
from nextcord.ext import commands
import math
from datetime import datetime, timezone
from nextcord import Interaction
from config import guild_id

    
# NOTE : Class for AdditionalBasic
class AdditionalBasic(commands.Cog) :


    # NOTE : Initialize parameter for class
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"
        

    # NOTE : Command to find factor a number 
    @ nextcord.slash_command(
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

        embed_msg.add_field(
            name = "Input :", 
            value = f"Factor of `{number}`.", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to find common factor of 2 number 
    @ nextcord.slash_command(
        description = "Find the common factor of 2 number."
    )

    async def common_factor(self, ctx : Interaction, number_1 : int, number_2 : int) :

        if (number_1 > 0 and number_2 > 0) :

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

            embed_msg.add_field(
                name = "Input :", 
                value = f"Common Factor of `{number_1}` and `{number_2}`.", 
                inline = False
            )

            embed_msg.add_field(
                name = "Output :", 
                value = f"`{evalu}`", 
                inline = True
            )

            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide input that has values more than 0.")


    # NOTE : Command to find highest common factor of 2 number 
    @ nextcord.slash_command(
        description = "Find the highest common factor of 2 number."
    )

    async def highest_common_factor(self, ctx : Interaction, number_1 : int, number_2 : int) :

        if (number_1 > 0 and number_2 > 0) :

            evalu = math.gcd(number_1, number_2)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(
                name = "Input :", 
                value = f"Highest Common Factor of `{number_1}` and `{number_2}`.", 
                inline = False
            )

            embed_msg.add_field(
                name = "Output :", 
                value = f"`{evalu}`", 
                inline = True
            )

            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide input that values are more than 0.")


    # NOTE : Command to find multiple of a number 
    @ nextcord.slash_command(
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

        embed_msg.add_field(
            name = "Input :",
            value = f"Multiple of `{number}`.", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


    # NOTE : Command to find common multiple of 2 number 
    @ nextcord.slash_command(
        description = "Find the common multiple of 2 numbers."
    )

    async def common_multiple(self, ctx : Interaction, number_1 : int, number_2 : int, number_range : int) :

        if (number_1 > 0 and number_2 > 0 and number_range > 0) :

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

            embed_msg.add_field(
                name = "Input :", 
                value = f"Common Multiple of `{number_1}` and `{number_2}`.", 
                inline = False
            )

            embed_msg.add_field(
                name = "Output :", 
                value = f"`{arr}`", 
                inline = True
            )

            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide input that values are more than 0.")


    # NOTE : Command to find the lowest common multiple of 2 number 
    @ nextcord.slash_command(
        description = "Find the lowest common multiple of 2 numbers."
    )

    async def lowest_common_multiple(self, ctx : Interaction, number_1 : int, number_2 : int) :

        if (number_1 > 0 and number_2 > 0) :

            evalu = math.lcm(number_1, number_2)

            embed_msg = nextcord.Embed(
                title = "Math Query", 
                description = "The requested `Math Query` have been evaluated by **Atom Query**", 
                timestamp = datetime.now(timezone.utc), 
                colour = nextcord.Color.from_rgb(179, 27, 27)
            )

            embed_msg.add_field(
                name = "Input :", 
                value = f"Lowest Common Multiple of `{number_1}` and `{number_2}`.", 
                inline = False
            )

            embed_msg.add_field(
                name = "Output :", 
                value = f"`{evalu}`", 
                inline = True
            )

            embed_msg.set_thumbnail(url = self.link)

            await ctx.response.send_message(embed = embed_msg)

        else :
            await ctx.response.send_message("Please provide valid input.")


    # NOTE : Command to find the Fibonacci Sequence
    @ nextcord.slash_command(
        description = "Calculate the Fibonacci Sequence using the numbers provided by user."
    )
    
    async def fibonacci_sequence(self, ctx : Interaction, number_list : str, number_range : int) :

        str_list : list = number_list.split()

        int_list = [int(i) for i in str_list]

        while len(int_list) < number_range:
            int_list.append(sum(int_list[-2:]))

        evalu = int_list[:number_range]

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{int_list}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)



    # NOTE : Command to find the Tribonacci Sequence
    @ nextcord.slash_command(
        description = "Calculate the Tribonacci Sequence using the numbers provided by user."
    )
    
    async def tribonacci_sequence(self, ctx : Interaction, number_list : str, number_range : int) :

        str_list : list = number_list.split()

        int_list = [int(i) for i in str_list]

        while len(int_list) < number_range:
            int_list.append(sum(int_list[-3:]))

        evalu = int_list[:number_range]

        embed_msg = nextcord.Embed(
            title = "Math Query", 
            description = "The requested `Math Query` have been evaluated by **Atom Query**", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(179, 27, 27)
        )

        embed_msg.add_field(
            name = "Input :", 
            value = f"`{int_list}`", 
            inline = False
        )

        embed_msg.add_field(
            name = "Output :", 
            value = f"`{evalu}`", 
            inline = True
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


# NOTE : Add AdditionalBasic to the bot
def setup(bot : commands.Bot) :
    bot.add_cog(AdditionalBasic(bot))