import discord
import os
import random
import datetime
from discord.ext import commands, tasks


class Avatar(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.avatars = []
        self.avafp = []

        # Load avatars from the avatar folder into a list
        for avatar in os.listdir('./avatar'):
            if avatar.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                with open(f'./avatar/{avatar}', 'rb') as f:
                    self.avatars.append(f.read())
                    self.avafp.append(f.name)

        self.avaCycle.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Startup] Cog Avatar loaded successfully')

    # Command to set a random avatar from the avatars folder
    @commands.slash_command(name='avatarrandom', description='Set Kei-chan to a random avatar')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def random(self, ctx: discord.ApplicationContext):
        print('[Avatar] Updating Avatar...')
        try:
            await self.bot.user.edit(avatar=random.choice(self.avatars))
        except discord.errors.HTTPException:
            await ctx.respond('Error: Avatar changed too fast, please wait at least 10 minutes between changes', ephemeral=True)
        else:
            await ctx.respond('Avatar updated', ephemeral=True)
            print('[Avatar] Avatar updated')

    # Command to set an image posted by the user as the avatar
    @commands.slash_command(name='avatarset', description='Send an image to set Kei-chan\'s avatar')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def set(self, ctx: discord.ApplicationContext):
        if ctx.message.attachments[0] != None:
            try:
                attach = discord.File(str(
                    'attachments/attach' + self.imagetypes.search(ctx.message.attachments[0].filename)[0]))
            except (IndexError, FileNotFoundError, AttributeError):
                print("[Avatar] No valid image detected", ctx.message)
            else:
                await ctx.message.attachments[0].save('attachments/' + attach.filename)
                avatar = open('attachments/' + attach.filename, 'rb')
                print('[Avatar] Updating Avatar...')
                try:
                    await self.bot.user.edit(avatar=avatar)
                except discord.errors.HTTPException:
                    await ctx.respond('Error: Avatar changed too fast, please wait at least 10 minutes between changes')
                else:
                    await ctx.respond('Avatar updated')
                    print('[Avatar] Avatar updated from attachment')
        else:
            await ctx.respond('You must include an image with this command')

    # Command to select a specific avatar from the avatars folder
    @commands.slash_command(name='avatarselect', description='Select Kei-chan\'s avatar')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def select(self, ctx: discord.ApplicationContext, i: int):
        print('[Avatar] Updating Avatar...')
        try:
            await self.bot.user.edit(avatar=self.avatars[i])
        except discord.errors.HTTPException:
            await ctx.respond('Error: Avatar changed too fast, please wait at least 10 minutes between changes')
        else:
            await ctx.respond('Avatar updated')
            print('[Avatar] Avatar updated')

    # Command to show a specific image from the avatars folder, mostly for debugging
    @commands.slash_command(name='avatarshow', description='Show a Kei-chan avatar')
    async def show(self, ctx: discord.ApplicationContext, i: int):
        sava = discord.File(self.avafp[i])
        await ctx.respond(file=sava)
        print(f'[Avatar] Sending {self.avafp[i]}')

    # Task that automatically changes the avatar to a random one from the avatars folder every 30 minutes
    @tasks.loop(hours=1.0)
    async def avaCycle(self):
        print('[avaCycle] Automatically Updating Avatar...')
        try:
            await self.bot.user.edit(avatar=random.choice(self.avatars))
        except discord.errors.HTTPException:
            print(
                '[avaCycle] Error: Avatar changed too fast, please wait at least 10 minutes between changes')
        else:
            print(
                f'[avaCycle] Avatar updated automatically ({datetime.datetime.now()})')

    # Make sure the bot is ready before trying to update avatar automatically
    @avaCycle.before_loop
    async def before_avaCycle(self):
        await self.bot.wait_until_ready()
        print('[avaCycle] Starting avaCycle...')

    # Command to toggle the automatic cycling of avatars
    @commands.slash_command(name='avatarcycle', description='Toggle hourly avatar cycle')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def cycle(self, ctx: discord.ApplicationContext):
        try:
            self.avaCycle.start()
        except RuntimeError:
            self.avaCycle.cancel()
            await ctx.respond('Stopped Avatar Cycle')
            print('[Avatar] Stopped Avatar Cycle')
        else:
            await ctx.respond('Started Avatar Cycle')


def setup(bot: commands.Bot):
    bot.add_cog(Avatar(bot))
