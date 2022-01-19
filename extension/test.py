from datetime import datetime, timezone
from nextcord import Interaction
import nextcord
from nextcord.ext import commands
from config import guild_id


# <--- Test_Command class --->
class Test_Command(commands.Cog) :


    # <--- Initialize variable for class --->
    def __init__(self, bot : commands.Bot) :
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # <--- Test command --->
    @ nextcord.slash_command(
        name = "test",
        description = "Testing feature",
        guild_ids = guild_id
    )

    async def test(self, ctx : Interaction, age : int, name : str = None) :

        embed_msg = nextcord.Embed(
            title = "Test", 
            description = "Testing feature", 
            timestamp = datetime.now(timezone.utc), 
            colour = nextcord.Color.from_rgb(127, 0, 255)
        )

        embed_msg.add_field(
            name = "Age", 
            value = f"{age}", 
            inline = False
        )

        embed_msg.add_field(
            name = "Name", 
            value = f"{name}", 
            inline = False
        )

        embed_msg.set_thumbnail(url = self.link)

        await ctx.response.send_message(embed = embed_msg)


# <--- Add Test_Command to bot --->
def setup(bot : commands.Bot) :
    bot.add_cog(Test_Command(bot))