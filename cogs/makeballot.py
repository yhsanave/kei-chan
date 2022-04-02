import json
import discord, os
from discord.ext import commands

class MakeBallot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #makeballot command, begins taking input from the user who runs the command and using that input to create an embed to put in #announcements
    @commands.command(name="makeballot",help="Create a ballot and post it in given channel; requires Officer role")
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def makeballot(self, ctx, *, chan='<#429126404567859200>', importCode=''):
        def check(m):
            return m.author == ctx.message.author

        def checkr(r, u):
            return ctx.message.author == u

        if importCode:
            try: 
                imported = json.load(importCode)
                title = imported['title']
                description = imported['body']
                ballot = '\n'.join(imported['ballot'])
                footer = imported['footer']
                send_preview()
            except json.JSONDecodeError:
                await ctx.send('Invalid import code')
        else:
            await ctx.send('Enter Meeting Title and Date (Theme Night MM/DD/YY):')
            title = await self.bot.wait_for('message',check=check)

            await ctx.send('Enter Announcement Body (Don\'t include \\@everyone):')
            description = await self.bot.wait_for('message',check=check)

            await ctx.send('Enter Ballot (Put each show on a new line):')
            ballot = await self.bot.wait_for('message',check=check)

            await ctx.send('Enter Closing Statement:')
            footer = await self.bot.wait_for('message',check=check)

            send_preview()

        async def send_preview():
            embed = discord.Embed(description = description.content, color = discord.Color.dark_red())
            embed.set_author(name=title.content)
            embed.set_footer(text=footer.content)
            embed.add_field(name='Ballot:', value=ballot.content, inline=False)

            preview = await ctx.send(embed=embed)
            await preview.add_reaction('👍')
            await preview.add_reaction('👎')
            confirm = await self.bot.wait_for('reaction_add', check=checkr)
            if str(confirm[0].emoji) == '👍':
                channel = self.bot.get_channel(int(chan[2:-1]))
                await ctx.send(f'Confirmed, sending in #{channel}')
                await channel.send(embed = embed)
                await channel.send(content='@everyone',delete_after=.01)
            else:
                await ctx.send('Announcement Cancelled')

def setup(bot):
    bot.add_cog(MakeBallot(bot))
