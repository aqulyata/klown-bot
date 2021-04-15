import asyncio
from discord import FFmpegPCMAudio
from bot.command.command import Command
from bot.klown import id_deb


class HoholCommand(Command):
    async def execute(self, ctx):
        if ctx.author.id in id_deb:
             ctx.channel.send('соси')
        elif ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            source = FFmpegPCMAudio('hohol.mp3')
            player = voice.play(source)
            player.start()
            while not player.is_done():
                await asyncio.sleep(1)
            player.stop()
            await voice.disconnect()
        else:
            await ctx.send('в голосовой зайди ебло)')

    def get_name(self):
        return "hohol"