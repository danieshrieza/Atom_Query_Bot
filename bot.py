import discord
import os
from discord.ext import commands
from config import TOKEN, OWNER_ID
import asyncio


bot = commands.Bot(
    command_prefix="!",
    case_insensitive=True,
    strip_after_prefix=True,
    help_command=None,
    owner_id=OWNER_ID,
    intents=discord.Intents.all(),
    activity=discord.Activity(type=discord.ActivityType.watching, name="The Complex Plane")
)


@ bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"I have logged in as {bot.user}")


async def load():
    for file in os.listdir("./extension"):
        if file.endswith(".py"):
            await bot.load_extension(f"extension.{file[:-3]}")


async def main():
    async with bot:
        await load()
        await bot.start(TOKEN)


asyncio.run(main())
