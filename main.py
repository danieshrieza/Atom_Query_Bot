subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'discord.py'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'discord-py-slash-command'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'fraction'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'Flask'])

import discord
import os
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from itertools import cycle
from online import keep_alive
import sys
import subprocess


client = commands.Bot(command_prefix = "!", case_insensitive = True, strip_after_prefix = True, help_command = None)

slash = SlashCommand(client, sync_commands = True, sync_on_cog_reload = True)

owner = ("775930138881163286")

status = cycle([
    " Unanswered Question of Life", 
    " Self - Referential Paradox",
    " Near-infinite density", 
    " Dark matter ",
    " Schrodinger's cat",
    " The light side of Discord is a pathway to many abilities some consider unnatural",
    " Recursion in life"
])


@ tasks.loop(minutes = 5)
async def status_swap():
  await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = next(status)))

@ client.event
async def on_ready():
  print("I have logged in as {0.user}".format(client))
  status_swap.start()

@ commands.is_owner()
@ slash.slash(description = "Reload cogs file (Owner only).")
async def reload(ctx, extension) :
  try :
    client.reload_extension(f"cogs.{extension}")
    print(f"Reload : {ctx.author.name}")
    await ctx.send(f"`{{0.user}}` has reloaded `{extension}`.".format(client), delete_after = 3)
  except :
    await ctx.send(f"`{extension}` not found.")

@ commands.is_owner()
@ slash.slash(description = "Load cogs file (Owner only).")
async def load(ctx, extension) :
  try :
    client.load_extension(f"cogs.{extension}")
    print(f"Load : {ctx.author.name}")
    await ctx.send(f"`{{0.user}}` has loaded `{extension}`.".format(client), delete_after = 3)
  except :
    await ctx.send(f"`{extension}` not found.")

@ commands.is_owner()
@ slash.slash(description = "Unload cogs file (Owner only).")
async def unload(ctx, extension) :
  try :
    client.unload_extension(f"cogs.{extension}")
    print(f"Unload : {ctx.author.name}")
    await ctx.send(f"`{{0.user}}` has unloaded `{extension}`.".format(client), delete_after = 3)
  except :
    await ctx.send(f"`{extension}` not found.")

for filename in os.listdir("./cogs") :
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")

token = os.environ['MATH_VAR']

keep_alive()

client.run(token)