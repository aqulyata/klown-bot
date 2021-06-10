import sys
from io import BytesIO

import discord
from bot.bot_command.botcommand import BotCommand
from PIL import Image, ImageFont, ImageDraw
import os
import random

from bot.bot_command.monke import MonkeCommand


class PhotoCommand(BotCommand):
    async def execute(self, message):
        random_image_path = random.choice(MonkeCommand.get_images_from_folder(r'C:\Users\Роман\klown-bot\images'))
        with Image.open(random_image_path) as im:
            drawing = ImageDraw.Draw(im)
            font = ImageFont.truetype(r'arial.ttf', 45)
            drawing.line((0, 0) + im.size, fill=128)
            drawing.line((0, im.size[1], im.size[0], 0), fill=128)
            img_byte_arr = BytesIO()
            drawing.text(
                (100, 100),
                text='monkey?',
                fill='#1C0606',
                font=font
            )
           # im.show()
            im.save(img_byte_arr, format='PNG')
            img_byte_arr.seek(0)
            await message.channel.send(file=discord.File(img_byte_arr, filename="Test.png"))

    def get_name(self):
        return "Photo"
