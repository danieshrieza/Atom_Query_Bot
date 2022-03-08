from datetime import datetime, timezone
import discord
from discord.ext import commands
import math
from discord import Interaction, app_commands


# NOTE : Class for PythaTheorem
class PythaTheorem(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to find the hypotenuse, height or the base of a triangle using Pythagoras Theorem
    @ app_commands.command(
        description="Calculate the Pythagoras Theorem."
    )
    async def pythagoras_theorem(self, ctx: Interaction, height: float, base: float):

        if (height>0 and base>0):

            exp=f"√{base}² + {height}²"
            evalu=math.sqrt((base**2)+(height**2))

            embed=discord.Embed(
                title="Trigonometry Query",
                description="The requested `Trigonometry Query` have been evaluated by **Atom Query**",
                timestamp=datetime.now(timezone.utc),
                colour=discord.Color.from_rgb(139, 0, 0)
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

            await ctx.response.send_message(embed=embed)

        else:
            await ctx.response.send_message("Please provide input that has values more than 0.")


# NOTE : Add PythaTheorem to the bot
def setup(bot: commands.Bot):
    bot.add_cog(PythaTheorem(bot))
