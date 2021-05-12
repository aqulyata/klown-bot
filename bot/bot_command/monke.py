import random
import discord
from bot.bot_command.botcommand import BotCommand
import os
from discord import Message


class MonkeCommand(BotCommand):
    async def execute(self, msg: Message, content: str):
        random_image = random.choice(self.get_images_from_folder())
        await msg.channel.send(file=discord.File(random_image))

    def get_name(self):
        return "monke"

    @staticmethod
    def get_images_from_folder(path_to_folder=r'C:\Users\stas_mashina\Documents\dz\klown-bot\images'):
        files = os.listdir(path_to_folder)
        images = filter(lambda x: x.endswith('.jpg'), files)
        images_paths = list(map(lambda image: f'{path_to_folder}\\{image}', images))
        return images_paths
