import discord
from discord.ext import commands

class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Command to manually load a cog
    @commands.command()
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def load(self, ctx, extension):
        try:
            self.bot.load_extension(f'cogs.{extension}')
        except:
            print(f'[Cogs] Failed to load cog {extension}')
            await ctx.send(f'Failed to load cog *{extension}*')
        else:
            print(f'[Cogs] Cog {extension} loaded successfully')
            await ctx.send(f'Cog *{extension}* loaded successfully')

    #Command to manually unload a cog
    @commands.command()
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def unload(self, ctx, extension):
        try:
            self.bot.unload_extension(f'cogs.{extension}')
        except:
            print(f'[Cogs] Failed to unload cog {extension}')
            await ctx.send(f'Failed to unload cog *{extension}*')
        else:
            print(f'[Cogs] Cog {extension} unloaded successfully')
            await ctx.send(f'Cog *{extension}* unloaded successfully')

    #command to manually reload a cog
    @commands.command()
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def reload(self, ctx, extension):
        try:
            self.bot.reload_extension(f'cogs.{extension}')
        except:
            print(f'[Cogs] Failed to reload cog {extension}')
            await ctx.send(f'Failed to reload cog *{extension}*')
        else:
            print(f'[Cogs] Cog {extension} reloaded successfully')
            await ctx.send(f'Cog *{extension}* reloaded successfully')

def setup(bot):
    bot.add_cog(Cogs(bot))