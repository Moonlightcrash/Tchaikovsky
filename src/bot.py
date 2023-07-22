import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()


def run_discord_bot():
    intents = discord.Intents.default()  # Подключаем "Разрешения"
    intents.message_content = True

    # Задаём префикс и интенты

    bot = commands.Bot(command_prefix='>', intents=intents)

    # С помощью декоратора создаём первую команду
    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run(os.getenv("API_TOKEN"))
