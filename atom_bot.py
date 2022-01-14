import discord
import os
from discord.ext import commands, tasks
from discord.ext.commands.context import Context
from discord_slash import SlashCommand
from itertools import cycle

# ! <--- Declaring bot or bot --->
bot = commands.Bot(command_prefix = "!", case_insensitive = True, strip_after_prefix = True, help_command = None)

# ! <--- Declaring slash command for bot --->
slash = SlashCommand(bot, sync_commands = True, sync_on_cog_reload = True, debug_guild = 883147972337090610)

# ! <--- Status cycle for bot --->
status = cycle([
    " Unanswered Question of Life", 
    " Self - Referential Paradox",
    " Near-infinite density", 
    " Dark matter ",
    " Schrodinger's cat",
    " Recursion in life",
    " A person stuck in a while loop"
])

# ! <--- Looping through status --->
@ tasks.loop(minutes = 5)
async def status_swap():
    await bot.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = next(status)))

# ! <--- Activating bot once it's ready --->
@ bot.event
async def on_ready():
    print("I have logged in as {0.user}".format(bot))
    status_swap.start()

# ! <--- Command to reload extension file for owner --->
@ commands.is_owner()
@ bot.command()
async def reload(ctx : Context, extension) :

    try :
        bot.reload_extension(f"extension.{extension}")
        await ctx.send(f"`{{0.user}}` has reloaded `{extension}`.".format(bot), delete_after = 3)

    except :
        await ctx.send(f"`{extension}` not found.")

# ! <--- Command to load extension file for owner --->
@ commands.is_owner()
@ bot.command()
async def load(ctx : Context, extension) :

    try :
        bot.load_extension(f"extension.{extension}")
        await ctx.send(f"`{{0.user}}` has loaded `{extension}`.".format(bot), delete_after = 3)

    except :
        await ctx.send(f"`{extension}` not found.")

# ! <--- Command to unload extension file for owner --->
@ commands.is_owner()
@ bot.command()
async def unload(ctx : Context, extension) :

    try :
        bot.unload_extension(f"extension.{extension}")
        await ctx.send(f"`{{0.user}}` has unloaded `{extension}`.".format(bot), delete_after = 3)

    except :
        await ctx.send(f"`{extension}` not found.")

# ! <--- Command to find all server that houses this bot --->
@ bot.command()
@ commands.is_owner()
async def server(ctx : Context):
    for guild in bot.guilds:
        await ctx.send(f"{guild.name}")

# ! <--- Load extension file once bot is ready --->
for filename in os.listdir("./extension") :
    if filename.endswith(".py"):
        bot.load_extension(f"extension.{filename[:-3]}")

# ! <--- Key for bot to run --->
bot.run(os.getenv("MATH_VAR"))