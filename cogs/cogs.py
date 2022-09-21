import discord
from discord.ext import commands


class Cogs(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Startup] Cog Cogs loaded successfully')

    # Command to manually load a cog
    @commands.slash_command()
    @commands.check_any(commands.is_owner())
    async def cogload(self, ctx: discord.ApplicationContext, extension):
        try:
            self.bot.load_extension(f'cogs.{extension}')
        except:
            print(f'[Cogs] Failed to load cog {extension}')
            await ctx.respond(f'Failed to load cog *{extension}*', ephemeral=True)
        else:
            print(f'[Cogs] Cog {extension} loaded successfully')
            await ctx.respond(f'Cog *{extension}* loaded successfully', ephemeral=True)

    # Command to manually unload a cog
    @commands.slash_command()
    @commands.check_any(commands.is_owner())
    async def cogunload(self, ctx: discord.ApplicationContext, extension):
        try:
            self.bot.unload_extension(f'cogs.{extension}')
        except:
            print(f'[Cogs] Failed to unload cog {extension}')
            await ctx.respond(f'Failed to unload cog *{extension}*', ephemeral=True)
        else:
            print(f'[Cogs] Cog {extension} unloaded successfully')
            await ctx.respond(f'Cog *{extension}* unloaded successfully', ephemeral=True)

    # command to manually reload a cog
    @commands.slash_command()
    @commands.check_any(commands.is_owner())
    async def cogreload(self, ctx: discord.ApplicationContext, extension):
        try:
            self.bot.reload_extension(f'cogs.{extension}')
        except:
            print(f'[Cogs] Failed to reload cog {extension}')
            await ctx.respond(f'Failed to reload cog *{extension}*', ephemeral=True)
        else:
            print(f'[Cogs] Cog {extension} reloaded successfully')
            await ctx.respond(f'Cog *{extension}* reloaded successfully', ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Cogs(bot))
