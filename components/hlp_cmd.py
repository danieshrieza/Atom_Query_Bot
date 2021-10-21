import discord
from discord.ext import commands
from discord_slash import cog_ext

# ! <--- Class for Help_Command
class Help_Command(commands.Cog) :
    # ? <--- Initialize variable for class
    def __init__(self, client):
        self.client = client
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

    # ? <--- Command to send help command for user
    @ cog_ext.cog_slash(description = "Find the list of command for Basic Calculator.")
    async def help(self, ctx) :
        self.embed = discord.Embed(title = "Help!", description = "Listing all commands on Basic Calculator.", color = discord.Color.from_rgb(175, 143, 233))
        self.embed.add_field(name = "Basic Commands :", 
        value = "`cal` `generator` `square` `cube` `square root` `cube root` `variable power` `variable root` \n `factor` `common factor` `highest common factor` `multiple` `common multiple` `lowest common multiple` \n `terminate`",
        inline = False)
        self.embed.add_field(name = "Geometry Commands :",
        value = "`circle circumference` `area of circle` `area of quadrilateral` \n `area of triangle` `area of parallelogram` `area of trampezium` `area of kite` `surface area of cube` `surface area of cuboid` \n `surface area of pyramid` `surface area of cylinder` `surface area of cone` `surface area of sphere` \n `volume of quadrilateral` `volume of pyramid` `volume of cylinder` `volume of cone` `volume of sphere`",
        inline = False)
        self.embed.add_field(name = "Trigonometry Commands :", 
        value = "`sine` `cosine` `tangent` `pythagoras theorem`",
        inline = False)
        self.embed.add_field(name = "Unit Commands :",
        value = "`milimeter to centimeter` `centimeter to meter` `meter to kilometer` `kilometer to meter` `meter to centimeter` `centimeter to meter` `gram to kilogram` `kilogram to gram` `mililitre to litre` `litre to mililitre` `decimal to fraction` `fraction to decimal`",
        inline = False)
        self.embed.add_field(name = "Physics Commands :", 
        value = "`density` `electric current` `electric resistance` \n `electric voltage` `speed` `moment of force` `pressure`",
        inline = False)
        self.embed.set_author(name = f'{ctx.author.name}\'s request. ',  icon_url = ctx.author.avatar_url)
        self.embed.set_thumbnail(url = self.link)
        await ctx.author.send(embed = self.embed)
        await ctx.send("Check your DM ⚡")

# ! <--- Add Help_Command into the bot
def setup(client):
  client.add_cog(Help_Command(client))