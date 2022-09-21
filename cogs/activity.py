import discord
from discord.ext import commands


class Activity(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.activities = [discord.ActivityType.playing, discord.ActivityType.streaming,
                           discord.ActivityType.listening, discord.ActivityType.watching]

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Startup] Cog Activity loaded successfully')

    # Change the bot's status message
    @commands.slash_command(name='activity', description='Set Kei-chan\'s activity type  and message')
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    @discord.option('type', int, description = '0: Playing, 1: Streaming, 2: Listening, 3: Watching')
    @discord.option('activity', str, description = 'Activity text')
    async def activity(self, ctx: discord.ApplicationContext, type: int, *, activity: str):
        print('[Activity] Status updated:', self.activities[type], activity)
        await self.bot.change_presence(activity=discord.Activity(name=activity, type=self.activities[type]))
        await ctx.respond('Activity updated!', ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(Activity(bot))
