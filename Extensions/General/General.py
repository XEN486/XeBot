import discord
from discord.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='invite')
    async def invite(self, ctx):
        await ctx.respond('Hi! I am XeBot! I think most of you will like this bot which was developed by XENON#7763!\nIf you would like me in your server with my commands, just invite me with the link:\n\n:link: **https://discord.com/api/oauth2/authorize?client_id=716330108042084424&permissions=8&scope=applications.commands%20bot**\n\nIf you need support or any help just join our support server at: https://discord.gg/bvCRFJcHCH')

def setup(bot):
    bot.add_cog(General(bot))
