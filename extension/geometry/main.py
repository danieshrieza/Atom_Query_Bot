from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, slash_command


# NOTE : Class for SurfaceAndVolume
class SurfaceAndVolume(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate surface area of a quadrilateral
    @ slash_command(
        description="Calculate the surface area of a cuboid."
    )
    async def surface_area_quadrilateral(self, interaction: Interaction, length: float, width: float, height: float):

        exp=f"2({length} × {width}) + 2({length} × {height}) + 2({width} × {height})"
        evalu=2*(length*width)+2*(length*height)+2*(width*height)

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate surface area of pyramid
    @ slash_command(
        description="Calculate the surface area of a pyramid."
    )
    async def surface_area_pyramid(self, interaction: Interaction, length: float, width: float, face_height: float):

        exp=f"2(1/2 × {face_height} × {length/2}) + 2(1/2 × {face_height} × {width/2}) + ({length} × {width})"
        evalu=2*((1/2)*face_height*(length/2))+2*((1/2)*face_height*(width/2))+(length*width)

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate surface area of a cylinder
    @ slash_command(
        description="Calculate the surface area of a cylinder."
    )
    async def surface_area_cylinder(self, interaction: Interaction, height: float, radius: float):

        exp=f"2 × 22/7 × {radius}² + 2 × 22/7 × {radius} × {height}"
        evalu=2*(22/7)*(radius**2)+2*(22/7)*radius*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate surface area of a cone
    @ slash_command(
        description="Calculate the surface area of a cone."
    )
    async def surface_area_cone(self, interaction: Interaction, slant_height: float, radius: float):

        exp=f"22/7 × {radius}² + 22/7 × {radius} × {slant_height}"
        evalu=(22/7)*(radius**2)+(22/7)*radius*slant_height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculte surface area of a sphere
    @ slash_command(
        description="Calculate the surface area of a sphere."
    )
    async def surface_area_sphere(self, interaction: Interaction, radius: float):

        exp=f"4 × 22/7 × {radius}²"
        evalu=4*(22/7)*(radius**2)

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate volume of a cube or a cuboid
    @ slash_command(
        description="Calculate the volume of a cube or a cuboid."
    )
    async def volume_quadrilateral(self, interaction: Interaction, length: float, width: float, height: float):

        exp=f"{length} × {width} × {height}"
        evalu=length*width*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate volume of a pyramid
    @ slash_command(
        description="Calculate the volume of a pyramid."
    )
    async def volume_pyramid(self, interaction: Interaction, length: float, width: float, height: float):

        exp=f"1/3 × {length} × {width} × {height}"
        evalu=(1/3)*length*width*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate volume of a cylinder
    @ slash_command(
        description="Calculate the volume of a cylinder."
    )
    async def volume_cylinder(self, interaction: Interaction, height: float, radius: float):

        exp=f"22/7 × {radius}² × {height}"
        evalu=(22/7)*(radius**2)*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate volume of a cone
    @ slash_command(
        description="Calculate the volume of a cone."
    )
    async def volume_cone(self, interaction: Interaction, height: float, radius: float):

        exp=f"1/3 × 22/7 × {radius}² × {height}"
        evalu=(1/3)*(22/7)*(radius**2)*height

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate volume of a sphere
    @ slash_command(
        description="Calculate the volume of a sphere."
    )
    async def volume_sphere(self, interaction: Interaction, radius: float):

        exp=f"4/3 × 22/7 × {radius}²"
        evalu=(4/3)*(22/7)*(radius**2)

        embed=nextcord.Embed(
            title="Geometry Query",
            description="The requested `Geometry Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(157, 34, 53)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


# NOTE : Add SurfaceAndVolume to the bot
def setup(bot: commands.Bot):
    bot.add_cog(SurfaceAndVolume(bot))
