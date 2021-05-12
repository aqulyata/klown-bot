from abc import abstractmethod
from discord import Message


class BotCommand:

    @abstractmethod
    async def execute(self, msg: Message, content: str):
        ...

    @abstractmethod
    def get_name(self):
        ...

    async def check_args(self, msg: Message, content: str):
        if content is None:
            await msg.channel.send("пiшов нахуй, чо искати?")
            return False
        return True
