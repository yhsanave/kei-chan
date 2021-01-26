import discord, re
from discord.ext import commands
from PIL import Image, ImageFile, ImageMath, ImageOps

class AntiLightMode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.imagetypes = re.compile(r'.png$|.jpg$|.jpeg$|.bmp$|.gif$', re.IGNORECASE)

    #AntiLightMode: Inverts the colors on images attached to messages when a user reacts with ⬜
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == "⬜":
            await reaction.message.clear_reactions()
            await reaction.message.channel.trigger_typing()
            try:
                attach = discord.File(str('attachments/attach' + self.imagetypes.search(reaction.message.attachments[0].filename)[0]))
            except (IndexError, FileNotFoundError, AttributeError):
                print("[ALM] No valid image detected", reaction.message)
            else:
                await reaction.message.attachments[0].save('attachments/' + attach.filename)
                image = Image.open('attachments/' + attach.filename)
                if image.mode != 'RGB' and image.mode != 'L':
                    image = ImageMath.eval("convert(im, 'RGB')", im=image)
                image = ImageOps.invert(image)
                image.save('attachments/' + attach.filename)
                await reaction.message.channel.send("Light Mode Detected! Let me fix that for you:", file=attach)

def setup(bot):
    bot.add_cog(AntiLightMode(bot))