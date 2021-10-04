import discord
from discord.ext import commands
from discord_slash import cog_ext

class Geometry_Calculation(commands.Cog) :
  def __init__(self, client):
    self.client = client
    self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/912c1601116f083c03ecc0a8a7b00697.png?size=128"

  @ cog_ext.cog_slash(description = "Calculate the circumference of a circle using radius.")
  async def rcircle_circumference(self,ctx,radius : float) :
    self.exp = f"2 * 22/7 * {radius}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the circumference of a circle using diameter")
  async def dcircle_circumference(self,ctx, diameter : float) :
    self.exp = f"22/7 * {diameter}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the area of a circle.")
  async def area_circle(self,ctx,radius : float) :
    self.exp = f"22/7 * {radius} ** 2"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :", value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :", value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the area of a rectangle or a square.")
  async def area_rectangle_square(self,ctx,length : float, width : float) :
    self.exp = f"{length} * {width}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the area of a triangle.")
  async def area_triangle(self,ctx,base : float, height : float) :
    self.exp = f"1/2 * {base} * {height}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the area of a parallelogram.")
  async def area_parallelogram(self,ctx,base : float, height : float) :
    self.exp = f"{base} * {height}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the area of a kite.")
  async def area_kite(self,ctx,long_diagonal : float, short_diagonal : float) :
    self.exp = f"1/2 * {long_diagonal} * {short_diagonal}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the area of a trampezium.")
  async def a_trampezium(self,ctx,first_parallel : float, second_parallel : float, height : float) :
    self.exp = f"1/2 * ({first_parallel + second_parallel}) * {height}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the surface area of a cube.")
  async def surface_area_cube(self,ctx,length : float) :
    self.exp = f"6 * {length} ** 2"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
  
  @ cog_ext.cog_slash(description = "Calculate the surface area of a cuboid.")
  async def surface_area_cuboid(self,ctx,length : float, width : float, height : float) :
    self.exp = f"2 * (({length} * {width}) + ({length} * {width}) + ({width} * {height}))"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Calculate the surface area of a pyramid.")
  async def surface_area_pyramid(self,ctx,length : float, width : float, face_height : float) :
    self.exp = f"({length*width}) + 2 * (1/2 * {face_height} * {(length/2)}) + 2 * (1/2 * {face_height} * {(width/2)})"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
  
  @ cog_ext.cog_slash(description = "Calculate the surface area of a cylinder.")
  async def surface_area_cylinder(self,ctx,radius : float, height : float) :
    self.exp = f"(2 * 22/7 * {radius} ** 2) + (2 * 22/7 * {radius} * {height})"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Calculate the surface area of a cone.")
  async def surface_area_cone(self,ctx,radius : float, slant_height : float) :
    self.exp = f"(22/7 * {radius} ** 2) + (22/7 * {radius} * {slant_height})"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Calculate the surface area of a sphere.")
  async def surface_area_sphere(self,ctx,radius : float) :
    self.exp = f"4 * 22/7 * {radius} ** 2"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Calculate the volume of a cube or a cuboid.")
  async def volume_cube_cuboid(self,ctx,length : float, width : float, height : float) :
    self.exp = f"{length} * {width} * {height}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Calculate the volume of a pyramid.")
  async def volume_pyramid(self,ctx,length : float,width : float,height : float) :
    self.exp = f"1/3 * {length} * {width} * {height}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

  @ cog_ext.cog_slash(description = "Calculate the volume of a cylinder.")
  async def volume_cylinder(self,ctx,radius : float, height : float) :
    self.exp = f"22/7 * ({radius} ** 2) * {height} "
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Calculate the volume of a cone.")
  async def volume_cone(self,ctx,radius : float, height : float) :
    self.exp = f"1/3 * 22/7 * ({radius} ** 2) * {height}"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)
    
  @ cog_ext.cog_slash(description = "Calculate the volume of a sphere.")
  async def volume_sphere(self,ctx,radius : float) :
    self.exp = f"4/3 * 22/7 * ({radius} ** 3)"
    self.evalu = f"{eval(self.exp)}"
    self.User = ctx.author
    self.embed = discord.Embed(title = "Geometry Query", colour = discord.Color.from_rgb(244, 113, 116))
    self.embed.set_author(name = f"{ctx.author.name}'s query.", icon_url = self.User.avatar_url)
    self.embed.add_field(name = "Input :",value = f"`{self.exp}`", inline = False)
    self.embed.add_field(name = "Output :" , value = f"`{self.evalu}`", inline = True)
    self.embed.set_thumbnail(url = self.link)
    await ctx.send(embed = self.embed)

def setup(client):
  client.add_cog(Geometry_Calculation(client))