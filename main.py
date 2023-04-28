import discord
import random
from bot_logic import gen_pass
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.message_content = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)
mode = "main"
health = 100
player_health = 100
shield = False
coins = 0
attack = 0
defence = 0
heal = 0


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    global mode
    global health
    global player_health
    global shield
    global coins
    global attack
    global defence
    global heal
    if message.author == bot.user:
        return
    if mode == "main":
        if message.content.startswith('$hello'):
            await message.channel.send("Hi!")
        elif message.content.startswith('$bye'):
            await message.channel.send("\\U0001f642")
        elif message.content.startswith('$fight'):
            mode = "fight"
            health = 100
            player_health = 100
            shield = False
            await message.channel.send("Сразимся?")
            await message.channel.send("Моё здоровье - " + str(health))
            await message.channel.send("Твоё здоровье - " + str(player_health))
            await message.channel.send("Атаковать - 1")
            await message.channel.send("Защищаться - 2")
            await message.channel.send("Лечиться - 3")
            await message.channel.send("Закончить - 4")
        elif message.content.startswith('$shop'):
            mode = "shop"
            await message.channel.send("Магазин:")
            await message.channel.send("Усилисть атаку - 1")
            await message.channel.send("Усилисть защиту - 2")
            await message.channel.send("Усилисть лечение - 3")
            await message.channel.send("Закончить - 4")
    elif mode == "shop":
        if message.content.startswith('1'):
            if coins >= attack + 1:
                attack += 1
                coins -= attack
                await message.channel.send("Атака повышена!")
        elif message.content.startswith('2'):
            if coins >= defence + 1:
                defence += 1
                coins -= defence
                await message.channel.send("Защита повышена!")
        elif message.content.startswith('3'):
            if coins >= heal + 1:
                heal += 1
                coins -= heal
                await message.channel.send("Лечение повышено!")
        elif message.content.startswith('4'):
            mode = "main"
            await message.channel.send("До встречи!")
            return
    elif mode == "fight":
        if message.content.startswith('1'):
            a = random.randint(1, 10) + attack
            health -= a
            await message.channel.send("Нанесено " + str(a) + " урона!")
            b = True
        elif message.content.startswith('2'):
            shield = True
            await message.channel.send("Блок готов!")
            b = True
        elif message.content.startswith('3'):
            a = random.randint(1, 10) + heal
            player_health += a
            await message.channel.send("Вылечено " + str(a) + " здоровья!")
            b = True
        elif message.content.startswith('4'):
            mode = "main"
            await message.channel.send("Сыграем в следующий раз!")
            return
        if b:
            await message.channel.send("Я атакую!")
            a = random.randint(1, 10)
            if shield:
                a -= random.randint(1, 10) - defence
                if a == 0:
                    await message.channel.send("Урон поностью блокирован!")
                elif a < 0:
                    health += a
                    await message.channel.send("Контратака! Нанесено " + str(-(a)) + " урона!")
                shield = False
            if a > 0:
                player_health -= a
                await message.channel.send("Вам нанесено " + str(a) + " урона!")
        if health <= 0:
            await message.channel.send("Вы победили!")
            mode = "main"
            coins += 1
        if player_health <= 0:
            await message.channel.send("Вы проиграли! Повезёт в следующий раз!")
            mode = "main"
        else:
            await message.channel.send("Моё здоровье - " + str(health))
            await message.channel.send("Твоё здоровье - " + str(player_health))

bot.run("Типа есть")
