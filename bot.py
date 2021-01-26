# bot.py
import discord, os
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

#Send a message in the console when the bot is ready and set default activity
@bot.event
async def on_ready():
    activity = discord.Activity(name='Anime', type=discord.ActivityType.watching)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'[Startup] {bot.user.name} has connected to Discord!')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

#load all cogs by default
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'[Startup] Cog {filename[:-3]} loaded successfully')

bot.run(r'NTI5ODU1OTE0NjY5MjQ0NDE3.Xg8FqA.YS3cmGw10Or2CgP40Oe9Mk-lqRI')