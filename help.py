import nextcord
from nextcord.ext import commands

# For test currently
class CustomHelpCommand(commands.DefaultHelpCommand):


    def __init__(self) :
        super().__init__()


    async def send_bot_help(self, mapping) :

        info_board = nextcord.Embed(
            title = f"{self.context.bot.user.display_name}",
            colour = nextcord.Colour.blurple()
        )

        info_board.set_footer(text = f"{self.context.bot.user.display_name}")

        info_board.add_field(name = "\u200B", value="\u200B", inline=False)

        for cog, commands_list in mapping.items() :

            if not cog or not commands_list :
                continue

            info_board.add_field(
                name = f"{cog.qualified_name}",
                value = cog.description or "No description added",
                inline = False)

            undo = True

            for command in commands_list :

                if await command.can_run(self.context) :

                    info_board.add_field(
                        name = f"{command}",
                        value = command.help or "No description added",
                        inline = True
                    )

                    undo = False

            if undo :

                info_board.remove_field(-1)
            
            info_board.add_field(name = "\u200B", value = "\u200B", inline = False)

        else:

            while info_board.fields[-1].name == "\u200b" :

                info_board.remove_field(-1)

        await self.context.send(embed = info_board)

        return await self.context.send(embed = info_board)