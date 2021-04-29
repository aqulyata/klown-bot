import asyncio
from discord import FFmpegPCMAudio
from bot.bot_command.botcommand import BotCommand


class HoholCommand(BotCommand):
    async def execute(self, msg):
        if msg.author.voice:
            channel = msg.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('hohol.mp3')
            voice.play(source)
            while voice.is_playing():  # Checks if voice is playing
                await asyncio.sleep(1)  # While it's playing it sleeps for 1 second
            else:
                await asyncio.sleep(3)  # If it's not playing it waits 15 seconds
                while voice.is_playing():  # and checks once again if the bot is not playing
                    break  # if it's playing it breaks
                else:
                    await voice.disconnect()  # if not it disconnects
        else:
            await msg.channel.send('в голосовой зайди ебло)')

    def get_name(self):
        return "hohol"