import nextcord
import os
from nextcord.ext import commands
from nextcord.ext.commands.context import Context
from config import TOKEN, OWNER_ID


def main():

    bot = commands.Bot(
        command_prefix="!",
        case_insensitive=True,
        strip_after_prefix=True,
        help_command=None,
        owner_id=OWNER_ID,
        intents=nextcord.Intents.all(),
        activity=nextcord.Activity(
            type=nextcord.ActivityType.watching, name="The Complex Plane")
    )

    @ bot.event
    async def on_ready():
        print(f"I have logged in as {bot.user}")

    @ commands.is_owner()
    @ bot.command()
    async def server(ctx: Context):
        for guild in bot.guilds:
            await ctx.send(f"{guild.name}")

    for file in os.listdir("./extension"):
        if file.endswith(".py"):
            bot.load_extension(f"extension.{file[:-3]}")

    bot.run(TOKEN)


# NOTE : Call main
if __name__ == "__main__":
    main()
