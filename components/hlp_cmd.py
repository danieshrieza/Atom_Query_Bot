from datetime import datetime, timezone
import discord
from discord.ext import commands
from discord_slash import cog_ext

# ! <--- Class for Help_Command
class Help_Command(commands.Cog) :
    # ? <--- Initialize variable for class
    def __init__(self, client):
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    # ? <--- Command to send help command for user
    @ cog_ext.cog_slash(description = "Find the list of command for Basic Calculator.")
    async def help(self, ctx) :
        emby_ctx = discord.Embed(title = "Help!", description = "Listing all commands on **Atom Query**.", 
        timestamp = datetime.now(timezone.utc), color = discord.Color.from_rgb(175, 143, 233))
        emby_ctx.add_field(name = "Basic Commands :", 
        value = "`cal` `generator` `square` `cube` `square_root` `cube_root` `var_power` `var_root` `factor` `common_factor` `highest_common_factor` `multiple` `common_multiple` `lowest_common_multiple` `terminate`",
        inline = False)
        emby_ctx.add_field(name = "Geometry Commands :",
        value = "`circle_circumference` `area_circle` `area_quadrilateral` `area_triangle` `area_parallelogram` `area_trampezium` `area_kite` `surface_area_cube` `surface_area_cuboid` `surface_area_pyramid` `surface_area_cylinder` `surface_area_cone` `surface_area_sphere` `volume_quadrilateral` `volume_pyramid` `volume_cylinder` `volume_cone` `volume_sphere`",
        inline = False)
        emby_ctx.add_field(name = "Trigonometry Commands :", 
        value = "`sine` `cosine` `tangent` `pythagoras_theorem`",
        inline = False)
        emby_ctx.add_field(name = "Unit Commands :",
        value = "`mm_cm` `cm_m` `m_km` `km_m` `m_cm` `cm_mm` `g_kg` `kg_g` `ml_l` `l_ml` `decimal_fraction` `fraction_decimal`",
        inline = False)
        emby_ctx.add_field(name = "Physics Commands :", 
        value = "`density` `electric_current` `electric_resistance` `electric_voltage` `speed` `moment_of_force` `pressure`",
        inline = False)
        emby_ctx.add_field(name = "Cartesian Commands :", 
        value = "`linear_function` `quadratic_function` `cubic_function` `reciprocal_function`", 
        inline = False)
        emby_ctx.set_author(name = f'@{ctx.author.name}\'s request. ',  icon_url = ctx.author.avatar_url)
        emby_ctx.set_thumbnail(url = self.link)
        await ctx.author.send(embed = emby_ctx)
        await ctx.send("Check your DM ⚡")

# ! <--- Add Help_Command into the bot
def setup(client):
  client.add_cog(Help_Command(client))