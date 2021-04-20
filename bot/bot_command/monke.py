import random
import discord
from bot.bot_command.botcommand import BotCommand
import os


class MonkeCommand(BotCommand):
    async def execute(self, message):
        random_image = random.choice(self.get_images_from_folder())
        await message.channel.send(file=discord.File(random_image))

    def get_name(self):
        return "monke"

    def get_images_from_folder(self, path_to_folder=r'C:\Users\stas_mashina\Documents\dz\klown-bot\images'):
        files = os.listdir(path_to_folder)
        images = filter(lambda x: x.endswith('.jpg'), files)
        images_paths = list(map(lambda image: f'{path_to_folder}\\{image}', images))
        return images_paths
