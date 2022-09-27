import discord
import re
from discord.ext import bridge, commands


class Say(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.imagetypes = re.compile(
            r'.png$|.jpg$|.jpeg$|.bmp$|.gif$', re.IGNORECASE)

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Startup] Cog Say loaded successfully')

    # say command, makes the bot send a message in a given channel
    @bridge.bridge_command(name='say', description='Kei-chan sends a message in the designated channel')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    @discord.option('channel', discord.SlashCommandOptionType.channel, description='The channel to send the message in')
    @discord.option('message', str, description='The message to send (supports attachments)')
    async def say(self, ctx: discord.ApplicationContext, channel: discord.TextChannel, *, message: str):
        await channel.trigger_typing()
        try:
            attach = discord.File(str(
                'attachments/attach' + self.imagetypes.search(ctx.message.attachments[0].filename)[0]))
        except (IndexError, FileNotFoundError, AttributeError):
            print(f'[Say] Sending "{message}" in #{channel}')
            await channel.send(message)
        else:
            await ctx.message.attachments[0].save('attachments/' + attach.filename)
            print(f'[Say] Sending "{message}" in #{channel} with attachment: {attach.filename}')
            await channel.send(message, file=attach)
        await ctx.respond('Message Sent', ephemeral=True)

    @bridge.bridge_command(name='edit', description='Edit a message sent by Kei-chan')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    @discord.option('channel', discord.SlashCommandOptionType.channel, description='The channel that the message is in')
    @discord.option('id', int, description='The id of the message')
    @discord.option('newmessage', str, description='The edited message')
    async def edit(self, ctx: discord.ApplicationContext, channel: discord.TextChannel, id: int, *, newmessage: str):
        await ctx.channel.trigger_typing()
        history = await channel.history(limit=200).flatten()
        for message in history:
            if message.id == id:
                try:
                    await message.edit(content=newmessage)
                    await ctx.respond("Message Edited", ephemeral=True)
                except discord.Forbidden:
                    await ctx.respond("Error: That message does not belong to me", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Say(bot))
