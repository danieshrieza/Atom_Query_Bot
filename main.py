import discord
import os
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from itertools import cycle

client = commands.Bot(command_prefix = "!")

slash = SlashCommand(client, sync_commands = True)

status = cycle([
    " Unanswered Question of Life", " Self - Referential Paradox",
    " Near-infinite density", " Dark matter ",
    " Measurement of the speed of light in one straight line",
    " Schrodinger's cat",
    " The light side of Discord is a pathway to many abilities some consider unnatural",
    " Go touch some grass",
    " Why bully others when you can bully yourself",
    " https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    " Recursion in life",
    " Why my dad didn't came back after going to grocery ?"
])

@ tasks.loop(minutes = 2)
async def status_swap():
  await client.change_presence(activity = discord.Activity(type = discord.ActivityType.watching, name = next(status)))

@ client.event
async def on_ready():
  print("I have logged in as {0.user}".format(client))
  status_swap.start()

for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    client.load_extension(f"cogs.{filename[:-3]}")

client.run(os.getenv("MATH_VAR"))