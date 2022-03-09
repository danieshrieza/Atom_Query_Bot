from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from fraction import Fraction
from nextcord import Interaction, slash_command


# NOTE : Class for Converter
class Converter(commands.Cog):


    # NOTE :  Initialize parameter for class
    def __init__(self, bot: commands.Bot):
        self.bot=bot
        self.link="https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"


    # NOTE : Command convert g to kg
    @ slash_command(
        description="Convert gram to kilogram."
    )
    async def g_to_kg(self, interaction: Interaction, gram: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {gram} g \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {gram/1000} kg \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert kg to g
    @ slash_command(
        description="Convert kilogram to gram."
    )
    async def kg_to_g(self, interaction: Interaction, kilogram: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {kilogram} kg \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {kilogram*1000} g \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert ml to l
    @ slash_command(
        description="Convert mililitre to litre."
    )
    async def ml_to_l(self, interaction: Interaction, millilitre: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {millilitre} ml \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {millilitre/1000} l \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert l to ml
    @ slash_command(
        description="Convert litre to mililitre."
    )
    async def l_to_ml(self, interaction: Interaction, litre: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {litre} l \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {litre*1000} ml \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert decimal to fraction
    @ slash_command(
        description="Convert a decimal number to fraction."
    )
    async def deci_to_frac(self, interaction: Interaction, decimal: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {decimal} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {Fraction(str(decimal))} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert fraction to decimal
    @ slash_command(
        description="Convert a fraction value to a decimal number."
    )
    async def frac_to_deci(self, interaction: Interaction, numerator: int, denominator: int):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {numerator}/{denominator} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {numerator/denominator} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert Newton to kilogram
    @ slash_command(
        description="Convert Newton to kilogram."
    )
    async def N_to_kg(self, interaction: Interaction, newton: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {newton} N \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {newton/9.8} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert kg to Newton
    @ slash_command(
        description="Convert kilogram to Newton."
    )
    async def kg_to_N(self, interaction: Interaction, kilogram: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {kilogram} kg \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {kilogram * 9.8} \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert Astronomical Unit to kilometer
    @ slash_command(
        description="Convert Astronomical Unit to kilometer."
    )
    async def au_to_km(self, interaction: Interaction, au: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {au} A.U \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {au*(1.5*10**8)} km \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert kilometer to Astronomical Unit
    @ slash_command(
        description="Convert kilometer to Astronomical Unit."
    )
    async def km_to_au(self, interaction: Interaction, km: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {km} km \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {km/(1.5*10**8)} A.U \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert Light Year to kilometer
    @ slash_command(
        description="Convert Light Year to kilometer."
    )
    async def ly_to_km(self, interaction: Interaction, ly: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {ly} ly \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {ly*(9.5*10**12)} km \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert kilometer to Light Year
    @ slash_command(
        description="Convert kilometer to Light Year."
    )
    async def km_to_ly(self, interaction: Interaction, km: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {km} km \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {km/(9.5*10**12)} km \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert mm to cm
    @ slash_command(
        description="Convert milimeter to centimeter."
    )
    async def mm_to_cm(self, interaction: Interaction, milimeter: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {milimeter} mm \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {milimeter/10} cm \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert cm to m
    @ slash_command(
        description="Convert centimeter to meter."
    )
    async def cm_to_m(self, interaction: Interaction, centimeter: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {centimeter} cm \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {centimeter/100} m \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to m to km
    @ slash_command(
        description="Convert meter to kilometer."
    )
    async def m_to_km(self, interaction: Interaction, meter: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {meter} m \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {meter/1000} km \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to km to m
    @ slash_command(
        description="Convert kilometer to meter."
    )
    async def km_to_m(self, interaction: Interaction, kilometer: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {kilometer} km \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {kilometer*1000} m \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert m to cm
    @ slash_command(
        description="Convert meter to centimeter."
    )
    async def m_to_cm(self, interaction: Interaction, meter: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {meter} m \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {meter*100} cm \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


    # NOTE : Command to convert cm to mm
    @ slash_command(
        description="Convert centimeter to milimeter."
    )
    async def cm_to_mm(self, interaction: Interaction, centimeter: float):

        embed=nextcord.Embed(
            title="Unit Converter",
            description="The requested `Unit Conversion` have been evaluated by **Atom Query**",
            timestamp=datetime.now(timezone.utc),
            colour=nextcord.Color.from_rgb(178, 34, 34)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {centimeter} cm \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {centimeter*10} mm \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


# NOTE : Add Converter to the bot
def setup(bot: commands.Bot):
    bot.add_cog(Converter(bot))
