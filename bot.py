import nextcord
import os
from nextcord.ext import commands
from nextcord.ext.commands.context import Context
from config import TOKEN, OWNER_ID


# NOTE : Declare bot variable
bot = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    strip_after_prefix=True,
    help_command=None,
    owner_id=OWNER_ID,
    intents=nextcord.Intents.all(),
    activity=nextcord.Activity(type=nextcord.ActivityType.watching, name="The Complex Plane")
)


# # NOTE : Declare tree variable for slash command
# tree = app_commands.CommandTree(bot)


# NOTE : Activating bot once it's ready
@ bot.event
async def on_ready():
    # await tree.sync()
    print(f"I have logged in as {bot.user}")


# NOTE : Command to find all server that houses this bot
@ commands.is_owner()
@ bot.command()
async def server(ctx: Context):
    for guild in bot.guilds:
        await ctx.send(f"{guild.name}")


# NOTE : Load extension file once bot is ready
for folder in os.listdir("./extension"):
    
    if os.path.exists(os.path.join("extension", folder, "index.py")):
        bot.load_extension(f"extension.{folder}.index")
        
    elif os.path.exists(os.path.join("extension", folder, "main.py")):
        bot.load_extension(f"extension.{folder}.main")


# NOTE : Key for bot to run
bot.run(TOKEN)
