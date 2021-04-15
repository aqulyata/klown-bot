import random
import discord
from bot.command.command import Command
from bot.klown import id_deb

images = ['./images/6quii5Zg_400x400.jpg', './images/M-YnMbnh_400x400.jpg', './images/aMLNBRcbuSo.jpg']
open(images[0])

class Monke(Command):
    async def execute(self, ctx):
        if ctx.author.id in id_deb:
            await ctx.channel.send('соси')
        else:
            random_image = random.choice(images)
            await ctx.send(file=discord.File(random_image))

    def get_name(self):
        return "monke"