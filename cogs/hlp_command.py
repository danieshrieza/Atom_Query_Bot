import discord
from discord.ext import commands
from discord_slash import cog_ext


class Help_Command() :
    def __init__(self, client):
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

    @ cog_ext.cog_slash(description = "Find the list of command for Basic Calculator.")
    async def help(self, ctx) :
        self.embed = discord.Embed(title = "Help!", description = "Listing all commands on Basic Calculator.", color = discord.Color.from_rgb(175, 143, 233))
        self.embed.add_field(name = "Basic Commands :", 
        value = "`cal` `generator` `square` `cube` `sqrt` `cbrt` `varpower` `varroot` \n `factor` `common_factor` `highest_common_factor` `multiple` `common_multiple` `lowest_common_multiple` \n `terminate`",
        inline = False)
        self.embed.add_field(name = "Geometry Commands :",
        value = "`rcircle_circumference` `dcircle_circumference` `area_circle` `area_rectangle_square` \n `area_triangle` `area_parallelogram` `area_trampezium` `area_kite` `surface_area_cube` `surface_area_cuboid` \n `surface_area_pyramid` `surface_area_cylinder` `surface_area_cone` `surface_area_sphere` \n `volume_cube_cuboid` `volume_pyramid` `volume_cylinder` `volume_cone` `volume_sphere`",
        inline = False)
        self.embed.add_field(name = "Trigonometry Commands :", 
        value = "`sin` `cos` `tan` `pythagoras_theorem`",
        inline = False)
        self.embed.add_field(name = "Unit Commands :",
        value = "`mm_cm` `cm_m` `k_km` `km_m` `m_cm` `cm_m` `g_kg` `kg_g` `ml_l` `l_ml` `decimal_frac` `frac_decimal`",
        inline = False)
        self.embed.set_author(name = {ctx.author.name},  icon_url = ctx.author.avatar_url)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

def setup(client):
  client.add_cog(Help_Command(client))