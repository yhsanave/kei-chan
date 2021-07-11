import discord, re
from discord.ext import commands

class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.imagetypes = re.compile(r'.png$|.jpg$|.jpeg$|.bmp$|.gif$', re.IGNORECASE)

    #say command, makes the bot send a message in a given channel
    @commands.command(name='say', help='Kei-chan sends a message in the designated channel')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def say(self, ctx, chan, *, message=''):
        channel = discord.utils.get(self.bot.get_all_channels(), id=int(chan[2:-1]))
        await channel.trigger_typing()
        try:
            attach = discord.File(str('attachments/attach' + self.imagetypes.search(ctx.message.attachments[0].filename)[0]))
        except (IndexError, FileNotFoundError, AttributeError):
            print(f'[Say] Sending "{message}" in #{channel}')
            await channel.send(message)
        else:
            await ctx.message.attachments[0].save('attachments/' + attach.filename)
            print(f'[Say] Sending "{message}" in #{channel} with attachment: {attach.filename}')
            await channel.send(message, file=attach)

def setup(bot):
    bot.add_cog(Say(bot))