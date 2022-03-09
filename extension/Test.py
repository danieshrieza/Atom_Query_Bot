from nextcord.ext import commands
from config import GUILD_ID
from nextcord import Interaction, slash_command, SlashOption

class Test(commands.Cog):
    
    
    def __init__(self, bot: commands.Bot):
        self.bot=bot
     
        
    @ slash_command(guild_ids=[GUILD_ID])
    async def test(interaction: Interaction, option: SlashOption(choices={"name": str})):
        
        if option == "name":
            
            await interaction.response.send_message(f"Hello, {option}")
        
        else:
            
            await interaction.response.send_message("Hello")
            
    
def setup(bot: commands.Bot):
    bot.add_cog(Test(bot))