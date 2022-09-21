import discord
from discord.ext import commands

class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Check if message is level up announcement from Tatsumaki and if so, react with :LVL:
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 172002275412279296 and message.content.startswith('🆙'):
            await message.add_reaction('<:LVL:471812453290737704>')

def setup(bot):
    bot.add_cog(Level(bot))