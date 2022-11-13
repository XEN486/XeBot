import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        embed = discord.Embed(title='Invite Link', description='https://discord.com/api/oauth2/authorize?client_id=716330108042084424&permissions=8&scope=bot')
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(General(bot))
