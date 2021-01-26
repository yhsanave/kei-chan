import discord, re, deeppyer
from discord.ext import commands
from PIL import Image, ImageFile

class DeepFry(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.imagetypes = re.compile(r'.png$|.jpg$|.jpeg$|.bmp$|.gif$', re.IGNORECASE)

    #AntiLightMode: Inverts the colors on images attached to messages when a user reacts with ⬜
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "🍟":
            await reaction.message.clear_reactions()
            await reaction.message.channel.trigger_typing()
            try:
                attach = discord.File(str('attachments/attach' + self.imagetypes.search(reaction.message.attachments[0].filename)[0]))
            except (IndexError, FileNotFoundError, AttributeError):
                print("[DeepFry] No valid image detected", reaction.message)
            else:
                await reaction.message.attachments[0].save('attachments/' + attach.filename)
                image = Image.open('attachments/' + attach.filename)
                image = await deeppyer.deepfry(image, flares=False)
                image.save('attachments/' + attach.filename)
                await reaction.message.channel.send("One image, hot off the fryers!", file=attach)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.id == 658586539634458625 and not message.author.bot:
            await message.clear_reactions()
            await message.channel.trigger_typing()
            try:
                attach = discord.File(str('attachments/attach' + self.imagetypes.search(message.attachments[0].filename)[0]))
            except (IndexError, FileNotFoundError, AttributeError):
                print("[DeepFry] No valid image detected", message)
            else:
                await message.attachments[0].save('attachments/' + attach.filename)
                image = Image.open('attachments/' + attach.filename)
                image = await deeppyer.deepfry(image, flares=False)
                image.save('attachments/' + attach.filename)
                await message.channel.send("One image, hot off the fryers!", file=attach)
                await message.delete()

def setup(bot):
    bot.add_cog(DeepFry(bot))