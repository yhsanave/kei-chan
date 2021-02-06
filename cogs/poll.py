import requests, discord
from discord.ext import commands

class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def poll(self, ctx, channel, *, title):
        def check(m):
            return m.author == ctx.message.author

        await ctx.send("Enter options (one per line):")
        options = await self.bot.wait_for('message',check=check)
        options = options.content.split('\n')

        data = '{' + f'"title": "{title}", "options": {options}, "multi": true, "dupcheck": "permissive"' + "}"

        response = requests.post(url="https://strawpoll.me/api/v2/polls",json=data).json()
        link = f'https://strawpoll.me/{response["id"]}'

        await channel.send(f"@here {link}")

def setup(bot):
    bot.add_cog(Poll(bot))
