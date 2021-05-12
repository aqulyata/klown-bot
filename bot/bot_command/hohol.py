import asyncio
from discord import FFmpegPCMAudio
from bot.bot_command.botcommand import BotCommand
from discord import Message


class HoholCommand(BotCommand):
    async def execute(self, msg: Message, content: str):
        if msg.author.voice:
            channel = msg.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('hohol.mp3')
            voice.play(source)
            while voice.is_playing():
                await asyncio.sleep(1)
            else:
                await asyncio.sleep(3)
                while voice.is_playing():
                    break
                else:
                    await voice.disconnect()
        else:
            await msg.channel.send('в голосовой зайди ебло)')

    def get_name(self):
        return "hohol"
