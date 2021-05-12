import requests
from bot.bot_command.botcommand import BotCommand
from discord import Message
import re


class AnekParserCommand(BotCommand):
    def __init__(self):
        self.pattern = re.compile(r'JSON\.parse\(\'\[\\\"(.{1,})\\\"\]\'\);')

    async def execute(self, msg: Message, content: str):

        r = requests.get('https://www.anekdot.ru/rss/randomu.html')
        if r.status_code == 200:
            r.encoding = 'utf-8'
            perem = r.text
            anekdot = self.find_text(text=perem)
            if anekdot is not None:
                anekdot = anekdot.replace('<br>', "\n")
                # anekdot = anekdot.replace('\\",\\"', "\n*")
                anekdot = anekdot.replace('\\\\\"', "\"")
                anekdots = anekdot.split('\\",\\"')
                result = ''
                for i in range(len(anekdots)):
                    result += f'{i + 1}: {anekdots[i]}\n'
                await msg.channel.send(result)

    def get_name(self):
        return "humor"

    def find_text(self, text):
        result = self.pattern.findall(text)
        if len(result) > 0:
            return result[0]
        return None
