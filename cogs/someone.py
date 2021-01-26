import discord, re, random, asyncio
from discord.ext import commands

class Someone(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        check = re.search('@someone', message.content, re.IGNORECASE)
        if check != None:
            new = re.sub('@someone', random.choice(message.channel.members).mention, message.content, 0, re.IGNORECASE)
            await message.channel.send(new)

def setup(bot):
    bot.add_cog(Someone(bot))