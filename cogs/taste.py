import discord
from discord.ext import commands

class Taste(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Devon has shit taste
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.get_role(664047585329283073) in before.roles and before.nick != after.nick:
            await after.edit(reason='Cyber Stalking',nick="Actual Cyber Stalker")
            print(f'[Tatse] {after} is a Cyber Stalker')

def setup(bot):
    bot.add_cog(Taste(bot))