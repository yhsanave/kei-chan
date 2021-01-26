import discord
from discord.ext import commands

class Activity(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.activities = [discord.ActivityType.playing, discord.ActivityType.streaming, discord.ActivityType.listening, discord.ActivityType.watching]

    #Change the bot's status message
    @commands.command(name='activity', help='set the activity type (0: Playing, 1: Streaming, 2: Listening, 3: Watching) and message')
    @commands.has_role('Officers')
    async def activity(self, ctx, type: int, *, activity: str):
        print('[Activity] Status updated:', self.activities[type], activity)
        await self.bot.change_presence(activity=discord.Activity(name=activity, type=self.activities[type]))

def setup(bot):
    bot.add_cog(Activity(bot))