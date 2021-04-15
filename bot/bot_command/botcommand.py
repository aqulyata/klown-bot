from discord import Message


class BotCommand:

    async def execute(self, msg: Message):
        ...

    def get_name(self):
        ...
