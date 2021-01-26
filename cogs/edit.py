import discord
from discord.ext import commands

class Edit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role('Officers')
    async def edit(self, ctx, chan, id: int, *, newmessage):
        await ctx.channel.trigger_typing()
        channel = discord.utils.get(self.bot.get_all_channels(), id=int(chan[2:-1]))
        history = await channel.history(limit=200).flatten()
        for message in history:
            if message.id == id:
                try:
                    await message.edit(content=newmessage)
                    await ctx.send("Message Edited")
                except discord.Forbidden:
                    await ctx.send("Error: That message does not belong to me")
    
def setup(bot):
    bot.add_cog(Edit(bot))
