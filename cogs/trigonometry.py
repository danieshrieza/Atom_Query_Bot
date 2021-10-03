import discord
from discord.ext import commands
import math
from discord_slash import cog_ext

class Trigonometry_Calculation(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

  @ cog_ext.cog_slash(description = "Calculate the sine of a triangle.")
  async def sin(self,ctx, number : float):
    self.exp = f"sin({number})"
    self.evalu = f"{math.sin(number)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the cosine of a triangle.")
  async def cos(self,ctx, number : float):
    self.exp = f"cos({number})"
    self.evalu = f"{math.cos(number)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the tangent of a triangle.")
  async def tan(self,ctx, number : float):
    self.exp = f"tan({number})"
    self.evalu = f"{math.tan(number)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the Pythagoras Theorem.")
  async def pythagoras_theorem(self,ctx, height : float, base : float, hypotenuse : float):
    if hypotenuse == 0 :
      self.exp = f"(({base} ** 2) + ({height} ** 2)) ** 1/2"
      self.evalu = f"{math.sqrt((base ** 2) + (height ** 2))}"
      self.User = ctx.author
      self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
      self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
      self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
      self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
      self.embed.set_thumbnail(url = self.link)
      await ctx.send(embed = self.embed)
    elif height == 0 :
      if hypotenuse > base :
        self.exp = f"(({hypotenuse} ** 2) - ({base} ** 2)) ** 1/2"
        self.evalu = f"{math.sqrt((hypotenuse ** 2) - (base ** 2))}"
        self.User = ctx.author
        self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)
      else :
        self.exp = f"(({base} ** 2) - ({hypotenuse} ** 2)) ** 1/2"
        self.evalu = f"{math.sqrt((base ** 2) - (hypotenuse ** 2))}"
        self.User = ctx.author
        self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)
    elif base == 0 :
      if hypotenuse > height :
        self.exp = f"(({hypotenuse} ** 2) - ({height} ** 2)) ** 1/2"
        self.evalu = f"{math.sqrt((hypotenuse ** 2) - (height ** 2))} "
        self.User = ctx.author
        self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)
      else :
        self.exp = f"(({height} ** 2) - ({hypotenuse} ** 2)) ** 1/2"
        self.evalu = f"{math.sqrt((height ** 2) - (hypotenuse ** 2))}"
        self.User = ctx.author
        self.embed = discord.Embed(title = "Trigonometry Query", colour = discord.Color.from_rgb(147, 202, 237))
        self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
        self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
        self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
        self.embed.set_thumbnail(url = self.link)
        await ctx.send(embed = self.embed)

def setup(client):
  client.add_cog(Trigonometry_Calculation(client))