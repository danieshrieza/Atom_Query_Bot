from datetime import datetime, timezone
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption, slash_command
from config import GUILD_ID


class Physics(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.link = "https://cdn.discordapp.com/app-icons/881526346411556865/8d9f1ba8cc150ebe85cf9e9f1a7fc345.png?size=128"

    @ slash_command(
        description="Calculate the pressure acts on an object.",
        guild_ids=[GUILD_ID]
    )
    async def pressure(self, interaction: Interaction, F: float = SlashOption(description="The force exerted on the surface."), A: float = SlashOption(description="The surface area of the surface.")):

        formula = "P = F / A"
        P = F / A

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {P} N/m² \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the density of an object.",
        guild_ids=[GUILD_ID]
    )
    async def density(self, interaction: Interaction, m: float = SlashOption(description="The mass of the object."), V: float = SlashOption(description="The volume of the object.")):

        formula = 'p = m / V'
        p = m / V

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {p} g/cm³ \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the work done of an object.",
        guild_ids=[GUILD_ID]
    )
    async def workdone(self, interaction: Interaction, F: float = SlashOption(description="The force exerted to push/pull the object."), d: float = SlashOption(description="The distance that the object travelled from the push/pull.")):

        formula = 'W = Fd'
        W = F * d

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {W} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the power possessed by an object.",
        guild_ids=[GUILD_ID]
    )
    async def power(self, interaction: Interaction, W: float = SlashOption(description="The work done of the object."), t: float = SlashOption(description="The time taken to carry out the action.")):

        formula = 'P = W / t'
        P = W / t

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {P} W \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the gravitational potential energy possessed by an object.",
        guild_ids=[GUILD_ID]
    )
    async def gravitationalenergy(self, interaction: Interaction, m: float = "The mass of the object.", h: float = SlashOption(description="The height the object lifted to from the ground/")):

        formula = 'U = mgh'
        U = m * 9.81 * h

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {U} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the elastic potential energy possessed by an object.",
        guild_ids=[GUILD_ID]
    )
    async def elasticenergy(self, interaction: Interaction, F: float = SlashOption(description="The force exerted to push/pull the object."), x: float = SlashOption(description="The difference in length before and after compression or expansion.")):

        formula = "U = 1/2 Fx"
        U = (1 / 2) * (F * x)

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {U} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the kinetic energy possessed by an object.",
        guild_ids=[GUILD_ID]
    )
    async def kineticenergy(self, interaction: Interaction, m: float = SlashOption(description="The mass of the object."), v: float = SlashOption(description="The velocity of the object.")):

        formula = "K = 1/2 mv²"
        K = (1 / 2) * (m * v ** 2)

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {K} J \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the velocity of an object.",
        guild_ids=[GUILD_ID]
    )
    async def velocity(self, interaction: Interaction, s: float = SlashOption(description="The displacement from the starting point."), t: float = SlashOption(description="The time taken to travel from starting point.")):

        formula = "v = s / t"
        v = s / t

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {v} m/s \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the accelaration of an object.",
        guild_ids=[GUILD_ID]
    )
    async def accelaration(self, interaction: Interaction, v: float = SlashOption(description="The final velocity after accelaration."), u: float = SlashOption(description="The initial velocity before accelaration."), t: float = SlashOption(description="The time taken for the inital velocity to accelarate to the final velocity.")):

        formula = "a = (v - u) / t"
        a = (v - u) / t

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {a} m/s² \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the momentum of an object.",
        guild_ids=[GUILD_ID]
    )
    async def momentum(self, interaction: Interaction, m: float = SlashOption(description="The mass of the object."), v: float = SlashOption(description="The velocity of the object.")):

        formula = "p = mv"
        p = m * v

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {p} Ns \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the impulse possesed by an object.",
        guild_ids=[GUILD_ID]
    )
    async def impulse(self, interaction: Interaction, mv: float = SlashOption(description="The final momentum after change in momentum."), mu: float = SlashOption(description="The initial change before change in momentum.")):

        formula = "I = mv - mu"
        I = mv - mu

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {I} Ns \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)

    @ slash_command(
        description="Calculate the weight of an object.",
        guild_ids=[GUILD_ID]
    )
    async def weight(self, interaction: Interaction, m: float = SlashOption(description="The mass of the object.")):

        formula = "W = mg"
        W = m * 9.81

        embed = nextcord.Embed(
            title="Physics Query",
            description="The requested `Physics Query` have been evaluated by **Atom Query**",
            timestamp=nextcord.utils.format_dt(
                dt=datetime.now(timezone.utc), style="f"),
            colour=nextcord.Color.from_rgb(127, 0, 255)
        )

        embed.add_field(
            name="Input :",
            value=f"```Python\n {formula} \n```",
            inline=False
        )

        embed.add_field(
            name="Output :",
            value=f"```Python\n {W} N \n```",
            inline=True
        )

        embed.set_thumbnail(url=self.link)

        await interaction.response.send_message(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(Physics(bot))
