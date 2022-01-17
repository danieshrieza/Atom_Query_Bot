import nextcord
import os
from nextcord.ext import commands
from nextcord.ext.commands.context import Context
from config import token
from nextcord import Interaction
from datetime import timezone, datetime


# ! <--- Declaring bot --->
bot = commands.Bot(command_prefix = "!", case_insensitive = True, strip_after_prefix = True, help_command = None)


# ! <--- Declaring link for bot profile picture --->
link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


# ! <--- Activating bot once it's ready --->
@ bot.event

async def on_ready():
    print("I have logged in as {0.user}".format(bot))
    await bot.change_presence(activity = nextcord.Activity(type = nextcord.ActivityType.watching, name = "Dark matter"))


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
@ commands.is_owner()
@ bot.command()

async def server(ctx : Context):
    for guild in bot.guilds:
        await ctx.send(f"{guild.name}")


# ! <--- Load extension file once bot is ready --->
for filename in os.listdir("./extension") :
    if filename.endswith(".py"):
        bot.load_extension(f"extension.{filename[:-3]}")


# ! <--- Command to send help command for user --->
@ bot.slash_command(
    name = "help",
    description = "Find the list of command for Basic Calculator."
)

async def help(ctx : Interaction) :
    
    embed_msg = nextcord.Embed(
        title = "Help!", 
        description = "Listing all commands on **Atom Query**.", 
        timestamp = datetime.now(timezone.utc), 
        color = nextcord.Color.from_rgb(175, 143, 233)
    )

    embed_msg.add_field(
        name = "Basic Commands :", 
        value = "`cal` `generator` `square` `cube` `square_root` `cube_root` `var_power` `var_root` `factor` `common_factor` `highest_common_factor` `multiple` `common_multiple` `lowest_common_multiple`",
        inline = False
    )

    embed_msg.add_field(
        name = "Geometry Commands :",
        value = "`circle_circumference` `area_circle` `area_quadrilateral` `area_triangle` `area_parallelogram` `area_trampezium` `area_kite` `surface_area_cube` `surface_area_cuboid` `surface_area_pyramid` `surface_area_cylinder` `surface_area_cone` `surface_area_sphere` `volume_quadrilateral` `volume_pyramid` `volume_cylinder` `volume_cone` `volume_sphere`",
        inline = False
    )

    embed_msg.add_field(
        name = "Trigonometry Commands :", 
        value = "`sine` `cosine` `tangent` `pythagoras_theorem`",
        inline = False
    )

    embed_msg.add_field(
        name = "Unit Commands :",
        value = "`mm_cm` `cm_m` `m_km` `km_m` `m_cm` `cm_mm` `g_kg` `kg_g` `ml_l` `l_ml` `decimal_fraction` `fraction_decimal`",
        inline = False
    )

    embed_msg.add_field(
        name = "Physics Commands :", 
        value = "`density` `electric_current` `electric_resistance` `electric_voltage` `speed` `moment_of_force` `pressure`",
        inline = False
    )

    embed_msg.add_field(
        name = "Cartesian Commands :", 
        value = "`linear_function` `quadratic_function` `cubic_function` `reciprocal_function` `distance` `gradient` `midpoint`", 
        inline = False
    )

    embed_msg.set_thumbnail(url = link)

    await ctx.response.send_message(embed = embed_msg)


# ! <--- Key for bot to run --->
bot.run(token)
