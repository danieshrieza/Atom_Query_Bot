import discord
from discord.ext import commands

class test_cmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @ commands.command(hidden = True)
    @ commands.is_owner()
    async def showguilds(self, ctx):

        if (ctx.guild.id == 883147972337090610) :

            guild_msg = ""

            for guild in self.bot.guilds:

                guild_msg += f"{guild.name}\n"

            await ctx.send(guild_msg)
        
        else :
            
            await ctx.send("This command is not allowed on this server.", delete_after = 1)
            await ctx.channel.purge(limit = 2)

def setup(bot):
    bot.add_cog(test_cmd(bot))