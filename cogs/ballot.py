import json
import discord
from discord.ext import commands


class BallotModal(discord.ui.Modal):
    class ConfirmView(discord.ui.View):
        def __init__(self, channel: discord.TextChannel, embed: discord.Embed):
            super().__init__()
            self.targetChannel = channel
            self.embed = embed

        @discord.ui.button(label='👍 Confirm', row=0, style=discord.ButtonStyle.success)
        async def confirm_button(self, button, interaction: discord.Interaction):
            await interaction.response.edit_message(view=None)
            await interaction.channel.send('Confirmed, sending message!')
            await self.targetChannel.send(embed=self.embed)
            await self.targetChannel.send('@everyone', delete_after=0)

        @discord.ui.button(label='👎 Reject', row=0, style=discord.ButtonStyle.danger)
        async def reject_button(self, button, interaction: discord.Interaction):
            await interaction.response.edit_message(view=None)
            await interaction.channel.send('Announcement rejected!')

    def __init__(self, channel: discord.TextChannel, imported: dict = {'header': '', 'body': '', 'shows': '', 'footer': ''}):
        super().__init__(title='Meeting Info')
        self.add_item(discord.ui.InputText(
            label='Title', placeholder='Theme Night MM/DD/YY', custom_id='title', value=imported['header']))
        self.add_item(discord.ui.InputText(label='Description', style=discord.InputTextStyle.long,
                      placeholder='Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt...',
                      custom_id='description', value=imported['body']))
        self.add_item(discord.ui.InputText(label='Shows', style=discord.InputTextStyle.long,
                      placeholder='Detective Conan\nKyousougiga\nSSSS.Gridman\n...', custom_id='shows', value='\n'.join(imported['shows'])))
        self.add_item(discord.ui.InputText(
            label='Footer', placeholder='Don\'t forget your receipts', custom_id='footer', value=imported['footer']))

        self.targetChannel: discord.TextChannel = channel

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(color=discord.Color.dark_red(),
                              title=self.children[0].value,
                              description=self.children[1].value)
        embed.add_field(name='Ballot', value=self.children[2].value)
        embed.set_footer(text=self.children[3].value)
        await interaction.response.send_message(embed=embed, view=self.ConfirmView(channel=self.targetChannel, embed=embed))


class Ballot(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('[Startup] Cog Ballot loaded successfully')

    @commands.slash_command(name="makeballot", help="Create a ballot and post it in given channel; requires Officer role")
    @commands.check_any(commands.has_role('Officers'), commands.is_owner())
    @discord.option('channel', discord.SlashCommandOptionType.channel, description='The channel to send the announcement in')
    @discord.option('import_code', str, description='Import code from AniPoint', required=False)
    async def makeballot(self, ctx: discord.ApplicationContext, channel: discord.SlashCommandOptionType.channel, *, import_code: str = None):
        if import_code:
            try:
                imported = json.loads(import_code)
                modal = BallotModal(channel=channel, imported=imported)
            except json.JSONDecodeError:
                await ctx.respond('Invalid Import Code', ephemeral=True)
        else:
            modal = BallotModal(channel=channel)

        await ctx.interaction.response.send_modal(modal)


def setup(bot: commands.Bot):
    bot.add_cog(Ballot(bot))
