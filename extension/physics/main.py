from datetime import datetime, timezone
import discord
from discord.ext import commands
from discord import Interaction, app_commands


# NOTE : Class for BasicPhysics
class BasicPhysics(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"
        
        
    # NOTE : Command to calculate speed of an object
    @ app_commands.command(
        description="Calculate the speed of an object using any distance and time unit."
    )
    async def speed(self, ctx: Interaction, distance: float, time: float):

        exp=f"{distance} ÷ {time}"
        evalu=distance/time

        embed=discord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=discord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} m/s \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await ctx.response.send_message(embed=embed)


    # NOTE : Command to calculate electric current of an object
    @ app_commands.command(
        description="Calculate the electric current of an object."
    )
    async def electric_current(self, ctx: Interaction, electric_voltage: float, electric_resistance: float):

        exp=f"{electric_voltage} V ÷ {electric_resistance} Ω"
        evalu=electric_voltage/electric_resistance

        embed=discord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=discord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} A \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await ctx.response.send_message(embed=embed)


    # NOTE : Command to calculate electric voltage of an object
    @ app_commands.command(
        description="Calculate the electric voltage of an object."
    )
    async def electric_voltage(self, ctx: Interaction, electric_current: float, electric_resistance: float):

        exp=f"{electric_current} A × {electric_resistance} Ω"
        evalu=electric_current*electric_resistance

        embed=discord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=discord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} V \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await ctx.response.send_message(embed=embed)


    # NOTE : Command to calculate electric resistance of an object
    @ app_commands.command(
        description="Calculate the electric resistance of an object."
    )
    async def electric_resistance(self, ctx: Interaction, electric_voltage: float, electric_current: float):

        exp=f"{electric_voltage} V ÷ {electric_current} A"
        evalu=electric_voltage/electric_current

        embed=discord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=discord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} Ω \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await ctx.response.send_message(embed=embed)


# NOTE : Add BasicPhysics to the bot
def setup(bot: commands.Bot):
    bot.add_cog(BasicPhysics(bot))
