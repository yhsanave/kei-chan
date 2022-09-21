import discord
from discord.ext import commands


class EditBallot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # makeballot command, begins taking input from the user who runs the command and using that input to create an embed to put in #announcements
    @commands.command(name="editballot", help="Create a ballot and post it in given channel; requires Officer role")
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    async def editballot(self, ctx: discord.ApplicationContext, chan, id: int):
        def check(m):
            return m.author == ctx.message.author

        def checkr(r, u):
            return ctx.message.author == u

        channel = discord.utils.get(
            self.bot.get_all_channels(), id=int(chan[2:-1]))
        history = await channel.history(limit=200).flatten()
        for message in history:
            if message.id == id:
                edit = message

        await ctx.send('Enter Meeting Title and Date (Theme Night MM/DD/YY):')
        title = await self.bot.wait_for('message', check=check)

        await ctx.send('Enter Announcement Body (Don\'t include \\@everyone):')
        description = await self.bot.wait_for('message', check=check)

        await ctx.send('Enter Ballot (Put each show on a new line):')
        ballot = await self.bot.wait_for('message', check=check)

        await ctx.send('Enter Closing Statement:')
        footer = await self.bot.wait_for('message', check=check)

        embed = discord.Embed(description=description.content,
                              color=discord.Color.dark_red())
        embed.set_author(
            name=title.content, icon_url='https://cdn.discordapp.com/avatars/529855914669244417/3917b07936f26ab5835c103a92048901.jpg')
        embed.set_footer(text=footer.content)
        embed.add_field(name='Ballot:', value=ballot.content, inline=False)

        preview = await ctx.send(embed=embed)
        await preview.add_reaction('👍')
        await preview.add_reaction('👎')
        confirm = await self.bot.wait_for('reaction_add', check=checkr)
        if str(confirm[0].emoji) == '👍':
            channel = self.bot.get_channel(int(chan[2:-1]))
            await ctx.send(f'Confirmed, editing in #{channel}')
            await edit.edit(embed=embed)
        else:
            await ctx.send('Edit Cancelled')


def setup(bot: commands.Bot):
    bot.add_cog(EditBallot(bot))
