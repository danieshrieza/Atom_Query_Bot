import discord
import os
from discord.ext import commands, tasks
from discord_slash import SlashCommand
from itertools import cycle

# ! <--- Declaring client or bot
client = commands.Bot(command_prefix = "!", case_insensitive = True, strip_after_prefix = True, help_command = None)

# ! <--- Declaring slash command for bot
slash = SlashCommand(client, sync_commands = True, sync_on_cog_reload = True, debug_guild = 883147972337090610)

# ? <--- Status cycle for bot
status = cycle([
    " Unanswered Question of Life", 
    " Self - Referential Paradox",
    " Near-infinite density", 
    " Dark matter ",
    " Schrodinger's cat",
    " Recursion in life",
    " A person stuck in a while loop"
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

# ? <--- Command to reload components file for owner
@ commands.is_owner()
@ client.command()
async def reload(ctx, extension) :
    try :
        client.reload_extension(f"components.{extension}")
        print(f"Reload : {ctx.author.name}")
        await ctx.send(f"`{{0.user}}` has reloaded `{extension}`.".format(client), delete_after = 3)
    except :
        await ctx.send(f"`{extension}` not found.")

# ? <--- Command to load components file for owner
@ commands.is_owner()
@ client.command()
async def load(ctx, extension) :
    try :
        client.load_extension(f"components.{extension}")
        print(f"Load : {ctx.author.name}")
        await ctx.send(f"`{{0.user}}` has loaded `{extension}`.".format(client), delete_after = 3)
    except :
        await ctx.send(f"`{extension}` not found.")

# ? <--- Command to unload components file for owner
@ commands.is_owner()
@ client.command()
async def unload(ctx, extension) :
    try :
        client.unload_extension(f"components.{extension}")
        print(f"Unload : {ctx.author.name}")
        await ctx.send(f"`{{0.user}}` has unloaded `{extension}`.".format(client), delete_after = 3)
    except :
        await ctx.send(f"`{extension}` not found.")

# ? <--- Command to send announcement to all server that host this Discord Bot
@ client.command()
@ commands.is_owner()
async def anno(ctx, *, permission : bool):
    if permission == True :
        for server in client.guilds:
            for channel in server.text_channels:
                try:
                    emby_ctx = discord.Embed(title = "Announcement", colour = discord.Color.from_rgb(212,175,55))
                    emby_ctx.add_field(name = "**Attention**", value = "", inline = False)
                    emby_ctx.add_field(name = "", value = "", inline = True)
                    emby_ctx.set_thumbnail(url = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128")
                    await channel.send(embed = emby_ctx)
                except Exception:
                    continue
                else:
                    break
    else :
        await ctx.send("No announcement as of now.")

# ! <--- Load components file once bot is ready
for filename in os.listdir("./components") :
    if filename.endswith(".py"):
        client.load_extension(f"components.{filename[:-3]}")

# ! <--- Key for bot to run
client.run(os.environ['MATH_VAR'])