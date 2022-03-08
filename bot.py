import discord
import os
from discord.ext import commands
from discord.ext.commands.context import Context
from config import TOKEN, OWNER_ID
from discord import app_commands


# NOTE : Declare bot variable
bot = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    strip_after_prefix=True,
    help_command=None,
    owner_id=OWNER_ID,
    intents=discord.Intents.all(),
    activity=discord.Activity(type=discord.ActivityType.watching, name="The Complex Plane")
)


# NOTE : Declare tree variable for slash command
tree = app_commands.CommandTree(bot)


# NOTE : Activating bot once it's ready
@ bot.event
async def on_ready():
    await tree.sync()
    print(f"I have logged in as {bot.user}")


# NOTE : Command to find all server that houses this bot
@ commands.is_owner()
@ bot.command()
async def server(ctx: Context):
    for guild in bot.guilds:
        await ctx.send(f"{guild.name}")


# NOTE : Load extension file once bot is ready
for folder in os.listdir("./extension"):
    
    if os.path.exists(os.path.join("extension", folder, "cog_1.py")):
        bot.load_extension(f"extension.{folder}.cog_1")
        
    elif os.path.exists(os.path.join("extension", folder, "cog_2.py")):
        bot.load_extension(f"extension.{folder}.cog_2")


# NOTE : Key for bot to run
bot.run(TOKEN)
