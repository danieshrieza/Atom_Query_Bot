import discord
import os
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from itertools import cycle
from online import keep_alive
import sys
import subprocess

# ? <--- Automatically download package for rep.it repo
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'discord.py'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'discord-py-slash-command'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'fraction'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'Flask'])

# ! <--- Declaring client or bot
client = commands.Bot(command_prefix = "!", case_insensitive = True, strip_after_prefix = True, help_command = None)

# ! <--- Declaring slash command for bot
slash = SlashCommand(client, sync_commands = True, sync_on_cog_reload = True)

# ? <--- Status cycle for bot
status = cycle([
    " Unanswered Question of Life", 
    " Self - Referential Paradox",
    " Near-infinite density", 
    " Dark matter ",
    " Schrodinger's cat",
    " The light side of Discord is a pathway to many abilities some consider unnatural",
    " Recursion in life"
])

# ? <--- Looping through status
@ tasks.loop(minutes = 5)
async def status_swap():
  await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = next(status)))

# ? <--- Activating bot once it's ready
@ client.event
async def on_ready():
  print("I have logged in as {0.user}".format(client))
  status_swap.start()

# ? <--- Command to reload cogs file for owner
@ commands.is_owner()
@ client.command()
async def reload(ctx, extension) :
  try :
    client.reload_extension(f"cogs.{extension}")
    print(f"Reload : {ctx.author.name}")
    await ctx.send(f"`{{0.user}}` has reloaded `{extension}`.".format(client), delete_after = 3)
  except :
    await ctx.send(f"`{extension}` not found.")

# ? <--- Command to load cogs file for owner
@ commands.is_owner()
@ client.command()
async def load(ctx, extension) :
  try :
    client.load_extension(f"cogs.{extension}")
    print(f"Load : {ctx.author.name}")
    await ctx.send(f"`{{0.user}}` has loaded `{extension}`.".format(client), delete_after = 3)
  except :
    await ctx.send(f"`{extension}` not found.")

# ? <--- Command to unload cogs file for owner
@ commands.is_owner()
@ client.command()
async def unload(ctx, extension) :
  try :
    client.unload_extension(f"cogs.{extension}")
    print(f"Unload : {ctx.author.name}")
    await ctx.send(f"`{{0.user}}` has unloaded `{extension}`.".format(client), delete_after = 3)
  except :
    await ctx.send(f"`{extension}` not found.")

# ! <--- Load cogs file once bot is ready
for filename in os.listdir("./cogs") :
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")

# ! <--- Function to make the bot online 24/7
keep_alive()

# ! <--- Key for bot to run
client.run(os.environ['MATH_VAR'])