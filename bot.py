# bot.py
import discord
import os
from discord.ext import commands
from dotenv import dotenv_values

TOKEN = dotenv_values()['TOKEN']
GUILD_ID = dotenv_values()['GUILD_ID']

bot = commands.Bot(command_prefix='.', activity=discord.Activity(
    name='Anime', type=discord.ActivityType.watching), intents=discord.Intents.all())


@bot.event
async def on_ready():
    print(f'[Startup] {bot.user.name} has connected to Discord!')


@bot.slash_command()
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f'Pong! {bot.latency*1000}ms')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(TOKEN)
