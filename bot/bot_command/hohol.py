import asyncio
from discord import FFmpegPCMAudio
from bot.bot_command.botcommand import BotCommand


class HoholCommand(BotCommand):
    async def execute(self, message):
        if message.author.voice:
            channel = message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('hohol.mp3')
            player = voice.play(source)
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)
            player.stop()
            await voice.disconnect()
        else:
            await message.channel.send('в голосовой зайди ебло)')

    def get_name(self):
        return "hohol"