from bot.bot_command.botcommand import BotCommand
import urllib
from urllib import request
from urllib.parse import quote
import re
from discord import Message


class FindYoutubeCommand(BotCommand):
    async def execute(self, msg: Message, content: str):
        if not await self.check_args(msg, content):
            return
        mas = []
        sq = 'https://www.youtube.com/results?search_query=' + quote(content)
        doc = urllib.request.urlopen(sq).read().decode('cp1251', errors='ignore')
        match = re.findall("\?v\=(.+?)\"", doc)
        if not (match is None):
            for ii in match:
                if len(ii) < 25:
                    mas.append(ii)
        mas = dict(zip(mas, mas)).values()
        mas2 = []
        for y in mas: mas2.append('https://www.youtube.com/watch?v=' + y)
        await msg.channel.send(mas2)

    def get_name(self):
        return "find"
