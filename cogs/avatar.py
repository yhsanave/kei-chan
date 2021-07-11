import discord, os, random, asyncio, datetime 
from discord.ext import commands, tasks
from PIL import Image, ImageFile

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.avatars = []
        self.avafp = []

        #Load avatars from the avatar folder into a list
        for avatar in os.listdir('./avatar'):
            if avatar.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                with open(f'./avatar/{avatar}', 'rb') as f:
                    self.avatars.append(f.read())
                    self.avafp.append(f.name)

        self.avaCycle.start()

    #Command to set a random avatar from the avatars folder
    @commands.command()
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def ravatar(self, ctx):
        print('[Avatar] Updating Avatar...')
        try:
            await self.bot.user.edit(avatar=random.choice(self.avatars))
        except discord.errors.HTTPException:
            await ctx.send('Error: Avatar changed too fast, please wait at least 10 minutes between changes')
        else:
            await ctx.send('Avatar updated')
            print('[Avatar] Avatar updated')

    #Command to set an image posted by the user as the avatar
    @commands.command()
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def avatar(self, ctx):
        if ctx.message.attachments[0] != None:
            try:
                attach = discord.File(str('attachments/attach' + self.imagetypes.search(ctx.message.attachments[0].filename)[0]))
            except (IndexError, FileNotFoundError, AttributeError):
                print("[Avatar] No valid image detected", ctx.message)
            else:
                await ctx.message.attachments[0].save('attachments/' + attach.filename)
                avatar = open('attachments/' + attach.filename, 'rb')
                print('[Avatar] Updating Avatar...')
                try:
                    await self.bot.user.edit(avatar=avatar)
                except discord.errors.HTTPException:
                    await ctx.send('Error: Avatar changed too fast, please wait at least 10 minutes between changes')
                else:
                    await ctx.send('Avatar updated')
                    print('[Avatar] Avatar updated from attachment')
        else:
            await ctx.send('You must include an image with this command')

    #Command to select a specific avatar from the avatars folder
    @commands.command()
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def lavatar(self, ctx, i: int):
        print('[Avatar] Updating Avatar...')
        try:
            await self.bot.user.edit(avatar=self.avatars[i])
        except discord.errors.HTTPException:
            await ctx.send('Error: Avatar changed too fast, please wait at least 10 minutes between changes')
        else:
            await ctx.send('Avatar updated')
            print('[Avatar] Avatar updated')

    #Command to show a specific image from the avatars folder, mostly for debugging
    @commands.command()
    async def savatar(self, ctx, i: int):
        sava = discord.File(self.avafp[i])
        await ctx.send(file=sava)
        print(f'[Avatar] Sending {self.avafp[i]}')
            
    #Task that automatically changes the avatar to a random one from the avatars folder every 30 minutes        
    @tasks.loop(hours=1.0)
    async def avaCycle(self):
        print('[avaCycle] Automatically Updating Avatar...')
        try:
            await self.bot.user.edit(avatar=random.choice(self.avatars))
        except discord.errors.HTTPException:
            print('[avaCycle] Error: Avatar changed too fast, please wait at least 10 minutes between changes')
        else:
            print(f'[avaCycle] Avatar updated automatically ({datetime.datetime.now()})')
    
    #Make sure the bot is ready before trying to update avatar automatically
    @avaCycle.before_loop
    async def before_avaCycle(self):
        await self.bot.wait_until_ready()
        print('[avaCycle] Starting avaCycle...')
    
    #Command to toggle the automatic cycling of avatars
    @commands.command()
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def cavatar(self, ctx):
        try:
            self.avaCycle.start()
        except RuntimeError:
            self.avaCycle.cancel()
            await ctx.send('Stopped Avatar Cycle')
            print('[Avatar] Stopped Avatar Cycle')
        else:
            await ctx.send('Started Avatar Cycle')

def setup(bot):
    bot.add_cog(Avatar(bot))