import nextcord
from nextcord.ext import commands
import math
import random
from datetime import datetime, timezone
from nextcord import Interaction, slash_command


# NOTE : Class for Query
class Query(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to find factor a number
    @ slash_command(
        description="Find the factor of a number."
    )
    async def factor(self, interaction: Interaction, number: int):

        evalu=[]
        for i in range(1, number+1):
            if number%i == 0:
                evalu.append(i)

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name="Input :",
            value=f"``` Factor of {number}. ```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to find common factor of 2 number
    @ slash_command(
        description="Find the common factor of 2 number."
    )
    async def common_factor(self, interaction: Interaction, number_1: int, number_2: int):

        if (number_1>0 and number_2>0):

            evalu=[]
            for i in range(1, min(number_1, number_2)+1):
                if number_1%i == number_2%i == 0:
                    evalu.append(i)

            embed=nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=datetime.now(timezone.utc),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"``` Common Factor of {number_1} and {number_2}. ```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {evalu} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        else:
            await interaction.response.send_message("Please provide input that has values more than 0.")


    # NOTE : Command to find highest common factor of 2 number
    @ slash_command(
        description="Find the highest common factor of 2 number."
    )
    async def highest_common_factor(self, interaction: Interaction, number_1: int, number_2: int):

        if (number_1>0 and number_2>0):

            evalu=math.gcd(number_1, number_2)

            embed=nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=datetime.now(timezone.utc),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"``` Highest Common Factor of {number_1} and {number_2}. ```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {evalu} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        else:
            await interaction.response.send_message("Please provide input that values are more than 0.")


    # NOTE : Command to find multiple of a number
    @ slash_command(
        description="Find the multiple of a number."
    )
    async def multiple(self, interaction: Interaction, number: int, number_range: int):

        evalu=[]

        for i in range(1, number_range+1):
            evalu.append(number*i)

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name="Input :",
            value=f"``` Multiple of {number}. ```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to find common multiple of 2 numbers
    @ slash_command(
        description="Find the common multiple of 2 numbers."
    )
    async def common_multiple(self, interaction: Interaction, number_1: int, number_2: int, number_range: int):

        if (number_1>0 and number_2>0 and number_range>0):

            arr=[]
            evalu=math.lcm(number_1, number_2)

            for i in range(1, number_range+1):
                arr.append(evalu*i)

            embed=nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=datetime.now(timezone.utc),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"``` Common Multiple of {number_1} and {number_2}. ```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {arr} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        else:
            await interaction.response.send_message("Please provide input that values are more than 0.")


    # NOTE : Command to find the lowest common multiple of 2 numbers
    @ slash_command(
        description="Find the lowest common multiple of 2 numbers."
    )
    async def lowest_common_multiple(self, interaction: Interaction, number_1: int, number_2: int):

        if (number_1>0 and number_2>0):

            evalu=math.lcm(number_1, number_2)

            embed=nextcord.Embed(
                title="Math Query",
                description="The requested `Math Query` have been evaluated by **Atom Query**",
                timestamp=datetime.now(timezone.utc),
                colour=nextcord.Color.from_rgb(179, 27, 27)
            )

            embed.add_field(
                name="Input :",
                value=f"``` Lowest Common Multiple of {number_1} and {number_2}. ```",
                inline=False
            )

            embed.add_field(
                name="Output :",
                value=f"```Python\n {evalu} \n```",
                inline=True
            )

            embed.set_thumbnail(url=self.link)

            await interaction.response.send_message(embed=embed)

        else:
            await interaction.response.send_message("Please provide valid input.")


    # NOTE : Command to find the Fibonacci Sequence
    @ slash_command(
        description="Calculate the Fibonacci Sequence using the numbers provided by user."
    )
    async def fibonacci_sequence(self, interaction: Interaction, number_list: str, number_range: int):

        str_list: list=number_list.split()

        int_list=[int(i) for i in str_list]

        while len(int_list)<number_range:
            int_list.append(sum(int_list[-2:]))

        evalu=int_list[:number_range]

        exp=[int(i) for i in str_list]

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


    # NOTE : Command to find the Tribonacci Sequence
    @ slash_command(
        description="Calculate the Tribonacci Sequence using the numbers provided by user."
    )
    async def tribonacci_sequence(self, interaction: Interaction, number_list: str, number_range: int):

        str_list: list=number_list.split()

        int_list=[int(i) for i in str_list]

        while len(int_list)<number_range:
            int_list.append(sum(int_list[-3:]))

        evalu=int_list[:number_range]

        exp=[int(i) for i in str_list]

        embed = nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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
        
        
    # NOTE : Command to calculate queries from user
    @ slash_command(
        description="Calculate your math's query."
    )
    async def calculate(self, interaction: Interaction, query: str):

        expliteral=("").join(query)
        exppoet=expliteral.replace("*", "×").replace("/", "÷")
        evalu=eval(expliteral)

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exppoet} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to generate random number
    @ slash_command(
        description="Generate random integer number from input range."
    )
    async def number_generator(self, interaction: Interaction, starting_point: int, ending_point: int):

        exp=f"Generate number between {starting_point} and {ending_point}."
        evalu=f"{random.randint(starting_point, ending_point)}"

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


    # NOTE : Command to square a number
    @ slash_command(
        description="Squared number from user."
    )
    async def square(self, interaction: Interaction, base: float):

        exp=f"{base}²"
        evalu=base**2

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


    # NOTE : Command to cube a number
    @ slash_command(
        description="Cubed number from user."
    )
    async def cube(self, interaction: Interaction, base: float):

        exp=f"{base}³"
        evalu=base**3

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


    # NOTE : Command to power a base using user's exponent
    @ slash_command(
        description="Power the user's base to the exponent."
    )
    async def variable_power(self, interaction: Interaction, base: float, exponent: float):

        exp=f"{base} ** {exponent}"
        evalu=base**exponent

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


    # NOTE : Command to square root a number
    @ slash_command(
        description="Square root user's number."
    )
    async def square_root(self, interaction: Interaction, radicand: float):

        exp=f"√{radicand}"
        evalu=math.sqrt(radicand)

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


    # NOTE : Command to cube root a number
    @ slash_command(
        description="Cube root user's number."
    )
    async def cube_root(self, interaction: Interaction, radicand: float):

        exp=f"³√{radicand}"
        evalu=radicand**1./3.

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


    # NOTE : Command to root a radicand using a radical
    @ slash_command(
        description="Radical(root) user's radicand(number)."
    )
    async def variable_root(self, interaction: Interaction, radicand: float, radical: float):

        exp=f"{radicand} ** 1/{radical}"
        evalu=radicand**1./radical

        embed=nextcord.Embed(
            title="Math Query",
            description="The requested `Math Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(179, 27, 27)
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


# NOTE : Add Query to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Query(bot))
