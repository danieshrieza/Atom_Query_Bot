import discord
from discord.ext import commands
from discord_slash import cog_ext

class help() :

  def __init__(self, client) :
    self.client = client
    super().__init__()

  async def helpCommand(self):
      self.embed = discord.Embed(title = "Command List`")
      self.embed.add_field()