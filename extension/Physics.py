from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, slash_command


# NOTE : Class for Physics
class Physics(commands.Cog):


    # NOTE : Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command to calculate moment of force of an object
    @ slash_command(
        description="Calculate the moment of force of an object."
    )
    async def moment_of_force(self, interaction: Interaction, force: float, perpendicular_distance: float):

        exp=f"{force} N × {perpendicular_distance} m "
        evalu=force*perpendicular_distance

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} Nm \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate the pressure acts on an object
    @ slash_command(
        description="Calculate the pressure acts on an object."
    )
    async def pressure(self, interaction: Interaction, force: float, surface_area: float):

        exp=f"{force} N ÷ {surface_area} m²"
        evalu=force/surface_area

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )
        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} N/m² \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate the density of an object
    @ slash_command(
        description="Calculate the density of an object."
    )
    async def density(self, interaction: Interaction, mass: float, volume: float):

        exp=f'{mass} g ÷ {volume} cm³'
        evalu=mass/volume

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} g/cm³ \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate the work done of an object
    @ slash_command(
        description="Calculate the work done of an object."
    )
    async def work_done(self, interaction: Interaction, force: float, distance: float):

        exp=f'{force} N × {distance} m'
        evalu=force*distance

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate the power possessed by an object
    @ slash_command(
        description="Calculate the power possessed by an object."
    )
    async def power(self, interaction: Interaction, force: float, distance: float, time: float):

        exp=f'({force} N × {distance} m) ÷ {time} s'
        evalu=(force*distance)/time

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} W \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate the gravitational potential energy possessed by an object
    @ slash_command(
        description="Calculate the gravitational potential energy possessed by an object."
    )
    async def gravitational_energy(self, interaction: Interaction, mass: float, distance: float):

        exp=f'{mass} kg × 9.8 m/s × {distance} m'
        evalu=mass*9.8*distance

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate the elastic potential energy possessed by an object
    @ slash_command(
        description="Calculate the elastic potential energy possessed by an object."
    )
    async def elastic_energy(self, interaction: Interaction, force: float, original_length: float, new_length: float):

        exp=f'1/2 × {force} N × ({original_length} - {new_length}) m'
        evalu=(1/2)*(force*(original_length-new_length))

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate the kinetic energy possessed by an object
    @ slash_command(
        description="Calculate the kinetic energy possessed by an object."
    )
    async def kinetic_energy(self, interaction: Interaction, mass: float, distance: float, time: float):

        exp=f'1/2 × {mass} kg × ({distance / time} m/s)²'
        evalu=(1/2)*mass*(distance/time)**2

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)
        
        
    # NOTE : Command to calculate speed of an object
    @ slash_command(
        description="Calculate the speed of an object."
    )
    async def speed(self, interaction: Interaction, distance: float, time: float):

        exp=f"{distance} ÷ {time}"
        evalu=distance/time

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} m/s \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate electric current of an object
    @ slash_command(
        description="Calculate the electric current of an object."
    )
    async def electric_current(self, interaction: Interaction, electric_voltage: float, electric_resistance: float):

        exp=f"{electric_voltage} V ÷ {electric_resistance} Ω"
        evalu=electric_voltage/electric_resistance

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} A \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate electric voltage of an object
    @ slash_command(
        description="Calculate the electric voltage of an object."
    )
    async def electric_voltage(self, interaction: Interaction, electric_current: float, electric_resistance: float):

        exp=f"{electric_current} A × {electric_resistance} Ω"
        evalu=electric_current*electric_resistance

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} V \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to calculate electric resistance of an object
    @ slash_command(
        description="Calculate the electric resistance of an object."
    )
    async def electric_resistance(self, interaction: Interaction, electric_voltage: float, electric_current: float):

        exp=f"{electric_voltage} V ÷ {electric_current} A"
        evalu=electric_voltage/electric_current

        embed=nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {exp} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {evalu} Ω \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


# NOTE : Add Physics to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Physics(bot))
