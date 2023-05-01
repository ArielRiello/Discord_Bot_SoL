import discord
from config import TOKEN
from comandos_mensagem import on_bot_message

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} ONLINE !!!")

@bot.event
async def on_message(message):
    await on_bot_message(bot, message)
    
bot.run(TOKEN)