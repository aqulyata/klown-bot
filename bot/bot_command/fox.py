import json
import discord
import requests
from bot.bot_command.botcommand import BotCommand
from discord import Message


class FoxCommand(BotCommand):
    async def execute(self, msg: Message, content: str):
        response = requests.get('https://some-random-api.ml/img/fox')
        json_data = json.loads(response.text)
        embed = discord.Embed(color=0xff9900, title='Random Fox')
        embed.set_image(url=json_data['link'])
        await msg.channel.send(embed=embed)

    def get_name(self):
        return "fox"
