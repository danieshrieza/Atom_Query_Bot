import discord
from discord.ext import commands
from discord_slash import cog_ext
from fraction import Fraction

# ! <--- Class for Unit_Converter
class Unit_Converter(commands.Cog):

  """
  Unit_Converter is a class that contains unit conversion commands.

  Commands :
  ----------
  mm_cm : return `str` embed

  cm_m : return `str` embed

  m_km : return `str` embed

  km_m : return `str` embed

  m_cm : return `str` embed

  g_kg : return `str` embed

  kg_g : return `str` embed

  ml_l : return `str` embed

  l_ml : return `str` embed

  frac_decimal : return `str` embed

  decimal_frac : return `str` embed
  """

  # ? <---  Initialize variable for class
  def __init__(self, client):
    self.client = client
    self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

  # ? <--- Command to convert mm to cm
  @ cog_ext.cog_slash(description = "Convert milimeter to centimeter.")
  async def mm_cm(self,ctx,milimeter : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{milimeter}` mm", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{milimeter/10}` cm", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to convert cm to m
  @ cog_ext.cog_slash(description = "Convert centimeter to meter.")
  async def cm_m(self,ctx,centimeter : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{centimeter}` cm", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{centimeter/100}` m", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to m to km
  @ cog_ext.cog_slash(description = "Convert meter to kilometer.")
  async def m_km(self,ctx,meter : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{meter}` m", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{meter/1000}` km", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to km to m
  @ cog_ext.cog_slash(description = "Convert kilometer to meter.")
  async def km_m(self,ctx,kilometer : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{kilometer}` km", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{kilometer * 1000}` m", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to convert m to cm
  @ cog_ext.cog_slash(description = "Convert meter to centimeter.")
  async def m_cm(self,ctx,meter : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{meter}` m", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{meter * 100}` cm", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  # ? <--- Command to convert cm to mm
  @ cog_ext.cog_slash(description = "Convert centimeter to milimeter.")
  async def cm_mm(self,ctx,centimeter : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{centimeter}` cm", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{centimeter * 10}` mm", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command convert g to kg
  @ cog_ext.cog_slash(description = "Convert gram to kilogram.")
  async def g_kg(self,ctx,gram : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{gram}` g", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{gram / 1000}` kg", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to convert kg to g
  @ cog_ext.cog_slash(description = "Convert kilogram to gram.")
  async def kg_g(self,ctx,kilogram : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{kilogram}` kg", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{kilogram * 1000}` g", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to convert ml to l
  @ cog_ext.cog_slash(description = "Convert mililitre to litre.")
  async def ml_l(self,ctx,mililitre : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{mililitre}` ml", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{mililitre/1000}` l", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to convert l to ml
  @ cog_ext.cog_slash(description = "Convert litre to mililitre.")
  async def l_ml(self, ctx, litre : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{litre}` l", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{litre * 1000}` ml", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to convert decimal to fraction
  @ cog_ext.cog_slash(description = "Convert a decimal number to fraction.")
  async def decimal_fraction(self, ctx, decimal : float) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{decimal}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{Fraction(str(decimal)).limit_denominator()}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  # ? <--- Command to convert fraction to decimal
  @ cog_ext.cog_slash(description = "Convert a fraction value to a decimal number.")
  async def fraction_decimal(self,ctx, numerator : int, denominator : int) :
    self.user = ctx.author
    self.embed = discord.Embed(title = "Unit Converter", colour = discord.Color.from_rgb(238, 238, 155))
    self.embed.set_author(name = f"{self.user.name}'s query.", icon_url = self.user.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{numerator}/{denominator}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{numerator/denominator}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

# ! <--- Add Unit_Converter into the bot
def setup(client):
  client.add_cog(Unit_Converter(client))