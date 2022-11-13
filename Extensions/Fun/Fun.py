import discord, random, asyncio, io, requests
from PIL import Image, ImageFilter
from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['8ball'],pass_context=True)
    async def eightball(self, ctx, *question):
        question = ' '.join(question)
        possibleChoices = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.', 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                           'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.',
                           'Don\'t count on it.', 'My reply is no.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

        m = await ctx.send(embed=discord.Embed(title=question)) # create empty embed
        embed = discord.Embed(title='8-Ball')
        embed.add_field(name=question, value='Concentrate hard for 3 seconds to get the answer.')
        await m.edit(embed=embed) # edit so that it doesn't look like the edited is changing anything lol
        newEmbed = discord.Embed(title='8-Ball')
        newEmbed.add_field(name=question, value=random.choice(possibleChoices))
        await asyncio.sleep(3)
        await m.edit(embed=newEmbed)

    @commands.command(pass_context=True)
    async def imageFilter(self, ctx, imageFilter:str):
        if ctx.message.attachments:
            attachment = requests.get(ctx.message.attachments[0].url).content
            img = Image.open(io.BytesIO(attachment))
            if imageFilter == 'blur':
                img = img.filter(ImageFilter.BLUR)
            elif imageFilter == 'contour':
                img = img.filter(ImageFilter.CONTOUR)
            elif imageFilter == 'detail':
                img = img.filter(ImageFilter.DETAIL)
            elif imageFilter == 'edge_enhance':
                img = img.filter(ImageFilter.EDGE_ENHANCE)
            elif imageFilter == 'edge_enhance_more':
                img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
            elif imageFilter == 'emboss':
                img = img.filter(ImageFilter.EMBOSS)
            elif imageFilter == 'find_edges':
                img = img.filter(ImageFilter.FIND_EDGES)
            elif imageFilter == 'sharpen':
                img = img.filter(ImageFilter.SHARPEN)
            elif imageFilter == 'smooth':
                img = img.filter(ImageFilter.SMOOTH)
            elif imageFilter == 'smooth_more':
                img = img.filter(ImageFilter.SMOOTH_MORE)
                
            with io.BytesIO() as imgBin:
                img.save(imgBin, 'PNG')
                imgBin.seek(0)
                await ctx.send(file=discord.File(fp=imgBin, filename=f'{imageFilter}.png'))
        else:
            await ctx.send('You should provide an image first!')

async def setup(bot):
    await bot.add_cog(Fun(bot))
