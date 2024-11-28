#pip3 install discord.py

import random
import discord
from discord.ext import commands
from config import settings

#Переменная настройки вероятности для каждого действия
v5=list(range(1,11))
v4=list(range(11,41))
v3=list(range(41,61))
v2=list(range(61,91))
v1=list(range(91,101))

intents = discord.Intents.default() #Подключаем "Разрешения"
intents.message_content = True

#Задаём префикс и интенты
bot = commands.Bot(command_prefix = settings['prefix'], intents=intents)

#Текст сообщений для действий.
a1="```diff\n+ Вы идеально совершили действие.\n(Вы можете выполнить намеренное действие) ```"
a2="```diff\n+ Вы почти справились с действием.\n(Вы можете выполнить действие, но не так идеально как хотели) ```"
a3="```md\n# Вы не смогли сделать действие.\n(Ничего не происходит, вы задумались и пропускаете ход) ```"
a4="```diff\n- Вы плохо выполнили действие.\n(Ваше действие принесло больше вреда, чем пользы) ```"
a5="```diff\n- Вы потерпели неудачу.\n(Всё, что могло пойти не так, пошло не так) ```"

#Cоздаём команду проверки работоспособности
@bot.command()
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Hello, {author.mention}!\nStatus: active\nHelp:\n !Help - Открыть подсказки. \n !dice - сделать бросок игральных костей. \n !do - проверить возможность выполнения действия.') # Выводим сообщение.

#Создаём команду help
@bot.command()
async def Help(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'{author.mention}\nHelp:\n !Help - Открыть подсказки. \n !dice - сделать бросок игральных костей. \n !do - проверить возможность выполнения действия.') # Выводим сообщение.

#Cоздаём команду игральных кубиков
@bot.command()
async def dice(ctx):
    author = ctx.message.author
    r=str(random.randint(0, 12))  #обычный рандомайзер
    r="**"+r+"**"
    await ctx.send(f'### Игрок: {author.mention} выбросил число: (' + r + ')')

#Создаём команду для действий
@bot.command()
async def do(ctx):
    author = ctx.message.author
    r1=random.randint(0, 100)  #обычный рандомайзер
    if r1 in v1:
        await ctx.send(f"{author.mention}"+a1)
    if r1 in v2:
        await ctx.send(f"{author.mention}"+a2)
    if r1 in v3:
        await ctx.send(f"{author.mention}"+a3)
    if r1 in v4:
        await ctx.send(f"{author.mention}"+a4)
    if r1 in v5:
        await ctx.send(f"{author.mention}"+a5)

# Прослушивание трафика
#@bot.event
#async def on_message(message):
#    print('Message from {0.author}: {0.content}'.format(message))

bot.run(settings['token']) #Запуск Бота
