from discord.ext import commands
from bot.bot_command.botcommand import BotCommand


class AbobaCommand(BotCommand):
    @commands.is_owner()
    async def execute(self, msg):
        await msg.bot.logout()

    def get_name(self):
        return "aboba"
