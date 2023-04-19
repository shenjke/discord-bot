from logic import *
import discord

intents = discord.Intents.default()

intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send('Привет! Я бот!')
    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())
    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())
    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))
    elif message.content.startswith('https://'):
        await message.delete()
        await message.channel.send(f"{message.author.mention} Не отправляй ссылки")
    else:
        await message.channel.send("Я не понимаю такую команду!")

client.run("tkn")
