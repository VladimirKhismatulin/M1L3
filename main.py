import discord
import random
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
mode = "main"
health = 100
player_health = 100
shield = False

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global mode
    global health
    global player_health
    global shield
    if message.author == client.user:
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
            message.channel.send("Моё здоровье -" + health)
            message.channel.send("Твоё здоровье -" + player_health)
            message.channel.send("Атаковать - 1")
            message.channel.send("Защищаться - 2")
            message.channel.send("Лечиться - 3")
            message.channel.send("Закончить - 4")
    elif mode == "fight":
        if message.content.startswith('1'):
            a = random.randint(1, 10)
            health -= a
            await message.channel.send("Нанесено" + a + "урона!")
            b = True
        elif message.content.startswith('2'):
            shield = True
            await message.channel.send("Блок готов!")
            b = True
        elif message.content.startswith('3'):
            a = random.randint(1, 10)
            player_health += a
            await message.channel.send("Вылечено" + a + "здоровья!")
            b = True
        elif message.content.startswith('4'):
            mode = "main"
            await message.channel.send("Сыграем в следующий раз!")
            return
        if b:
            await message.channel.send("Я атакую!")
            a = random.randint(1, 10)
            if shield:
                a -= random.randint(1, 10)
                if a == 0:
                    await message.channel.send("Урон поностью блокирован!")
                elif a < 0:
                    health += a
                    await message.channel.send("Контратака! Нанесено" + (-(a)) + "урона!")
                shield = False
            if a > 0:
                player_health -= a
                await message.channel.send("Вам нанесено" + a + "урона!")
        if health <= 0:
            await message.channel.send("Вы победили!")
            mode = "main"
        if player_health <= 0:
            await message.channel.send("Вы проиграли! Повезёт в следующий раз!")
            mode = "main"
        else:
            message.channel.send("Моё здоровье -" + health)
            message.channel.send("Твоё здоровье -" + player_health)
            message.channel.send("Атаковать - 1")
            message.channel.send("Защищаться - 2")
            message.channel.send("Лечиться - 3")
            message.channel.send("Закончить - 4")

client.run("MTA5Njc2MDk4Nzg3ODY5OTA2OA.GtAayi.BGZ9yFnjq5GQlAHRmWv-bKM98VrrCtErPyaMKA")
