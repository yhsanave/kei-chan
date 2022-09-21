import discord
import re
import random
from discord.ext import commands


class Someone(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Startup] Cog Someone loaded successfully')

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        check = re.search('@someone', message.content, re.IGNORECASE)
        if check != None:
            new = re.sub('@someone', random.choice(message.channel.members).mention,
                         message.content, 0, re.IGNORECASE)
            await message.channel.send(new)


def setup(bot: commands.Bot):
    bot.add_cog(Someone(bot))
