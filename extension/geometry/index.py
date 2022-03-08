from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, slash_command


# NOTE : Class for PerimeterAndArea
class PerimeterAndArea(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate circumference of a circle using radius
    @ slash_command(
        description="Calculate the circumference of a circle using radius."
    )
    async def circumference_circle_radius(self, interaction: Interaction, radius: float):

        exp=f"2 × 22/7 × {radius}"
        evalu=2*(22/7)*radius

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
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


    # NOTE : Commmand to calculate area of a circle
    @ slash_command(
        description="Calculate the area of a circle."
    )
    async def area_circle(self, interaction: Interaction, radius: float):

        exp=f"22/7 × {radius}²"
        evalu=(22/7)*(radius**2)

        embed = nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
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


    # NOTE : Command to calculate area of a quadrilateral
    @ slash_command(
        description="Calculate the area of a rectangle, a square or a quadrilateral."
    )
    async def area_quadrilateral(self, interaction: Interaction, length: float, width: float):

        exp=f"{length} × {width}"
        evalu=length*width

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
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


    # NOTE : Command to calculate area of a triangle
    @ slash_command(
        description="Calculate the area of a triangle."
    )
    async def area_triangle(self, interaction: Interaction, base: float, height: float):

        exp=f"1/2 × {base} × {height}"
        evalu=(1/2)*base*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
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


    # NOTE : Command to calculate area of a parallelogram
    @ slash_command(
        description="Calculate the area of a parallelogram."
    )
    async def area_parallelogram(self, interaction: Interaction, base: float, height: float):

        exp=f"{base} × {height}"
        evalu=base*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
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


    # NOTE : Command to calculate area of a kite
    @ slash_command(
        description="Calculate the area of a kite."
    )
    async def area_kite(self, interaction: Interaction, long_diagonal: float, short_diagonal: float):

        exp=f"1/2 × {long_diagonal} × {short_diagonal}"
        evalu=(1/2)*long_diagonal*short_diagonal

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
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


    # NOTE : Command to calculate area of a trampezium
    @ slash_command(
        description="Calculate the area of a trampezium."
    )
    async def area_trampezium(self, interaction: Interaction, first_parallel: float, second_parallel: float, height: float):

        exp=f"1/2 × ({first_parallel + second_parallel}) × {height}"
        evalu=(1/2)*(first_parallel+second_parallel)*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
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


# NOTE : Add PerimeterAndArea to the bot
def setup(bot: commands.Bot):
    bot.add_cog(PerimeterAndArea(bot))
