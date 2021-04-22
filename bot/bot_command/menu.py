import discord
#from discord.ext.commands import bot
from bot.bot_command.botcommand import BotCommand


class MenuCommand(BotCommand):
    async def execute(self, message):
        page1 = discord.Embed(
            title='Page 1/9',
            description=">ржака - выдает рандомный анекдот из списка 'anekdoty'",
            colour=discord.Colour.orange()
        )
        page2 = discord.Embed(
            title='Page 2/9',
            description=">рофл - рандомный анекдот в виде jpg",
            colour=discord.Colour.orange()
        )
        page3 = discord.Embed(
            title='Page 3/9',
            description=">абоба - завершение работы бота и запись взаимодействия с ним в json файл",
            colour=discord.Colour.orange()
        )
        page4 = discord.Embed(
            title='Page 4/9',
            description=">kick - выгнать участника с сервера через тег(@),(необходимо иметь определенные разрешения)",
            colour=discord.Colour.orange()
        )
        page5 = discord.Embed(
            title='Page 5/9',
            description=">ban - забанить участника на сервере через тег(@),(необходимо иметь определенные разрешения)",
            colour=discord.Colour.orange()
        )
        page6 = discord.Embed(
            title='Page 6/9',
            description=">hohol - изгоните хохла из своего голосового канала",
            colour=discord.Colour.orange()
        )
        page7 = discord.Embed(
            title='Page 7/9',
            description=">monke - мартышки для всех желающих",
            colour=discord.Colour.orange()
        )
        page8 = discord.Embed(
            title='Page 8/9',
            description=">dog/>fox - рандомная картинка собаки или лисы",
            colour=discord.Colour.orange()
        )
        page9 = discord.Embed(
            title='Page 9/9',
            description="у бота есть несколько скрытых мини функций, о который я вам не скажу)))",
            colour=discord.Colour.orange()
        )
        pages = [page1, page2, page3, page4, page5, page6, page7, page8, page9]

        message = await message.channel.send(embed=page1)
        await message.add_reaction('⏮')
        await message.add_reaction('◀')
        await message.add_reaction('▶')
        await message.add_reaction('⏭')

        def check(reaction, user):
            return user == message.author

        i = 0
        reaction = None

        # while True:
        #     if str(reaction) == '⏮':
        #         i = 0
        #         await message.edit(embed=pages[i])
        #     elif str(reaction) == '◀':
        #         if i > 0:
        #             i -= 1
        #             await message.edit(embed=pages[i])
        #     elif str(reaction) == '▶':
        #         if i < 8:
        #             i += 1
        #             await message.edit(embed=pages[i])
        #     elif str(reaction) == '⏭':
        #         i = 8
        #         await message.edit(embed=pages[i])

        #     try:
        #         reaction, user = await bot.wait_for('reaction_add', timeout=30.0, check=check)
        #         await message.remove_reaction(reaction, user)
        #     except:
        #         break
        #
        # await message.clear_reactions()

    def get_name(self):
        return "menu"